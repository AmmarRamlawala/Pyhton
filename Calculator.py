print("this is a calculator It does all oprations but only with 2 numbers ")

opration = input("Enter your opration in symbolic way ")
print("Enter Your first number ")
n1 = int(input())
print("Enter Your second number ")
n2 = int(input())

if opration == "+":
    print(n1 + n2)
elif opration == "-":
    print(n1 - n2)
elif opration == "*":
    print(n1 * n2)
elif opration == "/":
    print(n1 / n2)
else:
    print("illogical Input!!")
