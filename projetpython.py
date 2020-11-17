import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt
from datetime import timedelta, timezone
from dateutil import tz
os.chdir('C:\\Users\\22bla\\Documents\\Damien_Ecole\\Info')
#df=pd.read_csv("EIVP_KM.csv")
# for idx,column in enumerate(df.columns):
#     print(idx,column)

# ID,NOISE,TEMP,HUMIDITY,LUM,CO2,SENT_AT=[],[],[],[],[],[],[]
# 
# for k in df['id']:
#     ID.append(k)
# for k in df['noise']:
#     NOISE.append(k)
# for k in df['temp']:
#     TEMP.append(k)
# for k in df['humidity']:
#     HUMIDITY.append(k)
# for k in df['lum']:
#     LUM.append(k)
# for k in df['co2']:
#     CO2.append(k)
# for k in df['sent_at']:
#     SENT_AT.append(k)
    
#x = df.iloc[1,6]['Date'].dtstrf.time('%Y-%m-%d %H:%M:%S')

# df.plot(x='Date',y='temp')
# plt.show()
#d_parser = lambda x:pd.datetime.strptime(x,'%Y-%m-%d %H-%Min-%S %tz')
#df=pd.read_csv('EIVP_KM.csv', sep=';',parse_dates=['sent_at'],date_parser=d_parser)
df=pd.read_csv('EIVP_KM.csv', sep=';', index_col='sent_at', parse_dates=True)
#df=pd.read_csv('EIVP_KM.csv', sep=';')

#df['sent_at']=pd.to_datetime(df.sent_at)


#df['year']=df.sent_at.dt.year
#df.sort_values(by='sent_at')
#voir type des séries: df.dtypes
#df.sort_values(by=['sent_at'])
#valeurs interessantes: df.describe()
#df.index

##Selection d'une plage de date
#par exemple : df.loc['2019-08-11 21:31:40+02:00':'2019-08-14 05:31:35+02:00',"temp"]


##MOYENNE
# exemple qui ne donne pas grand chose : df.groupby(["temp"]).mean() plutot donner la moyenne des valeurs en fonction des id : df.groupby(["id"]).mean()

#selectionner que les valeurs avec id<2 :df['id']<2  on obtient un mask on peut injecter ce mask dans le dataf avec : df[df['id']<2]

##Matplotlib
# plt.subplot(221)
# df[df['id']==1]['temp'].plot(kind="b")
# plt.subplot(222)
# df[df['id']==2]['temp'].plot()
# plt.subplot(223)
# df[df['id']==3]['temp'].plot()
# plt.subplot(224)
# df[df['id']==4]['temp'].plot()
#plt.subplot(225)
#df[df['id']==5]['temp'].plot()
# plt.subplot(226)
# df[df['id']==6]['temp'].plot()

#plt.plot_date(df['sent_at'],df['temp'])
#df=df.drop(['id'],axis=1)
#df.plot(subplots=True, figsize=(6, 6))
A=df.loc['2019-08-11 21:31:40+02:00':'2019-08-14 05:31:35+02:00',"temp"]
A.plot()
plt.show()


#HUMIDEX (il 'sagit simplement de faire des opérations entre les colonnes du tableau pour calculer l'humidex par sa formule)
import numpy as np
df['alpha']=(17.27*df['temp']/(237.7+df['temp'])+np.log(df['humidity']))

df['temp_rosée']=((237.7*df['alpha'])/(17.27-df['alpha']))

df['humidex']= df['temp']+0.555*(6.11*np.exp(5417.7530*((1/273.16)-1/(273.15+df['temp_rosée'])))-10)
