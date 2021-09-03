import random

user_action = "y"
username = input("What is your name?: ")
print(f"Okay! {username} Type 'roll' to roll your dice")
action = input()
while user_action == "y":
    
    if action == "roll":
        number = random.randint(1, 6)
    

    if number == 1:
        print("[       ]")
        print("[       ]")
        print("[   0   ]")
        print("[       ]")
        print("[       ]\n")
    
    elif number == 2:
        print("[       ]")
        print("[       ]")
        print("[ 0   0 ]")
        print("[       ]")
        print("[       ]\n")
    
    elif number == 3:
        print("[ 0     ]")
        print("[       ]")
        print("[   0   ]")
        print("[       ]")
        print("[     0 ]\n")

    elif number == 4:
        print("[       ]")
        print("[ 0   0 ]")
        print("[       ]")
        print("[ 0   0 ]")
        print("[       ]\n")
    
    elif number == 5:
        print("[ 0   0 ]")
        print("[       ]")
        print("[   0   ]")
        print("[       ]")
        print("[ 0   0 ]\n")

    elif number == 6:
        print("[ 0   0 ]")
        print("[       ]")
        print("[ 0   0 ]")
        print("[       ]")
        print("[ 0   0 ]\n")

    user_action = input("Press 'y' to play again otherwise type 'n' to exit:  ")
    if user_action == "n":
        break
