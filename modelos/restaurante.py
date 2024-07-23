class Restaurante:
    nome = ''
    categoria = ''
    ativo = False
    
    
restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça da alimentação'
restaurante_praca.categoria = 'Comida variada'
restaurante_praca.ativo = False
restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]


print(restaurante_praca.nome)
