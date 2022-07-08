import string 
import random 

alfabeto = list(string.ascii_letters)
digitos = list(string.digits)
caracteres_especiales = list("!@#$%^&*()")
caracteres = list (string.ascii_letters + string.digits + "!@#$%^&*()")

def generador_contraseñas():
    length = int(input("longitud de caracteres "))

    
    alfabeto_count = int(input("escribe numero de caracteres letras del alfabeto a incluir "))
    digitos_count = int(input("cantidad caracteres numero a incluir "))
    caracteres_especiales_count = int(input("escribe numero de caracteres especiales a incluir "))
    caracteres_count = alfabeto_count + digitos_count + caracteres_especiales_count

    if caracteres_count > length:
        print("total de caracteres es mayor que la longitud de la contraseña")
        return

    contraseña = []   
    for i in range (alfabeto_count):
        contraseña.append(random.choice(alfabeto))
    
    for i in range (digitos_count):
        contraseña.append(random.choice(digitos))

    for i in range (caracteres_especiales_count):
        contraseña.append(random.choice(caracteres_especiales))
    
    if caracteres_count < length:
        random.shuffle(contraseña)
        for i in range(length - caracteres_count):
            contraseña.append(random.choice(caracteres))
   
    print("su contraseña segura es: " + "".join(contraseña))
    salir = input("Press enter to close program")      
generador_contraseñas()


