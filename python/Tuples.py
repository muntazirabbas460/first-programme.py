# Tuples are bulit in data type that lets us create  immutable sequences of values
# the big difference b/w tuple and lists is that tuple is immutable while list is muttable


# tup = (2, 3, 9, 7, 8)
# print(type(tup))

# tup = (2, 88, 9, 0)
# print(tup[0])
# print(tup[1])





# tup = (2, 88, 9, 0)
# print(tup[0:2])




# tup = (2, 88, 9, 0)
# print(tup.count(2))




# WAP to ask the user to enter the names of three favourite  movies and store them in lists

# movies = []

# movie1 = input("enter movie 1 ")
# movie2 = input("enter movie 2 ")
# movie3 = input("enter movie 3 ")

# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)

# print(movies)



# WAP to check If list contains palindrome of elements. 
# list1 = [1, 2, 1]
# list2 = [1, 2, 3]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("palindrome")  
# else:
#     print("Not plaindrome") 


# list1 = ["a", "b", "a"]                   
# list2 = ["a", "b", "c", "d"]  

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("palindrom")
# else:
#     print("Not Palindrome")




list1 = ["a", "b", "a"] 
list2 = ["a", "b", "c"]

copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list1):
    print("Palindrome")
else:
    print("Not Plaindrome")    
