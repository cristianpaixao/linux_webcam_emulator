import cv2

webcam_capture = cv2.VideoCapture(0)

# webcam configurations
webcam_width, webcam_height, webcam_fps = 1280, 720, 60
webcam_capture.set(cv2.CAP_PROP_FRAME_WIDTH, webcam_width)
webcam_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, webcam_height)
webcam_capture.set(cv2.CAP_PROP_FPS, webcam_fps)

while True:
  success, frame = webcam_capture.read()
  cv2.imshow("Webcam", frame)
  print(cv2.getVersionString())
  # Ending
  k = cv2.waitKey(30) & 0xff
  if k == 27:
      break

webcam_capture.release()
cv2.destroyAllWindows()
