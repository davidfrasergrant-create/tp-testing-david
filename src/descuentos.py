def calcular_precio_final(monto):
    # Si el monto es negativo, lanzamos un error
    if monto < 0:
        raise ValueError("El monto no puede ser negativo")
    
    # Si supera los 10000, aplicamos el 10% de descuento
    if monto > 10000:
        descuento = monto * 0.10
        return monto - descuento
    
    # Si es 10000 o menos, devolvemos el monto original
    return monto