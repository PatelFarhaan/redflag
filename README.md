# _**REDFLAG**_

## Requirements before running this application:
### Install Google Chorme in Ubuntu:
1. Enter the folloeing commands in your terminal:
    ```
    sudo apt-get update
    sudo apt-get install google-chrome-stable
    ```
2. Go to chromedriver_linux64.zip file or download the version from the website:
   ```
   https://chromedriver.chromium.org/downloads
   ```
3.Unzip chromedriver_linux64.zip and get the chromedriver file
4. If chromedriver is already available in the Code Section, so just change the permision and follow the steps below:
    ```
    chmod +x chromedriver
    sudo mv chromedriver /usr/local/share/chromedriver
    cd /usr/local/share/
    ls
    ls -al
    sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
    sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
    chromedriver --version
    ```



## Some Extra Information

1. If using google-chrome then:
    ```
    DRIVER_LOCATION = "/usr/bin/chromedriver"
    BINARY_LOCATION = "/usr/bin/google-chrome"
    ```

2. If using chromium browser then:
    ```   
    DRIVER_LOCATION = "/snap/bin/chromium.chromedriver"
    BINARY_LOCATION = "/usr/bin/chromium-browser"
    ```

# How to run the application:

1. Create a virtual environment using the command: 
    ```
    virtualenv venv
   ```
   
2. Actiavte the virtual environment using the command: 
    ```
    source venv/bin/activate
   ```

3. Install all the requirements: 
    ```
    pip3 install -r requirements.txt
   ```
   
4. Run the application:
    ```
   python3 app.py
    ```
   and it can be access via:
    ```
    http://localhost:5000/
   ```
   
5. This also assumes you have chrome installed in the right path as mentioned in the earlier steps.


# API Endpoints (Form Data):

``` 
url:        localhost:5000/movie-details 
movieName:  <some name>
siteDomain: https://www.imdb.com or https://www.youtube.com
```

Output Example:

```
{
    "videoLinks": [
        "https://www.imdb.com/title/tt0473445/?ref_=fn_al_tt_1",
        "https://www.imdb.com/title/tt0093601/?ref_=fn_al_tt_2",
        "https://www.imdb.com/name/nm0314514/?ref_=fn_al_nm_1",
        "https://www.imdb.com/name/nm0000297/?ref_=fn_al_nm_2",
        "https://www.imdb.com/search/keyword?keywords=avenger&ref_=fn_al_kw_1",
        "https://www.imdb.com/search/keyword?keywords=avengers&ref_=fn_al_kw_2",
        "https://www.imdb.com/company/co0210980/?ref_=fn_al_co_1",
        "https://www.imdb.com/company/co0301374/?ref_=fn_al_co_2"
    ]
}

{
    "videoLinks": [
        "https://www.youtube.com/watch?v=SLD9xzJ4oeU",
        "https://www.youtube.com/watch?v=ePpJDKfRAyM",
        "https://www.youtube.com/watch?v=cfVY9wLKltA",
        "https://www.youtube.com/watch?v=lHw-6AZvZ7I",
        "https://www.youtube.com/watch?v=udKE1ksKWDE",
        "https://www.youtube.com/watch?v=OxzKb4a1Qc4",
        "https://www.youtube.com/watch?v=lAKvbWlhb30",
        "https://www.youtube.com/watch?v=xUt-xDyoAlw",
        "https://www.youtube.com/watch?v=sKnpGhlDh10",
        "https://www.youtube.com/watch?v=5ljluGA4dQU",
        "https://www.youtube.com/watch?v=6ZfuNTqbHE8",
        "https://www.youtube.com/watch?v=-_78zC-KNR4",
        "https://www.youtube.com/watch?v=VDH88glioFE",
        "https://www.youtube.com/watch?v=g5_w5XrC7Ts",
        "https://www.youtube.com/watch?v=dE1P4zDhhqw",
        "https://www.youtube.com/watch?v=WbPfApxlqZY",
        "https://www.youtube.com/watch?v=Q2MEtOPzcUs",
        "https://www.youtube.com/watch?v=pBbsvavno8I",
        "https://www.youtube.com/watch?v=rLL11dEMGdU",
        "https://www.youtube.com/watch?v=fH921fbPB-g",
        "https://www.youtube.com/watch?v=kcrM6myhYxs",
        "https://www.youtube.com/watch?v=TATaO0sCmqI",
        "https://www.youtube.com/watch?v=TKm1t3a6WeA"
    ]
}
```