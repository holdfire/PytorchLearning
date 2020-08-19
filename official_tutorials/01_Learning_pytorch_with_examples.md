##### 1.1 Pytorch的Tensor和numpy比较的优势：
+ tensor能够使用GPU做运算而numpy不能；
+ 有更多的属性和方法，比如跟踪计算图和梯度；

##### 1.2 autograd
+ 当使用autograd的时候，网络的前向过程会定义一个**computational graph**；
+ 计算图的节点是Tensor，边是由input tensor到output tensor的函数；

##### 1.3 Pytorch支持自定义可微分的function
+ 首先写一个forward方法；
+ 然后写一个backward方法；

##### 1.4 nn.module提供高阶的计算图
+ Module接收input Tensor并计算出output Tensor；
+ 所以个人认为：nn.module相当于函数，计算图中的边；

##### 1.5 优化算法：optim包
##### 1.6 自定义nn.modules
+ 需要继承nn.Module这个类；
+ 定义一个forward方法，接收输入tensor，产生输出的tensor
  
  