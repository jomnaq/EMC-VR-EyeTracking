using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using System.IO;

public class Orb_Behavior : MonoBehaviour
{
    [SerializeField] float moveSpeed;
    [SerializeField] double randomValue;
    bool goingUp = false;

    private string filePath;
    private StreamWriter writer;
    private float lastTime;
    private const float INCREMENT = 0.02f;
    
    // Start is called before the first frame update
    void Start()
    {
        lastTime = 0;
        moveSpeed = 20f;
        transform.position = new Vector3(-20, 0, 20);
        System.Random random = new System.Random();
        double minValue = 1.0;
        double maxValue = 2.5;
        randomValue = random.NextDouble() * (maxValue - minValue) + minValue;
        Invoke("DoSomethingDifferent", (float)randomValue);
        filePath = Application.dataPath + "/out.csv";
        writer = new StreamWriter(filePath);
        writer.WriteLine("time (seconds), x, y");
    }

    void DoSomethingDifferent()
    {
        goingUp = true;
    }

    // Update is called once per frame
    void Update()
    {

        if(goingUp) {
            transform.Translate(0, moveSpeed * Time.deltaTime, 0);
        } else {
            transform.Translate(moveSpeed * Time.deltaTime, 0, 0);
        }

        lastTime += Time.deltaTime;
        if(lastTime >= INCREMENT) {
            lastTime = lastTime % INCREMENT;
            string textToWrite =
            $"{Time.time}, {transform.position.x}, {transform.position.y}";

            writer.WriteLine(textToWrite);
            
        }
        Debug.Log(lastTime);
    }
}
