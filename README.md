Proyecto Semestral, Algoritmos II
Título: Seguimiento de navegación.

(equipos de 2 estudiantes solamente)
Objetivos Generales

Desarrollar una aplicación para seguir la navegación de una flota naviera en diferentes instancias de tiempo
Desarrollar mecanismos eficientes de consultas sobre los elementos que componen la flota.

Introducción

Una flota naviera está compuesta por varias embarcaciones. Cada mes se recibe un informe de configuración (posición en el plano) de los barcos que conforman la flota. Dicho informe contiene dos componentes fundamentales: 
<fecha>  
<información sobre los barcos>

La <información sobre los barcos> indica por cada embarcación 4 elementos fundamentales:
Nombre de Embarcación
Posición en X
Posición en Y
Dirección

A continuación se describen cada uno de los elementos.

Nombre de Embarcación: String que representa el nombre por el cual se le conoce a la embarcación. Este String funciona como un identificador de cada barco ya que es único en  toda la flota.

Posición en X: Como su nombre lo indica representa la posición en X de la embarcación expresado sobre un eje cartesiano.

Posición en Y: Al igual que el elemento anterior representa la posición en el eje Y de la embarcación.

Dirección: String que indica la dirección que sigue la embarcación. Los posibles valores para una dirección son los siguientes: ‘N’ indica que la embarcación se mueve desde su posición actual hacia el norte, ‘S’ indica que la embarcación se mueve desde su posición actual hacia el sur, ‘E’ indica que la embarcación se mueve desde su posición actual hacia el este, ‘W’ indica que la embarcación se mueve desde su posición actual hacia el oeste, ‘NE’ indica que la embarcación se mueve desde su posición actual hacia el noreste, ‘NW’ indica que la embarcación se mueve desde su posición actual hacia el noroeste, ‘SE’ indica que la embarcación se mueve desde su posición actual hacia el sureste, ‘SW’ indica que la embarcación se mueve desde su posición actual hacia el suroeste. Teniendo en cuenta que cada día que pasa del mes cada embarcación se mueve una distancia 1 desde su posición hacia donde indica su dirección, la Figura 1. muestra cada una de las posibles direcciones y ubicaciones al pasar de los días. 

Indicaciones

Si dada la configuración inicial de la flota se sabe que cada día que pasa un barco avanza un valor en su posición de acuerdo a la dirección que lleva. Implementar las siguientes funcionalidades: 

Conocer, dado un día (dentro del mes), que posición tiene un barco en particular. 
Conocer, dado un día (dentro del mes), cuales son los dos barcos más cercanos entre sí (distancia euclidiana). Si hay más de un barco con la misma distancia indicar cada uno de estos.
Conocer si dentro del mes existe un día de riesgo de colisión (dos o más barcos a distancia 1). Indicar la fecha y el nombre de los barcos involucrados en él o los riesgos de colisión.
(Opcional) Brindar la funcionalidad de dado un día del mes mostrar un ranking de los 10 barcos más cercanos entre sí.

Figura 1: Movimientos de la flota en el plano. El barco B4 y B5 presentan riesgo de colisión en el día 1.

Requerimientos

Lograr el cumplimiento de los objetivos a través de una aplicación (script) utilizando el lenguaje de programación python3.
A través de la aplicación desarrollada, permitir la navegación de los elementos que componen la flota.
Para lograr la navegación de los elementos es necesario la creación de la flota y para ello se utilizará el siguiente comando: python sistema_navegacion.py -create <local_path>
Una vez cargados los elementos que componen la flota en la aplicación, permitir realizar consultas sobre las embarcaciones y su interacción entre sí.
Para la generación de consultas se utilizará el siguiente comando: 
python navigation_system.py -search <date> <nombre_embarcacion>
Devuelve la posición (X, Y) dado una fecha (<date>) y un nombre de embarcación (<nombre_embarcacion>)
python navigation_system.py -closer <date>
Devuelve el nombre de las dos embarcaciones más cercanas entre sí (menor distancia euclidiana). 
python navigation_system.py -collision
Devuelve el día del mes (date) y los barcos que están involucrados en un riesgo de colisión. En caso que no exista ningún riesgo de colisión en el mes se devuelve False
python navigation_system.py -collision_ranking <date>
Devuelve un ranking (10) de las embarcaciones más cercanas entre sí.
Para el desarrollo de la aplicación solamente queda permitido el uso de algunas bibliotecas y funciones, las cuales se detallan en el canal de slack #proyecto de la materia, y en las diapositivas que explican la lectura y escritura de datos en disco. El resto de las estructuras utilizadas deben ser exclusivamente implementadas por el equipo de trabajo.
Garantizar la persistencia de los datos. Esto significa que la estructura que compone el índice de los elementos de la flota tiene que ser recuperable a través de consultas en todo momento.
Los equipos de trabajo deben estar compuestos por 2 estudiantes. No se permiten trabajos individuales y en caso de que el número total de estudiantes sea impar se conformará solamente un equipo de 3 estudiantes. 
Evaluación del proyecto

Para la evaluación del proyecto entra en consideración los siguientes factores: 
Perfecto entendimiento de cada integrante del equipo de todo el código del proyecto.
Perfecto entendimiento de cada integrante del equipo de los problemas surgidos y soluciones generadas durante toda la fase de desarrollo de la aplicación.
Correcto funcionamiento de la aplicación acorde a los objetivos planteados. 
Claridad y documentación del código.
Correcta elección de las estructuras de datos y algoritmos utilizados.
Eficiencia de la aplicación relacionada al costo temporal y espacial.
Creación del Sistema de Navegación 

Para la creación del índice de la biblioteca se utilizará el siguiente comando: python navigation_system.py -create <local_path>
<local_path> representa la dirección local de la carpeta que contiene el documento con la información de las embarcaciones y su fecha correspondiente.
Una vez finalizado el proceso de creación del índice de embarcaciones de la flota, la aplicación devolverá el texto “navy created successfully”. A partir de este momento se pueden iniciar las búsquedas.
La información deberá persistir de manera que se pueda acceder a la información de la flota y la ubicación de sus embarcaciones en todo momento. Esto significa que no se deberá volver a crear tal índice de elementos en cada búsqueda, sino que se realizará sobre una estructura persistente en disco, que se levantará a memoria cada vez que se requiera hacer una consulta.
Estructura de la Aplicación a realizar

Se implementará un script en python utilizando la versión 3. El script tendrá el nombre navigation_system.py. Sobre ese script se realizarán las operaciones de creación y búsqueda de información. El manejo de errores, excepciones y posibles valores de entrada corren a cargo de los desarrolladores de la aplicación. Dicho script será utilizado para realizar las pruebas para evaluar el desempeño de la aplicación.
