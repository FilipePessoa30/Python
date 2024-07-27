from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça da alimentação', 'Comida variada')
restaurante_praca.avaliar('João', 5, 'Muito bom')
restaurante_praca.avaliar('Maria', 10, 'Bom')
restaurante_praca.avaliar('José', 3, 'Regular')
restaurante_praca = Restaurante('Mac Donalds', 'Fast Food')


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()