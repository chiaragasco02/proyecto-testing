def calcular_descuento(precio, descuento):
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")

    if descuento < 0 or descuento > 100:
        raise ValueError("El descuento debe estar entre 0 y 100")

    precio_final = precio - (precio * descuento / 100)
    return precio_final


resultado = calcular_descuento(1000, 20)
print(resultado)