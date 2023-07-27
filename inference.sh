#! /bin/bash 

python tools/test.py models/230721-1345/lsk_s_ema_fpn_1x_kari_ms_le90.py models/230721-1345/model-230721-1345_epoch_11.pth --work-dir models/230721-1345 --format-only
python make_submission.py --txt models/230721-1345/.subm/Task1_container.txt --outdir models/230721-1345

python tools/test.py models/230722-1556/lsk_s_ema_fpn_1x_kari_ms_le90.py models/230722-1556/model-230722-1556_epoch_11.pth --work-dir models/230722-1556 --format-only
python make_submission.py --txt models/230722-1556/.subm/Task1_container.txt --outdir models/230722-1556

python tools/test.py models/230724-1604/lsk_s_ema_fpn_3x_kari_ms_le90.py models/230724-1604/model-230724-1604_epoch_15.pth --work-dir models/230724-1604 --format-only
python make_submission.py --txt models/230724-1604/.subm/Task1_container.txt --outdir models/230724-1604
