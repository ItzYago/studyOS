##Lógica do terminal

from tasks import tasks

def termi_logic():
    user = tasks()

    if user == "help":
        print("Português\nMatemática\nQuímica\nFísica\nHistória\nEspanhol")


