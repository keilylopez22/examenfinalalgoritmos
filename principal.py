import openpyxl
import Err
def principal():
    continuar = True
    while(continuar):
        opcion_correcta = False
        while(not opcion_correcta):
            print("1. crear vehiculos")
            print("2. editar vehiculos")
            print("3. borrar vehiculos")
            print("4. listar vehiculos")
            print("5. salir del programa")
            opcion = int(input("seleccione una opcion porfavor"))
            if opcion <1 or opcion >5:
                print("opcion no valida por favor ingrese un numero del 1 al 5")
            elif opcion == 5:
                continuar = False
                print("gracias por utilizar este programa")
                break
            else:
                opcion_correcta= True
                ejecutar_opcion(opcion)
def  ejecutar_opcion(opcion):
    if opcion == 1:
        vehiculos = crear_vehiculos() 
        except exception as Error



def crear_vehiculos(codigo, marca, modelo, precio, kilometraje, cantidaddefotos):
    codigo = int(input("cual es el codigo del vehiculo"))
    marca = input("ingrese el la marca del vehiculo")
    modelo = input("ingrese el modelo del vehiculo")
    precio= float(input("ingrese el precio del vehivulo"))
    kilometraje = float(input("cuantos kilometro tiene el vehiculo"))
principal()
