# Gerekli kütüphaneleri içe aktarıyoruz.
import os  # Dosya ve dizin işlemleri için
import argparse  # Komut satırı argümanlarını yönetmek için
import cv2  # OpenCV: Görüntü ve video işlemleri için
import mediapipe as mp  # MediaPipe: Yüz algılama işlemleri için

# Yüzlerin bulanıklaştırılmasını sağlayan fonksiyon
def process_img(img, face_detection):
    # Görüntünün yükseklik (H), genişlik (W) ve renk kanallarını (RGB) alıyoruz.
    H, W, _ = img.shape

    # Görüntüyü BGR'den RGB formatına dönüştürüyoruz. MediaPipe RGB formatı ile çalışır.
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Yüz algılama işlemi yapıyoruz.
    out = face_detection.process(img_rgb)

    # Eğer yüz algılandıysa (out.detections boş değilse)
    if out.detections is not None:
        # Tespit edilen her yüz için döngüye giriyoruz
        for detection in out.detections:
            # Yüzün konum bilgilerini alıyoruz.
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box

            # Yüzün kutu içerisindeki konumunu alıyoruz.
            x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height

            # Yüz koordinatlarını görüntü boyutuna göre yeniden ölçekliyoruz.
            x1 = int(x1 * W)
            y1 = int(y1 * H)
            w = int(w * W)
            h = int(h * H)

            """
            x1 = int(x1 * W): x1, yüzün sol üst köşesinin x koordinatını temsil eder. 
            Bu değer, relative_bounding_box.xmin (0-1 arası) olarak gelir ve görüntünün genişliği W ile çarpılarak 
            gerçek piksel konumuna dönüştürülür. Bu dönüşüm, yüzün çerçevenin yatay eksenindeki gerçek konumunu sağlar.

            y1 = int(   y1 * H): y1, yüzün sol üst köşesinin y koordinatını temsil eder. relative_bounding_box.ymin ile gelen bu değer,
            görüntünün yüksekliği H ile çarpılarak gerçek piksel konumuna dönüştürülür. Bu işlem, yüzün dikey eksendeki gerçek konumunu 
            belirler.

            w = int(w * W): w, yüzün genişliğini temsil eder. relative_bounding_box.width değeri ile gelen bu oran, 
            görüntü genişliği W ile çarpılır, böylece yüzün genişliğini piksel cinsinden elde ederiz.

            h = int(h * H): h, yüzün yüksekliğini ifade eder. relative_bounding_box.height ile gelen bu değer, 
            görüntünün yüksekliği H ile çarpılarak yüzün yüksekliğini piksel cinsinden verir.
            """

            # Bulanıklaştırma işlemini uyguluyoruz: Belirlenen yüz alanını bulanıklaştırıyoruz.
            img[y1:y1 + h, x1:x1 + w, :] = cv2.blur(img[y1:y1 + h, x1:x1 + w, :], (30, 30))

    # İşlenmiş görüntüyü döndürüyoruz.
    return img


# Komut satırı argümanlarını işlemek için bir parser oluşturuyoruz.
args = argparse.ArgumentParser()

# Programın çalışma modunu (webcam, image veya video) belirten bir argüman ekliyoruz; varsayılan değer 'webcam'.
args.add_argument("--mode", default='webcam')

# İşlenecek dosya yolunu belirten bir argüman ekliyoruz; varsayılan olarak None değeri alır.
args.add_argument("--filePath", default=None)

# Argümanları ayrıştırarak kullanıcının girdiği değerlere göre ayarlıyoruz.
args = args.parse_args()


# Çıktıların kaydedileceği klasörü tanımlıyoruz. Klasör yoksa oluşturuyoruz.
output_dir = './output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Yüz algılama modeli
mp_face_detection = mp.solutions.face_detection

# Yüz algılamayı belirli bir güven eşiği ile başlatıyoruz.
with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:

    # Görüntü modu: Tek bir görüntüyü işlemek için
    if args.mode in ["image"]:
        # Belirtilen dosya yolundan görüntüyü okuyoruz.
        img = cv2.imread(args.filePath)

        # Görüntüyü işliyoruz (yüzleri bulanıklaştırıyoruz).
        img = process_img(img, face_detection)

        # İşlenmiş görüntüyü çıktı klasörüne kaydediyoruz.
        cv2.imwrite(os.path.join(output_dir, 'output.png'), img)

    # Video modu: Bir video dosyasını işlemek için
    elif args.mode in ['video']:
        # Belirtilen dosya yolundan video dosyasını okuyoruz.
        cap = cv2.VideoCapture(args.filePath)
        ret, frame = cap.read()

        # Çıkış videosu için bir VideoWriter nesnesi oluşturuyoruz.
        output_video = cv2.VideoWriter(os.path.join(output_dir, 'output.mp4'),
                                       cv2.VideoWriter_fourcc(*'MP4V'),  # Video formatını belirliyoruz.
                                       25,  # Video çıkış hızını (fps) belirliyoruz.
                                       (frame.shape[1], frame.shape[0]))  # Video boyutunu belirliyoruz.

        # Video karelerini döngü ile işliyoruz.
        while ret:
            # Her karede yüzleri bulanıklaştırıyoruz.
            frame = process_img(frame, face_detection)

            # İşlenmiş kareyi çıktı videosuna yazıyoruz.
            output_video.write(frame)

            # Sonraki kareyi okuyoruz.
            ret, frame = cap.read()

        # Video dosyasını serbest bırakıyoruz.
        cap.release()
        output_video.release()

    # Webcam modu: Canlı kamera akışını işlemek için
    elif args.mode in ['webcam']:
        # Kamera aygıtından görüntüleri okuyoruz (Kamera cihaz numarası 2 olarak ayarlanmış).
        cap = cv2.VideoCapture(0)

        # İlk kareyi okuyoruz.
        ret, frame = cap.read()
        while ret:
            # Her kareyi işliyoruz (yüzleri bulanıklaştırıyoruz).qqq
            frame = process_img(frame, face_detection)

            # İşlenmiş kareyi ekranda gösteriyoruz.
            cv2.imshow('frame', frame)
            if cv2.waitKey(25) & 0xFF == ord("q"): # Her kare arasında 25 ms bekliyoruz
                break

            # Sonraki kareyi okuyoruz.
            ret, frame = cap.read()
            

        # Kamera aygıtını serbest bırakıyoruz.
        cap.release()
        
        
