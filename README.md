# Projet-semestre-1
Présentation du projet python __Blaszczuk Damian__ et __Gasecki Nicolas__ __Groupe 23__

### Sujet n°1
--------------------
## Introduction brève du code source
* Recherche de la méthode de manipulation d’un tableau de données sur python:
Nous disposions d’un ensemble de données sous la forme d’un tableau csv traduisant l’évolution de différentes caractéristiques d’une pièce (température, humidité, bruit) en fonction du temps. Nous avons d'abord cherché à lire ce format csv sur python, pour ce faire la bibliothèque ```panda``` est la plus adaptée. Une fois ces données importées sur python nous avons commencé à traiter ces données afin de les étudier.
```javascript
import pandas as pd
```
  #### Indexing et présentation des courbes:
Nous avons cherché à afficher les courbes des différentes caractéristiques en fonction du temps. Pour ce faire, nous avons défini le temps (la Serie ```sent_at```) comme indice principal de notre tableau en prenant en compte qu’il s’agissait de dates. A l’aide de la bibliothèque matplotlib nous avons pu ensuite afficher les courbes souhaitées. 
```javascript
df=pd.read_csv('EIVP_KM.csv', sep=';', index_col='sent_at', parse_dates=True)
``` 

## Evolutions des valeurs
La fonction ```evolution()``` permet de faire apparaitre la courbe d'une variable pour des capteurs et une plage temporelle donnés. Ces informations sont inscrites par l'utilisateur lors de l'appel de la fonction. L'utilisateur a la liberté de choisir la combinaison de capteurs qu'il souhaite faire afficher.

```javascript
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
```
Dans cette première fonction on a crée deux bibliothèques. Une bibliothèque 'unites' pour pouvoir assimiler à une variable son unité de mesure puis l'afficher sur l'axe des ordonnées. Une bibliotèque 'variable_dico' pour traduire les noms des variables en français pour l'intitulé du graphique:
```javascript
unites={ 'temp':'°C', 'noise':'dBA' , 'lum':'lux', 'co2':'ppm' , 'humidity':'%' }
variable_dico={'temp':'température','noise':'bruit','lum':'luminosité','co2':'CO_2','humidity':'humidité relative'}
```
Par soucis de simplification du code on décide pour les prochaines fonctions de ne plus utiliser ces deux bibliothèques. Les données seront intuitivement interprétées. 

--------
### Détections d'anomalies
Après avoir observé à l'œil nu certaines anomalies sur les courbes tracées précédemment, nous avons cherché un moyen de détecter l’ensemble des anomalies présentes dans nos données. Pour ce faire, nous nous sommes penchés sur la définition d’une anomalie. Nous avons d'abord considéré qu' une valeure était considérée comme une anomalie si elle différait de plus de fois l’écart type par rapport à la moyenne. 

On a dévéloppé pour l'instant deux fonctions permettant de détecter:
* si un capteur s'arrête de fonctionner pendant un temps anormal (plus d'un jour). ___```anomalie_arret()```___
* des anomalies de valeurs en calculant leur différence avec la moyenne journalière et comparant cette différence à l'écart-type. ___```anomalie_valeur()```___

```java
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
```
