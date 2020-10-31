opration = input("Enter the symbol of your opration")
print("Enter Your first number")
n1 = int(input())
print("Enter Your second number")
n2 = int(input())

if(n1 == 45 and n2 == 3 and opration =="*") or (n1 == 3 and n2 == 45 and opration == "*"):
    print("555")

elif(n1 == 56 and n2 == 9 and opration =="+") or (n1 == 9 and n2 == 56 and opration == "+"):
    print("77")

elif(n1 == 56 and n2 == 6 and opration =="/") or (n1 == 6 and n2 == 56 and opration == "/"):
    print("4")
elif opration == "+":
    print(n1 + n2)
elif opration == "-":
    print(n1 - n2)
elif opration == "*":
    print(n1 * n2)
elif opration == "/":
    print(n1 / n2)
else:
    print("illogical Input!!")




 


