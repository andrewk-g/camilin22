from schedule_manager import  agregar_evento, eliminar_evento

from reportes import (
    imprimir_tabla,
    imprimir_reporte_paginado,
    exportar_reporte_json
)


eventos = []


def mostrar_menu():

    print("\n===== GESTOR DE HORARIOS =====")

    print("1. Agregar evento")
    print("2. Eliminar evento")
    print("3. Mostrar tabla")
    print("4. Mostrar reporte")
    print("5. Exportar reporte JSON")
    print("6. Salir")


def agregar():

    print("\n--- AGREGAR EVENTO ---")

    dia = input("Día: ")
    materia = input("Materia o actividad: ")
    hora_inicio = input("Hora de inicio: ")
    hora_fin = input("Hora de finalización: ")
    ubicacion = input("Ubicación: ")

    agregar_evento(
        eventos,
        dia,
        materia,
        hora_inicio,
        hora_fin,
        ubicacion
    )

    print("Evento agregado correctamente.")


def eliminar():

    print("\n--- ELIMINAR EVENTO ---")

    if len(eventos) == 0:

        print("No hay eventos para eliminar.")
        return

    imprimir_tabla(eventos)

    try:

        numero = int(input("Seleccione el número del evento a eliminar: "))

        eliminado = eliminar_evento(eventos, numero - 1)

        if eliminado:
            print("Evento eliminado correctamente.")

        else:
            print("Número de evento inválido.")

    except ValueError:

        print("Debes ingresar un número válido.")


while True:

    mostrar_menu()

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":

        agregar()

    elif opcion == "2":

        eliminar()

    elif opcion == "3":

        imprimir_tabla(eventos)

    elif opcion == "4":

        imprimir_reporte_paginado(eventos)

    elif opcion == "5":

        exportar_reporte_json(eventos)

    elif opcion == "6":

        print("\nPrograma finalizado.")
        break

    else:

        print("\nOpción inválida. Intenta nuevamente.")