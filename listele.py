import requests

reqUrl = "GET http://127.0.0.1:5000/users"

headersList = {
        "Accept": "/",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)"
        }

payload = ""

response = requests.request("GET", reqUrl, data=payload,  headers=headersList)

print(response.text)
                         