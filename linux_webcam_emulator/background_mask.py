import cv2
import numpy as np
from bodypix_client import BodypixClient

class BackgroundMask:
  def __init__(self):
    self._segmentation = BodypixClient(bodypix_url='http://localhost:9000')

  def mask(self, frame):
    mask_content = self._segmentation.get_mask(frame)
    mask = np.frombuffer(mask_content, dtype=np.uint8)
    return mask.reshape((frame.shape[0], frame.shape[1]))


  def post_process_mask(self, mask):
    mask = cv2.dilate(mask, np.ones((10,10), np.uint8) , iterations=1)
    mask = cv2.blur(mask.astype(float), (30,30))
    return mask
