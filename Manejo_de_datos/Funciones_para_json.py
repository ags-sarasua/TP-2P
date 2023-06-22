
import datetime
from Codigo_estructuras.Listas_enlazadas import *
import json
from Codigo_estructuras.Codigo_Cola import*

def normal_a_jason(lista_clase, nombre_archivo, atributo_fecha=None):
    lista_diccionario=[]
    for objeto in lista_clase:
        #Hay que chequear si hay un atributo de tipo datetime porque asi como está se rompe si lo queremos pasar a json
        if atributo_fecha!=None:
            fecha = getattr(objeto, atributo_fecha)
            setattr(objeto, atributo_fecha, fecha.isoformat())
        lista_diccionario.append(objeto.__dict__) #Agregamos el diccionario del objeto
    with open(nombre_archivo, 'w',encoding="utf-8") as archivo:
            json.dump(lista_diccionario, archivo,indent=2,ensure_ascii=False)
            """
            Escribimos la lista de diccionarios en formato JSON en el archivo. 
            Los parámetros indent=2 y ensure_ascii=False se usan para dar formato legible al archivo JSON 
            y permitir caracteres no ASCII.
            """
            archivo.write('\n')

#empleado avion
#normal_a_jason(lista_empleado,r'Jsons\empleado.json')
#normal_a_jason(lista_avion,r'Jsons\avion.json')


def json_a_normal(clase,nombre_archivo,atributo_fecha=None):
    lista_clase=[] #A esta lista normal le vamos agregando los objetos
    with open(nombre_archivo, 'r',encoding="utf-8") as archivo:
        data = json.load(archivo)
    for objeto in data:
        if atributo_fecha!=None:
            fecha = objeto[atributo_fecha]
            objeto[atributo_fecha]= datetime.date.fromisoformat(fecha)
        lista_clase.append(clase(**objeto))
    return lista_clase

def json_a_cola(clase,nombre_archivo):
    cola_clase=Cola()
    with open(nombre_archivo, 'r',encoding="utf-8") as archivo:
        data = json.load(archivo)
    for objeto in data:
        cola_clase.encolar(clase(**objeto))
    return cola_clase

#json_a_normal(Clases.empleado,r'Jsons\empleado.json')
#json_a_normal(Clases.avion,r'Jsons\avion.json') 
#PASARLE LA CLASE EN SI
    
def json_a_enlazada(clase,nombre_archivo,atributo_fecha=None,atributo_con_objeto=None,clase_nested_objeto=None,atributo_fecha_nested=None):
    lista_clase=Lista()
    with open(nombre_archivo, 'r',encoding="utf-8") as archivo:
        data = json.load(archivo)
    for objeto in data:
        
        """
        Si se proporcionó un atributo de fecha, obetenemos el valor de ese atributo del objeto JSON
        utilizando objeto[atributo_fecha]. 
        Luego, convierte ese valor en un objeto de fecha utilizando datetime.date.fromisoformat(fecha) 
        y lo actualiza en el objeto JSON.
        """
        if atributo_fecha!=None:
            fecha = objeto[atributo_fecha]
            objeto[atributo_fecha]= datetime.date.fromisoformat(fecha)
        
        """
        Verifica si se proporcionó un atributo con un objeto anidado (atributo_con_objeto) distinto de None.
        """
        if atributo_con_objeto !=None:
            #Obtenemos la lista de objetos anidados
            lista_objetos = objeto[atributo_con_objeto]
            for nested_objeto in lista_objetos:
                if atributo_fecha_nested!=None:
                    fecha = nested_objeto[atributo_fecha_nested]
                    nested_objeto[atributo_fecha_nested]= datetime.date.fromisoformat(fecha)
            """
            Ahora reemplazamos la lista de objetos anidados en el objeto JSON con una lista de instancias 
            de la clase anidada (clase_nested_objeto) creadas a partir de cada objeto anidado.  
            """
            objeto[atributo_con_objeto]= [clase_nested_objeto(**nested_objeto) for nested_objeto in lista_objetos]
        """
        Creamos una instancia de la clase principal (clase) a partir del objeto JSON
        y lo "envolvemos" en un nodo de la lista enlazada (Nodo(clase(**objeto))).
        """
        lista_clase.append(Nodo(clase(**objeto)))
    return lista_clase

#lista_persona.enlazada_a_jason(r'Jsons\persona.json',atributo_fecha='fecha_de_nacimiento')
#lista_vuelo.enlazada_a_jason(r'Jsons\vuelo.json')
#lista_viaje.enlazada_a_jason(r'Jsons\viaje.json',atributo_fecha='fecha',atributo_con_objeto='pasajeros',atributo_fecha_nested='fecha_de_nacimiento')
#lista_reserva.enlazada_a_jason(r'Jsons\reserva.json')
