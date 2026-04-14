info = {
    "name" : "Durga Prasad",  #str
    "city" : "Dehradun",  # str
    "age" : 40, # int
    "salary" : "12.5",  # float
    "married" : True,   # bool
    "favourites" : ["movies", "cricket"]
}


print("I live in city :- ", info["city"])
print("My favourite game is :- ", info.get("favourite","Not Found"))


info.update({"Channel": "DPTechwourld"})

print(info)

print(dir(info))

print(info.get.__doc__)

for key,value in info.items():
    print(key,value)