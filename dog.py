from flask import Flask
import requests

app = Flask(__name__)

def get_random_dog_image():
    reqUrl = "https://dog.ceo/api/breeds/image/random"

    headersList = {
        "Accept": "/",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
    }

    response = requests.get(reqUrl, headers=headersList)
    data = response.json()
    return data

@app.route('/random-dog-image')
def random_dog_image():
    dog_image_data = get_random_dog_image()
    dog_image_url = dog_image_data['message']
    return f"Here's a random dog image: <img src='{dog_image_url}'/>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)