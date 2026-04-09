import cv2
import os

os.makedirs("FotosCV", exist_ok=True)

foto = cv2.VideoCapture(0)
contador = 1
cx = 320
cy = 240

while True:
     ret,frame = foto.read()
     if not ret:
          break
     cv2.rectangle(frame,(cx-100, cy-150), (cx+100, cy+150),(0,255,0),2)
     roi = frame[cy-150:cy+150, cx-100:cx+100]
     cv2.imshow("Camera",frame)
     cv2.imshow("roi",roi)
     tecla = cv2.waitKey(1) & 0xff
     if tecla == ord("s"):
          cv2.imwrite(f"FotosCV/foto{contador}.jpg",roi)
          contador += 1
     if tecla ==ord("q"):
          cv2.destroyAllWindows()
          break
     


foto.release()
cv2.destroyAllWindows()

    