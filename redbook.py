from flask import Flask, render_template, request, send_from_directory, jsonify, json
from module import dbModule
from pprint import pprint
from jinja2 import UndefinedError

app = Flask(__name__, static_url_path="/templates")

app.debug = True


@app.route("/<path:path>")
def serve_page(path):
    return send_from_directory('templates', path)


@app.route("/")
def index():
    db_class = dbModule.Database()
    results = db_class.recentCrawledBook()
    results = json.loads(results)
    pprint(results)
    return render_template("index.html",
                           json=results)


@app.route("/search.html", methods=['post'])
def search():

    db_class = dbModule.Database()
    results = db_class.find(request.form['keyword'])
    try:
        results = json.loads(results)
        pprint(results)
        return render_template("search.html",
                               json=results)
    except UndefinedError:
        return render_template("search_fail.html",
                               json=results)


@app.route("/interBook/<page>", methods=['get'])
def interBook(page):
    db_class = dbModule.Database()
    print(page)
    results = db_class.load(page)
    results = json.loads(results)
    pprint(results)
    return jsonify(results)

@app.route("/getCount", methods=['get'])
def getCount():
    db_class = dbModule.Database()
    count = json.loads(db_class.getCount())
    return jsonify(count)


if __name__ == "__main__":
    app.run()
