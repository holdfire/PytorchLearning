from collection import namedtuple
from string import Template

import cupy as cp
import torch as t
from torch.autograd import Function
from model.utils.roi_cupy import kernel_backward, kernel_forward

Stream = namedtuple('Stream', ['ptr'])

