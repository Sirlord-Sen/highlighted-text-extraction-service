import os
from flask import Flask, jsonify, request
from datetime import datetime

from textdetect import textdetect as td

app = Flask(__name__)

@app.route('/detectText', methods = ['POST'])
def save_image():
    now = datetime.now()
    image_data = request.files['image']
    user = request.form['user_id']
    topic = request.form['topic_id']
    current_time = now.strftime("%b-%d-%Y_%H-%M-%S")
    img_path = os.path.abspath('static\images')
    img_title = f"{user}_{topic}_{current_time}.jpg"
    image_data.save(f"{img_path}/{img_title}")

    highlightedText = td.text_detect(img_title)
    return jsonify({'msg': "success", "text": highlightedText})

if  __name__ == '__main__':
    app.run(debug=True)