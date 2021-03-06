from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def root():
        return render_template("base.html")

@app.route("/response", methods = ["GET", "POST"])
def response():
        return render_template("response.html", name = request.args["userName"], reqMethod = request.method)
if __name__ == "__main__":
        app.debug = True
        app.run()