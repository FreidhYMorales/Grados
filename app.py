from grado import Grado
from alumno import Alumno
from os import system

def menu():
    encendido = True
    grados = list()
    
    while encendido:
        system("cls")
        print("Menu")
        print("1. Agregar Grado")
        print("2. Inscribir Alumno")
        print("3. Ver Alumnos Por Grado")
        print("4. Salir")
        print("-" * 30)
        opc = int(input("Ingrese una Opcion: "))
        
        if opc == 1:
            system("cls")
            codigo = int(input("Ingrese el codigo de Grado: "))
            nombre = input("Ingrese el nombre del Grado: ")
            grado = Grado()
            grado.AgregarGrado(codigo, nombre)
            grados.append(grado)
            print("Grado Creado Exitosamente!!")
            input()
        elif opc == 2:
            system("cls")
            nombre = input("Ingrese los nombres del Alumno: ")
            apellido = input("Ingrese los apellidos del Alumno: ")
            alum = Alumno(nombre, apellido)
            for grad in grados:
                grad.VerGrado()
            codigo = int(input("Ingrese el codigo del Grado: "))
            for grad in range(len(grados)):
                if grados[grad].codigo == codigo:
                    grados[grad].AgregarAlumno(alum)
            input()
        elif opc == 3:
            system("cls")
            for grad in range(len(grados)):
                grados[grad].VerGrado()
                grados[grad].VerAlumnos()
            input()
        elif opc == 4:
            encendido = False
            system("cls")
            print("Gracias por usar el programa!!")
            input()
            break
        else:
            system("cls")
            print("Ingrese una opcion correcta!!")
            input()
            
menu()