

#DEFINICIO
#a --> No sobrescriure
#w --> sobrescriure
#r --> llegir



####1) operacio com a input (que sigui variable)
####2) Arxiu tb sigui un input(variable)
def guardar_resultat (resultat_operacio, valor1, valor2,operacio_matematica): 
    with open("fitxer.txt", "w") as f:
        f.write(f"resultat de la {operacio_matematica}, {valor1} i {valor2} es {resultat_operacio}")

#EXECUCIO
if __name__ == "__main__":
    guardar_resultat(7,5,2,'multiplicacio')