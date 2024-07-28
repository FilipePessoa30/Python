from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_praca = Restaurante('Praça da alimentação', 'Comida variada')
bebida_refri = Bebida('Coca-cola', 5.0, '600ml')
prato_comida = Prato('Strogonoff', 25.0, 'Pequeno')
restaurante_praca.adicionar_item_cardapio(bebida_refri)
restaurante_praca.adicionar_item_cardapio(prato_comida)
bebida_refri.aplicar_desconto()
prato_comida.aplicar_desconto()

def main():
    restaurante_praca.exibir_cardapio
    
if __name__ == '__main__':
    main()