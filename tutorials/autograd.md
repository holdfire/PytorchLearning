### autograd包为tensor上所有的操作提供自动求导：  
+ **设置自动求导**：设置tensor的`.requires_grad`属性为True时(默认为False)，该张量后续所有的opreation都会被跟踪；
+ **张量计算梯度**：对tensor调用`.backward()`方法可以自动计算得到该tensor的所有元素的梯度，调用元素张量的`.grad`属性可获取其梯度；
+ **标量计算梯度**：对标量scalar使用`.backward()`方法不需要指定任何参数，对tensor则需要指定一个相同shape的tensor作为参数；
+ **关闭自动求导**：对一个要自动求导的tensor调用`.detach()`方法，或者预先声明`with torch.no_grad():`，可以不跟踪梯度，在evaluation时可以省内存；
+ **求导计算方法**：每个通过一系列operation创造的tensor都有一个`.grad_fn`属性，指向直接创造这个tensor的`Function`;
