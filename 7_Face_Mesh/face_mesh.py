import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture("video1.mp4")

mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
mpDraw = mp.solutions.drawing_utils
drawSpec = mpDraw.DrawingSpec(thickness=1,circle_radius=1)


pTime = 0
while True:
    ret, frame = cap.read()
    if ret is False:
        break

    ret, frame = cap.read()
    frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = faceMesh.process(frameRGB)
    print(results.multi_face_landmarks)

    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(frame,faceLms,mpFaceMesh.FACEMESH_CONTOURS, drawSpec, drawSpec) # FACEMESH_TESSELATION
        for id, lm in enumerate(faceLms.landmark):
            h, w, _ = frame.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            print([id,cx,cy])
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(frame, "FPS: " + str(int(fps)),(10,65),cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0), 2)


    cv2.imshow("frame", frame)
    if cv2.waitKey(100) & 0xFF == ord("q"):break
    
cap.release()    
cv2.destroyAllWindows()









