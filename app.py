import flask
import redis
import random
app = flask.Flask(__name__)

r = redis.Redis(decode_responses=True)

@app.route('/')
def index():
    return flask.render_template('index.html',
                                 image_num=random.randrange(0, 3))

@app.route('/status', methods=['GET'])
def status():
    return r.get('status') or "no"

@app.route('/set_yes', methods=['POST'])
def set_yes():
    r.set('status', 'yes')
    return "hello"

@app.route('/set_no', methods=['POST'])
def set_no():
    r.set('status', 'no')
    return "hello"

@app.route('/set_almost', methods=['POST'])
def set_almost():
    r.set('status', 'a bit')
    return "hello"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

