from guizero import App, Combo, Text, CheckBox, ButtonGroup, PushButton, info

def do_ordering():
    info("Ordering", "Thank you for ordering!!")
    print( food_choice.get() )
    print( lifestyle_choice.get_value() )
    print( sauce_choice.get() )

app = App(title="My Second GUI App", width=700, height=700, layout="grid")

instructions = Text(app, text="Please answer the following questions:", grid=[0,0], align="left")
food_choice = Combo(app, options=["None", "Spaghetti", "Rice", "Couscous", "Chickpea Stew"], grid=[1,1], align="left")
food_description = Text(app, text="Which food would you like?", grid=[1,0], align="left")
juice_choice = Combo(app, options=["None", "Grape Juice", "Orange Juice", "Mango Juice", "Guava Juice", "Apple Juice", "Peach Juice"], grid=[2,1], align="left")
juice_description = Text(app, text="Which juice would you like?", grid=[2,0], align="left")
lifestyle_choice = CheckBox(app, text="Vegan", grid=[3,1], align="left")
lifestyle_choice2 = CheckBox(app, text="None", grid=[3,2], align="left")
lifestyle_description = Text(app, text="Do you want your food to be vegeterian or vegan?", grid=[3,0], align="left")
sauce_choice = ButtonGroup(app, options=[ ["Cheese Sauce", "CS"], ["Tomato Sauce", "TS"], ["Pesto Sauce", "PS"] ], selected="TS", horizontal=True, grid=[4,1], align="left")
sauce_description = Text(app, text="Which sauce would you want in your food?", grid=[4,0], align="left")
order_food = PushButton(app, command=do_ordering, text="Order food", grid=[5,1], align="left")

app.display()
