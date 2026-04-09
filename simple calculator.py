num1 = float(input("enter a value: "))
num2 = float(input("enter another value: "))
operation = input("enter an operation(+,-,*,/): ")

if operation =="+":
    result = num1 + num2
    print("answer: ",result)
elif operation =="-":
    result = num1 - num2
    print("answer: ",result)
elif operation =="*":
    result = num1 * num2
    print("answer: ",result)
elif operation =="/":
    if num1 != 0 or num2 != 0:
        result = num1/num2
        print("answer",result)
    else:
        print("MATH ERROR!")
else:
    print("Invalid operation entered")