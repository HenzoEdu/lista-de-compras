import json
import time
import os

def adicionar_item(compras, item, quantidade):
    compras[item] = quantidade

def remover_item(compras, item):
    try:
        del compras[item]
    except KeyError:
        print('Não é possível deletar um item inexistente!')

def visualizar_compras(compras):
    for compra in compras:
        print(f'{compra}: {compras[compra]}')
    print()
    print(f'Pressione enter para continuar')
    input()

def salvar_compras(compras, nome_arquivo):
    with open(f'{nome_arquivo}', 'w') as arquivo:
        json.dump(compras, arquivo)

def carregar_compras(nome_arquivo):
    with open(f'{nome_arquivo}', 'r') as arquivo:
        return json.load(arquivo)

def gerenciar_compras(compras, nome_arquivo=None):
    while True:
        os.system("cls" if os.name == 'nt' else "clear")
        print("""- 1 Adicionar item
- 2 Remover item
- 3 Visualizar lista
- 4 Salvar e sair
- 5 Sair sem salvar""")
        escolha = str(input('-Insira uma opção: '))

        if escolha == '1':
            item = input('Digite o nome do item:')
            try:
                quantidade = float(input('Digite a quantidade:'))
            except ValueError:
                print("Quantidade inválida. Use apenas números")
                time.sleep(1)
                continue
            adicionar_item(compras, item, quantidade)

        elif escolha =='2':
            item = input('Digite o nome do item:')
            remover_item(compras, item)
            time.sleep(1)

        elif escolha=='3':
            visualizar_compras(compras)

        elif escolha=='4':
            if nome_arquivo is None:
                nome_arquivo = input('Insira o nome do arquivo para salvar:')
            if not nome_arquivo.endswith(".json"):
                nome_arquivo += '.json'
            salvar_compras(compras, nome_arquivo)
            break

        elif escolha=='5':
            print('Voltando ao menu principal!')
            time.sleep(1)
            break

        else:
            print('Insira uma opção válida!')
            time.sleep(1)
        
def main():
    while True:
        os.system("cls" if os.name == 'nt' else "clear")
        print("""- 1 Criar uma nova lista de compras
- 2 Carregar uma lista existente
- 3 Sair""")
        escolha = input('- Escolha uma opção : ')

        if escolha == '1':
            compras = {}
            gerenciar_compras(compras)

        elif escolha == '2':
            print("Listas Disponiveis:")
            arquivos = [arquivo for arquivo in os.listdir() if arquivo.endswith(".json")]
            if not arquivos:
                print('Nenhuma lista encontrada!')
                time.sleep(3)
                continue
            for i, arquivo in enumerate(arquivos, 1):
                print(f"{i} {arquivo}")
            escolha = int(input("Escolha uma lista para carregar (0 se nenhuma)): "))
            if escolha == 0:
                continue
            if escolha < 0 or escolha > len(arquivos):
                print('Insira uma opção válida!')
                time.sleep(1)
                continue
            compras = carregar_compras(arquivos[escolha-1])
            gerenciar_compras(compras, arquivos[escolha-1])

        elif escolha == '3':
            print('Encerrando programa em:')
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('1')
            time.sleep(1)
            print('Programa encerrado!')
            break
        else:
            print('Insira uma opção válida!')
            time.sleep(1)

if __name__ == '__main__':
    main()
