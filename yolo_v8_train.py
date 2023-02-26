from ultralytics import YOLO
import os

root = os.path.dirname(os.path.abspath(__file__))
custom_dataset_yaml = os.path.join(root,"datasets/CustomDataset.yml")
weight_path = os.path.join(root, "weights/yolov8n.pt")

# Load a model
model = YOLO(weight_path)  # load an official model
model.train(data = custom_dataset_yaml, epochs=5, imgsz=640)
model.export(format = "-")