import logging
from datetime import date, datetime

import pandas as pd
import plotly.express as px
from dateutil.relativedelta import relativedelta
from flask import Blueprint, render_template, send_from_directory, abort, redirect, request

from util import *

views = Blueprint(__name__, "views")
logging.basicConfig(level=logging.DEBUG)


@views.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)


def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "access_token" not in session:
            return abort(401)
        else:
            return function()

    return wrapper


@views.route("/login")
def login():
    authorization_url = get_authorization_url(get_https_redirect_call_back_url(request.root_url))
    return redirect(authorization_url)


@views.route("/callback")
def callback():
    if not session["state"] == request.args["state"]:
        abort(500)
    set_access_token(request.args["code"], get_https_redirect_call_back_url(request.root_url))
    return redirect("/")


@views.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@views.route("/")
def home():
    if "access_token" in session:
        return render_template("home.html")
    return render_template("welcome.html")


@views.route("/year_data_grouped_by_month")
@login_is_required
def year_data_grouped_by_month():
    months_before = 12
    client = get_splitwise_client()
    update_session_with_current_user_data()
    start_date = date.today() - relativedelta(months=int(months_before))
    expenses = client.getExpenses(dated_after=str(start_date), friend_id=session["id"], visible=True, limit=999999)
    df = pd.DataFrame.from_records(vars(o) for o in expenses)
    df = df.query('payment == False')
    df = df.query("creation_method != 'debt_consolidation'")
    df = df.query("currency_code == '{}'".format(session["default_currency"]))

    data = pd.DataFrame()
    data["month"] = df["date"].apply(
        lambda date: datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m"))
    data["category"] = df["category"].apply(lambda category: category.getName())
    data["cost"] = df["users"].apply(get_my_spending)

    data_group_by_month = data.groupby(['month', 'category']).agg({'cost': 'sum'}).reset_index()

    fig = px.bar(data_group_by_month, x='month', y='cost', color='category',
                 barmode='stack')
    fig.update_layout(
        xaxis_title='Month',
        paper_bgcolor='rgba(0,0,0,0)',
        yaxis_title='Cost ({})'.format(session["default_currency"])
    )
    graph_html = fig.to_html(full_html=False)
    return render_template('year_data_grouped_by_month.html', graph_html=graph_html)
