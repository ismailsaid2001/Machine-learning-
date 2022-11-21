#regression linéaire Numpy ML#8
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import  matplotlib.pyplot as plt
from sklearn.datasets import make_regression
def modele(x,theta) :
    return x.dot(theta)
#making dataset :
x,y=make_regression(n_samples=100,n_features=1,noise=10)
y=y.reshape(y.shape[0],1)
plt.scatter(x,y)
X=np.hstack( (x,np.ones(x.shape)) )
# print(x)
#vecteur theta :
theta=np.random.randn(2,1)
#fonction cout :
def cost_function(x,y,theta) :
    m=len(y)
    return 1/(2*m) *np.sum((modele(x,theta)-y)**2)
def grad(x,y,theta) :
    m=len(y)
    return (1/m) * x.T.dot((modele(x,theta)-y))
def gradient_decent(x,y,theta,learning_rate,n_iteration ):
    cost_history=np.zeros(n_iteration)
    for i in range(0,n_iteration) :
        theta=theta-learning_rate*grad(x,y,theta)
        cost_history[i]=cost_function(x,y,theta)
    return theta,cost_history
def coef_determination(y,pred) :
    u=((y-pred)**2).sum()
    v=((y-y.mean())**2).sum()
    R=1-u/v
    return R




theta_final,cost_history=gradient_decent(X,y,theta,0.01,1000)
# print(theta_final)
print(coef_determination(y,modele(X,theta_final)))
#ploting cost_history in 1000 iterations
# plt.plot(range(1000),cost_history)
predictions=modele(X,theta_final)
plt.scatter(x,y)
plt.plot(x,predictions,c='r')
plt.show()
# plt.plot(x,modele(X,theta))
# plt.show()
# print(theta)
#print(cost_function(x,y,theta)) :ça retourne un cout plus ou moins haut
#ploting nuage des points :
# plt.scatter(x,y)
# plt.show()
# print (x.shape)
# print(y.shape)