import os
import requests
from flask import Flask, send_file

app = Flask(__name__)

IMAGE_URL = "https://sp-ao.shortpixel.ai/client/to_auto,q_lossy,ret_img,w_800/https://www.flokq.com/blog/wp-content/uploads/2021/02/24-Belimbing-bali-Rice-Terrace-mapping-along-800x600.jpg"
IMAGE_PATH = 'picture.jpg'

@app.before_first_request
def download_image():
    if not os.path.exists(IMAGE_PATH):
        response = requests.get(IMAGE_URL)
        if response.status_code == 200:
            with open(IMAGE_PATH, 'wb') as f:
                f.write(response.content)

@app.route('/')
def home():
    return send_file(IMAGE_PATH, mimetype='image/jpg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

