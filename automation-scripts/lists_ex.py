a = [100,20,300,"True"]  # first way to create the list
a.append(500)
print(a)

clouds = list()   # Second way to create the list (Standard)
print(type(clouds))

clouds.append("aws")
clouds.append("azure")
clouds.append("gcp")
clouds.append("alibaba")
clouds.append("ibm")
clouds.append("utho")
clouds.append("oracle")
print(clouds)
print("Length of cloud list is :", len(clouds))
print("World Leader for Cloude Service Provider is : ", clouds[0])
print("What is last in the list: ",clouds[-1])

print(dir(clouds))

print(clouds.append.__doc__)

# ['aws', 'azure', 'gcp', 'alibaba', 'ibm', 'utho', 'oracle']
# range(5) -> 0,1,2,3,4

for cloud in clouds:
    if cloud == "aws":
        print("Market Leader")
    elif cloud == "utho":
        print("India Cloud")
    elif cloud == "alibaba":
        print("Chinees Cloud") 
    else:
        print("Anyone can play")               