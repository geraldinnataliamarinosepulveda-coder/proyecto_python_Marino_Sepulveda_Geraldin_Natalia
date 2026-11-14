# es el archivo que inicia el programa
from usuarios import iniciar_sesion
from pacientes import registrar_paciente
from diagnosticos import crear_consulta, ver_historia_clinica


def menu():
    print("\n====ACME CLINIC=====")
    print("1. Registrar paciente")
    print("2. Realizar diagnostico")
    print("3. Consultar historia clinica")
    print("4. Cerrar sesión")


def main():
    print("Bienvenido a ACME CLINIC")

    usuario = iniciar_sesion()

    if not usuario:
        return

    while True:
        menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_paciente()
        elif opcion == "2":
            crear_consulta(usuario)
        elif opcion == "3":
            ver_historia_clinica()
        elif opcion == "4":
            print("Sesion cerrada.")
            break
        else:
            print("Opcion incorrecta")


if __name__ == "__main__":
    main()