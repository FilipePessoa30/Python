import os

restaurantes = [{'nome':'Avenida', 'categoria': 'Pizza', 'ativo':False}, 
                {'nome':'Sabor', 'categoria': 'Hamburguer', 'ativo':True},
                {'nome':'Sushi', 'categoria': 'Japonesa', 'ativo':False}]

def exibir_nome_do_programa():
    print('================= Ｓａｂｏｒ Ｅｘｐｒｅｓｓ =================\n')

def exibir_menu():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')
    
def finalizar_app():
    exibir_subtitulo('App fechado \n')

    
def retornar_menu():
    input('\n Digite uma tecla para voltar ao menu principal\n')
    main()
    
def opcao_invalida():
    print('Opção inválida. Tente novamente.\n')
    retornar_menu()
    
def exibir_subtitulo(texto):
    os.system('cls') #limpa a tela no windows
    print(texto)
    print()
    
    
def cadastrar_novo_restaurante():
    exibir_subtitulo('================= Cadastrar novo restaurante =================\n')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'Restaurante {nome_do_restaurante} cadastrado com sucesso!\n')
    retornar_menu()
    
def listar_restaurantes():
    exibir_subtitulo('================= Lista de restaurantes =================\n')
    for index, restaurante in enumerate(restaurantes):
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Sim' if restaurante['ativo'] else 'Não'
        print(f'{index + 1}. Nome: {nome_restaurante.ljust(20)} | Categoria: {categoria.ljust(20)} | Ativo: {ativo}')
    print()
    retornar_menu()
    
def ativar_restaurante():
    exibir_subtitulo('================= Alterar estado do restaurante =================\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            ativar_ou_desativar = input(f'Deseja ativar ou desativar o restaurante {nome_restaurante}? (a/d): ')
            if ativar_ou_desativar == 'a':
                restaurante['ativo'] = True
                print(f'Restaurante {nome_restaurante} ativado com sucesso!\n')
                restaurante_encontrado = True
                break
            else:
                restaurante['ativo'] = False
                print(f'Restaurante {nome_restaurante} desativado com sucesso!\n')
                restaurante_encontrado = True
                break
        else:
            restaurante_encontrado = False
    if not restaurante_encontrado:
        print(f'Restaurante {nome_restaurante} não encontrado.\n')
    retornar_menu()
    
def escolher_opcao():
    try:
        opcao = int(input('Digite a opção desejada: '))

        # print(f'Opção escolhida: {opcao}')

        if opcao == 1:
            cadastrar_novo_restaurante()
        elif opcao == 2:
            listar_restaurantes()
        elif opcao == 3:
            ativar_restaurante()
        elif opcao == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()
        
    #uma opção é usar o match no Python 3.10
    #por exemplo:
    # match opcao:
    #     case 1:
    #         print('Cadastrar restaurante')
    #     case 2:
    #         print('Listar restaurante') ....
    
def main():
    os.system('cls') #limpa a tela no windows
    exibir_nome_do_programa()
    exibir_menu()
    escolher_opcao()
    
if __name__ == '__main__':
    main()