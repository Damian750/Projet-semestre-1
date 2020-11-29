# Projet-semestre-1
Présentation du projet python

La fonction ```evolution()``` permet de faire apparaitre la courbe d'une variable pour des capteurs et une plage temporelle donnés. Ces informations sont inscrites par l'utilisateur lors de l'appel de la fonction.

```html
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

On a dévéloppé pour l'instant deux fonctions permettant de détecter:
-si un capteur s'arrête de fonctionner pendant un temps anormal (plus d'un jour)
-des anomalies de valeurs en calculant leur différence avec la moyenne journalière et comparant cette différence à l'écart-type


