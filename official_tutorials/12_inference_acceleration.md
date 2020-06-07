#### 1. 使用Dynamic Quantization来减小模型尺寸，加速推理过程： 
+ 
```python
import torch.quantization

# Do the Quantization
torch.quantization.quantize_dynamic()

```



