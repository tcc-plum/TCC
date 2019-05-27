from flask import Flask, render_template, url_for, request
from flask_restful import Api, Resource
from sky_biometry import SkyBiometry
## from base import Sky

# url_for('static', filename='arquivo.teste')

app = Flask(__name__)
api = Api(app)

@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template('index.html', title='Home')

@app.route("/sky")
def skypage():
    return render_template('skypage.html', title= 'API')

@app.route("/gallery")
def gallery():
    return render_template('gallery.html', title='Gallery')

## RUNNING AND DEBUGGING
if __name__ == '__main__':
    app.run(debug=True)
