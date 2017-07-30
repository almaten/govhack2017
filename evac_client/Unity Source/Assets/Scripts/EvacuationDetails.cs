using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class EvacuationDetails : MonoBehaviour {
    //public Button[] 
    public AppController myApp;
	// Use this for initialization
	void Start () {
		
	}

    public void SelectEvacOption(int ID)
    {


        myApp.SetState(2);
    }
	
	// Update is called once per frame
	void Update () {
		
	}
}
