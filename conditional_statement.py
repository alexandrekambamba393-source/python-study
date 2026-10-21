#conditional statements => to make decisions based on a result of a certain condition
#conditions are created using comparaison operators (==,>,<,>=,<=,!=)
#conditions returns booleans (True or false)
#Pythons uses three primary keywords on conditional statements (if, else, elif)

    #if statements 
# Execute a block of code only when the condition is true 
    #syntax 
  # if condition:
         #block of code
if 20>10:
     print('twenty is greater')


age=20 

if age>18:
     print("adult")

# auth users with age from 18 to 60 
if age>=18 and age<=60:
   print("allow access")
    


# check if  the temperature is above 30 print too hot 

temperature=32 

if temperature>30: 
   print("too hot")

# if else statements 
# => else executes the else block when the conditions is false. You can't write else without if 

        #syntax
    # if condition 
           # if block 
    # else: 
           # else block

# print pass if the students marks is above 50 otherwise fall

marks=51

if marks>50:
    print("pass")
else:
    print("fail")

# if-elif-else => to check multiple conditions with diff outcomes or results 

# print pass if student marks is above 70, print average if amrks is 50 to 70 otherwise fail 

if marks>70: 
    print('pass')

elif marks>= 50 and marks<=70: 
     print('average')

else : 
      print('fail')     


# print A if marks is above 80 
# print B if marks is above 70
# print C if marks is above 60 
# print D of marks is above 50 
# otherwise print E

marks=65

if marks>80: 
   print('A')

elif marks>70:
     print('B')

elif marks>60:
     print('C')

elif marks>50:
     print('D')

else : 
      print('fail')

      #task 
      #slide 56 1 to 4 
      #slide 58 
      #slide 59 3 and 4
      
         # nested if