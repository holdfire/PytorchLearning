#### 1. 模型的可解释性Model Interpretability using Captum
+ Captum可以应用特征属性算法，如： `Guided GradCam` and `Integrated Gradients`；
+ 安装方法：`pip install captum`，官网：https://captum.ai/；

#### 2. 使用tensorboard可视化训练过程
+ tensorboard功能：可视化metrics如loss和accuracy，可视化计算图、直方图等；
+ 首先我们用`torch.utils.tensorboard.SummaryWriter`创建一个实例对象writer；
+ 使用`add_scalar(tag, scalar_value, global_step=None, walltime=None)`方法记录一个scalar的值；
+ 调用`flush()`方法确保所有events写入到磁盘中了；
+ 在终端中用`$ tensorboard --logdir=runs`命令启动tensorboard，递归文件夹找到*.tfevents*文件；
