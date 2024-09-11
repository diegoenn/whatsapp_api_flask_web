import psycopg2

#--- mostrar menu principal ------------------------------------------------------------------------
def menuprincipal():
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("Menu Principal:  x   x   x   x   x   x   x   x   x   x   x   x   x   x   x   x   x   x   ")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("este es un crud de base de datos")
    print("1.- consultar db")
    print("2.- agregar nuevo registro")
    print("3.- editar un registro de una db")
    print("4.- borrar un registro de una db")
    print("0.- salir")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    return()

#--- consultar todos los registros de una db --------------------------------------------------------
def consulta_usuarios():

    # sentencia sql
    sql= 'select * from users'

    # conexion a db
    try:
        connection=psycopg2.connect(
            host= "localhost",
            user= "postgres",
            password= "mondi",
            database= "postgres"
        )
        print("Conexion a db exitosa!!!!!")

        # utilizar cursor de la conexion a la base de datos
        cursor= connection.cursor()

        # ejecucion de consulta sql en db
        cursor.execute(sql)
        rows= cursor.fetchall()
        print(cursor.description)
        for row in rows:
            print(row)
        
        #cierre conexion a db
        cursor.close()
        connection.close()
        input("Presione cualquier tecla para continuar.......")
    # interrupcion en caso de error
    except Exception as ex:
        print ("error de conexion:", ex)

        #cierre conexion a db
        cursor.close()
        connection.close()
    return ()

#--- agregar un registro a db -------------------------------------------------------------------------
def agregar_usuario():

    # solicitud de datos al usuario
    id = input("Digite Id:")
    name = input("Digite Nombre:")
    email = input("Digite email:")
    phone = input("Digite phone:")

    # sentencia sql
    sql= 'insert into users (id, name, email, phone) values (%s,%s,%s,%s)'

    # recoleccion de datos
    datos=(id,name,email,phone)

    # conexion a db
    try:
        connection=psycopg2.connect(
            host= "localhost",
            user= "postgres",
            password= "mondi",
            database= "postgres"
        )
        print("Conexion a db exitosa")

        # utilizar cursor de la conexion a la base de datos
        cursor= connection.cursor()

        # ejecucion de consulta sql en db
        cursor.execute(sql,datos)

        # guardar registro
        connection.commit()
        
        # registros insertados
        registros= cursor.rowcount
        print(f'registro insertado: {registros}')

        # cierre de conexion a db
        cursor.close()
        connection.close()
        input("Presione cualquier tecla para continuar.......")
    # interrupcion en caso de error
    except Exception as ex:
        print ("error de conexion:", ex)

        # cierre de conexion a db
        cursor.close()
        connection.close()
    return ()

#--- editar un registro de una db ---------------------------------------------------------------------
def editar_usuario():

    # solicitud de datos al usuario
    id = input("Digite Id:")
    name = input("Digite Nombre:")
    email = input("Digite email:")
    phone = input("Digite phone:")

    # sentencia sql
    sql= 'update users set name=%s, email=%s, phone=%s where id = %s'

    # recoleccion de datos
    datos=(name,email,phone,id)

    # conexion a db
    try:
        connection=psycopg2.connect(
            host= "localhost",
            user= "postgres",
            password= "mondi",
            database= "postgres"
        )
        print("Conexion a db exitosa")

        # utilizar cursor de la conexion a la base de datos
        cursor= connection.cursor()

        # ejecucion de consulta sql en db
        cursor.execute(sql,datos)

        # guardar registro
        connection.commit()
        
        # registros insertados
        registros= cursor.rowcount
        print(f'registro actualizado: {registros}')

        # cierre de conexion a db
        cursor.close()
        connection.close()
        input("Presione cualquier tecla para continuar.......")
    # interrupcion en caso de error
    except Exception as ex:
        print ("error de conexion:", ex)

        # cierre de conexion a db
        cursor.close()
        connection.close()
    return()

#--- borrar un registro a db --------------------------------------------------------------------------
def borrar_usuario(id):

    # sentencia sql
    sql= 'delete from users where id = %s'

    # recoleccion de datos
    datos=(id)

    # conexion a db
    try:
        connection=psycopg2.connect(
            host= "localhost",
            user= "postgres",
            password= "mondi",
            database= "postgres"
        )
        print("Conexion a db exitosa")

        # utilizar cursor de la conexion a la base de datos
        cursor= connection.cursor()

        # ejecucion de consulta sql en db
        cursor.execute(sql,datos)

        # guardar registro
        connection.commit()
        
        # registros insertados
        registros= cursor.rowcount
        print(f'registro borrado: {registros}')

        # cierre de conexion a db
        cursor.close()
        connection.close()
        input("Presione cualquier tecla para continuar.......")
    # interrupcion en caso de error
    except Exception as ex:
        print ("error de conexion:", ex)

        # cierre de conexion a db
        cursor.close()
        connection.close()
    return ()

#--- Salir --------------------------------------------------------------------------------------------
def salir():
    print ("Gracias por su visita, Hasta pronto .........")
    return()

#--- opcion ingresada incorrecta --------------------------------------------------------------------------
def opcion_incorrecta():
    print ("opcion incorrecta, Intentelo nuevamente!!!!!!!")
    return ()
