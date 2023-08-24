'''
Create a country quiz where a user have to guess the name of country that randomly picked from a csv file.All the following points need to be covered in game.

1)some of the characters of the country name  need to be hidden behind underscore.

2)user can guess the name directly or can take hint:

3)If user ask for hint then name of the capital city needs to be displayed from csv file

4)If user guess the name correctly than 10 points will be awarded to user

5)If user guess the name after hint than 5 points will be awarded to user

6)The game ends when user guess the wrong answer

7)The name of top ten score needs to be maintained in a leaderboard file.
'''
#=================================== solution starts =========================================#

import random
import csv
  
# the below  code is for converting the csv file into a list so that we can use it fot our quiz 

# reading the data from a csv file 'country.csv'
with open('country.csv', newline='') as file:
    
    reader = csv.reader(file, delimiter = ',')
      
    # store the headers in a separate variable,
    # move the reader object to point on the next row
    headings = next(reader)
      
    # output list to store all rows
    Output = []
    for row in reader:
        Output.append(row[:])
  
for row_num, rows in enumerate(Output):
    #print('data in row number {} is {}'.format(row_num+1, rows))
    continue
  
print('headers were: ', headings)
print("\n")

# the above code is for converting the csv file into a list so that we can use it fot our quiz 


print("LETS START\n")

#======================================================
# hangman code starts (combining with the above)
#======================================================

# code works by finding the letter u chose or guess (for input x) and shows whether it is
#present or not in the word chosen by the random operator

score=[] 
#=============================== its all under the function test ======================
def test(score):
  
  chance=5              #chance given are only 5
  point=0
  t=True
  tan=0
  
  #================== choosing a country by random and having its list ========================
  
  chosen = random.choice(Output)
  word=list(chosen)

  #print(word)          // it will print the country that is randomly chosen 

  arr=word[0].lower()    # arr stores the state 

  num=list(arr)
  
  #print(num)

  hint=word[1].lower()   #hint stores the capital 

  #print(arr) 
  #print(" for crosschecking if it is printing right or not ",
  #      "its for the user to see if its working right or not ")
  print()
  
  #( will print the country randomly chosen )
  
  key=list(arr)          # key stores the list of arr
    
  #print(hint)            # //will print the capital of  the country randomly chosen

  #print("for crosschecking if it is printing right or not ",
   #     "its for the user to see if its working right or not ")
  print()



  dash= "_"*len(word[0])   # it is the underscore that will later get covered by letters present in arr

  dot=list(dash)

  print("the length of the word is ",len(dot))           #// will be replaced by words  [arr (word[0])] 1 by 1 (letter by letter given by the user)

  #================================================================================ 


  #============================= CHECK SPACEBAR ===================================

  # this below code check if there is a space bar present in the state name or not 
    
  i=" "
  d=arr.find(i)
    
  if d!=0 and d>0:
        print("space is present")  
        
        d=1

  else:
        print("no spacebar is present for the word state")
        d=0
 
  #=====================================================================================
  
  #====================================  WHILE LOOP STARTS =============================
    
  while (t==True):    
    z="0"         
    print()
  
  # this for number of players and is stored in array q 
  
  
    x=input("\n chose(guess) a letter:").lower()
    
    for i in range(0,len(dot)):
      if x == dot[i]:
        print("\nalready used this letter\n")
        chance-=1
        print(chance,"chance left")
        z="1"
        break
      elif x==" " and "*"==dot[i]:
        print("\nalready used this letter\n")
        chance-=1
        print(chance,"chance left")
        z="1"
        break
        
    
    index1=arr.find(x)                  # finding whether the letter is present in arr or not
    index2=arr.count(x)                 # count how many letters are present in arr
    
    if index2!= 0 and z=="0":  
      print("\nThe character",x, "is present in the string",index2," time(s).")
      for  i in range(1):
        for j in range(len(word[0])):
          if arr[j]==x:
            print("\nThe",i+1,"th character", x ," is present in the string at:",j+1,"position")
            if x==" ":
              dot[j]="*"
            else:
              dot[j]=x
            print(dot)  # overwriting  the places with word where the underscore is present 
            j=j+1
          
            
      # asking the user how to proceed next 
      
        print("\n1.DO u want a hint?")
        print("\n2.U want to guess the complete name.?")
        print("\n3.do u wnt to continue.(within the given chances)" )
        print()
        y=input("\nenter 1 or 2  or 3 as per your choice:")
        # taking integer input from the user only (1/2/3)
        if y=="1":
          print()
          print(hint)
          print("\nnow try to guess the country")
          point=5
          tan=1 
          
        elif y=="2":
          ans=input("\nenter  ur word:").lower()
          sol=list(ans)
          if arr==ans :
            if tan!=1:                             # to check if he used a hint or not
              print("\nHURRAY u guessed it right. U WON")
              point=10
              t= False
              break
            else:
              print("\nu won using hint")
              point=5
              t= False
              break
          else:
            print("\nU are wrong . U lost")
            point=0
            t=False
            break
                          # we are using it so we can come to know whether hint is used or not
        
        elif y=="3":
          if dot==key:                    # to check if it matches or not //key=list(arr)
            if tan!=1:
              t=False
              point=10
              break
            else:
              t=False
              point=5
              break
          else:
            
            continue
        elif y>"3":
          print("\nonly valid numbers 1,2,3 are allowed")  #try again 
          continue
          
      if t==False:
        break
      
    else:  
      if z=="0":                    # z is used to check whther the input letter is used again or not
          print('\nThe character is not present in the string') 
          chance=chance-1
          print(chance," chances left")

  if chance <= 5 and point==10 :
    print("\nu won")
    print("\nu scored :",point)
    score.append(point)
    
  elif chance <=5 and point==5:
    print("\nu won but with help of hint")
    print("\nu scored :",point)
    score.append(point)

  else:
    print("\nyou lost better luck next time")
    print("\nu scored :",point)
    score.append(point)
  
#===================================== the  function call ends here  ========================== 

# ===============now for taking the input for number of players====================

a=int(input("enter how many players are playing this quiz:"))
q=[]

for i in range(a):
    print()
    line=input(f"enter the name of {i+1} person:")   
    q.append(line)
    print()
    print(f"its {q[i]} chance")
    test(score)
    print(f"{q[i]} scored ",score[i])
    
#creating a dictionary to store the name and score of each player
my_dict = {q[i]: score[i] for i in range(a)}

print(str(my_dict))

#sorting the list 
sorted_done = sorted(my_dict.items(), key=lambda x:x[1],reverse=True)
#//print(sorted_done)

#converting it into dict
converted_dict = dict(sorted_done)
print(converted_dict)

out = dict(list(converted_dict.items())[0: 10])  
#// this will pick the first 10/top 10 scorer from the quiz and then we print it
print(out)

#============= NOW printing the above result in file =========================

with open("leaderboard.txt", 'w') as file:
    for key, value in out.items(): 
        file.write(' %s  \t:\t %s \n' % (key, value))

#==================================== THE END TO CODE =========================================