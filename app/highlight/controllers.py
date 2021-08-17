from  flask import Blueprint, request, jsonify

from .services import TextDetectService
from ..textdetect import textdetect as td
from .handlers import BuildResponse

api = Blueprint('high_detect', __name__, url_prefix='/api/v1/text_detection')

@api.route('/detectText', methods = ['POST'])
def textdetect():
    img = request.files['image']
    user = request.form['user_id']
    topic = request.form['topic_id']
    img_title = TextDetectService.saveImage(img, user, topic)
    highlightedText = td.text_detect(img_title)
    cleanHighlights = TextDetectService.cleanText(highlightedText)
    response = BuildResponse(user, cleanHighlights)
    
    return jsonify(response)