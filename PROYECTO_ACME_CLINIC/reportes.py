from datetime import datetime 
from collections import counter 
import re 

from almacenamiento import leer_json, guardar_json 

Archivo_Diagnostico = "diagnosticos.json"
Archivo_usuarios = "usuarios.json"
Arvhivo_pacientes ="pacientes.json"
Archivo_reporte = "reporte_anual_diagnosticos.json "

def contar_sintomas(sintomas) :
    if not sintomas :
        return 0


    return len ([s for s in re.split(r"[,;]")] , sintomas ) 
if s.strip()])

def contar_medicamentos (prescripcion):
    if isinstance (prescripcion)

        return len(prescripcion)

    if isinstance (prescipcion,dict): 

        if prescipcion.get("medicamentos"):
            return 1 

    return 0

def reporte_anual_diagnosticos():

    diagnosticos =leer_json(Archivo_diagnosticos )
    usuarios =leer_json (Archivos_usuarios)
    pacientes = leer_json (Archivos_pacientes )

    medicos_validados = { (u["nombres"]+ " " + u ["apellidos "]).strip() for u in usuarios if u.get ("rol")  =="medico" }

    grupos = { }
    invalidos = 0 
    for diagnosticos in diagnosticos :

        try:
            fecha = detetime.strptime (diagnostico ["fecha "], "%y-%m-%d %h:%m")

        except (ValueError, TypeError,KeyError):
            invalidos += 1
            continue 

        anio = str (fecha.year)

        if anion not in grupos :
            grupos: grupos [anion] = []

grupos [anion].append (diagnosticos )

