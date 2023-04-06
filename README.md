# Object Tracking

Here I utilized the most recent object detection and tracking algorithm in order to detect and track predefined objects in SMLE challenge.
in the following sections you'll find out how to use this repo and achieve high performance tracking results usable on jetson nano chips.

## Description

in order to detect objects I used the most recent Yolo-v8 from yolo family which has a very strong community and as a result I had to change dataset formats into acceptable structure for training the network. to boost the training time I used transfer learning and downloaded predefined weights which led to higher accuracy. after training, "ByteTrack" algorithm is utilized to achieve robust tracking results.

## Getting Started

### Dependencies

Frist clone the repo and create virtual environment inside it using : 
```
git clone https://github.com/elhammmoeini/Tracking-Object.git
cd "Tracking-Object"
python -m venv venv
(if you know your python version use pythonX.X for ex. python3.8)
```
then activate the venv using : 
```
source venv/bin/activate (on linux)
venv/scripts/activate.ps1 (on windows)
```
then install dependencies using : 

```
pip install -r requirements.txt
```

### Executing program

there are 3 modules in the repo :

1 - cook_dataset.py

2 - yolo_v8_train.py

3 - yolo_v8_tracking.py

#### Retrain Yolo-v8

if you wish to retrain the model you first need to reformat dataset to yolo acceptable ones, to do so, first download the dataset and extract it under "raw_dataset" directory (at the same level with cook_dataset.py) then use :
```
python cook_dataset.py
```
you will be asked to enter dataset type, your options are  : train/val/test. do this triple time for all 3 different data. after doing so you get a directory called dataset which contains everything needed to train your model. now your repo directory should look like following :

```
.
├── cook_dataset.py
├── datasets
├── raw_dataset
├── readme.md
├── requirements.txt
├── venv
├── weights
├── yolo_v8_tracking.py
└── yolo_v8_train.py
```
now create "CustomDataset.yml" file under "datasets" directory and write following lines to it :
```
path: cooked_dataset/
train: train/images
val: val/images
test: 

names:
  0: bolt
  1: nut
```
once everything is ok as similar as above just run :

```
python yolo_v8_train.py
```
it takes 5 epochs to finish training with high accuracy. after training finished you can find trained weights under :
```
runs/detect/train{i}/weights
```

#### Inference with tracking

simply run :
```
python yolo_v8_tracking.py
```

## Authors

[Elham Moeini](https://www.linkedin.com/in/elham-moeini-6178257a/)

## License

This project is licensed under the [Stroma-Vision] License.

## Acknowledgments

References :

* [yolo-v8 ultralytics](https://github.com/ultralytics/ultralytics)
* [ByteTrack algorithm](https://github.com/ifzhang/ByteTrack)
