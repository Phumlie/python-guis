from guizero import App,Text,TextBox,PushButton

def say_my_name():
    currentText = my_name.get()
    welcome_message.set(currentText)
    new_color = my_color.get()
    welcome_message.color(new_color)
    new_size = int(my_size.get())
    welcome_message.font_size(new_size)
    
app = App(title="Hello world", height=400, width=400)

welcome_message = Text(app, text="Welcome to my app", size=20, font="Times New Roman", color="#0000ff")
my_name = TextBox(app, width=30)
my_color = TextBox(app, width=30, text="red")
my_size = TextBox(app, width=30, text="30")
update_text = PushButton(app, command=say_my_name, text="Display my name")
 
app.display()

print("Bye bye!")
