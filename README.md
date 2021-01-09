# Projet_Python_Data_Analysis

#### Projet mené par Cécile AMSALLEM et Bastien ATTRAIT dans le cadre du cours de Python for Data Analysis.

Nous avons reçu le dataset suivant à étudier :
https://archive.ics.uci.edu/ml/datasets/Online+Shoppers+Purchasing+Intention+Dataset


Tâches à effectuer :
- Data-visualisation
-	Modélisation
-	Transformation du modèle en API 


Ne pas se fier à la répartition des tâches de ce GitHub. La répartition réelle est telle qui suit :
-	Importation du dataset et première exploration : Bastien
-	Exploration plus approfondie : Cécile
-	Réponses aux questions pertinentes : Bastien & Cécile
-	Modélisation de plusieurs modèles et tests des hyperparamètres : Cécile
-	Transformation en API : Bastien
-	Travail sur le PowerPoint de rendu : Bastien et Cécile
-	Rédaction du ReadMe : Bastien et Cécile

## Data-visualisation 

Notre dataset contient des informations relatives à des visites d'un site internet, et des achats effectués ou non. 
Nous avons commencé par regarder nos colonnes, ce qu’elles représentent, ainsi que les corrélations entre ces colonnes.

Voici les colonnes et ce qu'elles contiennet :
- Administrative int64 : nombre de page administrative vues
- Administrative_Duration float64 : temps passé sur les pages administratives
- Informational int64 : nombre de page d’information vues
- Informational_Duration float64 : temps passé sur les pages d’information
- ProductRelated int64 : nombre de page produit vues
- ProductRelated_Duration float64 : temps passé sur les pages produit
- BounceRates float64 : pourcentage de visiteurs qui entrent sur le site à partir de cette page et la quittent sans déclencher d’autres demandes au serveur 
- ExitRates float64 : pourcentage de visiteurs qui quittent la session après avoir vu la page web
- PageValues float64 : valeur moyenne d’une page web qu’un utilisateur a visitée avant de conclure une transactionSpecialDay float64 : indique la proximité d’un jour particulier (fête des mères, St Valentin etc. ..)
- Month object : mois de l’année
- OperatingSystems int64 : indique le système d’exploitation
- Browser int64 : indique le navigateur utilisé
- Region int64 : indique la région 
- TrafficType int64 : indique le type de trafic associé
- VisitorType object : type de visiteur (nouveau, de retour ou autre)
- Weekend bool : booléen indiquant si la visite a eu lieu un week-end
- Revenue bool : indique si un achat a été effectué



Parmis nos phases exploratoires, nous avons soulevés quelques questions qui nous semblaient pertinentes.
- Y a t il une différence sur le temps passé sur le site en fonction du type de visiteur ?

  Nous remarquons que les visiteurs déjà venus passent en moyenne deux fois plus de temps sur le site que les personnes le visitant pour la première fois.
  
- Quels sont les types de page les plus vues en fonction du type de visiteur ? Et en terme de pourcentage, y-a-t-il une différence ?

Pourcentage de visite administrative parmi les Returning_Visitor : 6.189591889677422
Pourcentage de visite de produit parmi les Returning_Visitor : 92.3645946508241
Pourcentage de visite administrative parmi les New_Visitor : 12.186733572012516
Pourcentage de visite de produit parmi les New_Visitor : 86.22050573675753
Pourcentage de visite administrative parmi les Other : 10.416666666666668
Pourcentage de visite de produit parmi les Other : 88.33333333333333

- Le type de pages vues change-t-il en fonction du mois de l'année ?

Les types de pages vues ne changent pas en fonction du mois de l'année.

- Est-ce que les utilisateurs ont un comportement différent le WE ? 

De même les utilisateurs regardent les pages dans les mêmes proportions le week-end en comparaison du reste de la semaine.

- Est-ce que le ratio d'achat par visite change-t-il en fonction du mois ? Et du moment de la semaine ?

On peut noter que les mois d'Août à Novembre offrent une plus grande proportion d'achat par visite. Ceci pourrait s'expliquer de différentes manières en fonction du type de services / fournitures vendues par le site.
Le week-end ne change pas le ratio achat par visite sur le site internet.




## Modélisation



### KMeans

Nous avons d'abord voulu classer nos données en faisant un KMeans. En effet, dans le cas de comportement d'un client, il peut être intéressant de les regrouper afin dans faire des catégories. Ici nous avons testé avec 7 et 13 clusters. Nous avons choisi la somme de l'erreur carrée moyenne comme métrique.

Nous avons obtenus des résultats intéressants, mais il est important de noter que dans les deux cas nous ne pouvons pas juger pleinement de la justesse de notre clustering car la somme de l'erreur moyenne sera toujours très élevée. Si on augmente beaucoup le nombre de clusters (de l'ordre du nombre de données) nous obtiendrions une SSE faible, mais le clustering aurait alors perdu totalement de son intérêt.

Nous avons aussi fait varier différents paramètres de notre étapes de clustering, afin de trouver les paramètres les plus "optimisés" (en prenant en considération que nous ne voulions pas d'un nombre de cluster très grand par exemple).

Bien entendu les graphiques du PowerPoint de présentation ne sont pas ceux du notebook car le notebook a été relancé depuis la création du PowerPoint.


### RandomForest

Nous avons voulu appliquer également des algorithmes de prédiction en choisissant comme label la colonne Revenue (c'est à dire la colonne qui correspond à l'achat effecuté ou non). Nous utilisons comme métrique l'accuracy et la matrice de confusion.

De la même manière nous avons voulu faire varier les paramètres mais notre nombre de données est assez limité, nous avons donc peu d'accuracy différentes. Cependant l'accuracy est très élevée dès que le nombre d'arbre dans la forêt et le nombre



### Support Vector Classifier

Nous avons également souhaité appliquer un deuxième algorithme de prédiction, nous avons donc choisi celui-ci. 

Nous avons conservé les mêmes métriques que précédement. Avec ces métriques, sur cet alogirthme, nous avons à nouveau des valeurs d'accuracy excellente.
