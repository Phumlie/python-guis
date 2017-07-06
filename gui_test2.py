from guizero import App, Combo, Text

app = App(title="My second GUI app", width=700, height=700, layout="grid")

film_choice = Combo(app, options=["None", "Pasta", "Rice", "Couscous"], grid=[0,1], align="left")
film_description = Text(app, text="Which food is your favourate?", grid=[0,0], align="left")

app.display()
