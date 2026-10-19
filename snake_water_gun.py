'''
snake = 1
water = -1
gun = 0

'''

import random
computer = random.choice([1, -1, 0])
you = input("Enter your choice:")
youDict = {"s" : 1 , "w" : -1 , "g" : 0}
reversedict = {1 :"Snake" , -1 : "Water" , 0 : "Gun"}
younum = youDict[you]

print(f"Computer choose {reversedict[computer]} \nyou choose {reversedict[younum]}")

if computer == younum:
     print("Both are same \nIt's Draw")
 
else: 
     if computer == -1 and younum == 1:
       print("You win!")

     elif computer == 1 and younum == -1:
       print("You lose!")

     elif computer == 1 and younum == 0 :
      print("You win")

     elif computer == 0 and younum == 1:
        print("You lose!")        

     elif computer == 0 and younum == -1 :
        print("You win!")

     elif computer == -1 and younum == 0:
        print("You lose!")          
 
     else : 
         print("Something went wrong....")     




