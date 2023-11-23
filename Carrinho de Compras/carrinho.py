class Carrinho():
    def __init__(self):
        self._produtos = []

    def total(self):
        return print(sum([p.preco for p in self._produtos]))

    def inserir_produtos(self, *produtos):
        self._produtos.extend(produtos)
        # self._produtos += produtos
        # for produto in produtos:
        #     self._produtos.append(produto)

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()

class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

#######################################

carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.50), Produto('Porshe GTR 911 Turbo', 2000000)

carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
carrinho.total()
