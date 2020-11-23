import os
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('EIVP_KM.csv', sep=';', index_col='sent_at', parse_dates=True)

##Matplotlib
plt.subplot(221)
df[df['id']==1]['temp'].plot(kind="b")
plt.subplot(222)
df[df['id']==2]['temp'].plot()
plt.subplot(223)
df[df['id']==3]['temp'].plot()
plt.subplot(224)
df[df['id']==4]['temp'].plot()
plt.subplot(225)
df[df['id']==5]['temp'].plot()
plt.subplot(226)
df[df['id']==6]['temp'].plot()


#HUMIDEX (il 'sagit simplement de faire des opérations entre les colonnes du tableau pour calculer l'humidex par sa formule)
import numpy as np
df['alpha']=(17.27*df['temp']/(237.7+df['temp'])+np.log(df['humidity']))

df['temp_rosée']=((237.7*df['alpha'])/(17.27-df['alpha']))

df['humidex']= df['temp']+0.555*(6.11*np.exp(5417.7530*((1/273.16)-1/(273.15+df['temp_rosée'])))-10)
