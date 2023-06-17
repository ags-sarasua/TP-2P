from Clases import *

def menu_actualizar_persona(lista_persona):
    print('1)DNI   2)Nombre     3)Apellido   4)Sexo  5)Fecha de nacimiento   6)Pais     7)Mail    8)Telefono')
    print('\n \t Comentario')
    print('DNI: 8 digitos numericos \nSexo: Masculino, Fenenino, Otro \nPais: en mayuscula y en ingles  \nMail: terminar en @gmail.com  \nTelefono: 10 digitos numericos \n')
    input_principal=input("ingrese el DNI de la persona a actualizar:    ")
    input_principal=persona.check_DNI(input_principal)
    eleccion_actualizar=input("Ingrese numero de atributo a actualizar:   ")
    
    if eleccion_actualizar!="5" and eleccion_actualizar in ['1','2','3','4','6','7','8']:
        nuevo_input=input("Ingrese el valor a actualizar:    ")
        if eleccion_actualizar=="1":
            nuevo_input=persona.check_DNI(nuevo_input) 
            if lista_persona.actualizar_le(input_principal,"DNI","DNI",nuevo_input) == False:
                print("El DNI ingresado no corresponde al de una persona existente. La información no ha sido actualizada con exito.")

        elif eleccion_actualizar=="2":
            nuevo_input=persona.check_nombre(nuevo_input,"nombre")
            if lista_persona.actualizar_le(input_principal,"DNI","nombre",nuevo_input) == False:
                print("El DNI ingresado no corresponde al de una persona existente. La información no ha sido actualizada con exito.")

        elif eleccion_actualizar=="3":
            nuevo_input=persona.check_nombre(nuevo_input,"apellido") 
            if lista_persona.actualizar_le(input_principal,"DNI","apellido",nuevo_input) == False:
                print("El DNI ingresado no corresponde al de un persona existente. La información no ha sido actualizada con exito.")

        elif eleccion_actualizar=="4":
            nuevo_input=persona.check_sexo(nuevo_input)
            if lista_persona.actualizar_le(input_principal,"DNI","sexo",nuevo_input) == False:
                print("El DNI ingresado no corresponde al de un persona existente. La información no ha sido actualizada con exito.")

        
        elif eleccion_actualizar=="6":
            nuevo_input=persona.check_pais(nuevo_input)
            if lista_persona.actualizar_le(input_principal,"DNI","pais",nuevo_input) == False:
                print("El DNI ingresado no corresponde al de un persona existente. La información no ha sido actualizada con exito.")

        elif eleccion_actualizar=="7":
            nuevo_input=persona.check_sintaxis_mail(nuevo_input) 
            if lista_persona.actualizar_le(input_principal,"DNI","mail",nuevo_input) == False:
                print("El DNI ingresado no corresponde al de un persona existente. La información no ha sido actualizada con exito.")
            

        elif eleccion_actualizar=="8":
            nuevo_input=persona.check_sintaxis_telefono(nuevo_input)
            if lista_persona.actualizar_le(input_principal,"DNI","telefono",nuevo_input) == False:
                print("El DNI ingresado no corresponde al de un persona existente. La información no ha sido actualizada con exito.")

    elif eleccion_actualizar=="5":
            nuevo_input=validarFecha()
            nuevo_input=persona.check_fecha(nuevo_input)
            if lista_persona.actualizar_le(input_principal,"DNI","fecha_de_nacimiento",nuevo_input) == False:
                print("El DNI ingresado no corresponde al de un persona existente. La información no ha sido actualizada con exito.")
    
    else: print("Ingrese alguna de las opciones numéricas y vuelva a intentarlo")
    
def menu_actualizar_empelado(lista_empleado):
    print('1)DNI   2)Nombre     3)Apellido   4)Sexo  5)Fecha de nacimiento   6)Pais    7)Legajo    8)Sector')
    print('\n \t Comentario')
    print('DNI: 8 digitos numericos \nSexo: Masculino, Femenino, Otro \nPais: en mayuscula y en ingles  \nLegajo: 4 numeros \nSector: Piloto,Tecnico,Administrativo \n')                    
    input_principal=input("ingrese el DNI del empleado a actualizar:    ")
    input_principal=persona.check_DNI(input_principal)
    eleccion_actualizar=input("Ingrese numero de atributo a actualizar:   ")
    

    if eleccion_actualizar!="5" and eleccion_actualizar in ['1','2','3','4','6','7','8']:
        nuevo_input=input("Ingrese el valor a actualizar:    ")
        if eleccion_actualizar=="1":
            nuevo_input=persona.check_DNI(nuevo_input)
            if actualizar(lista_empleado,input_principal,"DNI","DNI",nuevo_input)==False:
                print("El DNI ingresado no corresponde al de un empleado existente. La información no ha sido actualizada con exito.")

        elif eleccion_actualizar=="2":
            nuevo_input=persona.check_nombre(nuevo_input,"nombre")
            if actualizar(lista_empleado,input_principal,"DNI","nombre",nuevo_input)==False:
                print("El DNI ingresado no corresponde al de un empleado existente. La información no ha sido actualizada con exito.")
                
        elif eleccion_actualizar=="3":
            nuevo_input=persona.check_nombre(nuevo_input,"apellido")
            if actualizar(lista_empleado,input_principal,"DNI","apellido",nuevo_input)==False:
                print("El DNI ingresado no corresponde al de un empleado existente. La información no ha sido actualizada con exito.")

        elif eleccion_actualizar=="4":
            nuevo_input=persona.check_sexo(nuevo_input)
            if actualizar(lista_empleado,input_principal,"DNI","sexo",nuevo_input)==False:
                print("El DNI ingresado no corresponde al de un empleado existente. La información no ha sido actualizada con exito.")
        
        elif eleccion_actualizar=="7":
            nuevo_input=empleado.checklegajo(nuevo_input)
            if actualizar(lista_empleado,input_principal,"DNI","legajo",nuevo_input)==False:
                print("El DNI ingresado no corresponde al de un empleado existente. La información no ha sido actualizada con exito.") 

        elif eleccion_actualizar=="6":
            nuevo_input=persona.check_pais(nuevo_input)
            if actualizar(lista_empleado,input_principal,"DNI","pais",nuevo_input)==False:
                print("El DNI ingresado no corresponde al de un empleado existente. La información no ha sido actualizada con exito.")

        elif eleccion_actualizar=="8":
            nuevo_input=persona.check_sector(nuevo_input)
            if actualizar(lista_empleado,input_principal,"DNI""sector",nuevo_input)==False:
                print("El DNI ingresado no corresponde al de un empleado existente. La información no ha sido actualizada con exito.")

    elif eleccion_actualizar=="5":
            nuevo_input=validarFecha()
            nuevo_input=persona.check_fecha_de_nacimiento(nuevo_input)
            if actualizar(lista_empleado,input_principal,"DNI","fecha_de_nacimiento",nuevo_input)==False:
                print(" El DNI ingresado no corresponde al de un empleado existente. La información no ha sido actualizada con exito.")
    else: print("Ingrese alguna de las opciones numéricas y vuelva a intentarlo") 
    
def menu_actualizar_avion(lista_avion):
    print('1)Nro serie   2)Modelo   3)Fecha alta  4)Estado')
    print('\n \t Comentario')
    print('Nro serie: 10 digitos numericos \nEstado: En servicio , Fuera de servicio \n')
    input_principal=input("ingrese el Nro de serie del avion a actualizar:    ")
    input_principal=avion.check_sintaxis_nro_serie(input_principal)
    eleccion_actualizar=input("Ingrese numero de atributo a actualizar:   ")
    
    if eleccion_actualizar!="3":
        nuevo_input=input("Ingrese el valor a actualizar:    ")
        
        if eleccion_actualizar=="1":
            nuevo_input=avion.check_nro_serie(nuevo_input)
            if actualizar(lista_avion,input_principal,"nro_serie","nro_serie",nuevo_input) == False:
                print("El número de serie ingresado no corresponde al de un avión existente. La información no ha sido actualizada con exito.")

        elif eleccion_actualizar=="2":
            nuevo_input=nuevo_input
            if actualizar(lista_avion,input_principal,"nro_serie","modelo",nuevo_input) == False:
                print("El número de serie ingresado no corresponde al de un avión existente. La información no ha sido actualizada con exito.")
            
        elif eleccion_actualizar=="4":
            nuevo_input=avion.check_estado(nuevo_input)
            if actualizar(lista_avion,input_principal,"nro_serie","estado",nuevo_input) == False:
                print("El número de serie ingresado no corresponde al de un avión existente. La información no ha sido actualizada con exito.")

    elif eleccion_actualizar=="3":
        nuevo_input=validarFecha()
        if actualizar(lista_avion,input_principal,"nro_serie","fecha_alta",nuevo_input) == False:
            print("El número de serie ingresado no corresponde al de un avión existente. La información no ha sido actualizada con exito.")

    else:
        print("Ingrese una opción numérica válida y vuelva a intentarlo")
    
def menu_actualizar_viaje(lista_viaje):
    print('1)Nro viaje   2)Nro vuelo    3)Nro serie   4)Fecha')
    print('\n \t Comentario')
    print('Nro viaje: 4 digitos numericos \nNro vuelo: 4 digitos numericos \n')
    input_principal=input("ingrese el Nro de viaje del viaje a actualizar:    ")
    input_principal=viaje.check_sintaxis_nro_viaje(input_principal)
    eleccion_actualizar=input("Ingrese numero de atributo a actualizar:   ")
    
    if eleccion_actualizar!="4" and eleccion_actualizar in ['1','2','3']:
        nuevo_input=input("Ingrese el valor a actualizar:    ")
        if eleccion_actualizar=="1":
            nuevo_input=viaje.check_sintaxis_nro_viaje(nuevo_input)
            if lista_viaje.actualizar_le(input_principal,"nro_viaje","nro_viaje",nuevo_input) == False:
                print("El número de viaje ingresado no corresponde al de un viaje existente. La información no ha sido actualizada con exito.")
        elif eleccion_actualizar=="2":
            nuevo_input=vuelo.check_sintaxis_nro_vuelo(nuevo_input)
            if lista_viaje.actualizar_le(input_principal,"nro_viaje","nro_vuelo",nuevo_input) == False:
                print("El número de viaje ingresado no corresponde al de un viaje existente. La información no ha sido actualizada con exito.")
        elif eleccion_actualizar=="3":
            nuevo_input=avion.check_sintaxis_nro_serie(nuevo_input)
            if lista_viaje.actualizar_le(input_principal,"nro_viaje","nro_serie",nuevo_input) == False:
                print("El número de viaje ingresado no corresponde al de un viaje existente. La información no ha sido actualizada con exito.")
    elif eleccion_actualizar=="4":
        nuevo_input=validarFecha()
        if lista_viaje.actualizar_le(input_principal,"nro_viaje","fecha",nuevo_input) == False:             
            print("El número de viaje ingresado no corresponde al de un viaje existente. La información no ha sido actualizada con exito.")
    
    else: print("Ingrese alguna de las opciones númericas y vuelva a intentarlo")

def menu_actualizar_reserva(lista_empleado,lista_viaje,lista_reserva):
    print('1)Nro reserva   2)DNI cliente   3)Legajo Empleado  4)Nro viaje')
    print('\n \t Comentario')
    print('Nro reserva: 4 digitos numericos  \nDNI: 8 digitos numericos   \nLegajo: 4 digitos numericos   \nNro viaje: 4 numeros \n')
    input_principal=input("ingrese el Nro de reserva de la reserva a actualizar:    ")
    input_principal=reserva.check_sintaxis_nro_reserva(input_principal)
    eleccion_actualizar=input("Ingrese numero del atributo a actualizar:   ")
    nuevo_input=input("Ingrese el valor a actualizar:    ")

    if eleccion_actualizar in ['1','2','3','4']:
        if eleccion_actualizar=="1":
            nuevo_input=reserva.check_sintaxis_nro_reserva(nuevo_input)
            if lista_reserva.actualizar_le(input_principal,"nro_reserva","nro_reserva",nuevo_input) == False:
                print("El número de reserva ingresado no corresponde al de un reserva existente. La información no ha sido actualizada con exito.")
        if eleccion_actualizar=="2":
            nuevo_input=persona.check_DNI(nuevo_input)
            if lista_reserva.actualizar_le(input_principal,"nro_reserva","DNI_cliente",nuevo_input) == False:
                print("El número de reserva ingresado no corresponde al de un reserva existente. La información no ha sido actualizada con exito.")
        if eleccion_actualizar=="3":
            nuevo_input=empleado.check_legajo_existente(nuevo_input, lista_empleado)
            if lista_reserva.actualizar_le(input_principal,"nro_reserva","empleado",nuevo_input) == False:
                print("El número de reserva ingresado no corresponde al de un reserva existente. La información no ha sido actualizada con exito.")
        if eleccion_actualizar=="4":
            
            nuevo_input=viaje.check_sintaxis_nro_viaje(nuevo_input,lista_viaje)
            if lista_reserva.actualizar_le(input_principal,"nro_reserva","nro_viaje",nuevo_input) == False:
                print("El número de reserva ingresado no corresponde al de un reserva existente. La información no ha sido actualizada con exito.")
        
    else:
        print("Ingrese alguna de las opciones numéricas y vuelva a intentarlo")