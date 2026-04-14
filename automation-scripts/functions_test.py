#Function = Any work


def sum_of_num():    # Funtion defination
    num1 = int(input("Enter first num : "))   # step
    num2 = int(input("Enter second num : "))  # step

    sum = num1 + num2  # step
    print(sum)   # step

env = input("Enter the environment : ")

if env == "prd":
    sum_of_num() # call the function to get output    
else:
    print("Not required in your environment") 
       