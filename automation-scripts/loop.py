# list -> data structure which can hold multiple values of multiple type
#arrye -> data structure which can hold multiple values of same type
list_of_cloud = ["aws","azure","gcp","digital ocean","oracle"]
cloud = "gcp" #variable                 

print(list_of_cloud) 


# add a new cloud alibaba 

list_of_cloud.append("alibaba") # adds to the end of the list

# add a new cloud Salesforce

list_of_cloud.append("Salesforce") # adds to the end of the list

print(list_of_cloud)

list_of_cloud.insert(4,"Heroku")

print(list_of_cloud)

print(len(list_of_cloud)) # count index 

list_of_cloud.insert(0,"IBM")  # insert index at "0" first position

print(list_of_cloud)

for cloud in list_of_cloud: # Iteration of a list "using for loop"
    print("") # to put a blank line in between the output
    print(cloud)

for i in range(1,11):
    print(i)