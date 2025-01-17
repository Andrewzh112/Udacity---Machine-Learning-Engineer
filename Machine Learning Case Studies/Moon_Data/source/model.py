import torch
import torch.nn as nn
import torch.nn.functional as F

## TODO: Complete this classifier
class SimpleNet(nn.Module):
    
    ## TODO: Define the init function
    def __init__(self, input_dim, hidden_dim, output_dim, n_hidden=2):
        '''Defines layers of a neural network.
           :param input_dim: Number of input features
           :param hidden_dim: Size of hidden layer(s)
           :param output_dim: Number of outputs
         '''
        super(SimpleNet, self).__init__()
        
        # define all layers, here
        self.n_hidden=n_hidden
        self.input=nn.Linear(input_dim,hidden_dim)
        self.hidden=nn.Linear(hidden_dim,hidden_dim)
        self.out=nn.Linear(hidden_dim,output_dim)
        self.sig=nn.Sigmoid()
    
    ## TODO: Define the feedforward behavior of the network
    def forward(self, x):
        '''Feedforward behavior of the net.
           :param x: A batch of input features
           :return: A single, sigmoid activated value
         '''
        # your code, here
        x=F.relu(self.input(x))
        for l in range(self.n_hidden):
            x=F.relu(self.hidden(x))
        x=self.out(x)
        return self.sig(x)