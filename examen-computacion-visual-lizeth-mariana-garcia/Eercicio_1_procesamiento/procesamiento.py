import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO


image_path = 'image.jpg'  # Ruta de tu imagen
img_bgr = cv2.imread(image_path)
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

img_suavizada = cv2.GaussianBlur(img_bgr, (5, 5), 0)

img_canny = cv2.Canny(img_suavizada, 100, 200)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(img_rgb)
plt.title("Imagen Original")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(img_suavizada, cv2.COLOR_BGR2RGB))
plt.title("Imagen Suavizada")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(img_canny, cmap='gray')
plt.title("Bordes (Canny)")
plt.axis("off")

plt.tight_layout()
plt.show()

model = YOLO("yolov8n.pt") 

results = model(image_path)[0]  

annotated_img = results.plot()

plt.figure(figsize=(8, 6))
plt.imshow(cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB))
plt.title("YOLO - Objetos Detectados")
plt.axis("off")
plt.show()
