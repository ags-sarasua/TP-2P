
import matplotlib.pyplot as mlp

def menu_graficar_empleado(lista_empleado):
    print('1)Cupo de genero   2)Distribuicion de roles')
    eleccion_grafico=input('Ingrese su eleccion: ')
    if eleccion_grafico=='1':
        hombre=0
        mujer=0
        otro=0
        for instancia in lista_empleado:
            if instancia.sexo=='Masculino':hombre+=1
            elif instancia.sexo=='Femenino': mujer+=1
            elif instancia.sexo=='Otro':otro+=1
        lista_cantidad=[hombre,mujer,otro]
        lista_sexos=['Masculino','Femenino','Otro']
        lista_colores=['#00CC99','#DA70D6','Grey']
        mlp.bar(lista_sexos,lista_cantidad,color=lista_colores)
        mlp.title("Cupo de genero")
        mlp.xlabel("Generos")
        mlp.ylabel("Cantidad")
        mlp.show()

    if eleccion_grafico=='2':
        piloto=0
        tecnico=0
        administrativo=0
        for instancia in lista_empleado:
            if instancia.sector=='Administrativo':administrativo+=1
            elif instancia.sector=='Tecnico': tecnico+=1
            elif instancia.sector=='Piloto':piloto+=1
        lista_cantidad=[administrativo,tecnico,piloto]
        lista_roles=['Administrativo','Tecnico','Piloto']
        mlp.bar(lista_roles,lista_cantidad, color="#FF69B4",width=0.5)
        mlp.title("Distribuccion de roles")
        mlp.xlabel("Roles")
        mlp.ylabel("Cantidad")
        mlp.show()