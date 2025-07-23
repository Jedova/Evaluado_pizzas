from ingredientes import proteicos, vegetales, masas

class Pizza:
    ##todas las instancias compartiran las siguientes atributos de clases

    precio=10000
    tamaño="familiar"

    def __init__(self):
        self.ingredientes_vegetales = []
        self.ingrediente_proteico = None
        self.tipo_masa = None
        self.pizza_valida = None

    @staticmethod
    def validar_elemento(elemento, lista_valores):
        ## Método estático que valida si el elemento está en la lista permitida
        return elemento in lista_valores

    def realizar_pedido(self):
        ## Se piden los ingredientes al usuario y se almacenan en la instancia
        self.ingrediente_proteico = input("Ingrese un ingrediente proteico: ").lower()
        vegetal1 = input("Ingrese el primer ingrediente vegetal: ").lower()
        vegetal2 = input("Ingrese el segundo ingrediente vegetal: ").lower()
        self.tipo_masa = input("Ingrese el tipo de masa: ").lower()

        self.ingredientes_vegetales = [vegetal1, vegetal2]

        ## Se valida que todos los ingredientes ingresados sean válidos
        proteico_valido = Pizza.validar_elemento(self.ingrediente_proteico, proteicos)
        vegetales_validos = all(Pizza.validar_elemento(i, vegetales) for i in self.ingredientes_vegetales)
        masa_valida = Pizza.validar_elemento(self.tipo_masa, masas)

        ## Se define si la pizza es válida o no
        self.pizza_valida = proteico_valido and vegetales_validos and masa_valida