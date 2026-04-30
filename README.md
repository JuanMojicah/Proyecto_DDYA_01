# Proyecto_DDYA_01

## Elaborado por
- Juan Manuel Mojica Herrera
- Juan Camilo (pendiente de apellido)

## Proyecto Final de DDYA
### Proyecto 1: Waze Universitario (Sistema de Navegación y Rutas)

## Escenario
Moverse por el campus universitario o por el sistema de transporte de la ciudad en el primer día de clases puede ser un caos.  
La misión de este proyecto es construir un sistema de navegación por consola que permita al usuario ingresar en qué edificio está y a qué edificio quiere ir, para devolver la ruta exacta más corta y el tiempo estimado de llegada.

## Requisitos

### Funcionamiento en consola
Todas las operaciones del proyecto deben realizarse por medio de consola. No es necesario generar una interfaz gráfica.

### Operaciones básicas
El código debe soportar las siguientes operaciones básicas:

- **Calcular ruta** `(punto de inicio, punto final)`: mostrar el paso a paso de las indicaciones para llegar desde el punto inicial al final, junto con el tiempo invertido.
- **Agregar camino** `(punto de inicio, punto final, distancia)`: agregar dentro de la estructura la posibilidad de incluir nuevos caminos entre puntos existentes.
- **Bloquear punto** `(punto)`: hay momentos en los que pasar por ciertos puntos de la universidad es imposible, poco conveniente o directamente inhabilitado. Debe existir la contraparte de **habilitar punto**.
- **Calcular tiempo** `(punto de inicio, punto final)`: dados el punto de inicio y el de final, poder conocer el tiempo que tomaría el trayecto completo.

### Manejo del proyecto
El proyecto debe existir dentro de un repositorio de GitHub, donde ambos integrantes deben realizar commits significativos durante el tiempo de trabajo.

### Consideraciones de la información
Los usuarios no buscan el nodo “4”, buscan la “Biblioteca”. La implementación completa de la estructura debe ser capaz de identificar cada uno de estos casos de la forma más conveniente.

### Casos de justificación
Deben contar con un archivo de input de no menos de 100 líneas, en el que el código reciba órdenes y sea completamente capaz de ejecutarlas correctamente.

### Resultados
La nota final del proyecto será definida únicamente durante la sustentación. Las respuestas, la justificación del código y la ejecución del mismo serán los factores clave de la evaluación.
