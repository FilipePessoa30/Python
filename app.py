import os

restaurantes = ['Pizza', 'Hamburguer', 'Sushi']

def exibir_nome_do_programa():
    print('================= Ｓａｂｏｒ Ｅｘｐｒｅｓｓ =================\n')

def exibir_menu():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
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
    restaurantes.append(nome_do_restaurante)
    print(f'Restaurante {nome_do_restaurante} cadastrado com sucesso!\n')
    retornar_menu()
    
def listar_restaurantes():
    exibir_subtitulo('================= Lista de restaurantes =================\n')
    for index, restaurante in enumerate(restaurantes):
        print(f'{index + 1}. {restaurante}')
    print()
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
            print('Ativar restaurante')
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