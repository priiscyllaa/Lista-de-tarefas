tarefas = []

def mostrar_menu():
    print("\n--- Lista de Tarefas ---")
    print("A. Adicionar tarefa")
    print("B. Listar tarefas")
    print("C. Atualizar tarefa")
    print("D. Remover tarefa")
    print("E. Sair")
    opcao = input("Escolha uma opção: ").upper()
    return opcao

def adicionar_tarefa():
    descricao = input("Digite a descrição da tarefa: ")
    tarefa = {'descricao': descricao, 'concluida': False}
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
    else:
        tarefas.sort(key=lambda x: x['descricao'].lower())
        for i, tarefa in enumerate(tarefas, 1):
            letra = chr(64 + i)  # Converte o número para a letra correspondente
            status = "Concluída" if tarefa['concluida'] else "Pendente"
            print(f"{letra}. {tarefa['descricao']} - {status}")

def atualizar_tarefa():
    listar_tarefas()
    if len(tarefas) > 0:
        letra = input("Digite a letra da tarefa a atualizar: ").upper()
        indice = ord(letra) - 65
        if 0 <= indice < len(tarefas):
            descricao = input("Nova descrição (deixe em branco para não alterar): ")
            if descricao:
                tarefas[indice]['descricao'] = descricao
            concluida = input("Marcar como concluída? (s/n): ").lower()
            if concluida == 's':
                tarefas[indice]['concluida'] = True
            print("Tarefa atualizada com sucesso!")
        else:
            print("Letra inválida.")

def remover_tarefa():
    listar_tarefas()
    if len(tarefas) > 0:
        letra = input("Digite a letra da tarefa a remover: ").upper()
        indice = ord(letra) - 65
        if 0 <= indice < len(tarefas):
            tarefas.pop(indice)
            print("Tarefa removida com sucesso!")
        else:
            print("Letra inválida.")

while True:
    opcao = mostrar_menu()
    if opcao == 'A':
        adicionar_tarefa()
    elif opcao == 'B':
        listar_tarefas()
    elif opcao == 'C':
        atualizar_tarefa()
    elif opcao == 'D':
        remover_tarefa()
    elif opcao == 'E':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
