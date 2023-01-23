# Ejercicio entrega.

Realizar cada uno de los ejercicios utilizando este notebook como plantilla:

## Ejercicio 1 (7 puntos)

Queremos almacenar los datos de nuestros actores favoritos en una base de datos (BBDD), pero no nos gusta ninguna de las disponibles, por lo tanto vamos a construirla nosotros mismos.


La BBDD será un diccionario de diccionarios. Para el primer diccionario la clave será el nombre del actor. El segundo diccionario (el que estaría dentro del primer diccionario) consta de 3 campos: año de nacimiento, sexo y una lista con el nombre de las películas en las que ha participado.


El programa nos permitirá hacer una serie de cosas, elegidas por un menú:

1. Introducir los datos de un nuevo actor o actriz (el número de películas puede variar de un actor a otro) (si el actor ya existía en la BBDD se sobreescribirán los datos).
2. Listar todos los actores mostrando únicamente sus nombres (con cierto formato).
3. Mostrar los datos de un determinado actor o actriz (con cierto formato).
4. Buscar aquellos actores cuyo año de nacimiento se encuentre en un determinado rango de años (que se le pedirá al usuario).
5. Buscar aquellos actores de un sexo determinado.
6. Buscar aquellos actores que hayan participado en una película.
0. Salir del programa.


## Ejercicio 2 (1 punto)

Repetir el ejercicio anterior pero utilizando funciones. Como mínimo debe crearse una función para mostrar el menú y recoger la opción elegida por el usuario, y una función por cada opción que encapsule las acciones que se realizan en cada opción en particular (como parámetros, deben recibir al menos la BBDD). Adicionalmente, se pueden crear funciones para mostrar por pantalla la BBDD o parte de ella con cierto formato.


## Ejercicio 3 (2 puntos)

Para no perder los datos que el usuario va introduciendo vamos a almacenar la BBDD en un fichero llamado 'actores.txt'. De esta forma, cada vez que se ejecute el programa deberán recuperarse los datos almacenados previamente y al salir del programa debe escribirse la información de la BBDD en fichero.
