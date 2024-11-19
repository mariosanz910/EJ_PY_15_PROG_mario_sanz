import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",       
    user="root",            
    password="1234", 
    database="empresa"
)

# Función para insertar un nuevo departamento
def crear():
    cursor = conexion.cursor()
    nombre = input("Introduce el nombre del nuevo departamento: ")  # El usuario ingresa el nombre
    # Consulta para insertar un nuevo departamento
    consulta = "INSERT INTO departamento (nombredep) VALUES (%s)"
    cursor.execute(consulta, (nombre,))  # Inserta el nombre proporcionado por el usuario
    conexion.commit()  # Confirmar los cambios
    print(f"Departamento '{nombre}' agregado exitosamente.")
    cursor.close()

# Función para ver todos los departamentos
def ver():
    cursor = conexion.cursor()
    # Consulta para obtener todos los departamentos
    consulta = "SELECT * FROM departamento"
    cursor.execute(consulta)
    departamentos = cursor.fetchall()  # Obtiene todos los resultados de la consulta
    
    if departamentos:
        print("=== Departamentos ===")
        for depto in departamentos:
            print(f"Código: {depto[0]}, Nombre: {depto[1]}")
    else:
        print("No hay departamentos registrados.")
    
    cursor.close()

# Función para actualizar el nombre de un departamento
def actualizar():
    cursor = conexion.cursor()
    codigo = input("Introduce el código del departamento a actualizar: ")
    nuevo_nombre = input("Introduce el nuevo nombre para el departamento: ")
    
    # Consulta para actualizar el nombre del departamento
    consulta = "UPDATE departamento SET nombredep = %s WHERE numdep = %s"
    cursor.execute(consulta, (nuevo_nombre, codigo))  # Ejecuta la consulta
    conexion.commit()  # Confirmar los cambios
    cursor.close()

# Función para eliminar un departamento
def eliminar():
    cursor = conexion.cursor()
    codigo = input("Introduce el código del departamento a eliminar: ")
    
    # Consulta para eliminar el departamento
    consulta = "DELETE FROM departamento WHERE numdep = %s"
    cursor.execute(consulta, (codigo,))    
    conexion.commit()  # Confirmar los cambios
    cursor.close()


# Función del menú principal
def menu_principal():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Opción 1: Crear departamento")
        print("2. Opción 2: Ver departamentos")
        print("3. Opción 3: Actualizar departamentos")
        print("4. Opción 4: Eliminar departamentos")
        print("5. Opción 5: Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear()
        elif opcion == "2":
            ver()
        elif opcion == "3":
            actualizar()
        elif opcion == "4":
            eliminar()
        elif opcion == "5":
            print("Gracias por usar el programa. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Llamar al menú principal
menu_principal()

# Cerrar la conexión después de que termine el programa
conexion.close()
