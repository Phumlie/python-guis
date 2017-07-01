
name = input("What is your name?\n")

while True:
    if name == "exit":
        break
    
    if name == "Phumli":
        print("Hi "+name+"... You are a girl")
    else:
        print("Hi "+name+". You are a boy")
    print("")
    name = input("What is your name?\n")

print("\nBye bye")
