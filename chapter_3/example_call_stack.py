def greet(name):
    print("Hi, " + name + "!")
    greet2(name)

def greet2(name):
    print("How are you, " + name + "?")
    bye()

def bye():
    print("Okay. Bye bye!")

name = "Maggie"

# it calls the greet2 inside of it
# greet2 calls bye inside of it
# when bye finishes, greet2 will finish
# then greet's execution will be finished, after all functions inside of it finish.
greet(name)