



# funció preguntat valors

def valors (): 
    valor1 = int(input ('valor1: '))
    valor2 = int(input ('valor2: '))
    return valor1, valor2 

#Execució 
if __name__ == "__main__":
    valor1, valor2 = valors ()
    print(valor1, valor2)

