print("===Smart calculator===")
a = float(input("Pehla number:"))
b = float(input("Dusara number:"))
op = input("operation(+,-,*,/):")
if op == "+":
    print("Answer:",(a+b))
elif op == "-":
    print("Answer:", (a-b))
elif op == "*":
    print("Answer:", (a*b))
elif op == "/":
    print("Answer:", (a/b))
else:
    print("Invalid operation!")
