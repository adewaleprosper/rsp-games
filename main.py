import random
print("Rock Paper Scissors Game")
print("Please Enter Your Name")
user_name = (input())
#player inputs name
print("Welcome " + user_name + " You are Player1" )
print(user_name + " Please pick an option")

def rpc():
    print("Rock(R), Paper(P), Scissors(S)")
    print("Options:(R),(P),(S)")
    print("Select an option from the options listed above.")
    p_opt = ["R", "P", "S"]
    user_option_1 = (input())
    user_option = user_option_1.upper()
    cpu = (random.choice(p_opt))
    #user selects an option
    if user_option in p_opt:
        print("Player1 selected " + str(user_option))
        print("CPU selected " + str(cpu))
        print("Player:(" + str(user_option) + ")" + "CPU:(" + str(cpu) + ")")
        if user_option == p_opt[1] and cpu == p_opt[0]:
            print("Rock beats Scissors")

        if user_option == p_opt[0] and cpu == p_opt[2]:
            print("Paper beats Rock")

        if user_option == p_opt[2] and cpu == p_opt[1]:
            print("Scissors beats Paper")
        elif user_option == cpu:
            print("It's a tie. Retry")
            rpc() 
    else:
        print("Your option is invalid, Kindly select an option from the listed options.")
        rpc()


rpc()



