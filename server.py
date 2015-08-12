from flask import Flask
import keygen

app = Flask(__name__)


@app.route('/updates')
def get_updates():
    return keygen.update_tweets()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
