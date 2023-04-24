using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class IntroSlides : MonoBehaviour
{
    public GameObject slide1;
    public GameObject slide2;
    public GameObject slide3;

    public GameObject contSpace;
    public GameObject background;

    public int currSlide = 0;

    // Start is called before the first frame update
    void Start()
    {
        slide1.SetActive(true);
        slide2.SetActive(false);
        slide3.SetActive(false);
        contSpace.SetActive(true);
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            if (currSlide == 0) {
                slide1.SetActive(false);
                slide2.SetActive(true);
                currSlide++;
            }
            else if(currSlide == 1)
            {
                slide2.SetActive(false);
                slide3.SetActive(true);
                currSlide++;
            }
            else
            {
                SceneManager.LoadScene(sceneName: "SampleScene");                
            }
        }
    }
}
