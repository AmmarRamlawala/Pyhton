print("This is a game in this game you have to guess a number \n and if that number is greater than the orignal number \n then it will display it is too larger and if it is smaller it \n it will print that the entered number is samller than the orignal number\n You only have 8 chances if you enter 1 worng number 1 chance will be diducted\n")
n = 30
chances = 8 

while(True):
    inp = int(input("Enter your number\n"))
    if(chances == 1):
        print("Game over you lost")
   
        break
    elif(inp > n):
        print("Enter a smaller number")
        chances = chances -1
        print("chances left:",chances)
        continue 
    elif(inp < n ):
        print("Enter a greater number")
        chances = chances -1
        print("chances left:",chances)
        continue
    else:
        print("You won")
        chancesLeft = 8 - chances
        print("You took chances:",chancesLeft)
        break