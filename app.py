from flask import Flask, render_template, request, url_for, redirect
import mlab
from post import Post
from menu import Menu

app = Flask(__name__)
mlab.connect()

@app.route("/", methods=["GET","POST"])
def caculate():
    menu = Post.objects()
    if request.method == "GET":
        return render_template("function.html")
    elif request.method == "POST":
        form = request.form
        sex = form["sex"]
        weight = float(form["weight"])
        height = float(form["height"])
        age = int(form["age"])
        exercise = int(form["exercise"])
        raw_bmr= 9.99*weight + 6.25*height - 4.92*age
        sex_list = ["male", "female"]
        for sex in sex_list:
            if sex == "male":
                bmr= raw_bmr+5
            elif sex == "female":
                bmr= raw_bmr-161
        
        if exercise == 0:
            need = bmr*1.2
        elif exercise == 1:
            need = bmr*1.375
        elif exercise == 2:
            need = bmr*1.55
        elif exercise == 3:
            need = bmr*1.725
        elif exercise == 4: 
            need = bmr*1.9
        
        return render_template("bmr.html", bmr=str(bmr), need=str(need), post=menu)

@app.route("/menu/<post_id>")
def menu(post_id):
    menu = Menu.objects().with_id(post_id)
    return render_template('menu.html', menu=menu)


if __name__ == "__main__":
    app.run(debug=True)
