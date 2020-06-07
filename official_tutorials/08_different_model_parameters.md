#### 1.将模型A的参数加载到模型B中：
+ 应用场景：如在transefer learning中，将模型A的部分参数加载到模型B中后再训练模型B，来warmstart模型B；  
```
# Save model A
PATH = "model.pt"
torch.save(netA.state_dict(), PATH)

# Load into model B, strict参数为False：模型A和模型B参数的key不匹配时，可自动更改模型A的以匹配
netB.load_state_dict(torch.load(PATH), strict=False)
```





