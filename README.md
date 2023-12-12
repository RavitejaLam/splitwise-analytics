# Splitwise Analytics
Splitwise Analytics is an application designed to enhance your Splitwise experience by providing insightful graphs and analytics through OAuth 2.0 authentication.

### Features
- **OAuth 2.0 Integration:** Utilizes OAuth 2.0 for secure authentication and access to Splitwise.
- **Spending's Per Month:** This will show the spending's of last 12 months grouped by month.
- More features coming soon

### Screenshots
![welcome_screenshot](README/welcome_screenshot.png)
![home_screenshot](README/home_screenshot.png)
![spendings_per_month_screenshot](README/spendings_per_month_screenshot.png)

### FAQ

- **1: What if you have expenses of multiple currencies?** 

  Only default currency expenses are used by this application. Select preferred currency as default currency in your splitwise app and then use splitwise analytics.


### Getting Started

- Set Up OAuth 2.0 Credentials
  - Visit the Splitwise Developer Portal (https://www.splitwise.com/apps) and create a new application
  - Obtain your Consumer key and Consumer Secret ![register_your_app](README/register_your_app.png)

## Run with docker image

- **Pull Docker image**
  ```commandline
  docker pull ghcr.io/ravitejalam/splitwise-analytics:latest
  ```

- **Run docker image**
  ```commandline
  docker run -p -d 8000:80 -e CONSUMER_KEY=<CONSUMER_KEY> -e CONSUMER_SECRET=<CONSUMER_SECRET> splitwise-analytics:latest
  ```
- **Access the Dashboard:**

   Open your web browser and navigate to http://localhost to access the Splitwise Analytics dashboard.

### OR

## Build and run flask app

- **Clone the Repository:**
  ```bash
  git clone https://github.com/RavitejaLam/splitwise-analytics.git
  ```
- **Install Dependencies:**
    ```bash
    cd splitwise-analytics
    pip install -r requirements.txt
    ```
- Set these credentials in the `.env` file
    ```
    CONSUMER_KEY = "******"
    CONSUMER_SECRET = "******"
    ```
- **Run the Application:**
    ```commandline
    python app.py
    ```
- **Access the Dashboard:**

   Open your web browser and navigate to http://localhost to access the Splitwise Analytics dashboard.

### Acknowledgements
- This project utilizes the Splitwise API (https://dev.splitwise.com/) to retrieve user data.
- Special thanks to the contributors and the Splitwise community for their support and inspiration.