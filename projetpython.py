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
  
def ecart_type():
    capteur=int(input("entrer un id du capteur:"))
    variable=input('entrer une variable (temp,humidity,co2,noise,lum):')
    d=input('entrer date début (exemple 2020-09):')
    f=input('entrer date fin:')



    fig, ax = plt.subplots(figsize=(8,5))
    ax2 = ax.twinx()
    
    ax.plot(df[df["id"]==capteur][variable][d:f].resample('D').mean().index,df[df['id']==capteur][variable][d:f].resample('D').mean(),color='r')
    
    ax2.bar(df[df["id"]==capteur][variable][d:f].resample('D').std().index,df[df['id']==capteur][variable][d:f].resample('D').std(),color='b',alpha=0.2)


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
        
     
 #Anomalies   
    


def anomalie_arret():
    V=['temp','noise','lum','co2','humidity'] # on crée la liste des variables pour pouvoir la parcourir.
    capteur_defiant=0   # on initialise la variable qui va nous permettre d'identifier le capteur défiant.
    
    for variable in V:
        
        for capteur in range(1,7):
            
            for k in range(len(df[df['id']==capteur].index)-1):    #on parcourt toutes les données du capteur, choisi avec la boucle for précédente.
                
                T = df[df['id']==capteur].index[k+1] - df[df['id']==capteur].index[k] #on calcule la différence de temps écoulé entre deux prises de mesures. Il s'agit d'un Timedelta.
                
                if T.components.days!=0:   #si le temps entre deux mesures dépasse un jour on considère qu'il s'agit d'une anomalie d'interruption du capteur.
                    
                    indice=k
                    A=df[df['id']==capteur].index[indice]  # on relève les caractétistiques des deux valeurs entre lesquelles le temps écoulé dépasse un jour. Il s'agit d'un Timestamp
                    B=df[df['id']==capteur].index[indice+1]
                    
                    capteur_defiant=capteur
                    
                    df[df['id']==capteur][variable][A._repr_base:B._repr_base].plot(label=f'Arrêt du capteur {capteur}',ls=":",lw=5,color='r')   
                    #on représente alors toutes les valeurs qui ont présentées cette anomalie. Le module ._repr_base donne la date exacte
                    
            if capteur_defiant==capteur:   #Si un capteur défiant a été détecté alors on représente la courbe de la variable et du capteur concerné en totalité.
                
                df[df['id']==capteur_defiant][variable].plot(label=f'Capteur {capteur_defiant}')
                plt.title(f'Evolution de la variable "{variable}" en fonction du temps')
                plt.legend()
                plt.show()
    print(f'Le capteur qui présente une anomalie d arrêt est le capteur "{capteur_defiant}"')
    
    
    
def anomalie_valeur():
    
    capteur=int(input("entrer un id du capteur:"))
    variable=input('entrer une variable (temp,humidity,co2,noise,lum):')
        
    for k in range(len(df[df['id']==capteur].index)-1):  #on parcourt les valeurs du tableau du capteur correspondant.
        
        D=np.abs(df[df['id']==capteur][variable][k]-df[df['id']==capteur][variable].resample('D').mean()[df[df['id']==capteur][variable].index[k]._date_repr])
       
        # D est la différence entre la valeur d'une variable (d'indice k) pour un capteur donné et la valeur moyenne de cette variable sur la journée.
        
        s=df[df['id']==capteur][variable].std()
        
        # s est l'écart-type
        # Une valeur présentant un écart à la moyenne inférieur à l'écart type est banale, compris entre une et deux fois l'écart type est modérément courante, compris entre deux et trois fois l'écart type commence a être remarquable,compris entre trois et quatre fois l'écart type est exceptionnelle, supérieur à quatre fois l'écart type est historique et très rare.
        
        if D>=s and D<2*s:
                        df[df['id']==capteur][variable][k:k+1].plot(label='',lw=2,color='g',marker='o')
        
        if D>=2*s and D<3*s:
                        df[df['id']==capteur][variable][k:k+1].plot(label='',lw=2,color='r',marker='o')
        
        if D>=3*s and D<4*s:
                        df[df['id']==capteur][variable][k:k+1].plot(label='anomalie exceptionnelle',lw=2,color='m',marker='o')
        
        if D>=4*s:
                        df[df['id']==capteur][variable][k:k+1].plot(label='anomalie rare',lw=2,color='k',marker='o')
    
    df[df['id']==capteur][variable].plot()
    plt.legend()
    plt.show()
    
    
def occupation():
    
    capteur=int(input('choix des capteurs de 1 à 6:'))
# df[df['id']==capteur]['co2'].plot(label='co2')
# plt.show()
            
    for k in range(len(df[df['id']==capteur].index)-1):
        while df[df['id']==capteur]['co2'][k]>500:
            indice=k
            A=df[df['id']==capteur].index[indice]
            B=df[df['id']==capteur].index[indice+1]
                
            df[df['id']==capteur]['co2'][A._repr_base:B._repr_base].plot(ls=":",lw=5,color='r')   
    df[df['id']==capteur]['co2'].plot(label='co2')       
    plt.text('Hello World !')
    plt.show()
