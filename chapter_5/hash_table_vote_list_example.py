voted = {}

def verify_elector(name):
    if voted.get(name):
        print("Go away, " + name + "!")
    else:
        voted[name] = True
        print(name + " can vote.")

verify_elector("Tom")
verify_elector("Mike")
verify_elector("Suzy")
verify_elector("Mike")