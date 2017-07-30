using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AppController : MonoBehaviour {

    public GameObject PanelAlert;
    public GameObject PanelWarning;
    public GameObject PanelNormal;
    public GameObject PanelRegister;

    public GameObject PanelStatus;
    // Use this for initialization
    void Start () {
        SetState(0);
    }

    public void SetState(int what)
    {
        PanelAlert.SetActive(false);
        PanelWarning.SetActive(false);
        PanelNormal.SetActive(false);
        PanelRegister.SetActive(false);

        PanelStatus.SetActive(false);

        switch (what)
        {
            case 0:
                PanelRegister.SetActive(true);
                break;
            case 1:
                PanelNormal.SetActive(true);
                break;
            case 2:
                PanelStatus.SetActive(true);
                break;
            case -1:
                PanelWarning.SetActive(true);
                break;
            case -2:
                PanelAlert.SetActive(true);
                break;
        }

    }
	
	// Update is called once per frame
	void Update () {
		
	}
}
