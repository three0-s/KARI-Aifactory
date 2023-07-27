# Copyright (c) ga06033@yonsei.ac.kr
import torch
import torch.nn as nn

from ..builder import ROTATED_LOSSES



@ROTATED_LOSSES.register_module()
class BCELoss(nn.modules.loss.BCELoss):
    def __init__(self, reduction='mean'):
        super().__init__(reduction=reduction)
    
    def forward(self, input, target, **kwargs):
        super().forward(input, target, **kwargs)

    
@ROTATED_LOSSES.register_module()
class BCEWithLogitsLoss(nn.modules.loss.BCEWithLogitsLoss):
    def __init__(self, reduction='mean'):
        super().__init__(reduction=reduction)
    
    def forward(self, input, target, **kwargs):
        super().forward(input, target, **kwargs)
