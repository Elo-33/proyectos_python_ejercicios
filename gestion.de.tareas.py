print('*** Systema de gestión de tares ***')

tareas = []

def ver_menu():
    print(f''' Operaciones que puedes realizar:
            1. Mostrar todas las tareas
            2. Agregar tarea
            3. Marcar tarea completada
            4. Cuantas tareas pendientes
            5. Eliminar tarea
            6. Salir \n''')
    opcion = int(input('Que quieres hacer? : '))
    return opcion

def mostrar_tarea():
    if len(tareas) == 0:
        print("No hay tareas")
    else:
        for i, tarea in enumerate(tareas):
            estado = "✅ Hecha" if tarea["completada"] else "⏳ Pendiente"
            print(f"{i + 1}. {tarea["descripcion"]} - {estado}\n")

def agregar_tarea():
    descripcion = input('Cual es tu nueva tarea? ')
    nueva_tarea = {"descripcion": descripcion, "completada" : False}
    tareas.append(nueva_tarea)
    print(f"Tarea '{nueva_tarea ["descripcion"]}' agregada!\n")

def tarea_completada():
    numero = int(input('Cual tarea has completado? '))
    if 0 <= numero - 1 < len(tareas):
        tareas[numero - 1]["completada"] = True
        print(f'Tarea {tareas[numero -1]["descripcion"]} completada ✅\n')
    else:
        print("Esta tarea no existe")

def tareas_pendientes():
    pendientes = 0
    for tarea in tareas:
        if not tarea["completada"]:
            pendientes += 1
    print(f'📋 Tienes {pendientes} tareas pendientes\n')

def eliminar_tarea ():
    numero = int(input('Cual tarea quieres eliminar? '))
    if 0 <= numero - 1 < len(tareas):
        tarea_eliminada = tareas[numero -1]
        del tareas[numero -1]
        print(f'🗑 Has eliminado : {tarea_eliminada["descripcion"]} \n')
    else:
        print("Esta tarea no existe")

salir = False
while not salir:
    opcion = ver_menu()
    if opcion == 1:
        mostrar_tarea()
    elif opcion == 2:
        agregar_tarea()
    elif opcion == 3:
        tarea_completada()
    elif opcion == 4:
        tareas_pendientes()
    elif opcion == 5:
        eliminar_tarea()
    elif opcion == 6:
        salir = True
    else:
        print("Opcion no valida")
