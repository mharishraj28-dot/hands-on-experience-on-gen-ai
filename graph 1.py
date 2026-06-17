import pandas as pd
import matplotlib.pyplot as plt

data={'value':[40,50,60,70],'category':['it','cse','civil','it']}
df=pd.DataFrame(data)
print(df)

print('\n bar plot: \n')
df.plot(kind='line',x='category',marker='o',y='value',title='data anlysis')
plt.show()
