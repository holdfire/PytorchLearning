### 前言：
+ 使用GPU做运算时，模型输入张量要加载到GPU上并转换为cuda tensor：my_tensor = my_tensor.to("cuda")；
+ 模型参数在保存时会注明是gpu上和cpu的格式，所以设备A上训练的模型参数加载到设备B上，需要设置map_location参数做一个remap；
+ 当模型已经加载到GPU后，要使用model.to("cuda")，作用是convert model’s parameter tensors to CUDA tensors；

  
#### 1.将模型A的参数加载到模型B中：
+ 应用场景：如在transefer learning中，将模型A的部分参数加载到模型B中后再训练模型B，来warmstart模型B；  
```
# Save model A
PATH = "model.pt"
torch.save(netA.state_dict(), PATH)

# Load into model B, strict参数为False：模型A和模型B参数的key不匹配时，可自动更改模型A的以匹配
netB.load_state_dict(torch.load(PATH), strict=False)
```

#### 2.在不同的设备间保存和加载模型
+ 2.1在GPU上保存，在CPU上加载
```
# Specify a path to save to
PATH = "model.pt"
# Save
torch.save(net.state_dict(), PATH)
# Load
device = torch.device('cpu')
model = Net()
model.load_state_dict(torch.load(PATH, map_location=device))
```
+ 2.2在GPU上保存，在GPU上加载：记得要对所有输入的tensor使用`.to(torch.device('cuda'))`方法
```
# Save
torch.save(net.state_dict(), PATH)
# Load
device = torch.device("cuda")
model = Net()
model.load_state_dict(torch.load(PATH))
model.to(device)
```
+ 2.3在CPU上保存，在GPU上加载
```
# Save
torch.save(net.state_dict(), PATH)
# Load
device = torch.device("cuda")
model = Net()
# Choose whatever GPU device number you want
model.load_state_dict(torch.load(PATH, map_location="cuda:0"))
# Make sure to call input = input.to(device) on any input tensors that you feed to the model
model.to(device)
```

#### 3. 保存`torch.nn.DataParallel`模型
```
# Save
torch.save(net.module.state_dict(), PATH)
# Load to whatever device you want
```


#### 参考资料：
+ 1.https://blog.csdn.net/LXYTSOS/article/details/90639524?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.nonecase

