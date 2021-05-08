import requests

Base = "http://127.0.0.1:5000/"

# response = requests.get(Base+"helloWorld/tim")
# print(response.json())
response2 = requests.post(Base + "helloWorld/tim")
print(response2.json())

1
