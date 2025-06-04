def adicionar_tarefa(lista_de_tarefas, tarefa):
    lista_de_tarefas.append(tarefa)
    return lista_de_tarefas

def listar_tarefas(lista_de_tarefas):
    print('*' * 50)
    print('Tarefas a se fazer:')
    print('-'* 50)
    n = 1
    for tarefa in lista_de_tarefas:
        print(f'*{n} - {tarefa}')
        n += 1
    print('-'* 50)

def deletar_tarefa(lista_de_tarefas, tarefa):
    lista_de_tarefas.pop(tarefa-1)
    return lista_de_tarefas


def exibir_menu():
        print('\n1 - Inserir nova tarefa ' \
        '\n2 - Listar tarefas' \
        '\n3 - Excluir tarefa'
        '\n4 - Sair')


lista_de_tarefas = []
continuar = True


while continuar:
    exibir_menu()
    opcao = input('Insira o que deseja fazer: ')

    if opcao == '1':
        tarefa = input('Insira uma nova tarefa: ')
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)

    elif opcao == '2':
       listar_tarefas(lista_de_tarefas)

    elif opcao == '3':
        listar_tarefas(lista_de_tarefas)
        tarefa = input('Insira o  número da tarefa que deseja deletar:' )
        if int(tarefa) <= len(lista_de_tarefas):
            print('Número invválido, tente novamente!')
        else:
            tarefa = int(tarefa)
            deletar_tarefa(lista_de_tarefas, tarefa)

    elif opcao == '4':
        print('Programa interrompido pelo usuário.')
        continuar = False

    else:
        print()
        print('*** Opção inválida! Escolha uma opção existente! ***')
        print('\n')

    

print(lista_de_tarefas)