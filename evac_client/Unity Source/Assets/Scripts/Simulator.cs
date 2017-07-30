using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Simulator : MonoBehaviour {
    public int[] SelfChecks;
    public EventLoader myEvents;

    float SelfCheckTimer = 0;
    int SelfCheckID = 0;
	// Use this for initialization
	void Start () {

	}

    public void DoSelfChecks()
    {
        SelfCheckID = 0;
        SelfCheckTimer = Random.Range(1f, 2f);
        /*
        print("DO SELF CHECKS");
        for (int t = 0; t < SelfChecks.Length; t++)
        {
            myEvents.ChangeStatus("SelfChecked", SelfChecks[t]);
        }
        */
        
    }
	
	// Update is called once per frame
	void Update () {
		if (SelfCheckTimer > 0)
        {
            SelfCheckTimer -= Time.deltaTime;
            if (SelfCheckTimer <= 0)
            {
                myEvents.ChangeStatus("SelfChecked", SelfChecks[SelfCheckID]);
                SelfCheckID++;
                if (SelfCheckID < SelfChecks.Length)
                {
                    SelfCheckTimer = Random.Range(1f, 2f);
                }
            }
        }
	}
}
