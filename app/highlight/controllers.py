import os
from  flask import Blueprint, request, jsonify

from .services import TextDetectService
from ..textdetect import textdetect as td

api = Blueprint('high_detect', __name__, url_prefix='/api/v1/text_detection')

@api.route('/detectText', methods = ['POST'])
def textdetect():
    img = request.files['image']
    user = request.form['user_id']
    topic = request.form['topic_id']
    img_title = TextDetectService.saveImage(img, user, topic)
    highlightedText = td.text_detect(img_title)
    # return jsonify({'msg': "success"})
    return jsonify({'msg': "success", "text": highlightedText})