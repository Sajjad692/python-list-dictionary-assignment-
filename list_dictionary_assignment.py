# List Practice
# A list is an order collection of items. Large brackets [] is use for the list and each list contant having quotes.
# When we want to add items in list collection we use .append("abc") as syntex.
rainbow=["violet" , "indigo" , "blue" , "green", "blue"]
# Display all list items
print("Complete List",rainbow)
# Display a fruit at specific number
print("Forth color:",rainbow[3])
# Add new item in the list
rainbow.append("Orange") # use .append to add a color at last position
rainbow.insert(6, "red") # use .insert to add a color at specific position
print("Updated Fruits List:",rainbow) # to execute updated color list
for items in rainbow:                 # use loop function to print list in vertical
    print(items)

    # dictionary Practice
    # Dictionary is a collection of **Key value pairs**, each key is unique.
    # And each key points to a specfic value.
    student={
    "name":"wahab",
    "age": "12",
    "class":"seven",
    "roll no":"doc4556"
}
print("Student Info:",student) # for student complete info
print("Student Name:", student ["name"]) # for student name only
print("Student Age:", student ["age"])  # for student age only
print("Student Class:", student ["class"]) # for student class only
print("Student Roll No:", student ["roll no"]) # for student roll no only
student ["hobby"]="football"   # to add new key in dictionary
print("Updated Student Info:", student) # for updated info including new key
for key, value in student.items():   # use loop function to display the dictionary vertically
    print(f"{key}:{value}")