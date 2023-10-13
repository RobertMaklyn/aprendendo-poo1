class Pizza:
    pedacos = 8
    
    def __init__(self,sabor):
        self.sabor = sabor

    def pegar_pedaco(self):
        Pizza.pedacos -= 1

    @classmethod
    
    def mudar_tamanho(cls, pedacos):
        cls.pedacos = pedacos

    @staticmethod
    
    def ingridientes():
        return "ingredientes"

p = Pizza("frango")

print(Pizza.pedacos)
p.pegar_pedaco()
print(Pizza.pedacos)
Pizza.mudar_tamanho(12)
print(Pizza.pedacos)
print(p.ingridientes())

class carne (Pizza):
    @staticmethod
    def ingredientes ():
        return ["carne","queijo","oregano"]
    

print(carne.ingredientes())