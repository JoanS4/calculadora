

def preguntar_operacio_usuari():
    resultat = input( ' Quina operació vols fer?? (multiplicar sumar o restar) \n' )
    while resultat not in  ['sumar','restar','multiplicar']: # resultat != suma and resultat !=resta 
        print ( 'el nombre nos es correcto')
        resultat = input( ' Quina operació vols fer?? (multiplicar sumar o restar) \n' )
    return resultat


if __name__ == "__main__": #Importava com a tercera a file no es corre el codi
    #si l'executo directament com a file principal si
    resultat = preguntar_operacio_usuari()
    print(resultat)