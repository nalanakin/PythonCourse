import statsmodels.api as sm
import numpy as np
import pandas as pd

data = pd.read_csv('2ind.csv')

dep = data.iloc[:,2]
indep = np.array(data.iloc[:,0:2])
print(indep)

#indep = sm.add_constant(indep) (önemli)
model = sm.OLS(dep,indep)
results = model.fit()
print(results.params)
print(results.tvalues)

print(results.t_test([1,0]))
