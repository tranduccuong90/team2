from flask import Flask, render_template, request
import mlab
from post import Post

app = Flask(__name__)
mlab.connect()

@app.route("/", methods=["GET","POST"])
def caculate():
    if request.method == "GET":
        return render_template("function.html")
    elif request.method == "POST":
        form = request.form
        sex = form["sex"]
        weight = float(form["weight"])
        height = float(form["height"])
        age = int(form["age"])
        raw_bmr= 9.99*weight + 6.25*height - 4.92*age
        if sex == "male":
            bmr= str(raw_bmr+5)
            return render_template("bmr.html", bmr=bmr)
        elif sex == "female":
            bmr= str(raw_bmr-161) 
            return render_template("bmr.html", bmr=bmr)

if __name__ == "__main__":
    app.run(debug=True)
