import datetime

#validarNum valida que un número ingresado por el usuario sea un número entre cierto rango pedido
def validarNum(tipoDato: str, min: int, max: int) -> int:
    ingresado = min - 1
    booleana = False
    while(booleana == False):
        try:
            ingresado = int(input("Ingrese "+ tipoDato +": "))
            if(ingresado < min or ingresado > max):
                print("Error, el número debe estar entre {} y {}".format(min, max))
            else:
                return ingresado
        except:
            print("Error, tiene que ingresar un número. intente de nuevo")
            
#validarFecha recibe año, mes y día para convertirlo en un dato del tipo datetime 
def validarFecha():
    meses_31dias = [1, 3, 5, 7, 8, 10, 12]
    meses_30dias = [4, 6, 9, 11]

    año = validarNum("año", 1900, 2100)
    mes = validarNum("mes", 1, 12)

    # Pedir el día (acotado según el mes)
    if mes in meses_31dias:
        dia = validarNum("dia", 1, 31)
    elif mes in meses_30dias:
        dia = validarNum("dia", 1, 30)
    elif mes == 2:
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            dia = validarNum("dia", 1, 29)
        else:
            dia = validarNum("dia", 1, 28)
    return(datetime.date(año, mes, dia))
"""
#login recibe un usuario y una contraseña para chequear si está en el sistema.  NO SE USA MAS
def login(username, password):
        with open("Usuarios.txt", 'r', encoding='utf-8') as archivo:
            listaUsuarios=[]
            passwordList=[]
            for linea in archivo:
                usu, contra = linea.strip().split(".")
                listaUsuarios.append(usu)
                passwordList.append(contra)
            while username not in listaUsuarios:
                username = input("El usuario ingresado no existe. Intente de nuevo: ")
            index = listaUsuarios.index(username)
            while passwordList[index] != password:
                password = input("Error, contraseña incorrecta. Ingresela nuevamente: ")
            return True

#registrarse escribe el archivo que tiene los usuarios y contraseñas para registrar un nuevo usuario.  NO SE USA MAS
def registrarse(username):
    with open("Usuarios.txt", 'r', encoding='utf-8') as archivo:
        listaUsuarios=[]
        for linea in archivo:
            usu = linea.strip().split(".")[0]
            listaUsuarios.append(usu)
    while username in listaUsuarios or "." in username:
        username = input("Este nombre de usuario no es válido. Ingrese otro: ")
    password = input("Ingrese una contraseña: ")
    with open("Usuarios.txt", 'a', encoding='utf-8') as archivo:
        archivo.write(f"\n{username}.{password}")
        return True

#NO SE USA MAS
def actualizar_contra(us, con):
    with open("Usuarios.txt", 'r', encoding='utf-8') as archivo:
        listaUsuarios=[]
        passwordList=[]
        for linea in archivo:
            usu, contra = linea.strip().split(".")
            listaUsuarios.append(usu)
            passwordList.append(contra)    
        index = listaUsuarios.index(us)
        passwordList[index] = con
    with open("Usuarios.txt", 'w', encoding='utf-8') as archivo:
        for i, j in zip(listaUsuarios, passwordList):
            archivo.write(f"{i}.{j}\n")
        return True
"""
#actualizar para las listas fijas
def actualizar(lista, input_principal, atributo_principal, atributo_a_buscar, nuevo_input):
    for objeto in lista:
        if getattr(objeto,atributo_principal)==input_principal:
            setattr(objeto,atributo_a_buscar,nuevo_input)
            return True
    return False

