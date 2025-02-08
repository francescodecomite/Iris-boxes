TAILLE=500
from math import *

# travail en cours : remplacer les fond et le dessus par
# des plis d'origami (cf Tomoko Fuse Origmai Boxes page 93 et autour)



decalx=150 # decalage du dessin pour tenir dans la feuille
decaly=150
#Dimensions de la boite. Voir schéma (todo)
A=100
B=400
# coefficients des ellipses
D=(B*5)//9//2
E=(A*30)//45//2
# Nombre de côtés
N=6

def debut(c=TAILLE,n=N):
    entete="<svg viewBox=\"0 0 "+str(2*c)+" "+str(2*c)+"\" xmlns=\"http://www.w3.org/2000/svg\">\n"
    pied="</svg>\n"
    image=open("sp120_"+str(n)+"faces_origami.svg","w")
    image.write(entete)
    return image

def fin(image):
    pied="</svg>\n"
    image.write(pied)
    image.close()


def ligne(debut,fin,transform="",couleur="lime"):
     s="<line x1=\""+str(debut[0]+decalx)+"\" y1=\""+str(debut[1]+decaly)+"\" x2=\""+str(fin[0]+decalx)+"\" y2=\""+str(fin[1]+decaly)+"\" stroke=\""+couleur+"\"  transform="+transform+" />\n"
     return s

def ellipse(xradius,yradius,xcenter,ycenter,couleur="blue"):
    s="<ellipse rx=\""+str(xradius)+"\" ry=\""+str(yradius)+"\" cx=\""+str(xcenter+decalx)+"\" cy=\""+ str(ycenter+decaly)+"\" fill=\"none\"   stroke=\""+couleur+"\"/>\n"
    return s

    
def ligne_pointillee(depart,arrivee,couleur="blue"):
    x0=depart[0]
    y0=depart[1]
    x1=arrivee[0]
    y1=arrivee[1]
    # todo, il faudrait s'arranger pour que x0<x1, sinon ça déconne
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
        #s+="<line x1=\""+str(int(x0+mycos*(2*i*la))+decalx)+"\" y1=\""+str(int(y0+mysin*(2*i*la))+decaly)+"\" x2=\""+str(int(x0+mycos*(2*i+1)*la)+decalx)+"\" y2=\"" +str(int(y0+mysin*((2*i)+1)*la)+decaly)+"\" fill=\"none\" stroke=\""+couleur+"\"/>\n"
  
        s+="<line x1=\""+str(int(x0+mycos*(i*(la+lb))+decalx))+"\" y1=\""+str(int(y0+mysin*(i*(la+lb))+decaly))+"\" x2=\""+str(int(x0+mycos*(i*(la+lb)+la)+decalx))+"\" y2=\"" +str(int(y0+mysin*(i*(la+lb)+la)+decaly))+"\" fill=\"none\" stroke=\""+couleur+"\"/>\n"
    return s



def arc(debut,fin,rayon,couleur="\"lime\""):
    chaine="<path d=\"\n"
    chaine=chaine+"M"+str(debut[0]+decalx)+" "+str(debut[1]+decaly)+"\n"
    chaine=chaine+"A"+str(rayon)+" "+str(rayon)+" 0 0 1 "+str(fin[0]+decalx)+" "+str(fin[1]+decaly)+"\"  fill=\"none\"  stroke="+couleur+"\" />\n"
    return chaine

def contour(a=A,b=B,d=D,e=E,n=N):
    s=""
    for i in range(n):
        s+=ellipse(d,e,0.5*b,0.5*a+i*a)
    # lignes horizontales
    # seule la première est une ligne pleine
    s+=ligne((0,0),(b,0))
    for i in range(n):
        s+=ligne_pointillee((0,i*a+a),(b,i*a+a))
        s+=ligne_pointillee((0,i*a),(b,i*a+a))
    s+=ligne_pointillee((0,0),(0,n*a))
    s+=ligne_pointillee((b,0),(b,n*a))
     
    #Les languettes de collage
    #Celle du bas
    s+="<polyline points=\" "+str(0+decalx)+","+str(n*a+decaly)+" "+str(0.05*b+decalx)+","+str((n+0.3)*a+decaly)+" "
    s+=str(0.95*b+decalx)+","+str((n+0.3)*a+decaly)+" "+str(b+decalx)+","+str(n*a+decaly)+"\" "
    s+=" fill=\"none\" stroke=\"lime\"/>\n"

    # les couvercles
    l=a/(2*sin(pi/n))
    longueur_languette=l*sin((n-2)*pi/(2*n))
    print(l,longueur_languette)
    decalage=sqrt(l*l-longueur_languette*longueur_languette)
    print(decalage)
    decalage_pointille=decalage #0.6*a
    """
    # A  droite
    s+=ligne((b,0),(b+longueur_languette,0))
    s+=ligne((b+longueur_languette,0),(b+longueur_languette,n*a))
    # languette
    s+=ligne((b,n*a),(b+0.3*a,n*a+0.3*a))
    s+=ligne((b+0.3*a,n*a+0.3*a),(b+0.8*a,n*a+0.3*a))
    s+=ligne((b+0.8*a,n*a+0.3*a),(b+longueur_languette,n*a))

    # Plis origami
    for i in range(n):
        s+=ligne_pointillee((b,(i+1)*a),(b+longueur_languette,(i+1)*a))
        s+=ligne_pointillee((b,i*a),(b+longueur_languette,i*a+decalage_pointille))
    """    
    # A gauche
    s+=ligne((0,0),(-longueur_languette,0))
    s+=ligne((-longueur_languette,0),(-longueur_languette,n*a))
    # languette
    s+=ligne((0,n*a),(-0.02*a,n*a+0.3*a))
    s+=ligne((-0.02*a,n*a+0.3*a),(-0.5*a,n*a+0.3*a))
    s+=ligne((-0.5*a,n*a+0.3*a),(-longueur_languette,n*a))

     # Plis origami
    for i in range(n):
        s+=ligne_pointillee((0,(i+1)*a),(-longueur_languette,(i+1)*a))
        s+=ligne_pointillee((0,i*a),(-longueur_languette,i*a+decalage_pointille))

    
       

    return s    


if __name__=="__main__":
  
    cote=7
    image=debut(c=TAILLE,n=cote)
    image.write(contour(n=cote))
    #image.write(polygon1(n=cote))
    #image.write(polygon2(n=cote))
    fin(image)

    
    
