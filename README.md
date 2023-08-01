# KARI-Aifactory MYGA Team Submission - LSKNet Rotated Object Detection
This is a code-base of team MYGA submission. 



# Install 
```
pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
pip install -U openmim
mim install mmcv-full==1.7.1
mim install mmdet\<3.0.0
pip install opencv-python==4.5.5.64
apt-get update
apt-get -y install libgl1-mesa-glx
pip install timm
pip install shapely
pip install -r requirements.txt
pip install -v -e .
# Or use this docker image (dpsqlsdh/mmrotate3:latest)
```

## Test & Download Model Weights

Refer to test.ipynb


### Train 

Refer to train.ipynb
