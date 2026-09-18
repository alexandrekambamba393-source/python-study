#Questions create a new file
#Convert a float to an integer with an inbuilt function in Python

temp=56.8926    #to 57
#Convert the float below to give the results as follows
temp=56.8926  #to 56.89"
temp2=round(temp,2)
print(temp2) 

#Convert the float below to give the results as follows
temp= 56.8926   #to 56.893 
temp3=round(temp,3)
print(temp3)

#Convert the float below to give the results as follows
#temp=56.8926 to 8.926 
#NB: Use string  slice & concatenation, but have result as float 

temp=56.8926

# Convert to a string 
# str()-> converts variables into strings
temp=str(temp)#'56.8926'

#Slice 
temp=temp[3:]
#Concat
temp=temp[0]+'.'+temp[1:] #8 + '.' + 926
print(temp) #8926

#Float() -> converts numeric variables to floats 
temp=float(temp)
print(type(temp)) 

#convert to 5.678
my_float=5678.4567
my_float=str(my_float)
my_float=my_float[0:4]
my_float=my_float[0]+'.'+my_float[1:]
print(my_float)
my_float=float(my_float)
print(type(my_float))



# Attempt questions below. Whether you get the right answer or not, still read the solution explanation.
#https://realpython.com/quizzes/python-data-types/
