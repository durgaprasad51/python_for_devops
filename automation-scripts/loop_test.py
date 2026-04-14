for i in range(5):
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