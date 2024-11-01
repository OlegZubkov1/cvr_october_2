from ultralytics import YOLO
# Загружаем предобученную модель YOLOv8
model = YOLO('yolov8n.pt') # Выберите размер модели: n, s, m, l, x
# Запускаем обучение
model.train(data='config.yaml', epochs=100, batch=16, imgsz=640)