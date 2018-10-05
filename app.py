from flask import Flask, render_template, request, url_for, redirect
import mlab
from post import Post
from menu import Menu
from random import choice

app = Flask(__name__)
mlab.connect()

@app.route("/", methods=["GET","POST"])
def caculate():
<<<<<<< HEAD
    menu = Menu.objects()
=======
>>>>>>> 11846f12e8998782344372d66b1a81bf2e0109e9
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
<<<<<<< HEAD
        
        return redirect(url_for("menu", need=need, bmr=bmr)) #bmr=str(bmr), need=str(need), menu=menu)
=======
        return redirect(url_for("bmr", need=need, bmr=bmr))
        # return render_template("bmr.html", bmr=str(bmr), need=str(need), post=menu)
>>>>>>> 11846f12e8998782344372d66b1a81bf2e0109e9

@app.route("/menu/<float:need>/<float:bmr>")
def menu(need, bmr):
    menu = Menu.objects()
    breakfasts = Menu.objects(category="Ăn sáng")
    rices = Menu.objects(category="Cơm")
    meats = Menu.objects(category="Thịt")
    vegs = Menu.objects(category="rau")
    fruits = Menu.objects(category="hoa qua") 
    snacks = Menu.objects(category="món phụ")
    
    menu_list=[]

<<<<<<< HEAD
    breakfast = choice(breakfasts)
    print(type(need))
    print(type(breakfast['calori']))
    need1 = need - breakfast["calori"]
    rice = choice(rices)
    need2 = need1 - 2*rice["calori"]
    meat = choice(meats)
    need3 = need2 - 2*meat["calori"]
    veg = choice(vegs)
    need4 = need3 - 2*veg["calori"]
    print(breakfast)
    menu_list.append(breakfast)
    menu_list.append(rice)
    menu_list.append(meat)
    menu_list.append(veg)
    for snack in snacks:
        if 0 <= snack["calori"] <= 0.2*need is True:
            menu_list.append[snack]
        else: 
            pass
    print(menu_list)
    # return render_template('menu.html', menu=menu)
    return render_template('menu.html', breakfast = breakfast, bmr=bmr, need=need, snacks=snacks)
=======
@app.route("/bmr/<need>/<bmr>")
def bmr(need, bmr):
    
    food = Menu.objects(category="rau")
    # return "abc"
    return render_template("bmr.html", mondays = mondays)


>>>>>>> 11846f12e8998782344372d66b1a81bf2e0109e9

if __name__ == "__main__":
    app.run(debug=True)
