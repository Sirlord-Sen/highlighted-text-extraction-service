import os
from datetime import datetime

class TextDetectService:
    @staticmethod
    def saveImage(img, user, topic):
        now = datetime.now()
        current_time = now.strftime("%b-%d-%Y_%H-%M-%S")
        img_path = os.path.abspath('app\static\images')
        img_title = f"{user}_{topic}_{current_time}.jpg"
        img.save(f"{img_path}/{img_title}")

        return img_title