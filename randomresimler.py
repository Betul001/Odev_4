import requests

reqUrl = "https://picsum.photos/200/300"

headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
}

payload = ""

response = requests.get(reqUrl, data=payload, headers=headersList)

print(response.text)
