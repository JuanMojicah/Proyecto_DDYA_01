from sys import stdin

# Diccionario con todos los lugares del campus
LUGARES = {
    "1" : "Entrada principal (porteria)",
    "2" : "Edificio Administrativo",
    "3" : "Bloque A",
    "4" : "Bloque B",
    "5" : "Bloque C",
    "6" : "Bloque D",
    "7" : "Bloque E",
    "8" : "Bloque F",
    "9" : "Bloque G",
    "10": "Bloque H - Laboratorios/Ing Civil,Electrica,Electronica,Fisica",
    "11": "Bloque I - Laboratorios/Ing Sistemas",
    "12": "Bloque K - Cafeteria Principal",
    "13": "cafeteria Bloque F",
    "14": "Cafeteria (Reggio's)",
    "15": "Cafeteria- Videojuegos",
    "16": "Cafeteria (Harvie's)",
    "17": "Biblioteca Principal",
    "18": "Biblioteca - Bloque G",     
    "19": "Canchas De Futbol",
    "20": "Cancha Multiple / Polideportivo",
    "21": "Parqueadero Principal (Entrada)",
    "22": "Parqueadero Bloque C",
    "23": "Parqueadero Bloque E",
    "24": "Parqueadero Bloque H",
    "25": "Parqueadero PoliDeportivo",
    "26": "Auditorio"
}
# Colocar mas lugares y mayor detalle 
CONEXIONES = [
    ("1", "21", 20),  # Entrada principal -> Parqueadero Principal
    ("1", "2", 100),  # Entrada principal -> Administrativo
    ("1", "9", 110),  # Entrada principal -> Bloque G
    ("1", "3", 100),  # Entrada principal -> Bloque A
    ("1", "4", 120),  # Entrada principal -> Bloque B
    ("1", "5", 150),  # Entrada principal -> Bloque C
    ("1", "6", 130),  # Entrada principal -> Bloque D
    ("1", "7", 150),  # Entrada principal -> Bloque E
    ("1", "8", 100),  # Entrada principal -> Bloque F
    ("1", "17",130),  # Entrada principal -> Biblioteca Principal
    ("3", "1", 100),  # Bloque A -> Entrada principal
    ("3", "4", 10),   # Bloque A -> Bloque B
    ("3", "5", 25),   # Bloque A -> Bloque C
    ("3", "22", 30),  # Bloque A -> Parqueadero C
    ("3", "7", 70),   # Bloque A -> Bloque E
    ("4", "3", 10),   # Bloque B -> Bloque A
    ("4", "17", 15),  # Bloque B -> Biblioteca Principal
    ("4", "9", 20),   # Bloque B -> Bloque G
    ("4", "1", 120),  # Bloque B -> Entrada principal
    ("4", "21", 50),  # Bloque B -> Parqueadero Principal
    ("4", "8", 70),   # Bloque B -> Bloque F
    ("4", "13",70),   # Bloque B -> Cafeteria Bloque F
    ("4", "6", 65),   # Bloque B -> Bloque D
    ("5", "1", 150),  # Bloque C -> Entrada principal
    ("5", "3", 25),   # Bloque C -> Bloque A
    ("5", "22", 15),  # Bloque C -> Parqueadero Bloque C
    ("5", "15", 20),  # Bloque C -> Cafeteria Videojuegos
    ("5", "7", 60),   # Bloque C -> Bloque E
    ("6", "1", 130),  # Bloque D -> Entrada principal
    ("6", "7", 30),   # Bloque D -> Bloque E
    ("6", "17", 60),  # Bloque D -> Biblioteca Principal
    ("6", "4", 65),   # Bloque D -> Bloque B
    ("6", "14", 30),  # Bloque D -> Cafeteria Reggio's
    ("6", "10", 100), # Bloque D -> Bloque H
    ("7", "1", 150),  # Bloque E -> Entrada principal
    ("7", "5", 60),   # Bloque E -> Bloque C
    ("7", "3", 70),   # Bloque E -> Bloque A
    ("7", "6", 30),   # Bloque E -> Bloque D
    ("7", "22", 40),  # Bloque E -> Parqueadero Bloque C
    ("7", "15", 25),  # Bloque E -> Cafeteria Videojuegos
    ("7", "14", 45),  # Bloque E -> Cafeteria Reggio's
    ("7", "10", 110), # Bloque E -> Bloque H
    ("8", "1", 100),  # Bloque F -> Entrada principal
    ("8", "9", 15),   # Bloque F -> Bloque G
    ("8", "4", 70),   # Bloque F -> Bloque B
    ("8", "6", 50),   # Bloque F -> Bloque D
    ("8", "17", 70),  # Bloque F -> Biblioteca Principal
    ("8", "14", 90),  # Bloque F -> Cafeteria Reggio's
    ("9", "1",110),   # Bloque G -> Entrada principal
    ("9", "4", 20),   # Bloque G -> Bloque B
    ("9", "8", 15),   # Bloque G -> Bloque F
    ("9", "17", 35),  # Bloque G -> Biblioteca Principal
    ("9", "13", 15),  # Bloque G -> Cafeteria Bloque F
    ("10", "1", 250), # Bloque H -> Entrada principal
    ("10", "6", 100), # Bloque H -> Bloque D
    ("10", "7", 110), # Bloque H -> Bloque E
    ("10", "14", 90), # Bloque H -> Cafeteria Reggio's
    ("10", "11", 10), # Bloque H -> Bloque I
    ("10", "24", 20), # Bloque H -> Parqueadero Bloque H
    ("10", "19", 90), # Bloque H -> Canchas Futbol
    ("10", "20", 110),# Bloque H -> Cancha Multiple
    ("10", "22", 130),# Bloque H -> Parqueadero Bloque C
    ("10", "25", 130),# Bloque H -> Parqueadero Polideportivo
    ("10", "12", 120),# Bloque H -> Cafeteria Principal
    ("11", "10", 10)  # Bloque I -> Bloque H
]

# Funcion para convertir nombre de lugar a su codigo (inverso de LUGARES)
def nombre_a_codigo(nombre):
    for codigo in LUGARES:
        if LUGARES[codigo] == nombre:
            return codigo
    return None

# Funcion para obtener indice en la matriz
def codigo_a_indice(codigo, lista_codigos):
    i = 0
    while i < len(lista_codigos):
        if lista_codigos[i] == codigo:
            return i
        i += 1
    return -1

# Inicializa la matriz de adyacencia
def crear_matriz_adyacencia(lista_codigos, conexiones):
    n = len(lista_codigos)
    matriz = []
    i = 0
    while i < n:
        fila = []
        j = 0
        while j < n:
            fila.append(0)
            j += 1
        matriz.append(fila)
        i += 1
    
    i = 0
    while i < len(conexiones):
        u_cod, v_cod, peso = conexiones[i]
        u = codigo_a_indice(u_cod, lista_codigos)
        v = codigo_a_indice(v_cod, lista_codigos)
        if u != -1 and v != -1:
            matriz[u][v] = peso
            matriz[v][u] = peso
        i += 1
    return matriz

# Dijkstra sin usar clases, solo listas y variables
def dijkstra(matriz, num_nodos, nodo_inicio, nodos_bloqueados):
    INF = 9999999
    distancias = []
    visitado = []
    predecesor = []
    
    i = 0
    while i < num_nodos:
        distancias.append(INF)
        visitado.append(0)
        predecesor.append(-1)
        i += 1
    
    distancias[nodo_inicio] = 0
    
    continuar = True
    while continuar:
        min_dist = INF
        u = -1
        
        i = 0
        while i < num_nodos:
            if visitado[i] == 0 and nodos_bloqueados[i] == 0 and distancias[i] < min_dist:
                min_dist = distancias[i]
                u = i
            i += 1
        
        if u == -1:
            continuar = False
        else:
            visitado[u] = 1
            
            v = 0
            while v < num_nodos:
                if matriz[u][v] != 0 and visitado[v] == 0 and nodos_bloqueados[v] == 0:
                    nueva_dist = distancias[u] + matriz[u][v]
                    if nueva_dist < distancias[v]:
                        distancias[v] = nueva_dist
                        predecesor[v] = u
                v += 1
    
    return distancias, predecesor

# Reconstruye el camino desde el predecesor
def reconstruir_camino(predecesor, inicio, fin):
    camino = []
    actual = fin
    while actual != -1:
        camino.append(actual)
        actual = predecesor[actual]
    
    invertido = []
    i = len(camino) - 1
    while i >= 0:
        invertido.append(camino[i])
        i -= 1
    
    if invertido[0] != inicio:
        return []
    return invertido

# Genera texto legible de las instrucciones de la ruta
def generar_instrucciones(camino_indices, lista_codigos, matriz):
    if len(camino_indices) < 2:
        return "No hay suficientes puntos para generar instrucciones"
    
    instrucciones = []
    i = 0
    while i < len(camino_indices) - 1:
        idx_actual = camino_indices[i]
        idx_sig = camino_indices[i + 1]
        codigo_actual = lista_codigos[idx_actual]
        codigo_sig = lista_codigos[idx_sig]
        nombre_actual = LUGARES[codigo_actual]
        nombre_sig = LUGARES[codigo_sig]
        distancia = matriz[idx_actual][idx_sig]
        texto = "- Desde " + nombre_actual + " camine " + str(distancia) + " metros hacia " + nombre_sig
        instrucciones.append(texto)
        i += 1
    
    texto_final = ""
    i = 0
    while i < len(instrucciones):
        texto_final = texto_final + instrucciones[i] + "\n"
        i += 1
    return texto_final

# Bloquea un nodo
def bloquear_nodo(nodos_bloqueados, indice):
    if indice != -1:
        nodos_bloqueados[indice] = 1

# Habilita un nodo
def habilitar_nodo(nodos_bloqueados, indice):
    if indice != -1:
        nodos_bloqueados[indice] = 0

# Agrega una nueva conexion
def agregar_conexion(matriz, lista_codigos, u_cod, v_cod, peso):
    u = codigo_a_indice(u_cod, lista_codigos)
    v = codigo_a_indice(v_cod, lista_codigos)
    if u != -1 and v != -1:
        matriz[u][v] = peso
        matriz[v][u] = peso
        return True
    return False

# Menu principal
def main():
    # Crear lista de codigos ordenada
    lista_codigos = []
    for codigo in LUGARES:
        lista_codigos.append(codigo)
    
    num_nodos = len(lista_codigos)
    matriz = crear_matriz_adyacencia(lista_codigos, CONEXIONES)
    nodos_bloqueados = []
    i = 0
    while i < num_nodos:
        nodos_bloqueados.append(0)
        i += 1
    
    salida = ""
    
    continuar_programa = True
    while continuar_programa:
        salida = salida + "\n=== SISTEMA DE NAVEGACION CAMPUS ===\n"
        salida = salida + "1. Calcular ruta (inicio -> fin)\n"
        salida = salida + "2. Agregar camino\n"
        salida = salida + "3. Bloquear punto\n"
        salida = salida + "4. Habilitar punto\n"
        salida = salida + "5. Calcular tiempo (inicio -> fin)\n"
        salida = salida + "6. Salir\n"
        salida = salida + "Opcion: "
        
        opcion = input(salida)
        salida = ""
        
        if opcion == "6":
            salida = salida + "Saliendo del sistema...\n"
            continuar_programa = False
        
        elif opcion == "1":
            salida = salida + "Nombre del punto de inicio: "
            inicio_nom = input(salida)
            salida = salida + "Nombre del punto de destino: "
            fin_nom = input(salida)
            salida = ""
            
            inicio_cod = nombre_a_codigo(inicio_nom)
            fin_cod = nombre_a_codigo(fin_nom)
            
            if inicio_cod is None or fin_cod is None:
                salida = salida + "Error: Punto no valido\n"
            else:
                inicio_idx = codigo_a_indice(inicio_cod, lista_codigos)
                fin_idx = codigo_a_indice(fin_cod, lista_codigos)
                
                if nodos_bloqueados[inicio_idx] == 1 or nodos_bloqueados[fin_idx] == 1:
                    salida = salida + "Error: Punto de inicio o destino bloqueado\n"
                else:
                    distancias, predecesor = dijkstra(matriz, num_nodos, inicio_idx, nodos_bloqueados)
                    if distancias[fin_idx] >= 9999999:
                        salida = salida + "No hay ruta disponible\n"
                    else:
                        camino = reconstruir_camino(predecesor, inicio_idx, fin_idx)
                        instrucciones = generar_instrucciones(camino, lista_codigos, matriz)
                        salida = salida + "\n=== RUTA ENCONTRADA ===\n"
                        salida = salida + "Tiempo estimado: " + str(distancias[fin_idx]) + " minutos\n"
                        salida = salida + "Instrucciones paso a paso:\n"
                        salida = salida + instrucciones
        
        elif opcion == "5":
            salida = salida + "Nombre del punto de inicio: "
            inicio_nom = input(salida)
            salida = salida + "Nombre del punto de destino: "
            fin_nom = input(salida)
            salida = ""
            
            inicio_cod = nombre_a_codigo(inicio_nom)
            fin_cod = nombre_a_codigo(fin_nom)
            
            if inicio_cod is None or fin_cod is None:
                salida = salida + "Error: Punto no valido\n"
            else:
                inicio_idx = codigo_a_indice(inicio_cod, lista_codigos)
                fin_idx = codigo_a_indice(fin_cod, lista_codigos)
                
                distancias, _ = dijkstra(matriz, num_nodos, inicio_idx, nodos_bloqueados)
                if distancias[fin_idx] >= 9999999:
                    salida = salida + "No hay ruta disponible\n"
                else:
                    salida = salida + "Tiempo estimado de " + inicio_nom + " a " + fin_nom + ": " + str(distancias[fin_idx]) + " minutos\n"
        
        elif opcion == "2":
            salida = salida + "Punto A: "
            a_nom = input(salida)
            salida = salida + "Punto B: "
            b_nom = input(salida)
            salida = salida + "Distancia: "
            dist_str = input(salida)
            salida = ""
            
            a_cod = nombre_a_codigo(a_nom)
            b_cod = nombre_a_codigo(b_nom)
            
            if a_cod is None or b_cod is None:
                salida = salida + "Error: Punto no valido\n"
            else:
                try:
                    distancia_int = int(dist_str)
                    if agregar_conexion(matriz, lista_codigos, a_cod, b_cod, distancia_int):
                        salida = salida + "Camino agregado: " + a_nom + " <-> " + b_nom + " (" + str(distancia_int) + " metros)\n"
                    else:
                        salida = salida + "Error: No se pudo agregar el camino\n"
                except:
                    salida = salida + "Error: Distancia no valida\n"
        
        elif opcion == "3":
            salida = salida + "Nombre del punto a bloquear: "
            punto_nom = input(salida)
            salida = ""
            
            punto_cod = nombre_a_codigo(punto_nom)
            if punto_cod is None:
                salida = salida + "Punto no valido\n"
            else:
                punto_idx = codigo_a_indice(punto_cod, lista_codigos)
                bloquear_nodo(nodos_bloqueados, punto_idx)
                salida = salida + "Punto " + punto_nom + " bloqueado\n"
        
        elif opcion == "4":
            salida = salida + "Nombre del punto a habilitar: "
            punto_nom = input(salida)
            salida = ""
            
            punto_cod = nombre_a_codigo(punto_nom)
            if punto_cod is None:
                salida = salida + "Punto no valido\n"
            else:
                punto_idx = codigo_a_indice(punto_cod, lista_codigos)
                habilitar_nodo(nodos_bloqueados, punto_idx)
                salida = salida + "Punto " + punto_nom + " habilitado\n"
        
        else:
            salida = salida + "Opcion no valida\n"
    
    print(salida, end="")

if __name__ == "__main__":
    main()
"""
Cosas Faltantes:
-Implementar búsqueda por nombre parcial o palabra clave (ej: "Biblioteca" encuentra "Biblioteca Principal" y "Biblioteca - Bloque G")
-Listar todos los lugares disponibles con su código y nombre
-Mostrar el tiempo acumulado en cada paso de la ruta
-Mostrar tiempo parcial después de cada instrucción
-Añadir más conexiones faltantes
-Buscar errores de código para evitar que el programa no funcione correctamente
y nada ,esto medio funciona pero le falta cositas jsjs 
(de ser necesario simmplificar el codigo para que sea mas robusto y facil de entender)
"""