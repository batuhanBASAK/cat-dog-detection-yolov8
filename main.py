from ultralytics import YOLO


# create a new model with transfer learning
model = YOLO("yolov8n.yaml").load('yolov8n.pt')

# train the model
model.train(data="data.yaml",
            epochs=200,
            freeze=10, 
            batch=32,
            verbose=True)
