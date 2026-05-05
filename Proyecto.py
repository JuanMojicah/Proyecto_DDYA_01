from sys import stdin

#Diccionario
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
    "10": "Bloque H - Laboratorios/ Ing Civil,Electrica,Electronica,Fisica,",
    "11": "Bloque I - Laboratorios/ Ing Sistemas ",
    "12": "Bloque K - Cafeteria Principal",
    "13": "cafeteria Bloque F",
    "14": "Cafeteria (Reggio's)",
    "15": "Cafeteria- Videojuegos",
    "16": "Cafererua (Harvie's)",
    "17": "Biblioteca Principal",
    "18": "Biblioteca - Bloque G",     
    "19": "Canchas De Fultbol",
    "20": "Chancha Multiple / Polideportivo",
    "21": "Parqueadero Principal (Entrada)",
    "22": "Parqueadero Bloque C",
    "23": "Parqueadero Bloque E",
    "24": "Parqueadero Bloque H",
    "25": "Parqueadero PoliDeportivo",
    "26": "Auditorio"
}

#Lista de conexiones:(origen, destino, distancia en metros)
CONEXIONES = [
    ("1", "21", 20),    # Entrada -> parqueadero Principal
    ("1", "2", 100),    # Entrada -> Administrativo
    ("1", "9", 110),    # Entrada -> Bloque G
    ("1", "3", 100),    # Entrada -> Bloque A
    ("1", "4", 120),    # Entrada -> Bloque B
    ("1", "5", 150),    # Entrada -> Bloque C
    ("1", "6", 130),    # Entrada -> BLoque D
    ("1", "7", 150),    # Entrada -> Bloque E
    ("1", "8", 100),    # ENtrada -> BLoque F
    ("1", "17",130),    # Entrada -> Biblioteca Principal
    ("3", "1", 100),    # Bloque A -> Entrada
    ("3", "4", 10),     # BLoque A -> Bloque B
    ("3", "5", 25),     # Bloque A -> Bloque C
    ("3", "22", 30),    # Bloque A -> Parqueadero C
    ("3", "7", 70),     # Bloque A -> Bloque E
    ("4", "3", 10),     # Bloque B -> Bloque A
    ("4", "17", 15),    # Bloque B -> Biblioteca Principal 
    ("4", "9", 20),     # Bloque B -> Bloque G
    ("4", "1", 120),    # Bloque B -> Entrada 
    ("4", "21", 50),    # Bloque B -> Parqueadero Principal
    ("4", "8", 70),     # Bloque B -> Bloque F
    ("4", "13",70),     # Bloque B -> Cafeteria Bloque F
    ("4", "6", 65),     # Bloque B -> Bloque D
    ("5", "1", 150),    # BLoque C -> Entrada
    ("5", "3", 25),     # Bloque C -> BLoque A
    ("5", "22", 15),    # Bloque C -> Parqueadero Bloque C
    ("5", "15", 20),    # Bloque C -> Cafereria Videojuegos 
    ("5", "7", 60),     # Bloque C -> Bloque E
    ("6", "1", 130),    # Bloque D -> Entrada
    ("6", "7", 30),     # Bloque D -> Bloque E
    ("6", "17", 60),    # Bloque D -> Biblioteca Principal 
    ("6", "4", 65),     # Bloque D -> Bloque B
    ("6", "14", 30),    # Bloque D -> Cafeteria Reggio's
    ("6", "10", 100),   # Bloque D -> BLoque H
    ("7", "1", 150),    # Bloque E -> Entrada 
    ("7", "5", 60),     # Bloque E -> Bloque C
    ("7", "3", 70),     # BLoque E -> Bloque A
    ("7", "6", 30),     # Bloque E -> Bloque D
    ("7", "22", 40),    # Bloque E -> Parqueadero Bloque C
    ("7", "15", 25),    # Bloque E -> Cafeteria Videojuegos
    ("7", "14", 45),    # Bloque E -> Cafeteria Reggio's
    ("7", "10", 110),   # Bloque E -> Bloque H
    ("8", "1", 100),    # Bloque F -> Entarda
    ("8", "9", 15),     # Bloque F -> Bloque G
    ("8", "4", 70),     # Bloque F -> Bloque B
    ("8", "6", 50),     # Bloque F -> Bloque D
    ("8", "17", 70),    # Bloque F -> Biblioteca principal 
    ("8", "14", 90),    # Bloque F -> Cafeteria Reggio's
    ("9", "1",110),     # Bloque G -> Entrada 
    ("9", "4", 20 ),    # Bloque G -> Bloque B
    ("9", "8", 15),     # Bloque G -> Bloque F
    ("9", "17", 35),    # BLoque G -> Bibilioteca Principal
    ("9", "13", 15),    # Bloque G -> Cafeteria Bloque F
    ("10", "1", 250),   # Bloque H -> Entrada
    ("10", "6", 100),   # BLoque H -> Bloque D
    ("10", "7", 110),   # Bloque H -> Bloque E
    ("10", "14", 90),   # Bloque H -> Cafeteria Reggio's
    ("10", "11", 10),   # Bloque H -> Bloque I 
    ("10", "24", 20),   # Bloque H -> parqueadero Bloque H
    ("10", "19", 90),   # Bloque H -> Canchas Futbol
    ("10", "20", 110),  # Bloque H -> Canchas Multiples / Polideportivo
    ("10", "22", 130),  # Bloque H -> parqueadero Bloque C
    ("10", "25", 130),  # Bloque H -> Parqueadero Polideportivo
    ("10", "12", 120),  # Bloque H -> Cafeteria Principal 
    ("11", "10", 10),   # Bloque I -> Bloque H 
]

#Clase que representa el grafo del campus usando matriz de adyacencia
class Grafo:
    #Constructor: inicializa matriz de adyacencia, lista de nombres y estado de bloqueos
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]  # Matriz de distancias entre nodos
        self.size = size                                       # Cantidad de nodos
        self.vertex_data = [''] * size                         # Nombres de los lugares
        self.bloqueados = [False] * size                       # True si el lugar esta bloqueado
        
    #Agrega una arista bidireccional con peso entre u y v
    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
            
    #Asigna un nombre descriptivo a un nodo
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data 
    
    #Marca un nodo como bloqueado (no se puede usar en rutas)
    def bloquear(self, idx):
        if 0 <= idx < self.size:
            self.bloqueados[idx] = True
    
    #Marca un nodo como habilitado (se puede usar en rutas)
    def habilitar(self, idx):
        if 0 <= idx < self.size:
            self.bloqueados[idx] = False
            
    #Algoritmo de Dijkstra: calcula distancias minimas desde start_vertex_data
    #Retorna (distancias, predecesores)
    def dijkstra(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)  # Encuentra indice del nodo inicio
        distances = [float('inf')] * self.size                    # Inicializa distancias infinitas
        distances[start_vertex] = 0                               # Distancia al inicio es 0
        visited = [False] * self.size                             # Ningun nodo visitado al inicio
        predecessors = [None] * self.size                         # Para reconstruir la ruta
        
        continuar = True
        while continuar:
            #encuentra el nodo no visitado no bloqueado con menor distancia
            min_distance = float('inf')
            u = None
            i = 0
            while i < self.size:
                if not visited[i] and not self.bloqueados[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i
                i += 1
            
            if u is None:          #No hay mas nodos accesibles
                continuar = False
            else:
                visited[u] = True  #marcar el nodo como visitado
                #actualiza distancias a los vecinos
                v = 0
                while v < self.size:
                    if self.adj_matrix[u][v] != 0 and not visited[v] and not self.bloqueados[v]:
                        alt = distances[u] + self.adj_matrix[u][v]
                        if alt < distances[v]:
                            distances[v] = alt
                            predecessors[v] = u
                    v += 1
        
        return distances, predecessors

    #Reconstruye el camino desde start hasta end usando el arreglo de predecesores
    def rebuild_road(self, predecessors, start_vertex_data, end_vertex_data):
        start = self.vertex_data.index(start_vertex_data)
        end = self.vertex_data.index(end_vertex_data)
        
        #primero cuenta cuantos nodos tiene el camino
        actual = end
        length = 0
        while actual is not None:
            length += 1
            actual = predecessors[actual]
        
        #Llena el arreglo del camino desde el final hacia el inicio
        camino = [0] * length
        actual = end
        i = length - 1
        while actual is not None:
            camino[i] = actual
            actual = predecessors[actual]
            i -= 1
        
        #Verificar que el camino empiece en el nodo inicio
        if camino[0] != start:
            return []
        return camino

#Construye el grafo del campus a partir de LUGARES y CONEXIONES
def grafo_campus():
    n = len(LUGARES)                     #Cantidad de lugares
    g = Grafo(n)                         #Crea el grafo
    
    mapa = {}                            #Diccionario: codigo -> indice en matriz
    i = 0 
    for clave in LUGARES:
        mapa[clave] = i 
        i += 1 
    
    #Asigna nombres a cada vertice
    for clave in LUGARES:
        g.add_vertex_data(mapa[clave], LUGARES[clave])
    
    #Agrega todas las conexiones al grafo
    for a, b, dist in CONEXIONES:
        g.add_edge(mapa[a], mapa[b], dist)
    
    return g, mapa

#Funcion principal
def main():
    g, mapa = grafo_campus()            #Inicializa el grafo
    salida = ""                          #Acumulador de salida para un solo print(lo uso en los UVAs para que no se salga del tiempo limite por muchos prints)
    
    continuar = True
    while continuar:
        salida += "\n=== SISTEMA DE NAVEGACION CAMPUS ===\n"
        salida += "1. Calcular ruta (inicio -> fin)\n"
        salida += "2. Agregar camino\n"
        salida += "3. Bloquear punto\n"
        salida += "4. Habilitar punto\n"
        salida += "5. Calcular tiempo (inicio -> fin)\n"
        salida += "6. Salir\n"
        salida += "Opcion: "
        
        opcion = input(salida)
        salida = ""
        
        #Opc 6: Salir del programa
        if opcion == "6":
            salida += "Saliendo del sistema...\n"
            continuar = False
        
        #Opc 1: Calcular ruta completa (camino + tiempo)
        elif opcion == "1":
            salida += "Nombre del punto de inicio: "
            inicio_nom = input(salida)
            salida += "Nombre del punto de destino: "
            fin_nom = input(salida)
            salida = ""
            
            #comprobar que los nombres existan
            if inicio_nom not in g.vertex_data or fin_nom not in g.vertex_data:
                salida += "Error: Punto no valido\n"
            else:
                idx_inicio = g.vertex_data.index(inicio_nom)
                idx_fin = g.vertex_data.index(fin_nom)
                
                #verificar que no esten bloqueados
                if g.bloqueados[idx_inicio] or g.bloqueados[idx_fin]:
                    salida += "Error: Punto de inicio o destino bloqueado\n"
                else:
                    distancias, predecesores = g.dijkstra(inicio_nom)
                    if distancias[idx_fin] == float('inf'):
                        salida += "No hay ruta disponible\n"
                    else:
                        ruta = g.rebuild_road(predecesores, inicio_nom, fin_nom)
                        salida += "\n=== RUTA ENCONTRADA ===\n"
                        salida += "Tiempo estimado: " + str(distancias[idx_fin]) + " minutos\n"
                        salida += "Ruta: "
                        i = 0
                        while i < len(ruta):
                            salida += g.vertex_data[ruta[i]]
                            if i < len(ruta) - 1:
                                salida += " -> "
                            i += 1
                        salida += "\n"
        
        #Opc 5:calcular solo el tiempo (sin mostrar toda la ruta)
        elif opcion == "5":
            salida += "Nombre del punto de inicio: "
            inicio_nom = input(salida)
            salida += "Nombre del punto de destino: "
            fin_nom = input(salida)
            salida = ""
            
            if inicio_nom not in g.vertex_data or fin_nom not in g.vertex_data:
                salida += "Error: Punto no valido\n"
            else:
                idx_fin = g.vertex_data.index(fin_nom)
                distancias, _ = g.dijkstra(inicio_nom)
                if distancias[idx_fin] == float('inf'):
                    salida += "No hay ruta disponible\n"
                else:
                    salida += "Tiempo estimado de " + inicio_nom + " a " + fin_nom + ": " + str(distancias[idx_fin]) + " minutos\n"
        
        #Opc 2:Agregar un nuevo camino entre dos puntos existentes
        elif opcion == "2":
            salida += "Punto A: "
            a_nom = input(salida)
            salida += "Punto B: "
            b_nom = input(salida)
            salida += "Distancia: "
            dist_str = input(salida)
            salida = ""
            
            if a_nom not in g.vertex_data or b_nom not in g.vertex_data:
                salida += "Error: Punto no valido\n"
            else:
                try:
                    distancia = int(dist_str)
                    idx_a = g.vertex_data.index(a_nom)
                    idx_b = g.vertex_data.index(b_nom)
                    g.add_edge(idx_a, idx_b, distancia)
                    salida += "Camino agregado: " + a_nom + " <-> " + b_nom + " (" + str(distancia) + " metros)\n"
                except:
                    salida += "Error: Distancia no valida\n"
        
        #Opc 3:bloquear un punto (no se puede pasar por el)
        elif opcion == "3":
            salida += "Nombre del punto a bloquear: "
            punto_nom = input(salida)
            salida = ""
            
            if punto_nom not in g.vertex_data:
                salida += "Error: Punto no valido\n"
            else:
                idx = g.vertex_data.index(punto_nom)
                g.bloquear(idx)
                salida += "Punto " + punto_nom + " bloqueado\n"
        
        #Opc 4:habilitar un punto previamente bloqueado
        elif opcion == "4":
            salida += "Nombre del punto a habilitar: "
            punto_nom = input(salida)
            salida = ""
            
            if punto_nom not in g.vertex_data:
                salida += "Error: Punto no valido\n"
            else:
                idx = g.vertex_data.index(punto_nom)
                g.habilitar(idx)
                salida += "Punto " + punto_nom + " habilitado\n"
        
        # Opcion invalida
        else:
            salida += "Opcion no valida\n"
    
    # Un solo print al final con toda la salida acumulada
    print(salida, end="")

# Punto de entrada del programa
if __name__ == "__main__":
    main()