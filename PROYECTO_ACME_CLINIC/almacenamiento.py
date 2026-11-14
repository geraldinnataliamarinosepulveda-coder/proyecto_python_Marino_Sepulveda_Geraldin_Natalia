import json
import os

CARPETA_DATOS = os.path.join(os.path.dirname(__file__), "datos")


def leer_json(nombre_archivo):
    ruta = os.path.join(CARPETA_DATOS, nombre_archivo)

    if not os.path.exists(ruta):
        return []

    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_json(nombre_archivo, datos):
    os.makedirs(CARPETA_DATOS, exist_ok=True)

    ruta = os.path.join(CARPETA_DATOS, nombre_archivo)

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)