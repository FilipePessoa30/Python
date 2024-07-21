import os

print('================= Ｓａｂｏｒ Ｅｘｐｒｅｓｓ =================\n')

print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair\n')

opcao = int(input('Digite a opção desejada: '))

print(f'Opção escolhida: {opcao}')

def finalizar_app():
    print('Finalizando o app...\n')
    os.system('cls') #limpa a tela no windows
    

if opcao == 1:
    print('Cadastrar restaurante')
elif opcao == 2:
    print('Listar restaurante')
elif opcao == 3:
    print('Ativar restaurante')
else:
    finalizar_app()
    
