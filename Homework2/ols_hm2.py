import numpy as np
import pandas as pd

#y= dependent variable
#X = dataset matrix
#β=coeefficient, "unknown population parameter to estimate"
#e=error

def ols(X, y):
    #coeefficient
    B = np.linalg.inv(X.transpose() @ X) @ X.transpose() @ y
    #print(B)
    #standardizedcoeefficient
    BB = (np.std(X) / np.std(y)) * B
    print(BB)
    #error
    e = y - (X @ B)
    n= X.shape[0]
    #print(n)
    k= X.shape[1]
    #print(k)
    q2 = (e.transpose() @ e) / (n - k - 1)
    #variance
    varB = np.diag(q2 * (np.linalg.inv(X.transpose() @ X)))
    #print(varB)
    #standard error
    SE = np.sqrt(varB)
    #confidence intervals, in output it gives [int1,int1][int2,int2] I could not figure out how to match them correctly.
    int1 = B - SE * 1.96
    int2 = B + SE * 1.96
    Confi = (int1, int2)
    print("coefficient:", B)
    #print("standardized coeeficient:", BB)
    print("standard error:", SE)
    print("confidence intervals:", Confi)
    return
