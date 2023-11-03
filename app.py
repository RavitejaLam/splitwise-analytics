from flask import Flask

from views import views

app = Flask(__name__)
app.config['STATIC_URL_PATH'] = '/static'
app.secret_key = "tmp-secret"
app.register_blueprint(views, url_prefix="/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
