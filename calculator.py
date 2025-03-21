def calculator():
    # record the users inputs
    num = float(input("Enter a digit"))
    num1 = float(input("Enter a second digit"))
    sign = input("Enter a operation sign eg. +, - etc.")

    #Perform as per users operation sign
    if sign == '+':
        result = num + num1
    elif sign == '-':
        result = num - num1
    elif sign == '*':
        result = num * num1
    elif sign == '/':
        if num1 != 0:
            result = num / num1
        else:
            print("You cannot divide by zero!")
            return
    else:
        print("Invalid operation sign")
        return
    
    #Print the results of users inputs
    print("Your answer is ", result)

calculator()