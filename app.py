from flask import Flask, render_template, request, url_for, redirect
import mlab
from post import Post
from menu import Menu
from random import choice

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
        exercise = int(form["exercise"])
        raw_bmr= 9.99*weight + 6.25*height - 4.92*age
        sex_list = ["male", "female"]
        for sex in sex_list:
            if sex == "male":
                bmr= raw_bmr+5
            elif sex == "female":
                bmr= raw_bmr-161

#Tính chỉ số TDEE giữ cân:       
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

#Tính chỉ số BMI, gợi ý tăng giảm cân
        bmi = weight/((height/100)**2)
        if bmi < 18.5:
            status = "Gầy"
            suggest = need*1.2
        elif 18.5 <= bmi <24.9:
            status = "Bình thường"
            suggest = need
        else:
            status = "Béo"
            suggest = need*0.8
        return redirect(url_for("menu", need=round(need,2), bmr=bmr, bmi=bmi, status=status, suggest=round(suggest,2)))
        
@app.route("/menu/<float:need>/<float:bmr>/<status>/<float:suggest>")
def menu(need, bmr, status, suggest):

#Phân loại món ăn
    menu_week = []
    menu = Menu.objects()
    breakfasts = Menu.objects(category="Ăn sáng")
    rices = Menu.objects(category="Cơm")
    meats = Menu.objects(category="Thịt")
    vegs = Menu.objects(category="rau")
    fruits = Menu.objects(category="hoa qua") 
    snacks = Menu.objects(category="món phụ")
    

    for i in range(7):
        menu_list=[]

#Công thức tính tổng lượng
        breakfast = choice(breakfasts)
        suggest1 = suggest - breakfast["calori"]
        rice = choice(rices)
        suggest2 = suggest1 - rice["calori"]
        meat1 = choice(meats)
        meat2 = choice(meats)
        suggest3 = suggest2 - meat1["calori"] - meat2["calori"]
        veg1 = choice(vegs)
        veg2 = choice(vegs)
        suggest4 = suggest3 - veg1["calori"] - veg2["calori"]
        
        menu_list.append(breakfast)
        menu_list.append(rice)
        menu_list.append(meat1)
        menu_list.append(meat2)
        menu_list.append(veg1)
        menu_list.append(veg2)
        
        snack = choice(snacks)
        if suggest4 < snack["calori"]:
            snack = choice(snacks)
        else:
            menu_list.append(snack)
        menu_week.append(menu_list)

   
    return render_template('menu.html', bmr=bmr, status=status, need=need, suggest=suggest, menu_week=menu_week)

if __name__ == "__main__":
    app.run(debug=True)
