#### 1.反向传播过程中的梯度
+ 构建神经网络时需要zeroing out所有tensor的梯度，这是因为调用`.backward()`方法时，梯度默认在buffer中是accumulative
+ 每个batch在前向传播之前，都要先对tensor进行zero out；
+ 也可以对模型使用`model.zero_grad()`方法；
```python
for i, data in enumerate(trainloader, 0):
        # get the inputs; data is a list of [inputs, labels]
        inputs, labels = data

        # zero the parameter gradients
        optimizer.zero_grad()

        # forward + backward + optimize
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
```
