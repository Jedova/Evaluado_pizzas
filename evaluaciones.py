from pizza import Pizza

print ("Precio:", Pizza.precio)
print ("Tmaño:", Pizza.tamaño)

##Ingredientes sin instancias

print("¿La salsa de tomate está en la lista?", Pizza.validar_elemento
      ("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

##Datos del usuario##
mi_pizza = Pizza()
mi_pizza.realizar_pedido()

##Información resumen##
print("\n--- Detalle del pedido ---")
print("Ingrediente proteico:", mi_pizza.ingrediente_proteico)
print("Ingredientes vegetales:", mi_pizza.ingredientes_vegetales)
print("Tipo de masa:", mi_pizza.tipo_masa)
print("¿Pizza válida?", mi_pizza.pizza_valida)

##Ejecucion del error solicitado##

print("¿Pizza válida desde la clase?", Pizza.pizza_valida)


