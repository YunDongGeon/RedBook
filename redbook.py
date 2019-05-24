from flask import Flask, render_template
from flask import send_from_directory
from module import dbModule
app = Flask(__name__, static_url_path="/templates")

app.debug - True

@app.route("/<path:path>")
def serve_page(path):
    return send_from_directory('templates', path)

@app.route("/")
def index():
    db_class = dbModule.Database()
    sql = "select * from book_list order by crawl_time desc limit 6"
    row = db_class.recentCrawledBook(sql)
    print(row)
    return render_template("index.html",
                            result = None,
                            resultData = row,
                            resultUPDATE = None)

if __name__ == "__main__":
    app.run()