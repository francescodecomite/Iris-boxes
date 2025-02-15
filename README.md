# Iris-boxes
 Program and cut boxes with iris locking lids // Programmer et couper des boîtes à ouverture en iris

_ Vos questions et vos louanges : fdecomite at gmail.com

*** English version below (maybe)***

# Présentation

Le but de ce 'projet' est de généraliser le design de la page 120 du livre **Special Packaging**, acheté il y a vingt ans dans un musée de Bruxelles (voir photos). 

Pour le moment, je ne parle pas de la torsion qu'on peut réaliser sur le modèle une fois collé fermé. A suivre...




![Alt](./livre.JPG)
![Alt](./ellipsebox.jpg)


Les généralisations sont de plusieurs ordres : 
1. Obtenir un fichier SVG directement utilisable dans Inkscape et pour la découpe laser. 
2. Pouvoir construire des boîtes avec un nombre quelconque de côtés. 
3. Contrôler par programme la taille de l'objet (hauteur, largeur, forme des ellipses). 
4. Fabriquer des couvercles et des fonds de boîte *homogènes*, c'est-à-dire avoir des languettes toutes identiques.
5. Effet de bord, j'ai aussi été obligé de définir une fonction permettant de définir des lignes de découpe de pointillés, car la découpeuse laser ne reconnaît pas les 
pointillés d'Inkscape. J'ai entendu dire que c'était pareil pour Illustrator. 

Voilà le genre de trucs qu'on obtient : 
![Alt](./iris-exemple.jpeg)

C'est seulement des prototypes, il manque un couvercle et le papier n'est pas terrible. 

# Les deux programmes
1. sp120_nfaces_origami.py fabrique des bboîtes comme dans le livre, avec des trous ellispoïdaux. 
2. boites_en_iris fabrique des boîtes sans ellipses, avec un couvercle un peu plus large, mais sans trous. 
3. En bricolant un peu, on doit pouvoir faire des boîtes avec un couvercle et des trous en ellipse... à voir ...

# Boîtes en iris sans ellipse mais avec couvercle
Trois paramètres : 
1. **A** : longueur d'un côte de la boîte.
2. **B** : hauteur de la boîte. 
3. **N** : Nombre de côtés (mais ce paramètre est surchargé au début du programme principal).  
Le couvercle est un peu plus large que la boîte (pour le changer : voir le coéfficient devant A au début de la fonction qui construit le couvercle).
Le couvercle est moins haut que la boîte, la modification se fait en changeant le coefficient de B au début de la fonction qui construit le couvercle).

# Boîtes avec ellipses

Le programme est écrit en Python, je pense qu'il n'est pas très compliqué à comprendre. Les différentes variables qui vont influer sur la taille de la boîte sont les suivantes : 

1. **A** : longueur d'un côte de la boîte.
2. **B** : hauteur de la boîte. 
3. **E** : Petit axe de l'elipse (fonction de A). 
4. **D** : Grand axe de l'ellipse (fonction de B).
5. **N** : Nombre de côtés (mais ce paramètre est surchargé au début du programme principal).  
6. **sens_direct** : Si True, les couvercles tournent dans le même sens, si False, dans des sens opposés. 

Pour correspondre aux codes couleur pour la découpe du [Fabricarium de Polytech Lille](https://fabricarium-fabmanager.polytech-lille.fr/#!/), le bleu est utilisé pour les découpes à faire en premier, et le vert pour les découpes finales. En gros, les pointillés sont en bleu, et aussi les ellipses.

Le programme produit un ficher SVG directement exploitable. 


 # La partie un peu compliquée mais rendu simple par des explications super pédagogiques. 

Pour construire un couvercle en iris qui se ferme convenablement, il y a deux valeurs à calculer : 
1. La longueur de la languette. 
2. L'angle du pli de la languette. 



D'abord, la longueur _l_ du pointillé oblique, c'est plus facile : c'est la distance entre un sommet du polygone régulier obtenu quand on a fermé la boîte et le centre de ce polygone. 
Si le côté vaut _a_, alors _l_ vaut _a_/(2*sin(pi/n)

La hauteur de la languette vaut _l_/cos((n-2)*pi/(2*n), c'est le demi-angle entre deux côtés du polygone. 
Si ça vous semble magique, imprimer un modèle, peu importe le nombre de côtés, et voyez comment ça se plie. 

La réalité montre que mes calculs sont bons, ou au moins qu'ils peuvent faire illusion. 

## Questions et développements 

S'occuper de la découpe des ellipses et de la rotation de la boîte, comme dans le livre...

Voir si en rallongeant un peu les languettes, on n'obtient pas quelque chose de plus stable. 

Corriger les fautes de frappe. 
