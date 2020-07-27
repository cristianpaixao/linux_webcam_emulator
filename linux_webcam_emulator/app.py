import cv2
import requests
from background_mask import BackgroundMask
import pyfakewebcam

def get_mask(frame, background_scaled):
  mask = None
  while mask is None:
    try:
      mask = background_mask.mask(frame)
    except requests.RequestException:
            print("mask request failed, retrying")
  mask = background_mask.post_process_mask(mask)
  inv_mask = 1-mask
  return mask, inv_mask

webcam_capture = cv2.VideoCapture(0)
background_mask = BackgroundMask()
background_raw = cv2.imread('images/synth.jpeg')

# webcam configurations
width = int(webcam_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(webcam_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(webcam_capture.get(cv2.CAP_PROP_FPS))

print('Running webcam on Width: {}p Height: {}p and {} FPS'.format(width, height, fps))

background_scaled = cv2.resize(background_raw, (width, height))
fake = pyfakewebcam.FakeWebcam('/dev/video20', width, height)
counter = 5
while True:
  _, frame = webcam_capture.read()
  if counter % 5 == 0:
    mask, inv_mask = get_mask(frame, background_scaled)
  for c in range(frame.shape[2]):
    frame[:,:,c] = frame[:,:,c]*mask + background_scaled[:,:,c]*inv_mask
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  fake.schedule_frame(frame)
  counter += 1

webcam_capture.release()
cv2.destroyAllWindows()
