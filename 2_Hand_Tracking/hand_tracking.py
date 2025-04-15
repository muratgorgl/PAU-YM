import cv2  # OpenCV kütüphanesi görüntü işleme işlemleri için kullanılıyor.
import time  # FPS hesaplamak için zaman ölçümü yapmamızı sağlar.
import mediapipe as mp  # Mediapipe, el tanıma ve diğer algılama işlemleri için kullanılıyor.

# VideoCapture nesnesi oluşturuluyor ve 0, bilgisayarın varsayılan kamerasını ifade eder.
cap = cv2.VideoCapture(0)

# Mediapipe'de el izleme (hands) çözümünü yüklüyoruz.
mpHand = mp.solutions.hands

# Hands sınıfını çağırarak el tanıma modelini başlatıyoruz.
hands = mpHand.Hands()

# Çizim işlemleri için Mediapipe’in drawing_utils modülünü kullanıyoruz.
mpDraw = mp.solutions.drawing_utils

# FPS (saniye başına kare sayısı) hesaplamak için iki zaman değişkeni tanımlıyoruz.
pTime = 0  # Önceki zaman
cTime = 0  # Şu anki zaman

# Ana döngü: Her karede işlemlerimizi yapmamızı sağlar.
while True:
    # Kameradan kare okuma; ret okuma işleminin başarılı olup olmadığını belirtir, frame ise görüntü karesi.
    ret, frame = cap.read()

    # OpenCV'nin BGR formatındaki görüntüsünü RGB formatına dönüştürürüz, çünkü Mediapipe RGB ile çalışır.
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Eller üzerinde işlem yapılır, böylece el konumları tanımlanır ve sonuçlar değişkenine kaydedilir.
    results = hands.process(imgRGB)

    # Elde edilen el pozisyonlarının varlığını kontrol etmek için çıktı alıyoruz.
    print(results.multi_hand_landmarks)
    
    # Eğer elde edilen el pozisyonları varsa (yani, bir el algılandıysa):
    if results.multi_hand_landmarks:
        # Her bir el için işleme devam ediyoruz.
        for handLms in results.multi_hand_landmarks:
            # Çizim işlemi: Tespit edilen elin pozisyonlarını çerçeveye çizeriz.
            mpDraw.draw_landmarks(frame, handLms, mpHand.HAND_CONNECTIONS)
             
            # Her bir parmak noktası için id ve landmark (pozisyon) bilgisi sağlanır.
            for id, lm in enumerate(handLms.landmark):
                # El pozisyonunun çerçeve içindeki konumunu buluyoruz.
                h, w, c = frame.shape  # Görüntünün yüksekliği, genişliği ve kanal sayısını alıyoruz.
                
                # Landmark’ın görüntüdeki gerçek piksel koordinatlarını hesaplıyoruz.
                cx, cy = int(lm.x * w), int(lm.y * h)
                
                # Parmak bileği (id = 20) için özel bir işaretleme yapılacak.
                if id == 20:
                    # El bilek pozisyonunda bir mavi dolu daire çizilir.
                    cv2.circle(frame, (cx, cy), 9, (255, 0, 0), cv2.FILLED)
                                 
    # FPS hesaplama: Geçen süreye göre FPS değeri belirlenir.
    cTime = time.time()  # Şu anki zamanı alıyoruz.
    fps = 1 / (cTime - pTime)  # FPS, iki kare arasındaki süreyle ters orantılıdır.
    pTime = cTime  # pTime'ı güncelleyerek bir sonraki kare için referans olarak kullanırız.

    # FPS değerini çerçeve üzerine yazdırıyoruz.
    cv2.putText(frame, "FPS: " + str(int(fps)), (10, 75), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)

    # İşlenmiş görüntüyü ekranda gösteriyoruz.
    cv2.imshow("frame", frame)

    # 'q' tuşuna basıldığında döngüden çıkılır ve program sonlandırılır.
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
# Kamera yayını ve tüm OpenCV pencereleri serbest bırakılır.
cap.release()
cv2.destroyAllWindows()
