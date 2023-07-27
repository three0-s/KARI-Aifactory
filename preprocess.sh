#! /bin/bash 

mkdir -p container-dota/train/imgs
cp container_dataset/train_images/*.png container-dota/train/imgs
python dotaprocess.py
python tools/data/dota/split/img_split.py --base-json tools/data/dota/split/split_configs/ms_train.json

mkdir -p container-dota/val/imgs
cp container_dataset/valid_images/*.png container-dota/val/imgs
python tools/data/dota/split/img_split.py --base-json tools/data/dota/split/split_configs/ms_test.json

