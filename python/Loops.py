# Loops are used to repeate instructions

# 1) while loop
# while condition:
#    Work

# i = 1

# while i <= 100000:
#    print("hello", i) 
#    i += 1

# Print Loop from one to five

# i = 5

# while i >= 1:
#    print(i)
#    i -= 1

# print("Loop Ended")   


# i = 8
# while i >= 1:
#    print(i)
#    i -= 1

# print("loop ended")


# WAP to print numbers from 1 to 100

# i = 1
# while i <= 100:
#    print(i)
#    i += 1
# print("Loop ended")  

# WAP to print numbers from 100 to 1

# i = 100
# while i >= 1: #stopping Condition
#     print(i)
#     i -= 1 


# WAP to print a multiplication table of a number n

# n = int(input("enter num : "))
# i = 1
# while i <= 100:
#       print(n*i)
#       i +=1



# Print the element of following list using a loop

# nums = [1, 4, 9 ,16 , 25, 36, 49, 64, 81, 100]
# heros = ["superman", "spiderman", "batman", "Captaine America"]

# index = 0

# while index < len(heros):
#               print(heros[index])

#               index += 1


# nums = [1, 4, 9 ,16 , 25, 36, 49, 64, 81, 100]

# idx = 0
# while idx < len(nums):
#               print(nums[idx])
#               idx += 1



#Search for  a number x in this tuple using 
nums = (1, 4, 9 ,16 , 25, 36, 49, 64, 81, 100)

x = 36
i = 0
while i < len(nums):
    if(nums[i] == x):
       print("Found at : ", i)
    i += 1
              



