class Pizza:
    pedacos = 8

    def __init__(self):
        pass

    def pegar_pedaco(self):
        if Pizza.pedacos > 0:
            Pizza.pedacos -= 1
        else:
            print("acabou a pizza")

    @classmethod

    def mudar_tamanho(cls, pedacos):
        cls.pedacos = pedacos

p = Pizza()
print(Pizza.pedacos)
p.pegar_pedaco()
p.pegar_pedaco()
print(Pizza.pedacos)
Pizza.mudar_tamanho(12)
print(Pizza.pedacos)
p.pegar_pedaco()
p.pegar_pedaco()
print(p.pedacos)