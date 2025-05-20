# set is unique and unordered collection of items it must be mutable
# collection = {
#               1,2,3,4,5
# } 

# print(collection)
# print(type(collection))

# Methods of sets

# 1) add method
# 2) Remove method
# 3) clear method
# 4) 
# collection = set()
# collection.add(1)
# collection .add(2)

# collection .remove(1)
# print(collection)


# 4) Clear Method
# collection = set()
# collection .add(2)
# collection .add(4)

# collection .remove(2) 
# print(collection)

# 5) pop Method: It pops means prints the random values
  
# collection = {"2", "3", "mass", "string"}
# print(collection.pop())

# 6) Union Method
# set1 = {1, 2, 3, 4}
# set2 = {1, 2, 3, 4, 5}

# print(set1.union(set2))
# print(set1)

# WAP to for  a list of subjects . aAssume one class romm is required for i subject. 
# How many class rooms are needed by all subjects.sum

# subjects = {
#               "python", "java", "c++", "python", "javascript", "java", "python",
#               "java", "c++", "C"
# }
# print(len(subjects))

# WAP to enter marks of 3 subjects from the user and store them in dictionary. Start with an empty dictionary
# and add one by one. Use subjectsname as key and marks as value.


# marks = {}

# x = int(input("marks of Database : "))
# marks.update({"Databse ": x})

# x = int(input("marks of FOP : "))
# marks.update({"Marks of FOP ": x})

# x = int(input("marks of DLD : "))
# marks.update({"marks of DLD ": x})

# print(marks)



# marks = {}

# x = int(input("marks of DLD : "))
# marks.update({"marks of DLD ": x})

# x = int(input("marks of COAL : "))
# marks.update({"marks of COAL ":x})

# x = int(input("marks of AI : "))
# marks.update({"marks of AI ": x})
# print(marks)

# WAP to figure out a way to store 9 and 9.0  as seperatre values in the set.
# (You can take help of built in data)

# marks = ( 9, "9.0")
# print(marks)
#     or

values = {
              ("float", 9.0),
              ("int", 9)

}
print(values)
