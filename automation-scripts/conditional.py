day_of_week = input("Enter the day of week: ").lower()  # cobvert to lowercase
print(day_of_week)

if day_of_week == "saturday" or day_of_week == "sunday": # if condition is true 
    print("I will learn LIVE DevOps")
else: # if condition is false
    print("I will practice DevOps")   

num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: ")) 


choice = input("Enter the operation: (Option + , - , * , / , %) ")

if choice == "+":
    sum_of_num = num1 + num2 
    print("addition: ",sum_of_num )
elif choice == "-":
    diff_of_num = num1 - num2 
    print("subtraction: ",diff_of_num)
elif choice == "*": 
    prod_of_num = num1 * num2
    print("multiplication: ",prod_of_num)   
elif choice == "/":
    div_of_num = num1 / num2 
    print("division: ", div_of_num)    
elif choice == "%":
    remain_of_num = num1 % num2
    print("remainder: ",remain_of_num)
else:
    print("Invalid Choice")    
