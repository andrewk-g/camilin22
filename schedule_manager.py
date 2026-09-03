# schedule_manager.py

DIAS_VALIDOS = [
    "Lunes",
    "Martes",
    "Miercoles",
    "Jueves",
    "Viernes",
    "Sabado",
    "Domingo"
]


def agregar_evento(eventos,dia,materia,hora_inicio,hora_fin,ubicacion=""):
    evento = {
        "dia": dia,
        "materia":materia,
        "hora_inicio":hora_inicio,
        "hora_fin":hora_fin,
        "ubicacion": ubicacion
    }
    eventos.append(evento)
    return eventos
  
def eliminar_evento(eventos, materia):
    eventos[:] = [evento for evento in eventos if evento["materia"].lower() != materia.lower()]
    return eventos
def obtener_eventos_del_dia(eventos, dia):
    return[evento for evento in eventos if evento ["dia"]==dia]