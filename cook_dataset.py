import os, cv2, glob, sys, json, shutil
import numpy as np

from tqdm import tqdm

root = os.path.dirname(os.path.abspath(__file__))

dataset_type = input("Enter Dataset type [train/val/test] : ")
if dataset_type not in ["train", "val", "test"]:
    print("please choose correct data type !")
    sys.exit()

parent_dir = os.path.join(root, "raw_dataset")
if not os.path.isdir(parent_dir):
    os.makedirs(parent_dir, exist_ok = True)
    print("please copy your dataset into 'raw_dataset' directory !")
    sys.exit()
    
video_file = glob.glob(os.path.join(parent_dir, f"images/{dataset_type}/*.mp4"))[0]
annots_json = os.path.join(parent_dir, f"annotations/instances_{dataset_type}.json")

sub_dir = os.path.join(root, "datasets/cooked_dataset", f"{dataset_type}")
if os.path.isdir(sub_dir):
    shutil.rmtree(sub_dir)
images_dir = os.path.join(sub_dir, "images")
annots_txt_dir = os.path.join(sub_dir, "labels")

os.makedirs(images_dir, exist_ok= True)
os.makedirs(annots_txt_dir, exist_ok= True)

with open(annots_json) as f:
    annots = json.load(f)

all_frames = int(annots["images"][-1]["file_name"].split(".jpg")[0]) + 1
progress_bar = iter(tqdm(range(all_frames)))

def frame_extractor(video_file = video_file):
    cap = cv2.VideoCapture(video_file) 
    if not cap.isOpened(): 
        print("Error opening video stream or file")
    grabbed_frame = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            grabbed_frame += 1
            cv2.imwrite(os.path.join(images_dir, f'{grabbed_frame}.jpg'),frame)
        else: 
          break
        next(progress_bar)
    cap.release()

width = annots["images"][0]["width"]
height = annots["images"][0]["height"]

def move_center(inp1, inp2):
    return inp1 + inp2/2

frame_extractor()
for annot in tqdm(annots["annotations"]):
    with open(f"{annots_txt_dir}/{annot['image_id']}.txt", "a") as f:
        f.write(f"{annot['category_id']-1} {move_center(annot['bbox'][0], annot['bbox'][2])/width} \
                {move_center(annot['bbox'][1], annot['bbox'][3])/height} \
                {annot['bbox'][2]/width} {annot['bbox'][3]/height}\n")