from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", name="Doğa")


@app.route("/futbol")
def futbol():
    return render_template("futbol.html", name = "Doğa")


@app.route("/ozel")
def ozel():
    return render_template("ozel.html", name="Doğa")

if __name__ == "__main__":
    app.run(debug=True)