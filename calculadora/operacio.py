
from funcionsimport import preguntar_operacio_usuari
from file2 import operacionvalores
from file3 import valors
from Output2 import guardar_resultat


def calcular_operacio() :
    operacio_matematica = preguntar_operacio_usuari()
    valor1, valor2 = valors()
    resultat_operacio = operacionvalores(valor1,valor2, operacio_matematica)
    guardar_resultat(resultat_operacio, valor1, valor2,operacio_matematica)
    return resultat_operacio