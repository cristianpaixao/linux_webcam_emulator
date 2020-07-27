import cv2
import requests

class BodypixClient:
  def __init__(self, bodypix_url):
    self._bodypix_url = bodypix_url

  def get_mask(self, frame):
    _, data = cv2.imencode(".jpg", frame)
    response = requests.post(
        url=self._bodypix_url,
        data=data.tobytes(),
        headers={'Content-Type': 'application/octet-stream'})
    return response.content
