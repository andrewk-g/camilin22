import json


def imprimir_tabla(eventos):

    print("\n===== HORARIO SEMANAL =====")

    if len(eventos) == 0:
        print("No hay eventos registrados.")
        return

    print("-" * 80)

    for i, evento in enumerate(eventos, start=1):

        print(f"{i}. Día: {evento['dia']}")
        print(f"   Materia: {evento['materia']}")
        print(f"   Hora: {evento['hora_inicio']} - {evento['hora_fin']}")
        print(f"   Ubicación: {evento['ubicacion']}")

        print("-" * 80)


def imprimir_reporte_paginado(eventos):

    print("\n===== REPORTE DE EVENTOS =====")

    if len(eventos) == 0:
        print("No hay eventos registrados.")
        return

    for i, evento in enumerate(eventos, start=1):

        print(f"\nEvento {i}")
        print(f"Día: {evento['dia']}")
        print(f"Materia: {evento['materia']}")
        print(f"Hora inicio: {evento['hora_inicio']}")
        print(f"Hora fin: {evento['hora_fin']}")
        print(f"Ubicación: {evento['ubicacion']}")

        if i < len(eventos):
            input("\nPresiona ENTER para ver el siguiente evento...")


def exportar_reporte_json(eventos):

    nombre_archivo = "reporte_horarios.json"

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:

        json.dump(
            eventos,
            archivo,
            ensure_ascii=False,
            indent=4
        )

    print(f"\nReporte exportado correctamente como {nombre_archivo}")