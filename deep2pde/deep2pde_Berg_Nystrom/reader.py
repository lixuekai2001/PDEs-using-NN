import scipy.io as sio

data = sio.loadmat('burgers_sine.mat')
print(type(data))
print(data.keys())
print(data['usol'])