
"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
    user_input = input('Enter your equation: ')

    tokens = user_input.split(' ')
    # print(tokens)
    # [add 2 3]
    if 'q' in tokens:
        print('You will exit')
        break

    # check the length of arguments that user inputs
    if len(tokens) > 3 or len(tokens) < 2:
        print('please enter 2 or 3 inputs')
        continue
    else:
        if len(tokens) == 2:
            operator = tokens[0]  
            num1 = tokens[1] 
        else:
            operator = tokens[0]  
            num1 = tokens[1] 
            num2 = tokens[2] 
    
    # check if the num1 and num2 are the numbers
    if not num1.isdigit() or not num2.isdigit():
        print('Please enter numbers')
        continue 
    
    result = None

    if operator == '+':
        result = add(float(num1), float(num2))

    elif operator == '-':
        result = subtract(float(num1), float(num2))

    elif operator == '*':
        result = multiply(float(num1), float(num2))

    elif operator == '/':
        result = divide(float(num1), float(num2))

    elif operator == 'square':
        result = square(float(num1))

    elif operator == 'cube':
        result = cube(float(num1))

    elif operator == 'pow':
        result = pow(float(num1), float(num2))

    elif operator == 'mod':
        result = mod(float(num1), float(num2))

    
    print(result)

    


 
