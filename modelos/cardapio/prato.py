from modelos.cardapio.item_cardapio import ItemCardapio 
#Conceitos de Herança!!

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.descricao = descricao
        
    def __str__(self):
        return f'{self._nome} - R$ {self._preco}'
    
    def aplicar_desconto(self): #polimorfismo
        self._preco -= self._preco * 0.8