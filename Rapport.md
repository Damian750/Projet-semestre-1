Projet de programmation informatique
 
Participants : Damian Blaszczuk Nicolas Gasecki
Sujet n°1
 Recherche de méthode de manipulation d’un tableau de données sur python:
Nous disposions d’un ensemble de données sous la forme d’un tableau csv traduisant l’évolution de différentes caractéristiques d’une pièce (température, humidité, bruit) en fonction du temps. Nous avons d'abord cherché à lire ce format csv sur python, pour ce faire la bibliothèque panda nous a paru la plus adaptée. Une fois ces données importées sur python nous avons commencé à traiter ces données afin de les étudier.

Courbe:
Nous avons cherché à afficher les courbes des différentes caractéristiques en fonction du temps. Pour ce faire, nous avons défini le temps (« sent_at ») comme indice principal de notre tableau en prenant en compte qu’il s’agissait de dates. A l’aide de la bibliothèque matplotlib nous avons pu ensuite afficher les courbes souhaitées.
 Température en fonction du temps :
          	On présente l’évolution de la température relevée par les différents capteurs sur un même graphique pour distinguer au premier abord des anomalies entre certains capteurs qui sont visibles à l’œil nu. On remarque alors :
L’ id 5 est globalement toujours plus froid par rapport aux autres du 2020-09-11 au 2020-09-14 (écart de 2.5 °C entre id5 et id3 le 12 septembre le matin) calculer de combien de degré en moyenne il est plus chaud sur cette période puis du 2020-09-15 au 2020-09-25 est globalement toujours plus chaud que les autres capteurs des autres salles.pareil
Du 2020-09-21 à 16h jusqu’au 2020-09-23 à 15h l’id 5 ne relève plus aucune donnée.
L’id 1 ne présente pas d’anomalie visible jusqu’au 2020-09-19. Cependant après cette date la température relevée est nettement inférieure à celles détectées dans les autres salles.

Recherche d’anomalies:
Après avoir observé à l'œil nu certaines anomalies sur les courbes tracées précédemment, nous avons cherché un moyen de détecter l’ensemble des anomalies présentes dans nos données. Pour ce faire, nous nous sommes penchés sur la définition d’une anomalie. Nous avons d'abord considéré qu' une valeure était considérée comme une anomalie si elle différait de plus de fois l’écart type par rapport à la moyenne. 

Humidex :
L’humidex est une formule combinant température et humidité, ainsi pour la trouver nous avons effectué des opérations entre les diverses colonnes de notre tableau. Pour plus de lisibilité dans notre programme nous avons créé deux données intermédiaires ; la température de rosée et alpha dépendant également de la température et de l’humidité. Puis grâce à ces valeurs nous avons pu calculer l’humidex pour l’ensemble des dates.On s’est donc retrouvé avec une ligne de code nous permettant d’afficher le tableau de données avec une nouvelle colonne contenant l’humidex or  Enfin nous avons codé une fonction nous demandant l’intervalle de temps que l’on voulait étudié afin de réduire notre tableau à la colonne de l’humidex dans cette intervalle de temps puis enfin de tracer la courbe de l’humidex en fonction du temps

Valeur statistiques :
On cherche a calculer min, max, écart-type, moyenne*, variance, médiane. Pour cette partie nous nous sommes aidés des fonctions pandas déjà existantes. En utilisant les fonctions df.mean, df.max, df.min, df.median… on a les données souhaitées. Il nous restait seulement a les appliquer dans les intervalles souhaités et a l’afficher sur les courbes, pour ce faire on utilise matplotlib avec la fonction pyplot.text

Indice de corrélation:


