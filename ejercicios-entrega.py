# El módulo json en Python proporciona una manera fácil y estandarizada de trabajar con datos en formato json.
# El módulo pandas es una herramienta poderosa para la manipulación y análisis de datos. Proporciona estructuras de datos y herramientas de análisis para manejar y manipular tablas numéricas y series de tiempo. 
import json
import pandas as pd

# Creamos la BBDD (consiste en un diccionario de diccionarios):
BBDD_actores = {}

## Definimos las funciones:
# Función de creación del menú de opciones (he implementado una séptima opción, eliminar un actor de la base de datos y una octava función, eliminar todos los datos de la base de datos):
def menu():
    print("Menu:")
    print("1. Introducir datos de un actor o actriz.")
    print("2. Listar todos los actores.")
    print("3. Mostrar los datos de un actor o actriz.")
    print("4. Buscar actores por rango de fecha de nacimiento.")
    print("5. Buscar actores por sexo.")
    print("6. Buscar actores por película.")
    print("7. Eliminar un actor de la base de datos.")
    print("8. Eliminar todos los datos de la base de datos.")
    print("0. Salir.")
    
    option = input("Selecciona una opción: ")
    
    return option

# 1.
# Función de introducción de datos de un nuevo actor o actriz:
def add_actor(BBDD_actores):
    # Pedimos el nombre del actor o actriz al usuario:
    name = input("Nombre del actor o actriz: ").title()
    
    # Pedimos el año de nacimiento del actor o actriz al usuario:
    # Creamos un bucle infinito ('while True') que se ejecutará hasta que introduzcamos un valor válido
    while True:
        # La instrucción try-except se utiliza para controlar las excepciones que pueden ocurrir al intentar convertir la entrada del usuario en un entero. Si la entrada es válida, se asigna a la variable birth_year y se rompe el ciclo..
        try:
            birth_year = int(input("Año de nacimiento: "))
            break
        # Si la entrada no es válida, se imprime un mensaje de error y se vuelve a pedir la entrada.
        except ValueError:
            print("Introduce un número entero válido.")

    # Pedimos el género del actor o actriz al usuario:
    # Creamos un bucle infinito ('while True') que se ejecutará hasta que introduzcamos un valor válido
    while True:
        gender = input("Sexo (Masculino o Femenino): ").title()
        # Se utiliza un conjunto {"Masculino", "Femenino"}, para comparar las entradas del usuario, el operador in es utilizado para comparar si la entrada del usuario es igual a alguno de los elementos del conjunto.
        if gender in ["Masculino", "Femenino"]:
            break
        # De esta manera, el ciclo se repetirá hasta que el usuario introduzca un valor válido.
        else:
            print("Introduce una opción válida (Masculino o femenino)")

    # Pedimos las películas en las que ha participado el actor o actriz al usuario:
    films = input("Nombre de las películas (separadas por comas y sin espacios): ").split(",")
    
    # Guardamos todos los datos obtenidos:
    BBDD_actores[name] = {
        "Año de nacimiento": birth_year, 
        "Género": gender, 
        "Películas": films
    }

# Función de actualización de datos de un actor o actriz, sobreescribiendo:
def update_actor(BBDD_actores):
    # Pedimos el nombre del actor o actriz al usuario:
    name = input("Nombre del actor o actriz: ").title()
    
    # Si el nombre que nos ha facilitado el usuario se encuentra en nuestra BBDD procedemos a sobreescribirlo:
    if name in BBDD_actores:
        while True:
            try:
                # Pedimos el año de nacimiento del actor o actriz al usuario:
                birth_year = int(input("Año de nacimiento: "))
                break
            except ValueError:
                print("Introduce un número entero válido.")

        while True:
            # Pedimos el género del actor o actriz al usuario:
            gender = input("Sexo (Masculino o Femenino): ").title()
            
            if gender in ["Masculino", "Femenino"]:
                break
            else:
                print("Introduce una opción válida (Masculino o femenino)")
        
        # Pedimos las películas en las que ha participado el actor o actriz al usuario:
        films = input("Nombre de las películas (separadas por comas y sin espacios): ").split(",")
        
        # Guardamos todos los nuevos datos obtenidos:
        BBDD_actores[name] = {
            "Año de nacimiento": birth_year, 
            "Género": gender, 
            "Películas": films
        }
    else:
        print("Actor o actriz no encontrado.")

# 2.
# Función para listar el nombre de los actores que se encuentran en la BBDD:
def list_actors(BBDD_actores):
    # Creamos una lista vacía donde vamos a ir almacenando los nombres de los actores o actrices para posteriormente listarlos
    names = []
    
    # Con el bucle for vamos a recorrer cada uno de los actores o actrices que se encuentran en nuestra BBDD
    for name in BBDD_actores:
        # Cada uno de los nombres de los actores o actrices de la BBDD se van a almacenar en la lista vacía 'names'
        names.append(name)
    # Gracias a la librería pandas creamos un DataFrame y nos simplifica mucho la visualización de los datos
    # El código 'if names' nos verifica si la variable 'names' no está vacía
    if names:
        # Creamos un DF utilizando la variable "names" como los datos, y el nombre de la columna se establece en "Nombre" utilizando el parámetro columns en la función pd.DataFrame().
        df = pd.DataFrame(names, columns = ["Nombre"])
        print(df)
    else:
        print("No hay datos en la base de datos.")

# 3.
# Función para mostrar los datos de un determinado actor o actriz:
def get_actor(BBDD_actores):
    name = input("Nombre del actor o actriz: ").title()
    
    # Si el nombre que nos ha facilitado el usuario se encuentra en nuestra BBDD procedemos a mostrar por pantalla todos sus datos
    if name in BBDD_actores:
        actor = BBDD_actores[name]
        data = {'Año de nacimiento': [actor['Año de nacimiento']],
                'Género': [actor['Género']],
                'Películas': [actor['Películas']]}
        
        # Creamos un DF utilizando la variable 'data' como los datos
        df = pd.DataFrame(data)
        print(df)
        
    else:
        print("Actor o actriz no encontrado.")

# 4.
# Función para buscar aquellos actores cuyo año de nacimiento se encuentre en un determinado rango de años:
def search_by_birth_year_range(BBDD_actores):
    # Pedimos al usuario un año de inicio de la búsqueda:
    # Creamos un bucle infinito ('while True') que se ejecutará hasta que introduzcamos un valor válido
    while True:
        try:
            start = int(input("Año de inicio: "))
            break
        except ValueError:
            print("Introduce un número entero válido.")
    
    # Pedimos el año de nacimiento del actor o actriz al usuario:
    # Creamos un bucle infinito ('while True') que se ejecutará hasta que introduzcamos un valor válido
    while True:
        try:
            end = int(input("Año de fin: "))
            break
        except ValueError:
            print("Introduce un número entero válido.")
    
    # Creamos una lista vacía donde vamos a ir almacenando los nombres de los actores o actrices para posteriormente listarlos
    names = []
    
    # Con el bucle for vamos a recorrer cada uno de los actores o actrices que se encuentran en nuestra BBDD
    for name in BBDD_actores:
        # Si el año de nacimiento del actor o actriz en cuestión se encuentra entre los años introducios por el usuario...
        if start <= BBDD_actores[name]["Año de nacimiento"] <= end:
            # Añadimos a ese actor o actriz a la lista vacía
            names.append(name)
    
    # Gracias a la librería pandas creamos un DataFrame y nos simplifica mucho la visualización de los datos
    # El código 'if names' nos verifica si la variable 'names' no está vacía
    if names:
        # Creamos un DF utilizando la variable "names" como los datos, y el nombre de la columna se establece en "Nombre" utilizando el parámetro columns en la función pd.DataFrame().
        df = pd.DataFrame(names, columns = ["Nombre"])
        print(df)
    else:
        print("No se encontraron actores en ese rango de fechas.")


# 5.
# Función para buscar aquellos actores de un sexo determinado:
def search_by_gender(BBDD_actores):
    gender = input("Sexo (Masculino o Femenino): ").title()
    
    # Creamos una lista vacía donde vamos a ir almacenando los nombres de los actores o actrices para posteriormente listarlos
    names = []
    
    # Con el bucle for vamos a recorrer cada uno de los actores o actrices que se encuentran en nuestra BBDD
    for name in BBDD_actores:
        # Si la variable 'Género' de nuestra BBDD coincide con el género introducido por el usuario...
        if BBDD_actores[name]["Género"] == gender:
            # Añadimos a ese actor(es) o actriz(ces) a la lista vacía
            names.append(name)
    
    # Gracias a la librería pandas creamos un DataFrame y nos simplifica mucho la visualización de los datos
    # El código 'if names' nos verifica si la variable 'names' no está vacía
    if names:
        # Creamos un DF utilizando la variable "names" como los datos, y el nombre de la columna se establece en "Nombre" utilizando el parámetro columns en la función pd.DataFrame().
        df = pd.DataFrame(names, columns=["Nombre"])
        print(df)
    else:
        print("No se encontraron actores con ese género.")

# 6.
# Función para buscar aquellos actores que hayan participado en una película:
def search_by_film(BBDD_actores):
    film = input("Película: ")
    
    # Creamos una lista vacía donde vamos a ir almacenando los nombres de los actores o actrices para posteriormente listarlos
    names = []
    
    # Con el bucle for vamos a recorrer cada uno de los actores o actrices que se encuentran en nuestra BBDD
    for name in BBDD_actores:
        # Si la variable 'Películas' de nuestra BBDD coincide con la película introducido por el usuario...
        if film in BBDD_actores[name]["Películas"]:
            # Añadimos a ese actor(es) o actriz(ces) a la lista vacía
            names.append(name)
    
    # Gracias a la librería pandas creamos un DataFrame y nos simplifica mucho la visualización de los datos
    # El código 'if names' nos verifica si la variable 'names' no está vacía   
    if names:
        # Creamos un DF utilizando la variable "names" como los datos, y el nombre de la columna se establece en "Nombre" utilizando el parámetro columns en la función pd.DataFrame().
        df = pd.DataFrame(names, columns=["Nombre"])
        print(df)
    else:
        print("No se encontraron actores en esa película.")
           
# 7.
# Función para borrar los datos de un actor o actriz de la BBDD:
def delete_actor(BBDD_actores):
    name = input("Nombre del actor o actriz: ").title()
    
    # El código 'if name' nos verifica si un nombre específico ('name') existe en el diccionario BBDD_actores
    if name in BBDD_actores:
        # La función 'del' es utilizada para eliminar una entrada en un diccionario
        del BBDD_actores[name]
    else:
        print("Actor o actriz no encontrado.")
        
# 8.
# Función para borrar todos los datos de la BBDD:
def delete_BBDD(BBDD_actores):
    confirm = input("¿Está seguro de que quiere borrar todos los datos de la base de datos? (Si/No)").title()
    
    # Si la respuesta del usuario es Si...
    if confirm == "Si":
        # Se utiliza el método clear() para eliminar todas las entradas de un diccionario
        BBDD_actores.clear()
        print("Se han borrado todos los datos de la base de datos.")
    else:
        print("Proceso cancelado.")

#La función load_data() se encarga de cargar el archivo actores.txt al iniciar el programa y en caso de no existir el archivo, se asigna un diccionario vacio.
def load_data():
    try:
        with open('actores.txt') as json_file:
            BBDD_actores = json.load(json_file)
    except:
        BBDD_actores = {}
    return BBDD_actores

#La función save_data() se encarga de guardar la información en el archivo actores.txt cada vez que se sale del programa.
def save_data():
    # La función utiliza la sentencia with open para abrir el archivo "actores.txt" en modo escritura ('w') y con la codificación "utf-8". El parámetro "encoding = 'utf-8'" permite guardar caracteres especiales en el archivo de texto
    with open('actores.txt', 'w', encoding = 'utf-8') as json_file:
        # La función json.dump() se utiliza para escribir el contenido del diccionario "BBDD_actores" en el archivo de texto. El primer parámetro es el diccionario "BBDD_actores", el segundo parámetro es el archivo abierto "json_file" donde se guardará la información.
        # El parámetro indent = 4 indica que se deben utilizar 4 espacios para el sangrado en el archivo de texto. El parámetro ensure_ascii = False indica que se deben guardar los caracteres especiales tal cual son en el archivo de texto.
        json.dump(BBDD_actores, json_file, indent = 4, ensure_ascii = False)

# Asignamos el valor devuelto por la función 'load data()' a la variable 'BBDD_actores'
BBDD_actores = load_data()

while True:
    option = menu()
    if option == "0":
        save_data()
        print("Guardando datos en la BBDD y cerrando el programa...")
        break
        
    elif option == "1":
        add_actor(BBDD_actores)
        
    elif option == "2":
        list_actors(BBDD_actores)
        
    elif option == "3":
        get_actor(BBDD_actores)
        
    elif option == "4":
        search_by_birth_year_range(BBDD_actores)
        
    elif option == "5":
        search_by_gender(BBDD_actores)
        
    elif option == "6":
        search_by_film(BBDD_actores)
    
    elif option == "7":
        delete_actor(BBDD_actores)
        
    elif option == "8":
        delete_BBDD(BBDD_actores)
        
    else:
        print("Opción no válida.")
