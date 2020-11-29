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

    
##L’évolution d’une variable en fonction du temps


#On crée une bibliothèque 'unites' pour pouvoir assimiler à une variable son unité de mesure puis l'afficher sur l'axe des ordonnées. Une bibliotèque 'variable_dico' pour traduire les noms des variables en français pour l'intitulé du graphique:

unites={ 'temp':'°C', 'noise':'dBA' , 'lum':'lux', 'co2':'ppm' , 'humidity':'%' }
variable_dico={'temp':'température','noise':'bruit','lum':'luminosité','co2':'CO_2','humidity':'humidité relative'}

#La fonction 'evolution()' permet d'afficher l'evolution d'une variable en fonction du temps si on précise la variable, la plage horaire ('d' pour début et 'f' pour fin) et la liste 'L' des capteurs qu'on souhaite analyser:

def evolution():
        variable=input('entrer une variable (temp,humidity,co2,noise,lum):')
        d=input('entrer date début (exemple 2020-09):')
        f=input('entrer date fin:')
        L=[int(el) for el in input('choix des capteurs de 1 à 6 (ex: 1 3 5):').split()]
        
        
        for k in range(len(L)):  #on parcourt la liste des capteurs sélectionnés
                df[df['id']==L[k]][variable][d:f].plot(label=f' capteur {L[k]}') # et on dessine le graphique correspondant au capteur 'id' pour la variable et la plage horaire choisies
        plt.title( 'Evolution de la ' + variable_dico[f'{variable}'])
        plt.ylabel(unites[f'{variable}'])
        plt.legend()               
        plt.show()
