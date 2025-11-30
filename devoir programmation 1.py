import turtle
import random

def dessiner_arbre(longueur, angle_min, angle_max,
                   nombre_sous_arbres_min, nombre_sous_arbres_max,
                   facteur_min, facteur_max, longueur_min):
    
    if longueur <= longueur_min:
        turtle.forward(longueur)
        turtle.backward(longueur) 
        return
    position_depart = turtle.position()
    direction_depart = turtle.heading()
    turtle.forward(longueur)
    nsous_arbres = max(2, random.randint(nombre_sous_arbres_min, nombre_sous_arbres_max))

    if nsous_arbres > 1:
        branche_angle = (angle_max - angle_min) / (nsous_arbres - 1)
    else:
        branche_angle = 0 

    i = 0

    while i < nsous_arbres:
        angle = angle_min + i * branche_angle
        
        turtle.penup()
        turtle.goto(turtle.position())
        turtle.setheading(direction_depart) 
        turtle.pendown()

        turtle.left(angle)
        facteur = random.uniform(facteur_min, facteur_max)
        dessiner_arbre(longueur * facteur,
                       angle_min, angle_max,
                       nombre_sous_arbres_min, nombre_sous_arbres_max,
                       facteur_min, facteur_max,
                       longueur_min)
        i += 1
    turtle.penup()
    turtle.goto(position_depart)
    turtle.setheading(direction_depart)
    turtle.pendown()
turtle.speed("fastest")  
turtle.left(90)
turtle.penup()
turtle.goto(0, -200)  
turtle.pendown()

turtle.done()