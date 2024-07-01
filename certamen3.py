menu = '''
1.Registrar vehiculo
2.Listar todos los vehiculos registrados
3.Imprimir orden de reparación
4.Salir del programa'''

titulo = ''' Marca      Año de Fab.     Kilometraje     Costo      
------------------------------------------------------------------

------------------------------------------------------------------
'''
#Listas
reg_vehiculos = []
marcas = [('kia','chevrolet','hyundai', 'audi')]
#Listas

def registrov():
    while True:
        try:
            marca   = input("Ingrese la marca del vehiculo: ").lower().strip() 
            añofab  = input("Ingrese el año de fabricación: ")
            km      = str(input("Ingrese el kilometraje: "))
            costo   = int(input("Ingrese el costo de reparación: "))
            iva     = round(costo*0.08)
            total   = costo+iva
            reg_vehiculos.append([marca, añofab, km, total])
            print ("Pedido registrado con exito!")
            break
        except:
            print ("Error de excepcion")
            break

def listarvehiculos():
    mostrar = titulo
    for t in reg_vehiculos:
        mostrar += f"{t[0]:10s}"
        mostrar += f"{t[1]:9d}"
        mostrar += f"{t[2]:12d}"
        mostrar += f"{t[3]:14d}"
        mostrar += "\n"
    return mostrar

def Imprimir():
    with open ("listado.txt",'w') as archivo:
        archivo.write(listarvehiculos())

while True:
    print (menu)
    opcion = str(input("Por favor, seleccione una opción: "))
    try:
        if opcion == "4":
            break
        elif opcion == "1":
            registrov()
        elif opcion == "2":
            listarvehiculos()
        elif opcion == "3":    
            Imprimir()
    except:
        errorde = ("Error de excepción")
        break

