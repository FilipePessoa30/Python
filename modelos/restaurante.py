class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria): #É o Construtor
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
        
    def __str__(self): # Método especial que retorna uma string
        return f'Nome: {self._nome} | Categoria: {self._categoria}'
    
    
    @classmethod #Se é um método referenciado a classe e não a instância (É exclusivo dessa classe)
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f'Nome: {restaurante._nome.ljust(25)} | Categoria: {restaurante._categoria.ljust(25)} | Ativo: {restaurante.ativo}')
            
    @property #sempre que uso property quero alterar como esse atributo é lido (isso é o encapsulamento)
    def ativo(self):
        return '✅' if self._ativo else '❌'
    
    def mudar_status(self): #É um método para o objeto
        self._ativo = not self._ativo
    
    
restaurante_praca = Restaurante("Bar do Zé", "Prato Feito")
restaurante_praca.mudar_status()
restaurante_pizza = Restaurante("Pizzaria do Zé", "Pizza")

restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurante_praca)
print(restaurante_pizza)

Restaurante.listar_restaurantes()