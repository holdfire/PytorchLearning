```python
from torch.utils.tensorboard import SummaryWriter
writer = SummaryWriter("dir)

# inspect the model using TensorBoard
writer.add_graph(net, images)

# visualize the lower dimensional representation of higher dimensional data
writer.add_embedding(features)

# ...log the running loss
writer.add_scalar("training loss", )

# Assessing trained models with TensorBoard
writer.add_pr_curve()
```