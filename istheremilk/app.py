import flask
import random
app = flask.Flask(__name__)


milk_status = 'unknown'

@app.route('/')
def index():
    return flask.render_template('index.html',
                                 image_num=random.randrange(0, 3))

@app.route('/status', methods=['GET'])
def status():
    return milk_status

@app.route('/yes', methods=['POST'])
def yes():
    global milk_status
    milk_status = 'yes'
    return "True"

@app.route('/no', methods=['POST'])
def no():
    global milk_status
    milk_status = 'no'
    return "True"

@app.route('/almost', methods=['POST'])
def almost():
    global milk_status
    milk_status = 'a bit'
    return "True"
