class Pizza:
    pedacos = 8

    def __init__(self):
        pass

    def pegar_pedaco(self):
        if Pizza.pedacos > 0:
            Pizza.pedacos -= 1
        else:
            print("Acabou a pizza")

# Crie uma instância da classe Pizza
p = Pizza()

# Acesse o atributo de classe pedacos usando a classe Pizza
print(Pizza.pedacos)

# Chame o método pegar_pedaco da instância p
p.pegar_pedaco()
p.pegar_pedaco()

# Acesse o atributo de classe pedacos novamente usando a classe Pizza
print(Pizza.pedacos)
