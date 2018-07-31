known_users = ["Alice","Bob","Claire","Levent","Fred","Harry"]

print(len(known_users))

while True:
    print("Hi! My name is Machine")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").strip().lower()

        if remove == "y":
            print(known_users)
            known_users.remove(name)
            print(known_users)
        elif remove == "n":
            print("No problem, I didn't want you to leave anyway!")
        
    else:
        print("I can't find your name in my list, sorry {}".format(name))
        add_user = input("Would you like to be added to the system (y/n)?: ").strip().lower()

        if add_user == "y":
            print(known_users)
            known_users.append(name)
            print(known_users)
        elif add_user == "n":
            print("No worries, see you around!")
            
