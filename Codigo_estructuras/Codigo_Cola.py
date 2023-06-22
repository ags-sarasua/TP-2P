
class Cola:
    def __init__(self):
        self.lista=[]
        
    def __str__(self):
        return '\n'.join(str(avion) for avion in self.lista)
    
    def __iter__(self):
        return iter(self.lista)
    def encolar(self, avion):
        self.lista.append(avion)

    def primerObjeto(self):
        try:
            return self.lista[0]
        except:
            raise ValueError("La cola está vacía")

    def desencolar(self):
        try:
            self.lista.pop(0)
            print("El avion que estaba hace mas tiempo fue removido correctamente")
            return self.lista.pop(0)
        except:
            raise ValueError("No hay aviones en mantenimiento")


def menu_cola_avion(lista_avion,cola_mantenimiento):
    seleccion=input("1) Avión entre en mantemiento,         2) Sacar un avión de mantemiento: ")
    while (seleccion != "1" and seleccion !="2"):
        seleccion=input("Ingrese una selección válida: ")
    if seleccion=="1": 
        nro_serie=input("Ingrese el nro de serie del avión: ")
        Booleano=False
        for avion in lista_avion:
            if avion.nro_serie==nro_serie:
                cola_mantenimiento.encolar(avion)
                print("El avión fue agregado a estado de mantenimiento con éxito")
                print(cola_mantenimiento)
                Booleano=True
                break
        if Booleano!=True:
            print("No se encuentra el avión en la base de datos")
    if seleccion =="2":
        print('')
        print(cola_mantenimiento)
        print('')
        cola_mantenimiento.desencolar()
        print('')
        print(cola_mantenimiento)
    return None
            
            