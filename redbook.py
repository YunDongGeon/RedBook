from flask import Flask, render_template
from flask import send_from_directory

app = Flask(__name__, static_url_path="/templates")

app.debug - True

@app.route("/<path:path>")
def serve_page(path):
    return send_from_directory('templates', path)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()