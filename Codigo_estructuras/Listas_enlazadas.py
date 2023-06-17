import json



class Nodo():
    def __init__(self,dato=None,prox=None):
        self.dato=dato
        self.prox=prox
    def __str__(self) -> str:
        return self.dato.__str__() # Especificas como queres que se printee
    
class Lista():
    def __init__(self):
        self.head=None
        self.len=0
    def __str__(self):
        nodo = Nodo()
        nodo=self.head
        lista = []
        while nodo is not None:
            lista.append(str(nodo.dato))
            nodo = nodo.prox
        return "\n".join(lista)
    
    def append(self,nodo:Nodo):
        if(self.len==0):
            self.head=nodo
        else:
            nodomov=Nodo()
            nodomov=self.head
            while(nodomov.prox!=None):
                nodomov=nodomov.prox
            nodomov.prox=nodo   #muy bueno
        self.len+=1
        
    def pop(self,input_principal,atributo_principal):  #INPUT PRINCIPAL: VARIABLE QUE INGRESA EL USUARIO   ATRIBUTO_PRINCIPAL "DNI"
        nodo=Nodo()
        nodo=self.head
        for i in range(self.len-1):
            if i==0 and getattr(nodo.dato,atributo_principal)==input_principal:
                self.head=nodo.prox
                self.len-=1
                return True
            elif getattr(nodo.prox.dato,atributo_principal)==input_principal:
                nodo.prox=nodo.prox.prox
                self.len-=1
                return True
            nodo=nodo.prox
        return False
    
    def buscar_inst(self,input_principal, atributo_principal):
        nodo=Nodo()
        nodo=self.head
        for i in range(self.len):
            if getattr(nodo.dato,atributo_principal)==input_principal:
                return nodo.dato
            nodo=nodo.prox
        return False

    def buscar_attr(self,input_principal, atributo_principal,atributo_a_buscar):
        dato = self.buscar_inst(input_principal, atributo_principal)
        if dato:
            return getattr(dato,atributo_a_buscar)
        return False 
        


    def actualizar_le(self,input_principal, atributo_principal,atributo_a_buscar,nuevo_input):
        nodo=Nodo()
        nodo=self.head
        for i in range(self.len):
            
            if getattr(nodo.dato,atributo_principal)==input_principal:
                setattr(nodo.dato, atributo_a_buscar,nuevo_input)
        
                return True
            nodo=nodo.prox
        
        return False

    def enlazada_a_jason(self, nombre_archivo,atributo_fecha=None,atributo_con_objeto=None,atributo_fecha_nested=None):
        lista_diccionarios=[]
        self.guardar_lista_recursivo(self.head,nombre_archivo,lista_diccionarios,atributo_fecha,atributo_con_objeto,atributo_fecha_nested)
        with open(nombre_archivo, "w",encoding="utf-8") as archivo:
            json.dump(lista_diccionarios,archivo,indent=2,ensure_ascii=False)
    
    def guardar_lista_recursivo(self, nodo, nombre_archivo,lista_diccionarios,atributo_fecha,atributo_con_objeto,atributo_fecha_nested):
        if nodo is None:
            return
        #Chequeos
        if atributo_fecha!=None:
            fecha = getattr(nodo.dato, atributo_fecha)
            setattr(nodo.dato, atributo_fecha, fecha.isoformat())
            
        if atributo_con_objeto !=None:
            lista_objetos = getattr(nodo.dato, atributo_con_objeto)
            for nested_objeto in lista_objetos:
                if atributo_fecha_nested!=None:
                    fecha = getattr(nested_objeto, atributo_fecha_nested)
                    setattr(nested_objeto, atributo_fecha_nested, fecha.isoformat())
            setattr(nodo.dato, atributo_con_objeto, [nested_objeto.__dict__ for nested_objeto in lista_objetos])
        lista_diccionarios.append(nodo.dato.__dict__)
        #Llamada recursiva a los nodos proximos
        self.guardar_lista_recursivo(nodo.prox, nombre_archivo,lista_diccionarios,atributo_fecha,atributo_con_objeto,atributo_fecha_nested)
        return
