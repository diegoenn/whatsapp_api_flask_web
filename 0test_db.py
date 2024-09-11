#--- funciones para un crud con una base de datos------
#--- configuracion general para conexion a db

import conexion

#--- menu principal
opcion = 5
while opcion != 0:
    #--- importa funcion menu principal para imprimir las opciones del menu principal
    conexion.menuprincipal()

    opcion= int(input("seleccione opcion:"))
    
    #--- validar opcion
    if opcion == 1:
        conexion.consulta_usuarios()
    elif opcion == 2:
        conexion.agregar_usuario()
    elif opcion == 3:
        conexion.editar_usuario()
    elif opcion == 4:
        id_usuario = input("Digite Id usuario a eliminar:")
        conexion.borrar_usuario(id_usuario)
    elif opcion == 0:
        conexion.salir()
    else:
        conexion.opcion_incorrecta()
    