#### 1.模型参数的获取
+ 通过`model.parameters()`可以获取模型各层的说明；
+ 通过`model.state_dict()`可以获取键值对：各laye对应r的parameter tensor；
+ 通过`optimizer.state_dict()`可以获取各超参数的value；

#### 2.模型的保存和加载
+ 常保存为.pt或.pth拓展名的文件；
+ 加载模型后使用eval模式才能做inference：主要是因为dropout层和bn层要设置成evaluation
+ 第一种方式是只保存模型的参数state_dict：
```
# Specify a path
PATH = "state_dict_model.pt"
# Save
torch.save(net.state_dict(), PATH)
# Load
model = Net()
model.load_state_dict(torch.load(PATH))
model.eval()
```
+ 第二种方式是保存整个模型：  
这种方式使用了python的pickle模块，pickle对某些类保存的是路径，因而这种方式保存模型可能会出问题；
```
# Specify a path
PATH = "entire_model.pt"
# Save
torch.save(net, PATH)
# Load
model = torch.load(PATH)
model.eval()
```
#### 3. checkpoint的保存和加载
```
# Additional information
EPOCH = 5
PATH = "model.pt"
LOSS = 0.4
torch.save({
            'epoch': EPOCH,
            'model_state_dict': net.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            'loss': LOSS,
            }, PATH)
```
```
model = Net()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
checkpoint = torch.load(PATH)

model.load_state_dict(checkpoint['model_state_dict'])
optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
epoch = checkpoint['epoch']
loss = checkpoint['loss']
model.eval()
# model.train()
```

#### 4. 在一个文件中保存多个pytorch模型
```
# Specify a path to save to
PATH = "model.pt"
torch.save({
            'modelA_state_dict': netA.state_dict(),
            'modelB_state_dict': netB.state_dict(),
            'optimizerA_state_dict': optimizerA.state_dict(),
            'optimizerB_state_dict': optimizerB.state_dict(),
            }, PATH)
```
```
modelA = Net()
modelB = Net()
optimModelA = optim.SGD(modelA.parameters(), lr=0.001, momentum=0.9)
optimModelB = optim.SGD(modelB.parameters(), lr=0.001, momentum=0.9)

checkpoint = torch.load(PATH)
modelA.load_state_dict(checkpoint['modelA_state_dict'])
modelB.load_state_dict(checkpoint['modelB_state_dict'])
optimizerA.load_state_dict(checkpoint['optimizerA_state_dict'])
optimizerB.load_state_dict(checkpoint['optimizerB_state_dict'])

modelA.eval()
modelB.eval()
# - or -
modelA.train()
modelB.train()
```


