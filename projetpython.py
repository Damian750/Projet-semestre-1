import os
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('EIVP_KM.csv', sep=';', index_col='sent_at', parse_dates=True)



def humidex():

    date1=input('date de début en format;2019-08-11 11:31:42+02:00=')
    date2=input('date de fin en format;2019-08-11 11:31:42+02:00=')

    df['alpha']=(17.27*df['temp']/(237.7+df['temp'])+np.log(df['humidity']))

    df['temp_rosée']=((237.7*df['alpha'])/(17.27-df['alpha']))

    df['humidex']= df['temp']+0.555*(6.11*np.exp(5417.7530*((1/273.16)-1/(273.15+df['temp_rosée'])))-10)

    A=df.loc['date1':'date2',"humidex"]

    A.plot
    plt.show
