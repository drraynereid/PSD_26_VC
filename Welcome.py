# Welcome message
print (" Welcome , everyone , to the GitHub tutorial !")

def introduction_task ():
    print ("\n--- Python Task ---")
    print ("Let ’s write a function that adds two numbers !")

def add_numbers (a, b):
    return a + b

num1 = 5
num2 = 7
result = add_numbers (num1 , num2 )
print (f"The result of adding { num1 } and { num2 } is: { result }")
print("next:" + str(add_numbers (6 , 12 )))
print ("extra")

introduction_task ()