## BOSCH'S AGE AND GENDER DETECTION MODEL

---

### USAGE: 

#### Setup :

Clone this repository:
```
git clone <TODO : enter git repo link here>
```
Installing the dependencies:
```
# Changing the working directory into the repository
cd <TODO : insert repo name here>
# Installing the dependencies
pip3 install 'git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI'
pip3 install --upgrade --no-cache-dir gdown
pip3 install -r requirements.txt
```
 Downloading the pretrained models & storing them under `/pretrained`. Please note, if these commands do not work please download the files from the drive link provided here<TODO : PLEASE UPDATE THE LINKS HERE>
```
cd pretrained
gdown "1TBMa2JzJhhKt2lSF8rciUf3llk1XMRwD"
unzip New_32CL_5LR_43Epoc.zip
rm -rf New_32CL_5LR_43Epoc.zip
!gdown --id "1P4mY0Yyd3PPTybgZkjMYhFri88nTmJX5"
cd ..
```

Finally your `/pretrained/` directory should look as follows
 ```
pretrained
    ├── New_32CL_5LR_43Epoc
    ├── bytetrack_x_mot17.pth.tar
    └── .gitignore
 ```

Finally run the setup:
```
python3 setup.py develop
```
#### Testing on images/videos:

> The output csv file will be stored under the `/final_output` directory as `predictions.csv`.
> The csv file follows the format : `frame_id, track_id, x, y, w, h, age_actual, gender`

To test on videos :
```
python3 tools/demo_track.py video -c pretrained/bytetrack_x_mot17.pth.tar --path "<$path_to_video>" 
```

To test on a single image :
```
python3 tools/demo_track.py image -c pretrained/bytetrack_x_mot17.pth.tar --path "<$path_to_image>" 
```

To test on a directory of images :
```
python3 tools/demo_track.py image -c pretrained/bytetrack_x_mot17.pth.tar --path "<$path_to_directory_of_images>" 
```
