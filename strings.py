first_name="Alexandre"
last_name="Kambamba"
full_name=first_name+" "+last_name
print(full_name)


num1="100"
num2="200"

total=num1+num2
print(total)
# When we add strings the concat 

# indexing and slicing 
# indexing=> used to when accessing characters in a string 
# Every character in string variable has a numeric representation 
# Starting on the left we start with 0 
# Starting on the right we start with -1

text="I am a software developer"
print(text[3])
print(text[-5])

# t and e from software 
print(text[10])
print(text[-11])
#  Slicing 
# =>Extracting a part of a string using indexing 
# [starting_index:end_index+1]

print(text[7:15])
print(text[16:])

text1="I am student doing software Development and We are learning Python Programming"

#Software Development 
print(text1[19:39])

#Python programming 
print(text1[60:])

#I am a student 

print(text1[0:12])

#len() used to counts the number of all characters in a string  
print(len(text1))