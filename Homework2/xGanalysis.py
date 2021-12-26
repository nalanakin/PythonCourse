import numpy as np
import pandas as pd
import ols_hm2

data = pd.read_csv('2ind.csv')

dep = data.iloc[:,2]
indep = np.array(data.iloc[:,0:2])
#indep = np.reshape(indep, (760,2))
#dep = np.reshape(dep, (760,1))
#print(indep.ndim)
#print(indep.shape)
#print(dep.shape)

ols_hm2.ols(indep, dep)
