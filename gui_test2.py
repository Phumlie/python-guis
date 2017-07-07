from guizero import App, Combo, Text, CheckBox

app = App(title="My Second GUI App", width=700, height=700, layout="grid")

instructions = Text(app, text="*Please answer the following questions:", grid=[0,1], align="left")
food_choice = Combo(app, options=["None", "Spaghetti", "Rice", "Couscous", "Chickpea Stew"], grid=[1,1], align="left")
food_description = Text(app, text="What's your favourite food?", grid=[1,0], align="left")
juice_choice = Combo(app, options=["None", "Grape Juice", "Orange Juice", "Mango Juice", "Guava Juice", "Apple Juice", "Peach Juice"], grid=[2,1], align="left")
juice_description = Text(app, text="What's your favourite juice?", grid=[2,0], align="left")
lifestyle_choice = CheckBox(app, text="Vegan", grid=[3,1], align="left")
lifestyle_choice2 = CheckBox(app, text="None", grid=[3,2], align="left")
lifestyle_description = Text(app, text="Are you vegeterian or vegan?", grid=[3,0], align="left")

app.display()
