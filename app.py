import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    color = (
        os.environ.get("APP_COLOR")
        if os.environ.get("APP_COLOR")
        else "NOTHING PASSED AS ENV VARIABLE"
    )
    return render_template(
        "hello.html",
        color=color,
    )


app.run(host="0.0.0.0", port=8080, debug=True)
