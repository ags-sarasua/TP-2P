from Codigo_estructuras.Listas_enlazadas import *
from Clases import *
from Manejo_de_datos.Funciones_para_json import * 

from Codigo_estructuras.Codigo_Cola import *
from Codigo_estructuras.Codigo_arbol import *

from Funciones_normalizar_menu.Funciones_agregar_menu import *
from Funciones_normalizar_menu.Funciones_actualizar_menu import *
from Funciones_normalizar_menu.Funciones_graficar_menu import *

from colorama import init, Fore, Back, Style
#----------------

#menu una vez ingresado 
def menu_clase(lista_persona,lista_empleado,lista_avion,arbol_vuelo,lista_viaje,lista_reserva,cola_mantenimiento,usuario):
    menu = True
    while menu == True:
        print('')
        print(Fore.BLUE + '\033[1m1)Persona  2)Empleado  3)Avion  4)Vuelo   5)Viaje   6)Reserva  7)Cambiar Contraseña\033[0m' +  '  S)Salir\033[0m')
        eleccion_clase=input('Ingrese su eleccion: ')
        print('')
        
#persona
        if eleccion_clase=='1':
            Booleano=True
            while Booleano:  #Para que una vez hagas algun metodo puedas volver a este lugar
                print('')
                print(Fore.BLUE + '\033[1m1)Visualizar lista   2)Agregar persona   3)Actualizar Persona  4) Eliminar persona\033[0m'+ '  B)Volver')
                eleccion_metodo=input('Ingrese su eleccion: ')
                print('')
        #Visualizar
                if eleccion_metodo=='1':
                    print(lista_persona)
        #Agregar
                if eleccion_metodo=='2':
                    lista_filtro=menu_agregar_persona(lista_persona)
                    lista_persona.append(Nodo(persona(lista_filtro[0], lista_filtro[1], lista_filtro[2],lista_filtro[3],lista_filtro[4],lista_filtro[5],lista_filtro[6],lista_filtro[7])))
        #Actualizar
                if eleccion_metodo=='3':
                    menu_actualizar_persona(lista_persona)   
        #Eliminar
                if eleccion_metodo=='4':
                    DNI=input("Ingrese el DNI de la persona que quiere eliminar: ")
                    if lista_persona.pop(DNI,"DNI"):
                        print("Se eliminó correctamente la persona indicada")
                    else:
                        print("No se puedo eliminar correctamente la persona indicada")
        #Volver
                if eleccion_metodo=='B' or eleccion_metodo =="b":
                    menu_clase(lista_persona,lista_empleado,lista_avion,arbol_vuelo,lista_viaje,lista_reserva,cola_mantenimiento,usuario)
                    Booleano=False
                    menu=False
#empleado     
        if eleccion_clase=='2':
            Booleano=True
            while Booleano:
                print('')
                print(Fore.BLUE + '\033[1m1)Visualizar lista   2)Agregar empleado   3)Eliminar empleado  4)Actualizar empleado  5)Graficar\033[0m'+  '  B)Volver')
                eleccion_metodo=input('Ingrese su eleccion: ')
                print('')
        #Visualizar
                if eleccion_metodo=='1':
                    for objeto in lista_empleado:
                        print(objeto)
        #Agregar
                if eleccion_metodo=='2':
                    lista_filtro=menu_agregar_empelado(lista_empleado)
                    lista_empleado.append(empleado(lista_filtro[0], lista_filtro[1], lista_filtro[2],lista_filtro[3],lista_filtro[4],lista_filtro[5],lista_filtro[6],lista_filtro[7],lista_filtro[8],lista_filtro[9]))
                    
        #Eliminar
                if eleccion_metodo=='3':
                    input_principal=input('Ingrese el DNI del empleado que desea eliminar: ')
                    Booleano=False
                    for objeto in lista_empleado:
                        if input_principal==objeto.DNI:
                            lista_empleado.remove(objeto)
                            Booleano=True
                            print('El empleado con el DNI {} se ha eliminado correctamente'.format(input_principal))
                    if Booleano==False:
                        print('El empleado ingresado no se encuentra en la base de datos')
        #Actualizar
                if eleccion_metodo=='4':
                    menu_actualizar_empelado(lista_empleado)
        #Graficar
                if eleccion_metodo=='5':
                    menu_graficar_empleado(lista_empleado)
        #Volver                          
                if eleccion_metodo=='B' or eleccion_metodo =="b":
                    menu_clase(lista_persona,lista_empleado,lista_avion,arbol_vuelo,lista_viaje,lista_reserva,cola_mantenimiento,usuario)
                    Booleano=False
                    menu=False
#avion
        if eleccion_clase=='3':
            Booleano=True
            while Booleano:
                print('')
                print(Fore.BLUE + '\033[1m1)Visualizar lista   2)Agregar avion   3)Eliminar avion   4)Actualizar Avión  5) Mantenimiento de avión\033[0m'+  '  B)Volver')
                eleccion_metodo=input('Ingrese su eleccion: ')
                print('')
        #Visualizar
                if eleccion_metodo=='1':
                    for objeto in lista_avion:
                        print(objeto)
        #Agregar
                if eleccion_metodo=='2':
                    lista_filtro=menu_agregar_avion(lista_avion)
                    lista_avion.append(avion(lista_filtro[0], lista_filtro[1], lista_filtro[2],lista_filtro[3]))
        #Eliminar
                if eleccion_metodo=='3':
                    input_principal=input('Ingrese el nro de serie del avión que desea eliminar: ')
                    if avion.eliminarAvion(input_principal,lista_avion):
                        print('El avión con el nro de serie {} se ha eliminado correctamente'.format(input_principal))
                    else:
                        print('El avión ingresado no se encuentra en la base de datos')                      
        #Actualizar
                if eleccion_metodo=='4':
                    menu_actualizar_avion(lista_avion)

        #Mantenimiento
                if eleccion_metodo == "5":
                    menu_cola_avion(lista_avion,cola_mantenimiento)
        #Volver
                if eleccion_metodo=='B' or eleccion_metodo =="b":
                    menu_clase(lista_persona,lista_empleado,lista_avion,arbol_vuelo,lista_viaje,lista_reserva,cola_mantenimiento,usuario)
                    Booleano=False
                    menu=False
                    
#Vuelo
        if eleccion_clase=='4':
            Booleano=True
            while Booleano:
                print('')
                print(Fore.BLUE + '\033[1m1)Visualizar lista   2)Agregar vuelo  3) Eliminar vuelo   \033[0m'+  'B)Volver')
                eleccion_metodo=input('Ingrese su eleccion: ')
                print('')
        #Visualizar
                if eleccion_metodo=='1':
                    arbol.preorden(arbol_vuelo)
        #Agregar
                if eleccion_metodo=='2':
                    lista_filtro=menu_agregar_vuelo(lista_empleado,arbol_vuelo)
                    arbol_vuelo.insertar((vuelo(lista_filtro[0], lista_filtro[1], lista_filtro[2],lista_filtro[3],lista_filtro[4])))
        #Eliminar
                if eleccion_metodo=='3':
                    vuelo_eliminar=input("Ingrese el número de vuelo que quiere eliminar: ")
                    if arbol_vuelo.eliminar(vuelo_eliminar):
                        print("Se eliminó correctamente el vuelo indicado")
                    else:
                        print("No se puedo eliminar correctamente el vuelo indicado")                
        #Volver
                if eleccion_metodo=='B' or eleccion_metodo =="b":
                    menu_clase(lista_persona,lista_empleado,lista_avion,arbol_vuelo,lista_viaje,lista_reserva,cola_mantenimiento,usuario) 
                    Booleano=False
                    menu=False
                            
#viaje
        if eleccion_clase=='5':
            Booleano=True
            while Booleano:
                print('')
                print(Fore.BLUE + '\033[1m1)Visualizar lista   2)Agregar viaje     3)Eliminar viaje  4)Actualizar Viaje   \033[0m'+  'B)Volver')
                eleccion_metodo=input('Ingrese su eleccion: ')
                print('')
        #Visualizar
                if eleccion_metodo=='1':
                    print(lista_viaje)
        #Agregar
                if eleccion_metodo=='2':
                    lista_filtro=menu_agregar_viaje(lista_avion,lista_viaje,arbol_vuelo)
                    lista_viaje.append(Nodo(viaje(lista_filtro[0], lista_filtro[1], lista_filtro[2],lista_filtro[3])))
        #Eliminar
                if eleccion_metodo=='3':
                    input_principal=input('Ingrese el nro de viaje que desea eliminar: ')
                    if lista_viaje.pop(input_principal,"nro_viaje"): print('El viaje con el nro {} se ha eliminado correctamente'.format(input_principal))
                    else: print('El viaje ingresado no se encuentra en la base de datos')
        #Actualizar
                if eleccion_metodo=='4':
                    menu_actualizar_viaje(lista_viaje)
        #Volver
                if eleccion_metodo=='B' or eleccion_metodo =="b":
                    menu_clase(lista_persona,lista_empleado,lista_avion,arbol_vuelo,lista_viaje,lista_reserva,cola_mantenimiento,usuario)
                    Booleano=False
                    menu=False
                    
#reserva              
        if eleccion_clase=='6':
            Booleano=True
            while Booleano:
                print('')
                print(Fore.BLUE + '\033[1m1)Visualizar lista   2)Agregar reserva   3)Eliminar reserva    4)Actualizar Reserva  \033[0m'+  'B)Volver')
                eleccion_metodo=input('Ingrese su eleccion: ')
                print('')
        #Visualizar
                if eleccion_metodo=='1':
                    print(lista_reserva)
        #Agregar
                if eleccion_metodo=="2":
                    lista_filtro=menu_agregar_reserva(lista_persona,lista_empleado,lista_viaje,lista_reserva,arbol_vuelo)
                    pasajero=lista_persona.buscar_inst(lista_filtro[1],"DNI")
                    if viaje.agregar_pasajero(lista_filtro[3], pasajero ,lista_viaje): 
                        lista_reserva.append(Nodo(reserva(lista_filtro[0], lista_filtro[1], lista_filtro[2],lista_filtro[3],lista_filtro[4])))
        #Eliminar
                if eleccion_metodo=='3':
                    input_principal=input('Ingrese la reserva que desea eliminar: ')
                    dni_ingresado=input("Ingrese el dni del pasajero: ")
                    viaje_ingresado=input("Ingrese el número de viaje del cual desea eliminar al pasajero: ")
                    pasajero2=lista_persona.buscar_inst(dni_ingresado,"DNI")
                    if viaje.eliminar_pasajero(viaje_ingresado,pasajero2,lista_viaje): 
                        if lista_reserva.pop(input_principal,"nro_reserva"):
                            print('La reserva nro {} se ha eliminado correctamente'.format(input_principal))
        #Actualizar
                if eleccion_metodo=='4':
                    print('')
                    print('Solo casos excepcionales en donde la empresa no recibe mas dinero por el cambio')
                    print('')
                    menu_actualizar_reserva(lista_persona,lista_empleado,lista_viaje,lista_reserva)
        #Volver
                if eleccion_metodo=='B' or eleccion_metodo =="b":
                    menu_clase(lista_persona,lista_empleado,lista_avion,arbol_vuelo,lista_viaje,lista_reserva,cola_mantenimiento,usuario)
                    Booleano=False
                    menu=False

#Actualizar contraseña
        if eleccion_clase=='7':
            verificar = False
            while verificar == False:
                newPass1 = input("Ingrese una nueva contraseña: ")
                newPass2 = input("Ingresela nuevamente: ")
                if newPass1 == newPass2:
                    verificar = True
                else:
                    print("Error, las contraseñas deben ser iguales. Intente nuevamente.")
            setattr(usuario,"contraseña" ,newPass1)
            print("Su contraseña se ha cambiado con éxito.")
                
                
#salir
        if eleccion_clase=='S' or eleccion_clase =="s":
            #Para terminar la ejecución del programa, se pasan todas las listas de nuevo a los archivos
            normal_a_jason(lista_empleado,r'Jsons\empleado.json','fecha_de_nacimiento')
            normal_a_jason(lista_avion,r'Jsons\avion.json',"fecha_alta")
            list(cola_mantenimiento)
            normal_a_jason(cola_mantenimiento,r'Jsons\cola_mantenimiento.json')
            lista_persona.enlazada_a_jason(r'Jsons\persona.json',atributo_fecha='fecha_de_nacimiento')
            lista_viaje.enlazada_a_jason(r'Jsons\viaje.json',atributo_fecha='fecha',atributo_con_objeto='pasajeros',atributo_fecha_nested='fecha_de_nacimiento')
            lista_reserva.enlazada_a_jason(r'Jsons\reserva.json')
            
            arbol_vuelo.guardar_estructura('Objetos_y_arbol\\arbol-vuelo.txt')
            
            menu = False

#Menu de ingreso

def menu(): 
    inicio = True
    #Traemos las listas de objetos desde los jsons5 
    lista_empleado=json_a_normal(empleado,r'Jsons\\empleado.json','fecha_de_nacimiento')
    lista_avion=json_a_normal(avion,r'Jsons\\avion.json',"fecha_alta") 
    lista_persona=json_a_enlazada(persona,r'Jsons\\persona.json','fecha_de_nacimiento')
    arbol_vuelo=arbol()
    arbol_vuelo.cargar_estructura('Objetos_y_arbol\\arbol-vuelo.txt')
    lista_viaje=json_a_enlazada(viaje,r'Jsons\\viaje.json','fecha','pasajeros',persona,'fecha_de_nacimiento')
    lista_reserva=json_a_enlazada(reserva,r'Jsons\\reserva.json')
    cola_mantenimiento=json_a_cola(avion,r'Jsons\\cola_mantenimiento.json')
    
    
    while inicio == True:
        print('')
        print(Fore.RED + "\033[1mBienvenido a aerolineas Mamba\033[0m")
        print("Base de datos por y para empleados")
        print("                                          |")
        print("                                          |")
        print("                                        .-'-.")
        print("                                       ' ___ '")
        print("                             ---------'  .-.  '---------")
        print("             _________________________'  '-'  '_________________________")
        print("              ''''''-|---|--/    \==][^',_m_,'^][==/    \--|---|-''''''")
        print("                            \    /  ||/   H   \||  \    /")
        print("                             '--'   OO   O|O   OO   '--'")
        
        numero = input("\nSi se quiere registrar ingrese el número 1 si ya tiene una cuenta ingrese el número 2:   ")
        while numero != "1" and numero != "2": numero = input("Ingrese una opción válida:   ")
        if numero == "1":  
            lista_filtro=menu_agregar_empelado(lista_empleado)
            print(lista_filtro)
            lista_empleado.append(empleado(lista_filtro[0], lista_filtro[1], lista_filtro[2],lista_filtro[3],lista_filtro[4],lista_filtro[5],lista_filtro[6],lista_filtro[7],lista_filtro[8],lista_filtro[9]))
        if numero == "2":
            print('Recuerde que debe ser un empleado de la compania. (Usuario:Agos Contra:123 FUNCIONA)')
            print('')
            us = input("Ingrese su usuario: ")
            con = input("Ingrese su contraseña: ")
            usuario=empleado.login(us, con,lista_empleado)
            menu_clase(lista_persona,lista_empleado,lista_avion,arbol_vuelo,lista_viaje,lista_reserva,cola_mantenimiento,usuario)
            print('')
            print(Fore.RED + "\033[1mGracias por su visita\033[0m")
            print(Fore.RED + "\033[1mTerminó la ejecución del programa\033[0m")
            print('')
            print('')
            inicio = False
            
menu()
