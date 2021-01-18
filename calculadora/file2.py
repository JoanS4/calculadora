
"""
funcio def aplicar(valor1, valor2, operacio)
ef operacio ():
    resultat = input( ' Quina operació vols fer?? (multiplicar sumar o restar) \n' )
    return resultat


return varo1 operacio valor2
"""

#Definició 
def operacionvalores (valor1,valor2,operacion) :
    if operacion == "sumar":  
        resultat = valor1+valor2 
    elif operacion == "restar":
        resultat = valor1-valor2 
    elif operacion == "multiplicar": 
        resultat = valor1 * valor2      
    return resultat 



#Execució 
if __name__ == "__main__":
    resultat = operacionvalores (1,2, "multiplicar")
    print(resultat)