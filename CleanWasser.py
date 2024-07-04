from os import system
import random
import csv

pedidos = [['ID pedido', 'Cliente', 'Dirección', 'Sector', 'Disp.6lts', 'Disp.10lts', 'Disp.20lts']]
sectores_disponibles = ['Concepción', 'Chiguayante', 'Talcahuano', 'Hualpén', 'San Pedro']

def prevenir_limpieza(): #previene la limpieza inmediata de la terminal
    input('Presione Enter para continuar...')

def limpiar_pantalla():
    system('cls')

def cantidad_dispensadores(nombre):
    while True:
        try:
            cantidad = int(input(f'Ingrese la cantidad de dispensadores de {nombre} que desea agregar: '))
        except ValueError:
            print('Ingrese solamente digitos.\n')

        if cantidad >= 0:
            break
        else:
            print('Ingrese solo números positivos\n')
    return cantidad

def agregar_dispensadores():
    cantidad_6lts = cantidad_dispensadores('6lts')
    cantidad_10lts = cantidad_dispensadores('10lts')
    cantidad_20lts = cantidad_dispensadores('20lts')

    if (cantidad_6lts + cantidad_10lts + cantidad_20lts) != 0:
        return [cantidad_6lts, cantidad_10lts, cantidad_20lts]
    else:
        return 'Invalido'

def registrar_pedido():
    limpiar_pantalla()
    id_cliente = generador_id()

    while True:
        nombre_cliente = input('Ingrese el nombre del cliente: ')

        if len(nombre_cliente) >= 3 and nombre_cliente.isalpha():
            break
        else:
            print('El nombre ingresado es inválido.\n')

    while True:
        apellido_cliente = input('Ingrese el apellido del cliente: ')

        if len(apellido_cliente) >= 3 and apellido_cliente.isalpha():
            break
        else:
            print('El apellido ingresado es inválido.\n')
    
    cliente = f'{nombre_cliente} {apellido_cliente}'
        
    direccion_cliente = input('Ingrese la dirección del cliente: ')

    while True:
        sector_cliente = input('Ingrese el sector del cliente: ')

        if sector_cliente.title() in sectores_disponibles:
            sector_cliente = sector_cliente.title()
            break
        else:
            print('Servicio no disponible al sector ingresado.\n'
                  'Recuerda escribir el nombre del sector utilizando tíldes.\n')
    
    dispensadores_pedido = agregar_dispensadores()
    if dispensadores_pedido != 'Invalido':
        pedido_agregar = [id_cliente, cliente, direccion_cliente, sector_cliente, dispensadores_pedido[0], dispensadores_pedido[1], dispensadores_pedido[2]]
        pedidos.append(pedido_agregar)
        print('Pedido agregado con éxito.\n')
    else:
        print('Se ha cancelado el pedido.\n')
    prevenir_limpieza()

def generador_id(): # Verifica que el id asignado a cada pedido no se encuentre repetido
    id_valido = False
    invalido = 0

    while id_valido == False:
        id_cliente = random.randint(111111,999999)

        for pedido in pedidos:
            if pedido != pedidos[0]:
                if id_cliente == pedido[0]:
                    invalido = 1
        if invalido != 1:
            id_valido = True
    return id_cliente #la funcion devuelve el numero del id

def listar_pedidos():
    limpiar_pantalla()
    if len(pedidos) > 1:
        for pedido in pedidos:
            print(pedido)
    else:
        print('No se han registrado pedidos.\n')
    prevenir_limpieza()

def imprimir_hoja_ruta():
    limpiar_pantalla()
    if len(pedidos) > 1:
        while True:
            sector_imprimir = input('Ingrese el sector que desea imprimir: ')
            if sector_imprimir.title() in sectores_disponibles:
                sector_imprimir = sector_imprimir.title()
                break
            else:
                print('El sector ingresado no es válido.\n')
                prevenir_limpieza()
                limpiar_pantalla()

        pedidos_imprimir = [pedidos[0]]    

        for pedido in pedidos:
                if pedido[3] == sector_imprimir:
                    pedidos_imprimir.append(pedido)

        if len(pedidos_imprimir) > 1:                
            with open(f'Hoja de ruta {sector_imprimir}.csv', 'w') as archivo_csv:
                escritor_csv = csv.writer(archivo_csv)
                escritor_csv.writerows(pedidos_imprimir)
                print('Hoja de ruta generada con éxito.\n')
        else:
            print('No se han registrado pedidos para este sector.\n')
    else:
        print('No se han registrado pedidos.\n')
    prevenir_limpieza()
        
def buscar_pedido():
    limpiar_pantalla()
    if len(pedidos) > 1:
        while True:
            try:
                id_buscar = int(input('Ingrese el ID del pedido: '))
            except ValueError:
                print('Ingrese solamente digitos.\n')
                continue
            break

        encontrado = 0
        
        for pedido in pedidos:
            if pedido[0] == id_buscar:
                print(pedidos[0])
                print(pedido)
                encontrado = 1
        if encontrado == 0:
            print('El ID ingresado no se encuentra registrado.\n')
    else:
        print('No se han registrado pedidos.\n')
    prevenir_limpieza()

def menu():
    while True:
        limpiar_pantalla()
        while True:
            try:
                print('CleanWasser')
                op_menu = int(input('[1] Registrar pedido.\n'
                                    '[2] Listar todos los pedidos.\n'
                                    '[3] Imprimir hoja de ruta.\n'
                                    '[4] Buscar un pedido por ID.\n'
                                    '[5] Salir del programa.\n: '))
            except ValueError:
                print('Ingrese el dígito de la opción que desea utilizar.\n')
                prevenir_limpieza()
                limpiar_pantalla()
                continue
            if 1 <= op_menu <= 5:
                break
            else:
                print('La opción ingresada no es válida.')
                prevenir_limpieza()
                limpiar_pantalla()

        if op_menu == 1:
            registrar_pedido()
        elif op_menu == 2:
            listar_pedidos()
        elif op_menu == 3:
            imprimir_hoja_ruta()
        elif op_menu == 4:
            buscar_pedido()
        else:
            input('Presione Enter para finalizar...')
            break

if __name__ == '__main__':
    menu()