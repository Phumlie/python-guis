from guizero import App, Text, TextBox, PushButton, Slider, Picture

def say_my_name():
    welcome_message.set( my_name.get() )
    welcome_message.color( my_color.get() )
    welcome_message.font_size( my_size.get() )

def change_text_size(slider_value):
    welcome_message.font_size(slider_value)
    my_size.set(slider_value)

windowSize = 600
app = App(title="My Hello World", height=windowSize, width=windowSize)

welcome_message = Text(app, text="Welcome to my app", size=10, font="Times New Roman", color="#0000ff")
my_name = TextBox(app, width=30, text=welcome_message.get())
my_color = TextBox(app, width=30, text="red")
my_size = TextBox(app, width=30, text="30")
update_text = PushButton(app, command=say_my_name, text="Display my name")
text_size = Slider(app, command=change_text_size, start=10, end=52)
my_pikachu = Picture(app, image="pikachu.gif")

app.display()

print("Bye bye!!!")
