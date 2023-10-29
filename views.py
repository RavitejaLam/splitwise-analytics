from flask import Blueprint, render_template, send_from_directory
import logging
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import plotly.express as px

from util import Util

views = Blueprint(__name__, "views")
logging.basicConfig(level=logging.DEBUG)


@views.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)


@views.route("/")
def home():
    return render_template("home.html")


@views.route("/year_data_grouped_by_month")
def dashboard():
    months_before = 12
    util_instance = Util()
    client = util_instance.get_splitwise_client()
    my_id = util_instance.get_my_id()
    start_date = date.today() - relativedelta(months=int(months_before))
    expenses = client.getExpenses(dated_after=str(start_date), friend_id=my_id, visible=True, limit=999999)
    df = pd.DataFrame.from_records(vars(o) for o in expenses)
    df = df.query('payment == False')

    data = pd.DataFrame()
    data["month"] = df["date"].apply(
        lambda date: datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m"))
    data["category"] = df["category"].apply(lambda category: category.getName())
    data["cost"] = df["users"].apply(util_instance.get_my_spending)

    data_group_by_month = data.groupby(['month', 'category']).agg({'cost': 'sum'}).reset_index()

    fig = px.bar(data_group_by_month, x='month', y='cost', color='category', barmode='stack')
    graph_html = fig.to_html(full_html=False)
    return render_template('year_data_grouped_by_month.html', graph_html=graph_html)
