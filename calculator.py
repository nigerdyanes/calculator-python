print("Bienvenido a tu calculador")
print("Para salir, ingrese la palabra Salir")
print("Las operaciones permitidas son: suma, resta, div, multi")

resultado = ""

while True:
    if not resultado:
        resultado = input("Ingrese un número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingrese operación: ")
    if op.lower() == "salir":
            break
    n2 = input("Ingresa siguiente número: ")
    if n2.lower() == "salir":
         break
    n2 = int(n2)

    if op == "suma":
        resultado += n2
    elif op == "resta":
         resultado -= n2
    elif op == "multi":
         resultado *= n2
    elif op == "div":
         resultado /= n2
    else:
         print("Operación no valida")
         break
    print(f"El resultado es {resultado}") 