import os
from ultralytics import YOLO

root  = os.path.dirname(os.path.abspath(__file__))
weight_path = os.path.join(root, "weights/best.pt")
source = os.path.join(root, "raw_dataset/images/test/test.mp4")

model = YOLO(weight_path)
results = model.track(source = source, show = True, \
                      tracker='bytetrack.yaml') 

for result in results:
    print(result)