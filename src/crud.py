import sqlite3

def crear_conexion():
    try:
        conexion = sqlite3.connect("src/database/perifericos.db")
        return conexion
    except Exception as ex:
        print(f"Error al conectar: {ex}")
        return None


def agregar_periferico(conexion, nombre, tipo, precio, stock):
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO perifericos (nombre, tipo, precio, stock) VALUES (?, ?, ?, ?)", 
                       (nombre, tipo, precio, stock))
        conexion.commit()
        print("Periférico agregado correctamente.")
    except Exception as ex:
        print(f"Error al agregar periférico: {ex}")


def mostrar_perifericos(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM perifericos")
        perifericos = cursor.fetchall()
        print("Listado de productos:")
        for p in perifericos:
            print(f"ID: {p[0]}, Nombre: {p[1]}, Tipo: {p[2]}, Precio: ${p[3]}, Stock: {p[4]}")
    except Exception as ex:
        print(f"Error al mostrar periféricos: {ex}")


def actualizar_stock(conexion, id_periferico, nuevo_stock):
    try:
        cursor = conexion.cursor()
        cursor.execute("UPDATE perifericos SET stock = ? WHERE id = ?", (nuevo_stock, id_periferico))
        conexion.commit()
        print("Stock actualizado correctamente.")
    except Exception as ex:
        print(f"Error al actualizar el stock: {ex}")


def eliminar_periferico(conexion, id_periferico):
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM perifericos WHERE id = ?", (id_periferico,))
        conexion.commit()
        print("Periférico eliminado correctamente.")
    except Exception as ex:
        print(f"Error al eliminar periférico: {ex}")
        
        
def alerta_bajo_stock(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM perifericos WHERE stock <= 2")
        productos_bajo_stock = cursor.fetchall()
        
        if productos_bajo_stock:
            print("Productos con bajo stock( dos o menos)")
            for p in productos_bajo_stock:
              print(f"ID: {p[0]}, Nombre: {p[1]}, Tipo: {p[2]}, Precio: ${p[3]}, Stock: {p[4]}")
              
        else:
             print("No hay prodcutos con bajo stock")
             
    except Exception as ex:
        print(f"Error al buscar productos con bajo stock: {ex}")
        
def buscar_periferico(conexion, id_periferico):
    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM perifericos WHERE id = ?"
        cursor.execute(consulta, (id_periferico,))
        resultado = cursor.fetchone()
         
            
        if resultado:
             print("Perifericos encontrado: ") 
             print(f"ID: {resultado[0]}, Nombre: {resultado[1]}, Tipo: {resultado[2]}, Precio: ${resultado[3]}, Stock: {resultado[4]}")
        else:
            print("No se encontró ningun id con ese resultado")            
    except Exception as ex:
        print(f"Error al buscar perifericos por ID: {ex}")
                                      


def menu_principal():
    conexion = crear_conexion()
    if not conexion:
        print("No se pudo establecer conexión con la base de datos.")
        return

    while True:
        print("================== MENÚ PRINCIPAL ==================")
        print("1. Mostrar periféricos")
        print("2. Agregar periférico")
        print("3. Actualizar stock")
        print("4. Eliminar periférico")
        print("5. Reporte de bajo stock")
        print("6. Busqueda por ID: ")
        print("7. Salir")
        print("==================== © 2024 VCZ ====================")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_perifericos(conexion)
        elif opcion == "2":
            nombre = input("Nombre del periférico: ")
            tipo = input("Tipo del periférico: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))
            agregar_periferico(conexion, nombre, tipo, precio, stock)
        elif opcion == "3":
            id_periferico = int(input("ID del periférico a actualizar: "))
            nuevo_stock = int(input("Nuevo stock: "))
            actualizar_stock(conexion, id_periferico, nuevo_stock)
        elif opcion == "4":
            id_periferico = int(input("ID del periférico a eliminar: "))
            eliminar_periferico(conexion, id_periferico)
        elif opcion == "5":
            alerta_bajo_stock(conexion)
        elif opcion == "6":
            id_periferico = int(input("Ingrese el ID de su periferico: "))
            buscar_periferico(conexion, id_periferico)        
        elif opcion == "7":
            print("¡Gracias por usar este programa!")
            conexion.close()
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar el programa
menu_principal()
