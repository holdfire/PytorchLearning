### 数据并行：使用多个GPU加载数据
#### 1.将模型和数据加载到单个GPU中：
```
# 将模型加载到GPU中
device = torch.device("cuda:0)
model = model.to(device)
# 将数据加载到GPU中：在GPU中复制my_tensor1一份并返回
my_tensor2 = my_tensor1.to(device)
```

#### 2. Pytorch使用多个GPU（默认使用单个GPU）
+ 使用`model = nn.DataParellel(model)`可以让模型在多个GPU上并行；
+ 此时batch_size会被平均分配到各个GPU上分别计进行forward计算，然后归并到一起；

#### 参考资料：
并行训练：https://zhuanlan.zhihu.com/p/145427849?utm_source=wechat_session&utm_medium=social&utm_oi=44023196680192&utm_content=sec
