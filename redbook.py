from flask import Flask, render_template
from flask import send_from_directory
from module import dbModule
from pprint import pprint
app = Flask(__name__, static_url_path="/templates")

app.debug - True

@app.route("/<path:path>")
def serve_page(path):
    return send_from_directory('templates', path)

@app.route("/")
def index():
    db_class = dbModule.Database()
    results = db_class.recentCrawledBook()
    pprint(results)
    return render_template("index.html",
                           json=results)

if __name__ == "__main__":
    app.run()