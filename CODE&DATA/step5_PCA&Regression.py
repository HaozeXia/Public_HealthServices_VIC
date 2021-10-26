'''
    This is the fourth part of this project, which we do the modeling.
    before we do PCA, since we have to use logistic model, we have to do the Standardization
    the second step is PCA using sklearn library
    the third step is logistic regression
'''
import numpy as np
import math
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def standardization(x_raw):
    # the standardization function
    mean = np.mean(x_raw)
    var = np.var(x_raw, ddof=1)
    x_raw=(x_raw-mean)/math.sqrt(var)
    return x_raw

def pre_standardization(x_pre,mean,var):
    x_pre = (x_pre - mean) / math.sqrt(var)
    return x_pre

def sigmoid(inX):
    return 1.0/(1+np.exp(-inX))

def fit(X,t):
    n_s = X.shape[0]
    n_f = X.shape[1]
    X = np.mat(X)
    t = t.reshape(n_s,1)
    w = np.zeros((n_f,1))
    iter_num = 100 # number of iterations
    for i in range(iter_num):
        y = sigmoid(X*w)
        R = np.mat(np.eye(n_s))
        for j in range(n_s):
            R[j,j] = y[j]*(1-y[j])
        z = X*w - R.I*(y-t)
        w = (X.T*R*X).I*X.T*R*z
    return w

# first step, we read the data, and standardize it
x_raw=np.loadtxt(open("x1.csv", "rb"), delimiter = ",", skiprows = 0)
y_raw=np.loadtxt(open("y1.csv", "rb"), delimiter = ",", skiprows = 0)
# this is the highest average value for high income country from word bank WDI database
y_standard=13
# firstly transform y
y=y_raw/y_standard
# then standardize x
x=x_raw
# col 1 is the year
x[:,0]=standardization(x_raw[:,0])
# col 2 is the GVA
x[:,1]=standardization(x_raw[:,1])
# col 3 is the unemployment
x[:,2]=standardization(x_raw[:,2])
# col 4 is the recurrent
x[:,3]=standardization(x_raw[:,3])
# col 5 is the income
x[:,4]=standardization(x_raw[:,4])
# col 6 is the labour
x[:,5]=standardization(x_raw[:,5])
# col 7 is the life exp
x[:,6]=standardization(x_raw[:,6])
# col 8 is the PM2.5
x[:,7]=standardization(x_raw[:,7])
# col 9 is the pop density
x[:,8]=standardization(x_raw[:,8])
# col 10 is the population
x[:,9]=standardization(x_raw[:,9])

# second step, do the PCA for x
pca=PCA(n_components='mle')
pca.fit(x)
x_pca=pca.transform(x)
x_final=x
for i in range(9):
    x_final[:,i]=x_pca[:,i]
x_final[:,9]=1

# third step, logistic regression
w = fit(x_final,y)

# analysis the result
y_pre=sigmoid(x_final*w)*y_standard
y_pre=np.array(y_pre).flatten()
plt.ylim((2, 3.3))
plt.scatter(y_pre,y_raw,marker='.')
plt.plot(y_pre,y_pre, '-')
plt.xlabel('y predict')
plt.ylabel('y true value')
plt.title('true y vs y predict')

# hypothesis test
ssmean=sum(pow(y_raw-np.mean(y_raw),2))
ssfit=sum(pow(y_raw-y_pre,2))
F=(ssmean-ssfit)*(70-10)/ssfit/(10-1)
# this gives F-static=20.41236
# since 95% F value is 2.787 (df1=60,df2=9)
# thus this model is acceptable

# finally we use this model to predict how the change of factor will influence result (focus on VIC only)
x_raw=np.loadtxt(open("x.csv", "rb"), delimiter = ",", skiprows = 0)
prex=x_raw[27]
x_pre=[]
for i in range(70):
    j=int(i/7)
    k=i%7
    temp = prex * 1
    if k==0:
        temp[j]=temp[j]*1.1
        x_pre.append(temp)
    elif k==1:
        temp[j]=temp[j]*1.05
        x_pre.append(temp)
    elif k==2:
        temp[j]=temp[j]*1.01
        x_pre.append(temp)
    elif k==3:
        temp[j]=temp[j]
        x_pre.append(temp)
    elif k==4:
        temp[j]=temp[j]*0.99
        x_pre.append(temp)
    elif k==5:
        temp[j]=temp[j]*0.95
        x_pre.append(temp)
    else:
        temp[j]=temp[j]*0.9
        x_pre.append(temp)
x_pre=np.array(x_pre)
for i in range(10):
    x_pre[:, i] = pre_standardization(x_pre[:, i],np.mean(x_raw[:, i]),np.var(x_raw[:, i], ddof=1))
x_pre_pca=pca.transform(x_pre)
x_pre_final=x_pre
for i in range(9):
    x_pre_final[:,i]=x_pre_pca[:,i]
x_pre_final[:,9]=1
y_result=sigmoid(x_pre_final*w)*y_standard
output=y_result.reshape(7,10)
np.savetxt('result.csv', output, delimiter = ',')