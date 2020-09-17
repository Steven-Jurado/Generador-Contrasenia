import random as aleatorio

def generadorContrasenia():
    numero = ['1','2','3','4','5','6','7','8','9']
    lestrasMayuscula = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
    letrasMinuscula = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']

    caracteres = numero+lestrasMayuscula+letrasMinuscula

    contrasenia =[]

    for i in range(15):
        caracteresElegido = aleatorio.choice(caracteres)
        contrasenia.append(caracteresElegido)

    miContrasenia = "".join(contrasenia)
    return miContrasenia


def main():
    passwork = generadorContrasenia()
    print('Su contraseña de 15 caracteres es: '+passwork)


if __name__ == '__main__':
    main()
    