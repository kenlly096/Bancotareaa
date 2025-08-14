from datetime import datetime

clientes = {}

#  Crear cliente
def crear_cliente():
    cc = input("CC: ")
    nombre = input("Nombre: ")
    email = input("Email: ")
    edad = int(input("Edad: "))
    movil = input("Móvil: ")
    fijo = input("Fijo: ")
    pais = input("País: ")
    dep = input("Departamento: ")
    ciudad = input("Ciudad: ")
    dia = input("Día: ")

    clientes[cc] = {
        "nombre": nombre,
        "email": email,
        "edad": edad,
        "contacto": {"movil": movil, "fijo": fijo},
        "ubicacion": {"pais": pais, "dep": dep, "ciudad": ciudad, "dia": dia},
        "productos": []
    }
    print(" Cliente creado.")

#  Crear producto (cuenta o crédito)
def crear_producto():
    cc = input("CC del cliente: ")
    if cc in clientes:
        tipo = input("Tipo de producto (ahorros, corriente, cdt, libre, vivienda, auto): ")
        idp = f"{tipo[:3].upper()}-{len(clientes[cc]['productos'])+1}"
        producto = {
            "tipo": tipo,
            "id": idp,
            "fecha_inicio": datetime.now().strftime("%Y-%m-%d"),
            "estado": "Activo",
            "saldo": 0.0,
            "historial": []
        }
        clientes[cc]["productos"].append(producto)
        print(f" Producto {idp} creado.")
    else:
        print(" Cliente no encontrado.")

#  Buscar producto
def buscar_producto(cc, idp):
    for p in clientes[cc]["productos"]:
        if p["id"] == idp:
            return p
    return None

#  Registrar movimiento
def registrar_movimiento(producto, descripcion, monto):
    producto["historial"].append({
        "id": len(producto["historial"]) + 1,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "descripcion": descripcion,
        "monto": monto
    })

#  Depositar dinero
def depositar():
    cc = input("CC del cliente: ")
    idp = input("ID del producto: ")
    monto = float(input("Monto a depositar: "))
    if cc in clientes:
        producto = buscar_producto(cc, idp)
        if producto and producto["estado"] == "Activo":
            producto["saldo"] += monto
            registrar_movimiento(producto, "Depósito", monto)
            print(" Depósito realizado.")
        else:
            print(" Producto no encontrado o inactivo.")
    else:
        print(" Cliente no encontrado.")

#  Retirar dinero
def retirar():
    cc = input("CC del cliente: ")
    idp = input("ID del producto: ")
    monto = float(input("Monto a retirar: "))
    if cc in clientes:
        producto = buscar_producto(cc, idp)
        if producto and producto["estado"] == "Activo":
            if producto["saldo"] >= monto:
                producto["saldo"] -= monto
                registrar_movimiento(producto, "Retiro", -monto)
                print(" Retiro realizado.")
            else:
                print(" Saldo insuficiente.")
        else:
            print(" Producto no encontrado o inactivo.")
    else:
        print(" Cliente no encontrado.")

#  Solicitar crédito
def solicitar_credito():
    cc = input("CC del cliente: ")
    tipo = input("Tipo de crédito (libre, vivienda, auto): ")
    monto = float(input("Monto solicitado: "))
    if cc in clientes:
        idp = f"{tipo[:3].upper()}-{len(clientes[cc]['productos'])+1}"
        producto = {
            "tipo": tipo,
            "id": idp,
            "fecha_inicio": datetime.now().strftime("%Y-%m-%d"),
            "estado": "Activo",
            "saldo": monto,
            "historial": []
        }
        registrar_movimiento(producto, "Crédito aprobado", monto)
        clientes[cc]["productos"].append(producto)
        print(f" Crédito {idp} aprobado.")
    else:
        print(" Cliente no encontrado.")

#  Pagar cuota de crédito
def pagar_cuota():
    cc = input("CC del cliente: ")
    idp = input("ID del crédito: ")
    monto = float(input("Monto de la cuota: "))
    if cc in clientes:
        producto = buscar_producto(cc, idp)
        if producto and producto["estado"] == "Activo":
            producto["saldo"] -= monto
            registrar_movimiento(producto, "Pago cuota", -monto)
            if producto["saldo"] <= 0:
                producto["estado"] = "Pagado"
            print(" Cuota pagada.")
        else:
            print(" Crédito no encontrado o inactivo.")
    else:
        print(" Cliente no encontrado.")

#  Cancelar producto
def cancelar_producto():
    cc = input("CC del cliente: ")
    idp = input("ID del producto: ")
    if cc in clientes:
        producto = buscar_producto(cc, idp)
        if producto:
            producto["estado"] = "Cancelado"
            registrar_movimiento(producto, "Cancelación", 0)
            print(" Producto cancelado.")
        else:
            print(" Producto no encontrado.")
    else:
        print(" Cliente no encontrado.")

# Menú principal
def menu():
    while True:
        print("\n--- MENÚ BANCO ---")
        print("1. Crear cliente")
        print("2. Crear producto")
        print("3. Depositar dinero")
        print("4. Solicitar crédito")
        print("5. Retirar dinero")
        print("6. Pagar cuota crédito")
        print("7. Cancelar producto")
        print("8. Salir")
        op = input("Opción: ")

        if op == "1":
            crear_cliente()
        elif op == "2":
            crear_producto()
        elif op == "3":
            depositar()
        elif op == "4":
            solicitar_credito()
        elif op == "5":
            retirar()
        elif op == "6":
            pagar_cuota()
        elif op == "7":
            cancelar_producto()
        elif op == "8":
            print("Saliendo del sistema.")
            break
        else:
            print(" Opción inválida.")

menu()