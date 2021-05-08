import requests
Base = "http://127.0.0.1:5000/"

# response = requests.put(Base+"video/1",{"name":"Gone with the wind","view":10000, "likes":10})
# print(response.json())
# print(response)

# response2 =requests.get(Base+"video/1")
# print(response2.json())

data = [{"view":10000, "likes":10}]

for i in range(len(data)):
    response = requests.put(Base+"video/"+str(i),data[i])
    print(response.json())

response2 =requests.get(Base+"video/2")
print(response2.json())

# response3=requests.delete(Base+"video/0")
# print(response3)

test1