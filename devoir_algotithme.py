import sys 

fichier_avec_emplacement_initial=sys.argv[1]
emplacement_initial= open( fichier_avec_emplacement_initial,"r")
etat_du_plateau="pas verifie"
def generation_du_plateau (emplacement_initial):
    plateau= []
    for ligne in emplacement_initial:
        rangee= ligne.split (",")
        if "x" in ligne : #sert juste à déjà savoir où se trouve le x et ne pas avoir besoin d'aller le chercher par la suite dans toute les sous liste de plateau
            x_de_X = rangee.index("x")
            plateau.append (rangee)
            
        else:
            plateau.append(rangee)
    longueur_du_plateau= len(plateau)

    return x_de_X_ ,plateau,longueur_du_plateau 


def déplacement (position_du_x,plateau ):

    etat_du_plateau="pas verifie"
    y_de_X=index.plateau (dictionnaire )# cherche le dictionnaire avec la position de x
    x_de_x = [y_de_X][valeur dans le dictionnaire]
    coordonnee_de_x = [y_de_X][x_de_x]

    def récursivite_du_deplacement() :
        if y_de_X and x_de_x == longueur du plateau: #  verification de la condition initial de la récursivité 
            for i in plateau:
                for j in plateau:
                    if plateau[i][j]<plateau[i][j+1] == True :
                        if plateau[i][j]<plateau[i+1][j] == True:
                            etat_du_plateau= "resolu"
                        else:


                    



        

