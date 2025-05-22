# Break: Is used to terminate the loop when encountered

# Continue: Terminate the execution in the current iteratipon and
# continues execution of the loop with the next iyteration 

# i = 1
# while i <= 5:
#     print(i)
#     if (i == 3):
#       break
#     i += 1

i = 1
while i <= 10:
    if (i%2 != 0):
        i += 1
        continue
    print(i)
    i += 1

