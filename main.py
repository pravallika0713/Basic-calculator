user_input = int(input("Enter number\n"))
user_input_2 = int(input("Enter another number\n"))
function = int(input("choose 1:Addition 2:Substraction 3:multiplication 4:Division\n"))

def switch(function):
    if function == 1:
        return( user_input + user_input_2)

    if function == 2:
        return (user_input - user_input_2)

    if function == 3:
        return (user_input * user_input_2)

    if function == 4:
        return (user_input / user_input_2)


print(switch(function))