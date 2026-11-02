a = float(input("Первое число:"))
operation = input("Операция (+, -, *, /): ")
b = float(input("Второе число: "))

if operation == "+":
    print (a + b)
elif operation == "-":
    print (a - b)
elif operation == "*":
    print (a * b)
elif operation == "/":
    if b == 0:
        print("На ноль делить нельзя")
    else:
        print (a / b)
else:
    print("Неизвестная операция")

# v_2 - дописано деление на 0 + сценарий неизвестной операции