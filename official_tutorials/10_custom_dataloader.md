#### 1. 加载自定义的数据集通常三步走：  
参考资料：https://pytorch.org/tutorials/recipes/recipes/custom_dataset_transforms_loader.html
+ （1）使用pytorch的dataset api创建以自定义数据集；
+ （2）对数据集创建一系列的callable的transform，需要重写`__call__`方法；
+ （3）创建一个dataloader

#### 2. `torch.utils.data.Dataset`类：
+ `Dataset`是一个抽象类，自定义的数据集类应该继承`Dataset`；
+ 自定义的数据集要重写`__len__`和`__getitem__`方法；

#### 3. `torchvision.transform`类：
+ 常用的对数据的一些操作：rescale，randomCrop，toTensor；
```python
# example
transform = transforms.Compose([Rescale(256), RandomCrop(224), ToTensor()])
```

### 4. `torch.utils.data.DataLoader`类
+ DataLoader可以对dataset进行取batch、shuffle、多进程加载等操作；

