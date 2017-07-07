from guizero import App, Text, Combo, TextBox, PushButton, ButtonGroup, info

def open_instr():
    info("Instructions", "Birthday Reminder is an app you can use to set your friends', family's, or relatives' birthdays so that you can never forget them.")

def set_reminder():
    info("Setting Reminder","Your birthday reminder has been set!")
    print ("\nName: "+my_name.get())
    print ("Surname: "+type_surname.get())
    print ("D.O.B: "+type_dateofbirth.get())
    print ("Gender: "+gender.get())

Rod = App(title="Birthday Reminder", height=1000, width=1900, layout="grid")

welcome_message = Text(Rod, text="Welcome to Birthday Reminder", grid=[0,1], align="left", size=20, font="Helvetica", color="purple")
instruction = PushButton(Rod, command=open_instr, text="Instructions", grid=[0,0], align="left")
sign_in = Text(Rod, text="*Please enter the details below*:", grid=[5,0], align="left", size=15, color="blue")
my_name_label = Text(Rod, text="Name:", grid=[10,0], align="left", size=15, color="red")
my_name = TextBox(Rod, width=30, grid=[10,1], align="left")
my_surname = Text(Rod, text="Surname:", grid=[11,0], align="left", size=15, color="orange")
type_surname = TextBox(Rod, width=30, grid=[11,1], align="left")
my_dateofbirth = Text(Rod, text="Date of Birth:", grid=[12,0], align="left", size=15, color="green")
type_dateofbirth = TextBox(Rod, width=30, grid=[12,1], align="left")
my_gender = Text(Rod, text="Gender:", grid=[13,0], align="left", size=15, color="navy")
gender = ButtonGroup(Rod, options=[ ["Female", "F"],["Male", "M"] ], selected="F", horizontal=True, grid=[13,1], align="left")
set_bdr = PushButton(Rod, command=set_reminder, text="Set Reminder", grid=[14,1], align="left")

