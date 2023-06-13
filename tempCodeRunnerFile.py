for nested_objeto in lista_objetos:
                if atributo_fecha_nested!=None:
                    fecha = nested_objeto[atributo_fecha_nested]
                    nested_objeto[atributo_fecha_nested]= datetime.date.fromisoformat(fecha)
            objeto[atributo_con_objeto]= [clase_nested_objeto(**nested_objeto)]