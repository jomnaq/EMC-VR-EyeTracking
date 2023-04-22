using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Column_Behavior : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        float randomNumber = Random.Range(0.0f, 10.0f);
        transform.position = new Vector3(2, 0, randomNumber);
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
