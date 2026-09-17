my_name="Alexandre Kambamba"
#Capitalize -> make the first character have upper case and the rest lower case
print(my_name.capitalize())

#. lower and upper -> make all characters lower case or upper case

text1="MY name IS KeVIn"
print(text1)
text2=text1.lower()
print(text2)
text3=text1.upper()
print(text3)

# strip -> used to remove leading and trailing spaces 

text4="   My name is Alexandre        "
print(len(text4))
print(text4)
text5=text4.strip()
print(len(text5))


# Clean sentence1 to "Python programming"
sentence1="    PYthon programmiNG    "
sentence1=sentence1.strip()
sentence1=sentence1.capitalize()

print(sentence1)
# Clean sentence2 to "SOFTWARE DEVELOPMENT"
sentence2="Software DEVELOPMENT    "
sentence2=sentence2.strip()
sentence2=sentence2.upper()
print(sentence2)

# Clean sentence3 to "computer science"
sentence3="   COMputer SCieNCE   "
sentence3=sentence3.strip()
sentence3=sentence3.lower()
print(sentence3)


# replace -> used to replace a string with another string

sentence4="I am a python Developer"
sentence4=sentence4.replace("python", "Java")
print(sentence4)

sentence5="I am a python Developer"
sentence5=sentence5.replace("python ", "")
print(sentence5)

#count-> used to count the appearance of a character in a string 
sentence4="I am a python Developer"
sentence5=sentence4.count("a")
print(sentence5)


#split -> used to split a string using a character in the string
sentence6="I am a python Developer"
sentence6=sentence6.split(" ")
print(sentence6)

sentence6="I am a python Developer"
sentence6=sentence6.split("p")
print(sentence6)

#change sentence6 to Alex Mwangi 
sentence6="Alex Kimani"
sentence6=sentence6.replace("Kimani", "Mwangi")
print(sentence6)

#count the number of times o has appeared in the sentence7
sentence7="Python programming"
sentence8=sentence7.count("o")
print(sentence8)

# Split sentence8 using the colon
sentence8="Alex:Brian:Mike:Kevin"
sentence8=sentence8.split(":")
print(sentence8)