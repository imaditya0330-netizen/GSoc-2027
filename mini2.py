# def add(a,b):
#     return a+b
# def subtract(a,b):
#     return a-b
# def multiply(a,b):
#     return a*b
# def divide(a,b):
#     if b == 0:
#         return "Error! Zero se divide nhi kr sakte!"
#     return a/b

# print(add(10,5))
# print(subtract(10,5))
# print(multiply(10,5))
# print(divide(10,5))  

#
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