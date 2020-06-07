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


