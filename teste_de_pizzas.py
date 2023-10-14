class Pizzaria:
    def __init__(self):
        self._pizzaolo = Pizzaolo()

    def pedido (self, pizza):
        self._pizzaolo.prepara_pizza(pizza)


class Pizzaolo:
    def __init__(self):
        self._forno = Forno ()

    def prepara_pizza(self, pizza):
        self._forno.assar(pizza)



class Forno:
    def __init__(self):
        self.pizza = []
        self.lenha = None
    
    def assar (self, pizza):
       if not self.lenha:
           print("nao tem lenha")



pizzaaria_planeta = Pizzaria()
pizzaaria_planeta.pedido("frango")