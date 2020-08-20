import torch
import torch.nn.functional as F


class Mnist_CNN(nn.Module):
    def __init__(self):
        self.conv1 = torch.nn.Conv2d(1, 16, kernel_size=3, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(16, 16, kernel_size=3, stride=2, padding=1)
        self.conv3 = torch.nn.Conv2d(16, 10, kernel_size=3, stride=2, padding=1)

    def forward(self, x):
        x = x.view(-1, 1, 28, 28)
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        x = F.avg_pool2d(x, 4)
        x = x.view(-1, x.size(1))

net = Mnist_CNN()

