# Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class 
name ="  JOHn." "to" "john"

classname="  JOHn." 
classname=classname.replace(".","")
classname=classname.strip()
classname=classname.lower()
print(classname)

# Slice the below string to get you the resulting sentence:
sentence_one = "The Dog Breed is German Shepherd" "only display" "Breed is German"
print(sentence_one[8:24])

sentence_two = "Defeats for the Clinton forces, this was her moment of triumph" "only display" "Clinton forces"
print(sentence_two[16:30])

#Split the below sentence using a semicolon i.e ; And display length of the result.

sentence_three="The lazy dog; ran so fast; it hit the wall."
sentence_three=sentence_three.split(";")
print(sentence_three)
print(len(sentence_three))

#first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe

first_name="  Joh.n"
first_name=first_name.strip().replace(".","")

last_name="   Do,e"
last_name=last_name.strip().replace(",","")

full_name=first_name+" "+last_name
print(full_name)

#Having the string r = '["E","W","C"]' #Manipulate it to display EWC
r = '["E","W","C"]'
r = r.replace(",","")
r = r.replace("[","")
r = r.replace("]","")
r = r.replace('"',"")
print(r)