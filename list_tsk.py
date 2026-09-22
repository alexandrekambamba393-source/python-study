# create a new file list_task.py
trainees= ["John", [2, ["James", "Mary"]]]
# 1. Display 2 from the list 
print(trainees[1][0])
# Display Mary from the list
print(trainees[1][1][1])

# 2.Output James from the list 
print(trainees[1][1][0])

# 3.Using a method add 56 at the end of the list 
trainees.append(56) 
print(trainees)

# 4. Using a method add the name MIKe between James and Mary 


#Exercices 

#employees = ["TechElar", [4, ["Kevin", "Brian", "Alice"]]]
employees = ["TechElar", [4, ["Kevin", "Brian", "Alice"]]]

# 1. Display the number 4.
print(employees[1][0])

# 2. Display "Brian" from the list.
print(employees[1][1][1])

# 3. Display "Alice" from the list.
print(employees[1][1][2])


# 4. Using a list method, add the number 7 at the end of the outer list.
employees.append(7)

# 5. Add "David" between "Brian" and "Alice".
employees[1][1].insert(2, "David")

# 6. Change the number 4 to 10.
employees[1][0] = 10

# 7. Change "Kevin" to "James".
employees[1][1][0] = "James"

# 8. Remove "TechElar" from the list.
employees.remove("TechElar")

# 9. Remove "Alice" from the nested list.
employees[1][1].remove("Alice")

# 10. Add "Mary" at the beginning of the nested list.
employees[1][1].insert(0, "Mary")

# 11. Using len(), find the number of items
#     in the nested employee list.
len(employees)
print(employees)

# 12. Print the final list.
print("final list:", employees)