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
    with open(nombre_archivo, 'w',encoding="utf-8") as archivo:
            json.dump(lista_diccionario, archivo,indent=2,ensure_ascii=False)
            archivo.write('\n')

#empleado avion
#normal_a_jason(lista_empleado,r'Jsons\empleado.json')
#normal_a_jason(lista_avion,r'Jsons\avion.json')


def json_a_normal(clase,nombre_archivo,atributo_fecha=None):
    lista_clase=[]
    with open(nombre_archivo, 'r',encoding="utf-8") as archivo:
        data = json.load(archivo)
    for objeto in data:
        if atributo_fecha!=None:
            fecha = objeto[atributo_fecha]
            objeto[atributo_fecha]= datetime.date.fromisoformat(fecha)
        lista_clase.append(clase(**objeto))
    return lista_clase

#json_a_normal(Clases.empleado,r'Jsons\empleado.json')
#json_a_normal(Clases.avion,r'Jsons\avion.json') 
#PASARLE LA CLASE EN SI
    
def json_a_enlazada(clase,nombre_archivo,atributo_fecha=None,atributo_con_objeto=None,clase_nested_objeto=None,atributo_fecha_nested=None):
    lista_clase=Lista()
    with open(nombre_archivo, 'r',encoding="utf-8") as archivo:
        data = json.load(archivo)
    for objeto in data:
        
        if atributo_fecha!=None:
            fecha = objeto[atributo_fecha]
            objeto[atributo_fecha]= datetime.date.fromisoformat(fecha)
        
        if atributo_con_objeto !=None:
            lista_objetos = objeto[atributo_con_objeto]
            for nested_objeto in lista_objetos:
                if atributo_fecha_nested!=None:
                    fecha = nested_objeto[atributo_fecha_nested]
                    nested_objeto[atributo_fecha_nested]= datetime.date.fromisoformat(fecha)
            objeto[atributo_con_objeto]= [clase_nested_objeto(**nested_objeto) for nested_objeto in lista_objetos]

        lista_clase.append(Nodo(clase(**objeto)))
    return lista_clase

#lista_persona.enlazada_a_jason(r'Jsons\persona.json',atributo_fecha='fecha_de_nacimiento')
#lista_vuelo.enlazada_a_jason(r'Jsons\vuelo.json')
#lista_viaje.enlazada_a_jason(r'Jsons\viaje.json',atributo_fecha='fecha',atributo_con_objeto='pasajeros',atributo_fecha_nested='fecha_de_nacimiento')
#lista_reserva.enlazada_a_jason(r'Jsons\reserva.json')
