TAILLE=500
from math import *

# Boîtes avec couvercle, fond et couvercles en iris

decalx=150 # decalage du dessin pour tenir dans la feuille
decaly=150
#Dimensions de la boite.
# Longueur d'un côté
A=100
# Hauteur de la boîte
B=150

# Nombre de côtés (changé dans le programme principal
N=6


# Entête du fichier SVG. La taille fixée produit un document carré. Pour obtenir le cadrage dans une feuille A4, le plus simple est de le faire
# à l'intérieur d'Inkscape (FIchiers>Propriétés du document)

def debut(c=TAILLE,n=N):
    entete="<svg viewBox=\"0 0 "+str(2*c)+" "+str(2*c)+"\" xmlns=\"http://www.w3.org/2000/svg\">\n"
    pied="</svg>\n"
    # Le nom du fichier SVG, n est le nombre de côtés de la boite
    image=open("boite_"+str(n)+"iris.svg","w")
    image.write(entete)
    return image

# Fin du fichier SVG
def fin(image):
    pied="</svg>\n"
    image.write(pied)
    image.close()

# Une ligne droite verte
def ligne(debut,fin,transform="",couleur="lime"):
     s="<line x1=\""+str(debut[0]+decalx)+"\" y1=\""+str(debut[1]+decaly)+"\" x2=\""+str(fin[0]+decalx)+"\" y2=\""+str(fin[1]+decaly)+"\" stroke=\""+couleur+"\"  transform="+transform+" />\n"
     return s


    
# Une ligne pointillée (pour que la découpeuse laser fasse des vrais pointillés)
def ligne_pointillee(depart,arrivee,couleur="blue"):
    x0=depart[0]
    y0=depart[1]
    x1=arrivee[0]
    y1=arrivee[1]
    if x0>x1:
        tmp=x0
        x0=x1
        x1=tmp
        tmp=y0
        y0=y1
        y1=tmp
    distance=sqrt((x0-x1)*(x0-x1)+(y0-y1)*(y0-y1))
    if y1==y0:
        pente=0
    else:
        pente=atan2((y1-y0),(x1-x0))
    mycos=cos(pente)
    mysin=sin(pente)
    la=3
    lb=6
    nb=int(distance/(la+lb))
    s=""
    for i in range(nb):
        s+="<line x1=\""+str(int(x0+mycos*(i*(la+lb))+decalx))+"\" y1=\""+str(int(y0+mysin*(i*(la+lb))+decaly))+"\" x2=\""+str(int(x0+mycos*(i*(la+lb)+la)+decalx))+"\" y2=\"" +str(int(y0+mysin*(i*(la+lb)+la)+decaly))+"\" fill=\"none\" stroke=\""+couleur+"\"/>\n"
    return s



def boite(a=A,b=B,n=N):
    s="<g>/n"
    # lignes horizontales
    # seule la première est une ligne pleine
    s+=ligne((0,0),(b,0))
    for i in range(n):
        s+=ligne_pointillee((0,i*a+a),(b,i*a+a))
        #s+=ligne_pointillee((0,i*a),(b,i*a+a))
    s+=ligne((0,0),(0,n*a))
    s+=ligne_pointillee((b,0),(b,n*a))
     
    #Les languettes de collage
    #Celle du bas
    s+="<polyline points=\" "+str(0+decalx)+","+str(n*a+decaly)+" "+str(0.05*b+decalx)+","+str((n+0.3)*a+decaly)+" "
    s+=str(0.95*b+decalx)+","+str((n+0.3)*a+decaly)+" "+str(b+decalx)+","+str(n*a+decaly)+"\" "
    s+=" fill=\"none\" stroke=\"lime\"/>\n"

    # les couvercles
    # Pour les maths voir le read me
    l=a/(2*sin(pi/n))
    longueur_languette=l*sin((n-2)*pi/(2*n))
    decalage=sqrt(l*l-longueur_languette*longueur_languette)
    decalage_pointille=decalage #0.6*a
    
    # A  droite
    s+=ligne((b,0),(b+longueur_languette,0))
    s+=ligne((b+longueur_languette,0),(b+longueur_languette,n*a))
    # languette
    s+=ligne((b,n*a),(b+0.2*longueur_languette,n*a+0.3*a))
    s+=ligne((b+0.2*longueur_languette,n*a+0.3*a),(b+0.8*longueur_languette,n*a+0.3*a))
    s+=ligne((b+0.8*longueur_languette,n*a+0.3*a),(b+longueur_languette,n*a))
    
    # Plis origami
   
    for i in range(n):
        s+=ligne_pointillee((b,(i+1)*a),(b+longueur_languette,(i+1)*a)) 
        s+=ligne_pointillee((b,i*a),(b+longueur_languette,i*a+decalage_pointille))
    s+="</g>\n"      
    return s    


def couvercle(a=int(1.1*A),b=int(0.6*B),n=N):
    global decalx
    l=a/(2*sin(pi/n))
    longueur_languette=l*sin((n-2)*pi/(2*n))
    decalx=decalx+10+B+longueur_languette
    s="<g>/n"

    # lignes horizontales
    # seule la première est une ligne pleine
    s+=ligne((0,0),(b,0))
    for i in range(n):
        s+=ligne_pointillee((0,i*a+a),(b,i*a+a))
        #s+=ligne_pointillee((0,i*a),(b,i*a+a))
    s+=ligne((0,0),(0,n*a))
    s+=ligne_pointillee((b,0),(b,n*a))
     
    #Les languettes de collage
    #Celle du bas
    s+="<polyline points=\" "+str(0+decalx)+","+str(n*a+decaly)+" "+str(0.05*b+decalx)+","+str((n+0.3)*a+decaly)+" "
    s+=str(0.95*b+decalx)+","+str((n+0.3)*a+decaly)+" "+str(b+decalx)+","+str(n*a+decaly)+"\" "
    s+=" fill=\"none\" stroke=\"lime\"/>\n"

    # les couvercles
    # Pour les maths voir le read me
    l=a/(2*sin(pi/n))
    longueur_languette=l*sin((n-2)*pi/(2*n))
    decalage=sqrt(l*l-longueur_languette*longueur_languette)
    decalage_pointille=decalage #0.6*a
    
    # A  droite
    s+=ligne((b,0),(b+longueur_languette,0))
    s+=ligne((b+longueur_languette,0),(b+longueur_languette,n*a))
    # languette
    s+=ligne((b,n*a),(b+0.2*longueur_languette,n*a+0.3*a))
    s+=ligne((b+0.2*longueur_languette,n*a+0.3*a),(b+0.8*longueur_languette,n*a+0.3*a))
    s+=ligne((b+0.8*longueur_languette,n*a+0.3*a),(b+longueur_languette,n*a))
    
    # Plis origami
   
    for i in range(n):
        s+=ligne_pointillee((b,(i+1)*a),(b+longueur_languette,(i+1)*a)) 
        s+=ligne_pointillee((b,i*a),(b+longueur_languette,i*a+decalage_pointille))
    s+="</g>\n"   
    return s    

if __name__=="__main__":
  
    cote=8
    image=debut(c=TAILLE,n=cote)
    image.write(boite(n=cote))
    image.write(couvercle(n=cote))
    fin(image)

    
    
