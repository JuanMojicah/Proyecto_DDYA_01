# ─────────────────────────────────────────────
#  DEFINICIÓN DEL GRAFO
# ─────────────────────────────────────────────
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

#Definicion De conecciones y distancias
CONECXIONES = [
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
    
    
    #AUN FALTAN CONECXIONES PERO ALGO ES ALGO 
]

# ─────────────────────────────────────────────
#  CONSTRUCCIÓN DEL GRAFO
# ─────────────────────────────────────────────
def construir_grafo():
    grafo = {nodo: [] for nodo in LUGARES}
    for a, b, dist in CONECXIONES:
        grafo[a].append((dist,b))
        grafo[b].append((dist,a))
    return grafo 
