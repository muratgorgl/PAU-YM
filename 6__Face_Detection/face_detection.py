import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpFaceDetection = mp.solutions.face_detection
FaceDetection= mpFaceDetection.FaceDetection()

mpDraw = mp.solutions.drawing_utils

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = FaceDetection.process(imgRGB)
    
    # print(results.detections)
    
    if results.detections:
        for id, detection in enumerate(results.detections):
            bboxC = detection.location_data.relative_bounding_box
            # print(bboxC)
            h, w, _ = frame.shape
            bbox = int(bboxC.xmin*w), int(bboxC.ymin*h), int(bboxC.width*w), int(bboxC.height*h)
            cv2.rectangle(frame, bbox, (0,255,255),2)
    
    
    
    cv2.imshow("frame", frame)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()