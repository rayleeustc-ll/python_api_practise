import requests
Base = "http://127.0.0.1:5000/"

# response = requests.put(Base+"video/1",{"name":"Gone with the wind","view":10000, "likes":10})
# print(response.json())
# print(response)

# response2 =requests.get(Base+"video/1")
# print(response2.json())
#
# data = [{"name":"Gone with the wind","views":10000, "likes":10},
#        {"name":"Tatanic","views":9000, "likes":300},
#        {"name":"huamulan","views":7000, "likes":500}]
#
# for i in range(len(data)):
#     response = requests.put(Base+"video/"+str(i),data[i])
#     print(response.json())

# response2 =requests.get(Base+"video/8")
# print(response2.json())

response=requests.patch(Base+"video/0",{"views":9001, "likes":100})
print(response.json())

