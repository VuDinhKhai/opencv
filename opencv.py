import cv2
import time
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
i=0
start_time=time.time()
for i in range(50):
    return_value, image = cap.read()
    cv2.imwrite('C:/Users/DELL/OneDrive/Máy tính/Webcam/anh_thu_'+str(i)+'.png',image)
end_time=time.time()
print(end_time-start_time)
cap.release() 
cv2.destroyAllWindows()