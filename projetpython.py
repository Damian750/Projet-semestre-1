import os
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv('EIVP_KM.csv', sep=';', index_col='sent_at', parse_dates=True)


def min_max(): #on calcule les min et max journaliers
    
    variable=input('entrer une variable (temp,humidity,co2,noise,lum):')
    d=input('date debut:')
    f=input('date fin:')
    
    df.loc[d:f,variable].resample('D').min().plot(label='min')
    df.loc[d:f,variable].resample('D').max().plot(label='max')
    
    plt.title('min et max journaliers')
    plt.show()

    
def moyenne():   #on calcule la moyenne journalière
    
    variable=input('entrer une variable (temp,humidity,co2,noise,lum):')
    d=input('date debut:')
    f=input('date fin:')
    
    df[variable][d:f].resample('D').mean().plot(label='id=1',ls=':')
    
    plt.title('Moyenne journalière')
    plt.show()
    
    
    
def humidex():
    
    d=input('date debut:')
    f=input('date fin:')
    
    df['alpha']=((17.27*df['temp'])/(237.7+df['temp']))+np.log(df['humidity']/100)
    df['temp_rosée']=(237.7*df['alpha'])/(17.27-df['alpha'])
    df['humidex']= df['temp']+0.555*(6.11*np.exp(5417.7530*((1/273.16)-1/(273.15+df['temp_rosée'])))-10)
    
    
    df['humidex'][d:f].plot()

    plt.ylabel('°C')
    plt.title('Indice humidex au cours du temps')
    plt.show()
