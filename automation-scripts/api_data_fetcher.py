import requests 

url = "https://jsonplaceholder.typicode.com/todos/1"

responce = requests.get(url=url)
# print(responce)

# print(dir(responce))

print(type(responce.json()))

for key,value in responce.json().items():
       if key == "completed":
        if value == False:
            print("Data is not completed on the Server.")

for key,value in responce.json().items():
       if key == "userId":
        if value in [1,2,3]:
            print("Data is not Completed but User exists.")



