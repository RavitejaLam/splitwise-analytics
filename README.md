# Splitwise Analytics

### Steps to Run
* clone the project
* install python3
* install the required packages
    ```commandline
    pip install -r requirements.txt
    ```
* create a `.env` file 
    ```
    CONSUMER_KEY = "******"
    CONSUMER_SECRET = "******"
    API_KEY = "******"
    ```
  you can create your secrets [here](https://secure.splitwise.com/apps)
* run the code
    ```commandline
    python app.py
    ```
* open the url to get last 12 months data
    ```
    http://localhost:8888/dashboard/12
    ```
  you can change the number of months
    ```
    http://localhost:8888/dashboard/<months>
    ```