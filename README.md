# Projet-semestre-1
Présentation du projet python __Blaszczuk Damian__ et __Gasecki Nicolas__ __Groupe 23__  Le fichier python à télécharger se trouve sous le nom  `projetpython.py'
### Sujet n°1
--------------------------------------------------------------------------------
## Introduction brève du code source
* ##### Recherche de la méthode de manipulation d’un tableau de données sur python:
Nous disposions d’un ensemble de données sous la forme d’un tableau csv traduisant l’évolution de différentes caractéristiques d’une pièce (température, humidité, bruit et différents capteurs) en fonction du temps. Nous avons d'abord cherché à lire ce format csv sur python, pour ce faire la bibliothèque ```pandas``` est la plus adaptée. Une fois ces données importées sur python nous avons commencé à traiter ces données afin de les étudier.
```javascript
import pandas as pd
```
* ##### Indexing et présentation des courbes:
Nous avons cherché à afficher les courbes des différentes caractéristiques en fonction du temps. Pour ce faire, nous avons défini le temps (la Serie ```sent_at```) comme indice principal de notre tableau en prenant en compte qu’il s’agissait de dates. A l’aide de la bibliothèque matplotlib nous avons pu ensuite afficher les courbes souhaitées. 
```javascript
df=pd.read_csv('EIVP_KM.csv', sep=';', index_col='sent_at', parse_dates=True)
``` 
* ##### 2 dictionnaires:
On crée une bibliothèque ```unites``` pour pouvoir assimiler à une variable son unité de mesure puis l'afficher sur l'axe des ordonnées. Une bibliotèque `variable_dico` pour traduire les noms des variables en français pour l'intitulé du graphique:
```javascript 
unites={ 'temp':'°C', 'noise':'dBA' , 'lum':'lux', 'co2':'ppm' , 'humidity':'%' }
variable_dico={'temp':'température','noise':'bruit','lum':'luminosité','co2':'CO_2','humidity':'humidité relative'}
```
* ##### Choix arbitraire
En évaluant les variables (partie II) on a décide dans la plupart des fonctions de spécifier le capteur qu'on désire étudier. Le capteur 6 présente que des donnés de 2019 alors que les autres celles de 2020.

--------------------------------------------------------------------------------
## I  Valeurs statistiques 
On cherche a calculer min, max, écart-type, moyenne, variance, médiane. Pour cette partie nous nous sommes aidés au début des fonctions pandas déjà existantes. En utilisant les fonctions df.mean, df.max(), df.min(), df.median()…df.describe() on a les données souhaitées. Il nous restait seulement a les appliquer dans les intervalles souhaités et a l’afficher sur les courbes, pour ce faire on utilise matplotlib. 
Cependant pour cette question nous avons eu deux compréhensions différentes du sujet:
  * 1. l'un pensant qu'il fallait tracer la courbe en y ajoutant la valeur statistique calculée sur cet intervale(effectué dans le cas du calcul du minimum)
  * 2. l'autre qu'il fallait calculer la valeur statistique pour chaque journée et de tracer la courbe d'evolution sur l'intervalle donné. Nous avons donc décidé de coder les deux programmes car ceux-ci pourraient être utiles pour étudier les données de notre tableau.
 
 * ### a) Minimum et maximum
  * 1. #### Minimum ponctuel sur une plage de donnée et pour une combinaison de capteurs choisies par l'utilisateur !
```javascript
def minimum():
    M=[]#on crée la liste des minimums pour chaque capteur sélectioné
    i_mini=0 #on initialise l'indice de la valeur minimale
    I=[]#on crée la liste des indices des minimums pour chaque capteur sélectioné

    variable=input('entrer une variable (temp,humidity,co2,noise,lum):')
    d=input('entrer date début (exemple 2020-09):')
    f=input('entrer date fin:')
    L=[int(el) for el in input('choix des capteurs de 1 à 6 (ex: 1 3 5):').split()]  #on choisit la combinaison de capteurs souhaités.
        
        
    for capteur in range(len(L)):  #on parcourt la liste des capteurs sélectionnés
        
        df[df['id']==L[capteur]][variable][d:f].plot(label=f' capteur {L[capteur]}') #on affiche la courbe de la variable sélectionnée
        
        Min=df[df['id']==L[capteur]][variable][0] #Initialisation
        
        for k in range(len(df[df['id']==L[capteur]][d:f].index)-1):#on parcourt toutes les valeurs de la Serie dans la plage temporelle sélectionnée.
            
            if df[df['id']==L[capteur]][variable][d:f][k+1] < Min: #comparaison des valeurs au minimum en cours.
                i_mini = k+1 #on stocke l'indice de la valeur minimale en cours.
                Min = df[df['id']==L[capteur]][variable][d:f][k+1] #on actualise la valeur du minimum
        
        M.append(Min) #on stocke la valeur minimale du capteur qu'on est en train de parcourir.
        I.append(i_mini)  #on stocke également son indice
     
    
    Minimum = min(M)   #Ici on s'autorise à utiliser la bibliothèque python pour calculer le minimum de la liste et éviter à faire une boucle for en plus.
    Indice_du_minimum = I[M.index(Minimum)] #Identification de l'indice correspondant
    
    #on relève les caractétistiques (date précisément indexée sous le format Timestamp)de la valeur minimale pour pouvoir afficher le point avec .index:
    A = df[df['id']==L[M.index(Minimum)]][variable][d:f].index[Indice_du_minimum]           
    
    df[df['id']==L[M.index(Minimum)]][variable][A._repr_base:A._repr_base].plot(label='minimum',marker='o',color='r') #affiche la valeur minimum
    
    plt.ylabel(variable_dico[f'{variable}'] + ' en ' + unites[f'{variable}'])
    plt.title(f'Le minimum est de {Minimum} ' + unites[f'{variable}'])
    plt.legend()   
    plt.show()
```
On a fait la même fonction pour le maximum aussi `maximum()`. Elle se trouve dans le fichier `projetpython.py`

Pour ne pas s'embêter on fait apparaître le min et max tout capteurs confondus(salles ouvertes) pour visualiser l'intervalle qu'il y a entre les valeurs minimales et maximales par jour. On utilise le module `.resample()` avec D--> Day :

  *  2. #### Minimum et Maximum sous la forme plus simple

```javascript
def min_max(): #on calcule les min et max journaliers
    
    variable=input('entrer une variable (temp,humidity,co2,noise,lum):')
    d=input('date debut:')
    f=input('date fin:')
    
    df.loc[d:f,variable].resample('D').min().plot(label='min')
    df.loc[d:f,variable].resample('D').max().plot(label='max')
    
    plt.ylabel(variable_dico[f'{variable}'] + ' en ' + unites[f'{variable}'])
    plt.title('Minimum et Maximum journaliers')
    plt.legend() 
    plt.show()
```
    
  * 3. min max et moyenne

```javascript
def min_max_moy(): #on projette les min et max plus la moyenne par jour, on utilise ici .aggreagate pour regrouper facilement les valeurs statistiques
    
    variable=input('entrer une variable (temp,humidity,co2,noise,lum):')
    d=input('date debut:')
    f=input('date fin:')
    
    d=df[variable][d:f].resample('D').agg(['mean','min','max'])
    
    
    d['mean'].plot(label='Moyenne',ls=':')#on affiche la moyenne
    d['max'].plot(label='',ls='-',color='r')
    d['min'].plot(label='',ls='-',color='r')
    plt.fill_between(d.index, d['min'],d['max'],alpha=0.2,label='Ecart Min-Max par jour') #on affiche min et max
    
    
    plt.ylabel(variable_dico[f'{variable}'] + ' en ' + unites[f'{variable}'])
    plt.title('Minimum Maximum et Moyennes journaliers')
    plt.legend() 
    plt.show()
```
 
 * ### b) Moyenne
  * La fonction affiche la moyenne journalière d'une variable. Comme précisé en amont. Il serait plus judicieux de demander les capteurs choisis mais on se contente ici de voir la vision globale avec les valeurs de 2020 et de 2019 mesurées par le capteur id=6.
```javascript
def moyenne():   #on calcule la moyenne journalière
    
    variable=input('entrer une variable (temp,humidity,co2,noise,lum):')
    d=input('date debut:')
    f=input('date fin:')
    
    df[variable][d:f].resample('D').mean().plot(label='',ls=':')
    
    plt.ylabel(variable_dico[f'{variable}'] + ' en ' + unites[f'{variable}'])
    plt.title('Moyenne journalière')
    plt.show()
```


 * ### c) Ecart-type 
  * On décide d'afficher l'écart-type et la moyenne sur le même graohique. Pour cela on a créé deux repères différents `ax1` pour la moyenne `mean()` et `ax2` pour l'ecart-type`std()` grâce aux modules `.subplots`et `.twinx`. Un FutureWarning peut être retourné sur la console, cela dépend de la version de l'IDE.
```javascript 
def ecart_type():
    capteur=int(input("entrer un id du capteur:"))
    variable=input('entrer une variable (temp,humidity,co2,noise,lum):')
    d=input('entrer date début (exemple 2020-09):')
    f=input('entrer date fin:')

    fig, ax1 = plt.subplots(figsize=(10,4))
    ax2 = ax1.twinx()
    
    ax1.plot(df[df["id"]==capteur][variable][d:f].resample('D').mean().index , df[df['id']==capteur][variable][d:f].resample('D').mean(),color='r')
    ax1.set_ylabel(unites[f'{variable}'])
    
    ax2.bar(df[df["id"]==capteur][variable][d:f].resample('D').std().index , df[df['id']==capteur][variable][d:f].resample('D').std(),color='b',alpha=0.2,label='ecart-type')

    plt.title( 'Evolution de la moyenne de la variable ' + variable_dico[f'{variable}'] + " et son ecart-type" )
    plt.legend()
    plt.show()
```   
* ### d) Médiane
On retourne la valeur médiane
```javascript
def mediane():  

    variable=input('entrer une variable (temp,humidity,co2,noise,lum):')
    d=input('date debut:')
    f=input('date fin:')
    
    return (df[variable][d:f].median())
```
* ### e) Variance
Sur le même principe que l'écart-type
```javascript
def variance():
    capteur=int(input("entrer un id du capteur:"))
    variable=input('entrer une variable (temp,humidity,co2,noise,lum):')
    d=input('entrer date début (exemple 2020-09):')
    f=input('entrer date fin:')

    fig, ax1 = plt.subplots(figsize=(10,4))
    ax2 = ax1.twinx()
    
    ax1.plot(df[df["id"]==capteur][variable][d:f].resample('D').mean().index , df[df['id']==capteur][variable][d:f].resample('D').mean(),color='r')
    ax1.set_ylabel(unites[f'{variable}'])
    
    ax2.bar(df[df["id"]==capteur][variable][d:f].resample('D').var().index , df[df['id']==capteur][variable][d:f].resample('D').var(),color='b',alpha=0.2,label='variance')

    plt.title( 'Evolution de la moyenne de la variable ' + variable_dico[f'{variable}'] + " et sa variance" )
    plt.legend()
    plt.show()
```
* ### f) Indice de corrélation
Pour l'indice de corrélarion, tout comme pour les valeurs statistiques, nous nous sommes aidé des fonctions python existantes
```javascript
def correlation():
    
    variable1=input('entrer une variable (temp,humidity,co2,noise,lum):')
    variable2=input('entrer une deuxieme variable (temp,humidity,co2,noise,lum):')
    
    f = plt.figure()
    ax = f.add_subplot(111)

    df[variable1].plot(label='evolution de la ' +variable_dico[f'{variable1}'] )
    df[variable2].plot(label='evolution de la ' +variable_dico[f'{variable2}'] )#Affichage des deux courbes représentant les deux variables en fonction du temps.
    
    indice = df[variable1].corr(df[ variable2]) #indice de corrélation entre les deux variables

    
    plt.text(0.5,0.5,f"l'indice de correlation est {indice}",horizontalalignment='center',
     verticalalignment='center', transform = ax.transAxes, fontsize=7, color='r')#Indication dans de la valeur de l’indice de corrélation

    plt.legend()
    plt.show()
 ```
 * ### g) Indice Humidex
 L’humidex est une formule combinant température et humidité, ainsi pour la trouver nous avons effectué des opérations entre les diverses colonnes de notre tableau. Pour plus de lisibilité dans notre programme nous avons créé deux données intermédiaires ; la température de rosée et alpha dépendant également de la température et de l’humidité. Puis grâce à ces valeurs nous avons pu calculer l’humidex pour l’ensemble des dates.On s’est donc retrouvé avec une ligne de code nous permettant d’afficher le tableau de données avec une nouvelle colonne contenant l’humidex.
 Enfin nous avons codé une fonction nous demandant l’intervalle de temps que l’on voulait étudié afin de réduire notre tableau à la colonne de l’humidex dans cette intervalle de temps puis enfin de tracer la courbe de l’humidex en fonction du temps. Les difficultés rencontrées dans cette partie ont été différentes. Tout d'abord il a fallu comprendre les formules de calculs ainsi que les grandeurs y intervenant. En effet lors de la première version du programme, nous avons obtenus des valeurs d'humidex incohérentes. On s'est alors rendez compte que nous aavions un souci d'unité avec certaines données présentes sous forme de pourcentage. Une fois cela corrigé nous avons bien obtenu les valeurs souhaitées
 ```javascript
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
```
---------------------------------------------------------------------------------
## II  Affichage de l'évolution des valeurs
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
 
--------
## III  La détection des anomalies
Après avoir observé à l'œil nu certaines anomalies sur les courbes tracées précédemment, nous avons cherché un moyen de détecter l’ensemble des anomalies présentes dans nos données. Pour ce faire, nous nous sommes penchés sur la définition d’une anomalie. Nous avons d'abord considéré qu' une valeure était considérée comme une anomalie si elle différait de plus de fois l’écart type par rapport à la moyenne. 

On a dévéloppé pour l'instant deux fonctions permettant de détecter:
* si un capteur s'arrête de fonctionner pendant un temps anormal (plus d'un jour). ___```anomalie_arret()```___
* des anomalies de valeurs en calculant leur différence avec la moyenne journalière et comparant cette différence à l'écart-type. ___```anomalie_valeur()```___

###### Anomalie_Arret()
  * La fonction anomalie_arret() va montrer les arrêts possibles d'un capteur et montrer l'impact que cet arrêt a eu sur l'évolution des variables. Les graphiques se montrent un à un, cela prend un peu de temps.
```javascript
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
###### Anomalie_Valeurs()
  * Dans cette fonction on utilise un critère d'anomalie qui est utilisé par MeteoFrance. On demande les capteurs qu'on veut étudier, mais mieux vaut en sélectionner qu'un pour plus de rapidité et une lisibilité meilleure du graphique
```javascript
def anomalie_valeur():
    
    variable=input('entrer une variable (temp,humidity,co2,noise,lum):')
    d=input('entrer date début (exemple 2020-09):')
    f=input('entrer date fin:')  
    L=[int(el) for el in input('choix des capteurs de 1 à 6 (ex: 1 3 5):').split()]
        
        
    for capteur in range(len(L)):  #on parcourt la liste des capteurs
        
        anomalie_1, anomalie_2, anomalie_3, anomalie_4 = 0, 0, 0, 0   # on initialise 4 degrés d'anomalies pour chaque capteur
    
        for k in range(len(df[df['id']==L[capteur]][d:f].index)-1):  #on parcourt les valeurs du tableau du capteur correspondant.
            
            D=np.abs(df[df['id']==L[capteur]][variable][d:f][k] - df[df['id']==L[capteur]][variable][d:f].resample('D').mean()[df[df['id']==L[capteur]][variable][d:f].index[k]._date_repr])
        
            # D est la différence entre la valeur d'une variable (d'indice k) pour un capteur donné( L[capteur] ) et la valeur moyenne de cette variable sur la journée.
            
            s=df[df['id']==L[capteur]][variable][d:f].std()
            
            # s est l'écart-type
            # Une valeur présentant un écart à la moyenne inférieur à l'écart type est banale, compris entre une et deux fois l'écart type est modérément courante, compris entre deux et trois fois l'écart type commence a être remarquable,compris entre trois et quatre fois l'écart type est exceptionnelle, supérieur à quatre fois l'écart type est historique et très rare.
            
            if D>=s and D<2*s:
                            df[df['id']==L[capteur]][variable][d:f][k:k+1].plot(label='',lw=2,color='g',marker='o')   #on affiche les points pour les anomalies détéctées grâce à l'indice k
                            anomalie_1+=1
            
            if D>=2*s and D<3*s:
                            df[df['id']==L[capteur]][variable][d:f][k:k+1].plot(label='',lw=2,color='r',marker='o')
                            anomalie_2+=1
            
            if D>=3*s and D<4*s:
                            df[df['id']==L[capteur]][variable][d:f][k:k+1].plot(label='',lw=2,color='m',marker='o')
                            anomalie_3+=1
            
            if D>=4*s:
                            df[df['id']==L[capteur]][variable][d:f][k:k+1].plot(label='',lw=2,color='k',marker='o')
                            anomalie_4+=1
        if anomalie_4>=1:
            print(f'il existe au moins une anomalie extrême pour le capteur {L[capteur]}') 
        if anomalie_3>1:
            print(f'il existe des anomalies exceptionnelles pour le capteur {L[capteur]}')
        if anomalie_3>1:
            print(f'il existe des anomalies remarquables pour le capteur {L[capteur]}')
        if anomalie_2>1:
            print(f'il existe des anomalies courantes pour le capteur {L[capteur]}')
        
        df[df['id']==L[capteur]][variable][d:f].plot(label=f'capteur {L[capteur]}')
    plt.title('vert : anomalie courante \\ rouge : anomalie courante \\  magenta : anomalie exceptionnelle \\  noire : anomalie rare ')
    plt.figure(figsize=(20,10))
    plt.legend()
    plt.show()
```

## 4 Occupation des salles

On crée la fonction `occupation()` en considérant que les salles sont occupées lorsque la teneur en CO2 dépasse 470 ppm. Cette information vient de la lecture du [Centre de collaboration nationale en santé environnementale au canada (CCNSE)](https://ccnse.ca/documents/practice-scenario/le-dioxyde-de-carbone-dans-lair-int%C3%A9rieur). La teneur en CO2 ne dépassant pas 400ppm à l'air libre mais aussi pour ne pas compter les week-end où la teneur est négligeable pour notre étude, on s'intéresse ici à une occupation moyenne et haute. La fonction `occupation()` va afficher:
 * La courbe avec les points d'occupation en rouge
 * La liste des horaires d'occupation 
 * Et le tableau Dataframe

```javascript
def occupation():
    H,J=[],[] #Deux listes pour les horaires et les journées correspondantes
    capteur=int(input('entrer un id du capteur:'))
    
    for k in range(len(df[df['id']==capteur].index)-1):
    
        if df[df['id']==capteur]['co2'][k]>490 :  #on considère que la salle est occupée à partir de 490ppm, pour ne pas prendre en compte les week-end.
            
            indice=k
            A=df[df['id']==capteur].index[indice]
            
            Jour=A._date_repr    #Donnée du jour
            Horaire=A._time_repr #Donnée de l'horaire
            H.append(Horaire)
            J.append(Jour)
                
            
            
            df[df['id']==capteur]['co2'][A._repr_base:A._repr_base].plot(marker='o',color='r',label='occupation moyenne de la salle')  #on parcourt toutes les données du capteur
    
    #On peut aussi créer un dataframe avec les horaires d'occupation
    data = {'Periode_occupation': H , 'Jour':J}
    Tab = pd.DataFrame(data=data)
    Tab['Jour']=pd.to_datetime(SE.Jour) #on met le format jour en datetime
    
    df[df['id']==capteur]['co2'].plot(label='co2')  #on affiche la courbe co2   
   
    plt.show()
    print("Les horaires d'occupation: ", H,Tab)
