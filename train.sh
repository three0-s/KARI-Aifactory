#!/bin/bash

TIME=`date +%Y-%m-%d_%H:%M`

python tools/train.py configs/230721_lsk_s_ema_fpn_1x_kari_ms_le90.py \
        --work-dir $TIME"_1" --seed 991108 --deterministic


python tools/train.py configs/230722_lsk_s_ema_fpn_1x_kari_ms_le90.py \
        --work-dir $TIME"_2" --seed 991108 --deterministic

python tools/train.py configs/230724_lsk_s_ema_fpn_3x_kari_ms_le90.py \
        --work-dir $TIME"_3" --seed 991108 --deterministic