#!/usr/bin/python3
# Calculator Program
# Programmer: Nexus
# Date: 20211228
while 1:
    first_no = float(input('Please enter first number: '))
    operator = input('Please Enter operator: ')
    second_no = float(input('Please enter second number: '))
    if operator == '+':
        result = first_no + second_no
    elif operator == '-':
        result = first_no - second_no
    elif operator == '*':
        result = first_no * second_no
    elif operator == '/':
        result = first_no / second_no
    elif operator == '%':
        result = first_no % second_no
    else:
        print("wrong operator ")

    print("Result is: ",result)
