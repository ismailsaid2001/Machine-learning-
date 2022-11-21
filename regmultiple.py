#regression linéaire Numpy ML#8
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import  matplotlib.pyplot as plt
from sklearn.datasets import make_regression
#fonction cout :
def cost_function(x,y,theta) :
    m=len(y)
    return 1/(2*m) *np.sum((modele(x,theta)-y)**2)
def modele(x,theta) :
    return x.dot(theta)
def grad(x,y,theta) :
    m=len(y)
    return (1/m) * x.T.dot((modele(x,theta)-y))
def gradient_decent(x,y,theta,learning_rate,n_iteration ):
    cost_history=np.zeros(n_iteration)
    for i in range(0,n_iteration) :
        theta=theta-learning_rate*grad(x,y,theta)
        cost_history[i]=cost_function(x,y,theta)
    return theta,cost_history
x,y=make_regression(n_samples=100,n_features=1,noise=10)
y=y.reshape(y.shape[0],1)
y=y+abs(y/2)
plt.scatter(x,y)
X=np.hstack((x**2,x,np.ones(x.shape)))
theta=np.random.randn(3,1)
theta_final,cost_history=gradient_decent(X,y,theta,0.01,1000)
predictions=modele(X,theta_final)
plt.scatter(x,y)
plt.scatter(x,predictions,c='r')
plt.show()