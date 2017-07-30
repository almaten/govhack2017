using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using SimpleJSON;
//http://wiki.unity3d.com/index.php/SimpleJSON
using DG.Tweening;

public class anAddress
{
    public string address;
    public string status;
    public System.DateTime Date;
    public double lat;
    public double lon;
    public OnlineMapsMarker marker;
    public string checkedBy;

    

    public anAddress(string ad, string st, string dt, double lt, double ln, OnlineMapsMarker mark =null)
    {
        address = ad;
        status = st;
        Date = System.DateTime.Now;
        lat = lt;
        lon = ln;
        marker = mark;
        checkedBy = "";
    }
}

public class EventLoader : MonoBehaviour
{
    public bool useCannedData = false;
    List<anAddress> myAddresses = new List<anAddress>();
    List<GameObject> myListItems = new List<GameObject>();
    public Texture2D[] MarkerImages;

    public Text StatusText;
    public Text TeamStatusTex;
    public Text AreaStatusTex;

    public OnlineMapsMarker teamMarker;
    //   public GameObject MainEventPanel;
    //   public GameObject ScrollContainer;
    //   public GameObject PanelEntry;


    // public GameObject LoadingPanel;
    public OnlineMaps mapSystem;
    public static float maxMagnitude = 4.0f;

    public GameObject Messager;

    public GameObject GreenComplete;
    public string RequestURL = "http://localhost:8080/pga/api/v1.0/datasets/";

    // Use this for initialization
    void Start()
    {
        GreenComplete.SetActive(false);
        //PanelEntry.SetActive(false);
        //LoadingPanel.SetActive(false);
        LoadEventData("payload");
        ChangeStatus("Checked", 0);
    }

    public void EvacuationComplete()
    {
        for (int t = 0; t < myAddresses.Count; t++)
        {
            ChangeStatus("Checked", t);
        }
        GreenComplete.SetActive(true);
    }

    // Update is called once per frame
    void Update()
    {

    }

    public void ShowMessage()
    {
        Messager.transform.DOLocalMoveY(-135.4f, 0.25f);
    }

    void CalcStatus()
    {
        int c = 0;
        for (int t=0; t<myAddresses.Count; t++)
        {
            if (myAddresses[t].status.Contains("Checked"))
            {
                c++;
            }
        }
        StatusText.text = "Evacuated " +c +" of " + myAddresses.Count + 1;

        TeamStatusTex.text = (myAddresses.Count - c) + " sites to check";
        AreaStatusTex.text = (myAddresses.Count - c) + " sites to check";
    }

    public void ChangeStatus(string Status, int ID)
    {
        OnlineMapsMarker myMarker = new OnlineMapsMarker();
        myMarker.SetPosition(myAddresses[ID].lon, myAddresses[ID].lat);
        myMarker.label = myAddresses[ID].address;
        myMarker.scale = 0.5f;
        
        switch (Status)
        {
            case "Checked":
                if (myAddresses[ID].status!= "SelfChecked")
                {
                    myMarker.texture = MarkerImages[2];
                } else
                {
                    myMarker.texture = MarkerImages[1];
                }
                //myAddresses[ID].marker.texture = MarkerImages[2];
                break;
            case "SelfChecked":
                print("CHANGE IMAGE");
                myMarker.texture = MarkerImages[1];
                break;
            case "Assist":
                myMarker.texture = MarkerImages[3];
                break;
        }

        OnlineMapsMarker thisMarker = mapSystem.AddMarker(myMarker);
        myAddresses[ID].status = Status;
        CalcStatus();
        mapSystem.Redraw();
    }

    public void ResetSettings()
    {

    }

    public void LoadEventData(string File)
    {

        //LoadingPanel.SetActive(true);
        if (useCannedData)
        {
            try
            {
                TextAsset FileData = Resources.Load(File) as TextAsset;
                ParseJSON(FileData.text);
                //BuildUI();
            }
            catch (System.Exception ex)
            {
                print(ex.Message);
            }
        }
        else
        {
            
            string URL = RequestURL + File;
            WWW www = new WWW(URL);
            StartCoroutine(WaitForRequest(www));
        }

    }

    IEnumerator WaitForRequest(WWW www)
    {
        yield return www;

        // check for errors
        if (www.error == null)
        {
            Debug.Log("WWW Ok!: " + www.data);
            //TextAsset FileData = Resources.Load("11") as TextAsset;
            //Debug.Log(FileData.text);
            ParseJSON(www.text);
            BuildUI();
        }
        else
        {
            Debug.Log("WWW Error: " + www.error);
        }
        //LoadingPanel.SetActive(false);

    }
    Vector2 TeamPos;
    Vector2 TeamDest;
    int CurrentDest = 1;
    public void MoveTeam()
    {
        TeamPos = new Vector2((float)myAddresses[0].lat, (float)myAddresses[0].lon);

        TeamDest = new Vector2((float)myAddresses[1].lat, (float)myAddresses[1].lon);
        DOTween.To(() => TeamPos, x => TeamPos = x, TeamDest, 1).OnUpdate(SetTeamPos).OnComplete(NextTeamPos).SetDelay(0.5f);
    }

    void NextTeamPos()
    {
        if (CurrentDest == 10)
        {
            ChangeStatus("Assist", CurrentDest);
        }
        else
        {
            ChangeStatus("Checked", CurrentDest);
        }
        CurrentDest++;
        if (CurrentDest >= myAddresses.Count)
        {

        } else
        {
            //TeamPos = new Vector2((float)myAddresses[0].lat, (float)myAddresses[0].lon);

            TeamDest = new Vector2((float)myAddresses[CurrentDest].lat, (float)myAddresses[CurrentDest].lon);
            DOTween.To(() => TeamPos, x => TeamPos = x, TeamDest, 1).OnUpdate(SetTeamPos).OnComplete(NextTeamPos).SetDelay(0.5f);
        }
    }

    void SetTeamPos()
    {
        teamMarker.SetPosition((double)TeamPos.y, (double)TeamPos.x);
        mapSystem.Redraw();
    }

    void ParseJSON(string JSONString)
    {
        myAddresses.Clear();
        JSONNode N = JSON.Parse(JSONString);
       // print("Parse JSON");
        var DataSets = N[0]["addresses"];
        print(DataSets.Count);

        for (int t = 0; t < DataSets.Count; t++)
        {
            print(DataSets[t]);
            anAddress newAddress = new anAddress(DataSets[t]["address"], DataSets[t]["status"], "", DataSets[t]["lat"].AsDouble, DataSets[t]["long"].AsDouble);
            
            OnlineMapsMarker myMarker = new OnlineMapsMarker();
            myMarker.SetPosition(newAddress.lon, newAddress.lat);
            myMarker.texture = MarkerImages[0];
            myMarker.scale = 0.5f;
            myMarker.label = newAddress.address;
            OnlineMapsMarker thisMarker = mapSystem.AddMarker(myMarker);
            newAddress.marker = thisMarker;
            myAddresses.Add(newAddress);

           // print("ADDING EVENT " + newAddress.address);
        }

        OnlineMapsMarker myMarkerT = new OnlineMapsMarker();
        myMarkerT.SetPosition(myAddresses[0].lon, myAddresses[0].lat);
        myMarkerT.texture = MarkerImages[4];
        myMarkerT.scale = 0.5f;
        myMarkerT.label = "South Selwyn A";
        teamMarker = mapSystem.AddMarker(myMarkerT);
        myMarkerT.align = OnlineMapsAlign.BottomRight;
    }

    public void ResetColors()
    {
        for (int t = 0; t < myListItems.Count; t++)
        {
           // GameObject obj = Instantiate(PanelEntry, ScrollContainer.transform) as GameObject;
            myListItems[t].GetComponent<Image>().color = new Color(1, 1, 1, 0.5f);
        }
    }

    void BuildUI()
    {
        
    }

    public void PickEvent(string EventName)
    {
        //MainEventPanel.SetActive(false);

    }
}
