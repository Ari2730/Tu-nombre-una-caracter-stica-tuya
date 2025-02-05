import random

# Diccionario con nombres y características
caracteristicas = {
    "Ana": "eres muy creativa",
    "Carlos": "siempre eres muy amable",
    "Luis": "tienes un gran sentido del humor",
    "María": "eres una persona muy inteligente",
    "Sofía": "tu energía es contagiosa",
    "Pedro": "eres muy trabajador",
}

while True:
    nombre = input("Dime tu nombre: ")
    if nombre in caracteristicas:
        print(f"{nombre}, {caracteristicas[nombre]}!")
    else:
        nueva_caracteristica = random.choice([
            "tienes una gran personalidad",
            "eres una persona increíble",
            "tu sonrisa alegra el día",
            "tienes mucho talento",
        ])
        print(f"{nombre}, {nueva_caracteristica}!")
