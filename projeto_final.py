
# Função de adicionar tarefa à lista
def adicionar_tarefa(lista_de_tarefas, tarefa):
    lista_de_tarefas.append(tarefa)
    print('---> Tarefa adicionada com sucesso!')
    return lista_de_tarefas

# Lista as tarefas da lista já existente
def listar_tarefas(lista_de_tarefas):
    print('\n*' * 50)
    print('Tarefas a se fazer:')
    print('-'* 50)
    n = 1
    for tarefa in lista_de_tarefas:
        print(f'*{n} - {tarefa}')
        n += 1
    print('-'* 50)

# Deleta as tarefas pelos seus respectivos numeros
def deletar_tarefa(lista_de_tarefas, tarefa):
    lista_de_tarefas.pop(tarefa-1)
    return lista_de_tarefas

# Exibe o menu inicial com as opções disponiveis
def exibir_menu():
        print(' Escolha uma opção:')
        print('-'* 50)
        print(' 1 - Inserir nova tarefa ' \
        '\n 2 - Listar tarefas' \
        '\n 3 - Excluir tarefa'
        '\n 4 - Sair')
        print('-'* 50)


lista_de_tarefas = [] 
continuar = True

print('-'*50)
print('       Bem vinde à sua lista de tarefas!')
print('-'*50)
print('\n')


while continuar:
    exibir_menu()
    opcao = input('Insira o que deseja fazer: ')

    # Insere o nome da tarefa e adiciona à lista
    if opcao == '1':
        tarefa = input('Insira uma nova tarefa: ')
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)

    # Lista as tarefas existentes na lista
    elif opcao == '2':
       listar_tarefas(lista_de_tarefas)

    # Deleta a tarefa selecionada por seu respectivo numero
    elif opcao == '3':
        listar_tarefas(lista_de_tarefas)
        tarefa = input('Insira o  número da tarefa que deseja deletar:' )
        if not tarefa.isnumeric():
            print('É necessário inserir um número. Tente novamente!') # Seleciona a tarefa a se deletar apenas se o numero for válido
        elif int(tarefa) > len(lista_de_tarefas):
            print('Número invválido. Tente novamente!') # Se o numero da tarefa for menor que o numero de tarefas total da lista, ocorre um erro
        elif int(tarefa) <= 0:
            print('Números nulos não são aceitos. Tente novamente!') # Se o numero for igual ou menor a zero, o programa avisa o usúario
        else:
            tarefa = int(tarefa)
            deletar_tarefa(lista_de_tarefas, tarefa) # Caso tudo ocorra bem, deleta a tarefa escolhida

    # Para o programa
    elif opcao == '4':
        print('Programa interrompido pelo usuário.') 
        continuar = False
    
    # Se o usúario digitar uma opção não existente no menu, o programa avisa o usúario e reinicia 
    else:
        print()
        print('*** Opção inválida! Escolha uma opção existente! ***')
        print('\n')

    

print(lista_de_tarefas)