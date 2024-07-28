from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria): #É o Construtor
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        self._comentario = []
        Restaurante.restaurantes.append(self)
        
    def __str__(self): # Método especial que retorna uma string
        return f'Nome: {self._nome} | Categoria: {self._categoria}'
    
    
    @classmethod #Se é um método referenciado a classe e não a instância (É exclusivo dessa classe)
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f'Nome: {restaurante._nome.ljust(20)}\
                | Categoria: {restaurante._categoria.ljust(20)}\
                | Avaliação: {str(restaurante.media_avaliacoes).ljust(20)}\
                | Ativo: {restaurante.ativo}')
            
    @property #sempre que uso property quero alterar como esse atributo é lido (isso é o encapsulamento)
    def ativo(self):
        return '✅' if self._ativo else '❌'
    
    def mudar_status(self): #É um método para o objeto
        self._ativo = not self._ativo
    
    def avaliar(self, cliente, nota, comentario):
        avaliacao = Avaliacao(cliente, nota, comentario)
        self._avaliacao.append(avaliacao) if avaliacao._nota <= 5 and avaliacao._nota >= 0 else print('Alguma nota foi excluida por ser maior que 5 ou menor que 0')
        self._comentario.append(comentario)
        
    @property   
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        else:
            return round(sum([avaliacao._nota for avaliacao in self._avaliacao])/len(self._avaliacao),1)
        
    # def adicionar_bebida_cardapio(self, bebida):
    #     self._cardapio.append(bebida)
        
    # def adicionar_prato_cardapio(self, prato):
    #     self._cardapio.append(prato)
    
    def adicionar_item_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
    
    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}')
        for index, item in enumerate(self._cardapio, start=1):
            if hasattr(item,'descricao'):
                print(f'  {index} - {item} - {item.descricao}')
            if hasattr(item,'tamanho'):
                print(f'  {index} - {item} - {item.tamanho}')
        