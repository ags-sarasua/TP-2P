from Clases import *

def menu_agregar_avion(lista_avion):
    print('1)Nro serie   2)Modelo   3)Fecha alta  4)Estado')
    print('\n \t Comentario')
    print('Nro serie: 10 digitos numericos \nEstado: En servicio , Fuera de servicio \n')
    lista_filtro=[]
    listaMenu=['Nro serie','Modelo','Fecha alta','Estado']
    for i in range(4):
        if i == 2:
            print("Ahora a la fecha de alta.")
            lista_filtro.append(validarFecha())    
        else:
            user_input = str(input("Inroduzca {} : ".format(listaMenu[i])))
            lista_filtro.append(user_input)
    #Todos los checks
    lista_filtro[0]=avion.check_sintaxis_nro_serie(lista_filtro[0])
    lista_filtro[0]=avion.nro_serie_repetido(lista_filtro[0],lista_avion)
    lista_filtro[3]=avion.check_estado(lista_filtro[3])
    lista_filtro[2]=persona.check_fecha(lista_filtro[2])
    return lista_filtro

def menu_agregar_persona(lista_persona):
    print('1)DNI   2)Nombre   3)Apellido   4)Sexo  5)Fecha de nacimiento   6)Pais   7)Mail   8)Telefono')
    print('\n \t Comentario')
    print('DNI: 8 digitos numericos \nSexo: Masculino, Fenenino, Otro \nPais: en mayuscula y en ingles  \nMail: terminar en @gmail.com  \nTelefono: 10 digitos numericos \n')
    lista_filtro=[]
    listaMenu = ['DNI', 'Nombre', 'Apellido','Sexo', 'Fecha de nacimiento', 'Pais','Mail','Telefono']
    for i in range(8):
        if i == 4:
            print("Ahora a la fecha de nacimiento.")
            lista_filtro.append(validarFecha())    
        else:
            user_input = str(input("Inroduzca {} : ".format(listaMenu[i])))
            lista_filtro.append(user_input)
    lista_filtro[0]=persona.check_DNI(lista_filtro[0])
    lista_filtro[0]=persona.check_existencia_DNI(lista_filtro[0],lista_persona)
    lista_filtro[1]=persona.check_nombre(lista_filtro[1],'nombre')
    lista_filtro[2]=persona.check_nombre(lista_filtro[2],'apellido')
    lista_filtro[3]=persona.check_sexo(lista_filtro[3])
    lista_filtro[4]=persona.check_fecha(lista_filtro[4])
    lista_filtro[5]=persona.check_pais(lista_filtro[5])
    lista_filtro[6]=persona.check_sintaxis_mail(lista_filtro[6])
    lista_filtro[6]=persona.check_existencia_mail(lista_filtro[6],lista_persona)
    lista_filtro[7]=persona.check_sintaxis_telefono(lista_filtro[7])
    lista_filtro[7]=persona.check_existencia_telefono(lista_filtro[7],lista_persona)
    return lista_filtro

def menu_agregar_empelado(lista_empleado):
    print('1)DNI   2)Nombre  3)Apellido  4)Sexo  5)Fecha de nacimiento   6)Pais    7)Legajo    8)Sector   9)Us  10)Contreseña')
    print('\n \t Comentario')
    print('DNI: 8 digitos numericos \nSexo: Masculino, Femenino, Otro \nPais: en mayuscula y en ingles  \nLegajo: 4 numeros \nSector: Piloto,Tecnico,Administrativo \n')
    lista_filtro=[]
    listaMenu = ['DNI', 'Nombre','Apellido', 'Sexo', 'Fecha de nacimiento', 'Pais','Legajo','Sector','Usuario','Contrasña']
    for i in range(10):
        if i == 4:
            print("Ahora a la fecha de nacimiento.")
            lista_filtro.append(validarFecha())    
        else:
            user_input = str(input("Inroduzca {} : ".format(listaMenu[i])))
            lista_filtro.append(user_input)
    lista_filtro[0]=persona.check_DNI(lista_filtro[0])
    lista_filtro[0]=empleado.DNI_repetido_empleado(lista_filtro[0],lista_empleado)
    lista_filtro[1]=persona.check_nombre(lista_filtro[1],'nombre')
    lista_filtro[2]=persona.check_nombre(lista_filtro[2],'apellido')
    lista_filtro[3]=persona.check_sexo(lista_filtro[3])
    lista_filtro[4]=persona.check_fecha(lista_filtro[4])
    lista_filtro[5]=persona.check_pais(lista_filtro[5])
    lista_filtro[6]=empleado.checklegajo(lista_filtro[6], lista_empleado)
    lista_filtro[7]=empleado.checksector(lista_filtro[7])
    lista_filtro[8]=empleado.check_usuario_repetido(lista_filtro[8],lista_empleado)
    return lista_filtro

def menu_agregar_vuelo(lista_empleado,arbol_vuelo):
    print('1)Nro vuelo  2)Aeropuerto salida  3)Aeropuerto llegada   4)Legajo del piloto   5)Precio')
    print('\n \t Comentario')
    print('Nro vuelo: 4 digitos numericos \n')
    lista_filtro=[]
    listaMenu=['Nro vuelo'  ,'Aeropuerto salida' , 'Aeropuerto llegada'  ,'Legajo del piloto' ,  'Precio']
    for i in range(5):
        user_input = str(input("Inroduzca {} : ".format(listaMenu[i])))
        lista_filtro.append(user_input)
        
    #Todos los checks
    lista_filtro[0]=vuelo.check_sintaxis_nro_vuelo(lista_filtro[0])
    lista_filtro[0]=vuelo.check_existencia_nro_vuelo(lista_filtro[0],arbol_vuelo)
    lista_filtro[4]=vuelo.check_precio_vuelo(lista_filtro[4])
    lista_filtro[3]=vuelo.check_piloto(lista_filtro[3], lista_empleado)
    return lista_filtro
    
def menu_agregar_viaje(lista_avion,lista_viaje,arbol_vuelo):
    print('1)Nro viaje   2)Nro vuelo    3)Nro serie   4)Fecha')
    print('\n \t Comentario')
    print('Nro viaje: 4 digitos numericos \nNro vuelo: 4 digitos numericos \n')
    lista_filtro=[]
    listaMenu=['Nro viaje' ,  'Nro vuelo'  ,  'Nro serie'  , 'Fecha']
    for i in range(4):
        if i == 3:
            print("Ahora a la fecha del viaje.")
            lista_filtro.append(validarFecha())    
        else:
            user_input = str(input("Inroduzca {} : ".format(listaMenu[i])))
            lista_filtro.append(user_input)
    #Todos los checks
    lista_filtro[0]=viaje.check_sintaxis_nro_viaje(lista_filtro[0])
    lista_filtro[0]=viaje.check_existencia_nro_viaje(lista_filtro[0],lista_viaje)
    lista_filtro[1]=viaje.check_vuelo(lista_filtro[1], arbol_vuelo)
    lista_filtro[2]=viaje.check_nro_serie(lista_filtro[2],lista_avion)
    lista_filtro[2]=viaje.check_estado(lista_filtro[2],lista_avion)
    return lista_filtro

def menu_agregar_reserva(lista_persona,lista_empleado,lista_viaje,lista_reserva,arbol_vuelo):
    print('1)Nro reserva   2)DNI cliente   3)Legajo Empleado  4)Nro viaje   5)Monto')
    print('\n \t Comentario')
    print('Nro reserva: 4 digitos numericos  \nDNI: 8 digitos numericos   \nLegajo: 4 digitos numericos   \nNro viaje: 4 numeros \n')
    lista_filtro=[]
    listaMenu=['Nro reserva' ,  'DNI cliente '  ,'Legajo Empleado' , 'Nro viaje ' , 'Monto']
    for i in range(5):
        user_input = str(input("Inroduzca {} :".format(listaMenu[i])))
        lista_filtro.append(user_input)
    #Todos los checks
    lista_filtro[0]=reserva.check_sintaxis_nro_reserva(lista_filtro[0])
    lista_filtro[0]=reserva.check_existencia_nro_reserva(lista_filtro[0],lista_reserva)
    lista_filtro[1]=reserva.check_cliente(lista_filtro[1],lista_persona)
    lista_filtro[2]=reserva.check_empleado(lista_filtro[2],lista_empleado)
    lista_filtro[3]=reserva.check_viaje(lista_filtro[3],lista_viaje)
    lista_filtro[4]=reserva.check_monto(lista_filtro[4],lista_filtro[3],lista_viaje, arbol_vuelo)

    return lista_filtro