import random

possible_actions =["R","P","S"]
while True:
    user_action = input("Enter a choice (R:rock,P:paper,S:scissors): ")
    cpu_action =random.choice(possible_actions)
    user_action_caps=user_action.upper() 
    if user_action_caps in possible_actions:
        print(f"Player({user_action_caps}) : CPU({cpu_action}) ")
        if user_action_caps == cpu_action :
            print('It is a tie')
        elif user_action_caps=="R" and cpu_action=="P":
            print('computer wins')
            break
        elif user_action_caps=="P" and cpu_action=="R":
            print('user wins')
            break
        elif user_action_caps=="S" and cpu_action=="P":
            print('user wins')
            break
        elif user_action_caps=="P" and cpu_action=="S":
            print('computer wins')
            break
        elif user_action_caps=="S" and cpu_action=="R":
            print('computer wins')
            break
        elif user_action_caps=="R" and cpu_action=="S":
            print('user wins')
            break
    else :
        print('invalid choice')
