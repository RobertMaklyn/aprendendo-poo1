class Pizza:
    pedacos = 8

    def __init__(self):
        pass

    def pegar_pedaco(self):
        if Pizza.pedacos > 0:
            Pizza.pedacos -= 1
        else:
            print("Acabou a pizza")

    @classmethod
    def mudar_tamanho(cls, pedacos):
        cls.pedacos = pedacos  # Modificar o atributo de classe pedacos

print(Pizza.pedacos)
Pizza.mudar_tamanho(12)
print(Pizza.pedacos)
