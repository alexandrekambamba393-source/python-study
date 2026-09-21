fruits = ['apple', 'banana', 'cherry', 'date', 'fig']

print(fruits)
print(type(fruits))
#Indexing and slicing 
print(fruits[2])
print(fruits[-2])

#slicing ->extracting a aprt of a list 
# [Start_index:end_index+1]
print(fruits[1:4])
print(fruits[2:5])

#updating items 
fruits[2]='watermelon'
print(fruits[2])

#append
fruits.append('mango')
print(fruits)

#insert
fruits.insert(1,'kiwi')
print(fruits)

#remove 
fruits.remove('apple')
print(fruits)

#pop
fruits.pop()
print(fruits)

fruits.pop(0)
print(fruits)

#Clear 
fruits.clear()
print(fruits)

#Create a list of days of the week 
#Displays the day today 
#Displays tuesday to friday 

days=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
print(days[0])
print(days[1:5])

#update thursday to thur
#add january at the end of the list 
#add december between tuesday and wednesday 

days[3]='thur'
print(days)

days.append('january')
print(days)

days.insert(2, 'december')
print(days)

#delete friday from the list 
#delete the last item on the list
#delete the item at index 1
#delete all items from the list 

days.pop(4)
print(days)

days.pop()
print(days)

days.remove('monday')
print(days)

days.clear()
print(days)