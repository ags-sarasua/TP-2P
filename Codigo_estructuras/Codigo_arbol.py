from Clases import *

class NodoarbolVuelo:
    #constructor
    def __init__(self,dato=None):
        self.dato=dato
        self.derecha=None
        self.izquierda=None

    def agregarnodos(raiz,nodo):
        if raiz.dato<nodo.dato:
            if raiz.derecha==None:
                raiz.derecha=nodo
            else:
                 raiz.derecha.agregarnodos(nodo)
        elif raiz.dato>nodo.dato:
            if raiz.izquierda==None:
                raiz.izquierda=nodo
            else:
                raiz.izquierda.agregarnodos(nodo)

class Nodo_arbol:

    #constructor
    def __init__(self,valor=None):
        self.valor=valor
        self.derecha=None
        self.izquierda=None

class arbol():
    def __init__(self,nodo=None):
        self.raiz=nodo

    def insertar(self,valor):
        if self.raiz is None:
            self.raiz = Nodo_arbol(valor)
        else:
            self.insertar_ordenado(valor,self.raiz)
    
    def insertar_ordenado(self,valor,nodo_actual):
        if valor.nro_vuelo < nodo_actual.valor.nro_vuelo:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo_arbol(valor)
            else:
                self.insertar_ordenado(valor, nodo_actual.izquierda)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo_arbol(valor)
            else:
                self.insertar_ordenado(valor, nodo_actual.derecha)
    
    def buscar(self, dato):
        return self.buscar_recursivo(dato, self.raiz)
    
    def buscar_recursivo(self, dato, nodo_actual):
        if nodo_actual is None or nodo_actual.valor.nro_vuelo == dato:
            return nodo_actual
        
        if dato < nodo_actual.valor.nro_vuelo:
            return self.buscar_recursivo(dato, nodo_actual.izquierda)
        else:
            return self.buscar_recursivo(dato, nodo_actual.derecha)

    def preorden(self):
        self.preorden_recursivo(self.raiz)
    
    def preorden_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            print(nodo_actual.valor, end="\n")
            #Primero buscamos siempre a la izquierda
            self.preorden_recursivo(nodo_actual.izquierda)
            #Luego de ir todo a la izquierda, vamos a la derecha
            self.preorden_recursivo(nodo_actual.derecha)

    def postorden(self):
        self.postorden_recusivo(self.raiz)
    
    def postorden_recusivo(self, nodo_actual):
        if nodo_actual is not None:
            self.postorden_recusivo(nodo_actual.izquierda)
            self.postorden_recusivo(nodo_actual.derecha)
            print(nodo_actual.valor, end=" ")

    def cargar_estructura(self, nombre_archivo):
        # Carga la estructura del árbol desde un archivo de texto
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()

            for linea in lineas:
                datos = linea.strip().split(",")

                nro_vuelo = datos[0].split(":")[1].strip()
                origen = datos[1].split(":")[1].strip()
                destino = datos[2].split(":")[1].strip()
                legajo_piloto = datos[3].split(":")[1].strip()
                precio = datos[4].split(":")[1].strip()
                
                #Creamos una nueva instancia una vez tenemos separados todos los atributos
                vuelo_a_insertar = vuelo(nro_vuelo, origen, destino, legajo_piloto, precio)

                self.insertar(vuelo_a_insertar)

    def guardar_estructura(self, nombre_archivo):
        #guarda el árbol en un archivo de texto
        with open(nombre_archivo, "w") as archivo:
            self.guardar_estructura_recursivo(self.raiz, archivo)
    
    def guardar_estructura_recursivo(self, nodo, archivo):
        #Método auxiliar para guardar la estructura el árbol en un archivo
        if nodo is None:
            return
        
        #Guardar la información del nodo en el archivo
        archivo.write(f'{nodo.valor}\n')

        #Llamada recursiva a los nodos izquierda y derecha
        self.guardar_estructura_recursivo(nodo.izquierda, archivo)
        self.guardar_estructura_recursivo(nodo.derecha, archivo)

    #Eliminar toma un valor como parámetro y verifica si existe un nodo con ese valor en el árbol. Si no se encuentra el valor, devuelve False.
    def eliminar(self, valor):
        if self.buscar(valor) is None:
            return False
        self.raiz = self.eliminar_recursivo(valor, self.raiz)
        return True
        
    def eliminar_recursivo(self, valor, nodo_actual):
        if nodo_actual is None:
            return nodo_actual #Esto si no encuentra nada
        
        #Vemos si vamos a buscar a la izquierda o a la derecha 
        if valor < nodo_actual.valor.nro_vuelo:
            nodo_actual.izquierda = self.eliminar_recursivo(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor.nro_vuelo:
            nodo_actual.derecha = self.eliminar_recursivo(valor, nodo_actual.derecha)
        else:
            if nodo_actual.izquierda is None:
                return nodo_actual.derecha
            elif nodo_actual.derecha is None:
                return nodo_actual.izquierda
            else:
                nodo_actual.valor = self.obtener_minimo_valor(nodo_actual.derecha)
                nodo_actual.derecha = self.eliminar_recursivo(nodo_actual.valor.nro_vuelo, nodo_actual.derecha)
        """
        Si el valor es igual a nodo_actual.valor.nro_vuelo, se ha encontrado el nodo que se desea eliminar.
            Si el nodo actual no tiene un hijo izquierdo, se asigna el hijo derecho como el nuevo nodo_actual y se devuelve.
            Si el nodo actual no tiene un hijo derecho, se asigna el hijo izquierdo como el nuevo nodo_actual y se devuelve.
            Si el nodo actual tiene 2 hijos, se busca el valor mínimo en el subárbol derecho (el sucesor inmediato del nodo actual). Lugo, se asigna ese valor al nodo actual y se llama a eliminar_recursivo para eliminar el valor mínimo del subárbol derecho.
        """

        return nodo_actual #Ya actualizado   

    def obtener_minimo_valor(self, nodo_actual):
            while nodo_actual.izquierda is not None:
                nodo_actual = nodo_actual.izquierda
            return nodo_actual.valor