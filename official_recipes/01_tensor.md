### Pytorch中的tensor
#### 1.创建tensor
**在创建tensor时，如果指定参数device = torch.device("cuda")，会直接在GPU中创建tensor**  
**也可以先在cpu中创建好tensor，然后对该tensor对象调用.to("cuda")的方法，此时会在gpu中复制一份新的tensor并返回**  
+ torch.empty(5,3)创建一个5行3列的tensor，元素
+ torch.zeros()同上，元素为0
+ torch.ones()同上，元素为1
+ torch.rand()创建[0,1]之间的tensor
+ torch.randn()创建服从标准正态分布的tensor
+ torch.new_ones()创建元素为1的tensor
+ torch.tensor([3, 5.5])直接根据这些个元素创建tensor
+ torch.randn_like(a)创建和a一样shape的tensor，元素服从正态分布
+ torch.ones_like(a)创建和a一样shape的tensor，元素为1


#### 2.1 通过tensor对象obj，直接调用tensor的方法method
+ obj.size()返回一个tuple，张量的shape
+ obj.shape返回张量形状这个属性
+ obj.add_(obj2)将两个tensor对象相加
#### 2.2 通过类名调用tensor的方法
+ torch.add(tensor1, tensor2, out=):将两个张量相加，结果输出到out


#### 3. tenso对象obj的形状变化
+ obj.view(new_shape)

#### 4. tensor的索引index：和numpy的ndarray相似

#### 5. tensor和numpy的互相转换
+ obj.numpy()将一个tensor对象obj直接转换为numpy的ndarray类型数据
+ b = torch.from_numpy(a)将一个numpy的对象转换为tensor




