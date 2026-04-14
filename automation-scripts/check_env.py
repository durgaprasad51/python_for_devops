#get the environment(input) from user and print it
#  input can be taken using "input" variable"

env = input("Enter the env : ") 
#print(data)

# Conditional statement

if env == "prd":
    print("Don't Deploy on friday")
elif env == "stg":
    print("Take backup & test well")    
elif env == "test":
    print("Test it well")    
else: # False
    print("Safe to Deploy any day")    

# Type casting - convestion of 1 data type to anther



a = int(input("number one : ")) #  added "int" for type casting (converting data type)
b = int(input("number two : "))

print("Muliplecation is:", a * b)
print("Addition is: ", a + b)
print("Subtraction is: ", a - b)
print("Devision is :", a / b)


studentname = input("Enter your name : " )
maths = int(input("Enter your score in math : " ))
english = int(input("Enter your score in english : " ))
science = int(input("Enter your score in science : " ))
evs = int(input("Enter your score in evs : " ))
hindi = int(input("Enter your score in hindi : " ))

print("Total score of all subjects is : ", maths + english + science + evs + hindi)






