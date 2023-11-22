import os

from dotenv import load_dotenv
from flask import session
from splitwise import Splitwise

load_dotenv()


def get_authorization_url():
    client = get_splitwise_client()
    redirect_uri = "http://localhost/callback"
    url, state = client.getOAuth2AuthorizeURL(redirect_uri)
    session["state"] = state
    return url


def get_splitwise_client():
    if "access_token" in session:
        return Splitwise(consumer_key=os.getenv("CONSUMER_KEY"),
                         consumer_secret=os.getenv("CONSUMER_SECRET"),
                         api_key=session["access_token"])
    return Splitwise(consumer_key=os.getenv("CONSUMER_KEY"),
                     consumer_secret=os.getenv("CONSUMER_SECRET"))


def get_my_spending(user_expenses):
    for user_expense in user_expenses:
        if user_expense.getId() == session["id"]:
            return float(user_expense.getOwedShare())
    return 0


def update_session_with_current_user_data():
    client = get_splitwise_client()
    current_user = client.getCurrentUser()
    session["id"] = current_user.getId()
    session["default_currency"] = current_user.getDefaultCurrency()


def set_access_token(code):
    client = get_splitwise_client()
    redirect_uri = "http://localhost/callback"
    access_token = client.getOAuth2AccessToken(code, redirect_uri)['access_token']
    session["access_token"] = access_token
