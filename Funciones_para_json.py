import Clases
import datetime
from listasenlazadas import *
import json
from ListaObjetos import *


def normal_a_jason(lista_clase, nombre_archivo, atributo_fecha=None):
    lista_diccionario=[]
    for objeto in lista_clase:
        if atributo_fecha!=None:
            fecha = getattr(objeto, atributo_fecha)
            setattr(objeto, atributo_fecha, fecha.isoformat())
        lista_diccionario.append(objeto.__dict__)
    with open(nombre_archivo, 'w') as archivo:
            json.dump(lista_diccionario, archivo,indent=2)
            archivo.write('\n')

#empleado avion
normal_a_jason(lista_empleado,r'Jsons\empleado.json')
normal_a_jason(lista_avion,r'Jsons\avion.json')


def json_a_normal(clase,nombre_archivo,atributo_fecha=None):
    lista_clase=[]
    with open(nombre_archivo, 'r') as archivo:
        data = json.load(archivo)
    for objeto in data:
        if atributo_fecha!=None:
            fecha = objeto[atributo_fecha]
            objeto[atributo_fecha]= datetime.date.fromisoformat(fecha)
        lista_clase.append(clase(**objeto))
    return lista_clase

json_a_normal(Clases.empleado,r'Jsons\empleado.json')
json_a_normal(Clases.avion,r'Jsons\avion.json') 
#PASARLE LA CLASE EN SI


    
def json_a_enlazada(clase,nombre_archivo,atributo_fecha=None,atributo_con_objeto=None,clase_nested_objeto=None):
    lista_clase=Lista()
    with open(nombre_archivo, 'r') as archivo:
        data = json.load(archivo)
    for objeto in data:
        
        if atributo_fecha!=None:
            fecha = objeto[atributo_fecha]
            objeto[atributo_fecha]= datetime.date.fromisoformat(fecha)
        
        if atributo_con_objeto !=None:
            lista_objetos = objeto[atributo_con_objeto]
            objeto[atributo_con_objeto]= [clase_nested_objeto(**nested_objeto) for nested_objeto in lista_objetos]
        lista_clase.append(Nodo(clase(**objeto)))
    return lista_clase

print(json_a_enlazada(Clases.persona,r'Jsons\persona.json','fecha_de_nacimiento')) 
print(json_a_enlazada(Clases.vuelo,r'Jsons\vuelo.json')) 
print(json_a_enlazada(Clases.viaje,r'Jsons\viaje.json','fecha','pasajeros',Clases.persona))
print(json_a_enlazada(Clases.reserva,r'Jsons\reserva.json')) 