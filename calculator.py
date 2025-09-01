#mini project:- simple calculator
#Take input Two numbers
print('-----------welcome to simple calculator-------------')
num1 = float(input('Enter 1st number:'))
num2 = float(input('Enter 2nd number:'))
#choose operator
operators = input('Enter Operator(+,-,*,/,%,//,**):')
if operators == '+':
    print(f"addition:{num1+num2}")
elif operators == '-':
    print(f"substraction:{num1-num2}")
elif operators == '*':
    print(f"multiplication:{num1*num2}")
elif operators == '/':
    if num2!=0:
        print(f"division:{num1/num2}")
    else:
        print("Error! Division by zero.")
elif operators == '%':
    print(f"modulus:{num1%num2}")
elif operators == '//':
    if num2!=0:
        print(f"FloorDivision:{num1//num2}")
    else:
        print("Error! Division by zero.")
elif operators == '**':
    print(f'exponentiation:{num1**num2}')
else:
    print("Invalid Operator!")
print('------------Thanks for calculating---------------')