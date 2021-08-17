import os
import re
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

    @staticmethod
    def cleanText(highlights):
        cleanHighlights = []
        for hi in highlights:
            hi = hi.strip().replace('\n', " ")
            for k in hi.split("\n"): hi = re.sub(r"[^a-zA-Z0-9.,]+", " ", k)
            hi = hi.strip()
            cleanHighlights.append(hi)
        return cleanHighlights