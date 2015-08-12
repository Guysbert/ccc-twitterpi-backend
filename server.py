from flask import Flask
from flask.ext.cors import CORS
import keygen

app = Flask(__name__)
CORS(app)

@app.route('/updates')
def get_updates():
    return keygen.update_tweets()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
