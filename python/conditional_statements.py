light = "yellow"

if (light == "red"):
     print("Stop")
elif(light == "green"):
     print("go")
elif(light == "yellow"):
     print("reday")
print("out of order") 

# in case of two if compiler will check both if. but in case of one If
# compiler will see only one if afterward statements will ignored


marks = int(input("marks of the student: "))
if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"  
elif(marks >= 70 and marks < 80):
     grade = "C"
else:
     grade = "D"
print("grade of the student ->", grade)  

Nesting
age = 95
if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive") 
else:
    print("cannot drive")                     

# write a programme to check the num entered by user is even or odd?
num = int(input(" enter the num: "))

if(num % 2 == 0):
    print("Even")
else:
    print("Odd")

# WAP to find greater num among  three given numers  
   
a =int(input("type first num : "))
b =int(input("type second num : "))
c =int(input("type third num : "))

if(a >= b and a >= c):
    print("a is greater ", a)
elif(b >= c):
    print("b is greater", b)
else:
    print("c is greater")    

# write a programme to check a num is multiple of 7 or not?

num = int(input("write a num "))

if(num % 7 == 0):
    print( num, "Is multiple of seven")              
else:
    print( num, "Is not the multiple of seven") 