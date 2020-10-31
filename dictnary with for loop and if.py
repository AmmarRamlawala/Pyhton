dict1 = {"Ammar":"Argamerx","Batul":"batul@1982","host":"khatarnak","User":"Faltu"}
inp1 = input("Enter your name ")
inp2 = input("Enter your password ")
if inp1 =="host" and inp2 == "khatarnak":
    for infom , names in dict1.items():
        print(infom, names)

else:
    print("Only host have access to names and passwords")
 


