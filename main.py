from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/")
def index():
    # return render_template("index.html")
    return jsonify({"api": "ok"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
