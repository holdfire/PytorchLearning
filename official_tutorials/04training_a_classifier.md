### 训练一个分类神经网络
#### 1. 数据集的加载、标准化和切分
+ 第一步：使用`torchvision.transforms`构造一个数据变换的函数对象，作为下一步的参数；
+ 第二步：使用`torchvision.datasets()`生成数据集，shape是[batch_size, channels, height, weight]，和OpenCV读取的顺序不一样；
+ 注意：torchvision数据集的输出是[0, 1]范围之间的PILImage格式数据，通常将其标准化为[-1, 1]之间的tensor；
+ 第三步：使用`torch.utils.data.DataLoader()`用于加载上述数据集，生成数据集加载器；
+ 第四步：构造一个容器，加载数据集的标签。

#### 2. 定义一个CNN
+ Net类的构造函数`__init__()`：使用`torch.nn`和`torch.nn.functional`中的模块构神经网络的Module；
+ Net类的前向传播函数`forwad()`：不断前向传播；
+ 构建一个Net的实例对象net。

#### 3. 定义损失函数和优化器
+ 使用`torch.nn`模块构造损失函数
+ 使用`torch.optim`选择优化方法

#### 4. 训练神经网络
+ 指定训练的epoch，选取一个batch；
+ initialize：给data和label赋值，优化器对梯度初始化为零；
+ forward：网络前向传播计算输出output；
+ backward：计算损失loss，反向传播计算梯度；
+ optimize：优化器更新参数；
+ print：每隔一定的step打印出loss。
+ save：使用`torch.save(net.state_dict(), PATH)`保存模型，带第一个参数时只保存模型参数；

#### 5. 在测试集上测试
+ 构造模型：首先使用net=Net()构造一个对象，通过`net.to(device)`可以将模型加载到CUDA上；
+ 加载参数：然后用`net.load_state_dict(torch.load(PATH))`给模型参数赋值；
+ 模型预测：将dataloader中的item作为net的输入得到output，也要对数据使用.to(device)方法才能加载到CUDA上；
+ 后处理：选取概率最大的index作为分类预测结果；

#### 6. 使用训练好的模型推理
+ 将`with torch.no_grad():`添加到代码块前，可以不跟踪计算梯度；
+ 可以计算各个类别预测的准确率，找出badcase，从而通过改变数据来优化模型；
