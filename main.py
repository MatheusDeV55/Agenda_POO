
from agenda import Agenda
from contato import Contato
import threading
import time

agenda = Agenda()
agenda.carregar("dados.json")

# Evento para parar a thread
parar_thread = threading.Event()

# Variável de controle
ultima_qtd_contatos = 0

def listar_em_tempo_real():
    global ultima_qtd_contatos
    while not parar_thread.is_set():
        todos = [c for g in agenda.grupos for c in g.contatos]
        if len(todos) > ultima_qtd_contatos:
            novos = todos[ultima_qtd_contatos:]
            for c in novos:
                print(f"\n📌 Novo contato adicionado: {c.id} - {c.nome} - {c.telefone} - {c.email} - {c.categoria}")
            ultima_qtd_contatos = len(todos)
        time.sleep(1)  # Espera 1s para verificar de novo

#Thread de monitoramento começa
thread_listagem = threading.Thread(target=listar_em_tempo_real, daemon=True)
thread_listagem.start()

def menu():
    print("\n==== MENU ====")
    print("1. Adicionar grupo")
    print("2. Adicionar contato")
    print("3. Mostrar contato")
    print("4. Buscar nome dos contatos")
    print("5. Remover contato")
    print("6. Mostrar todos os contatos")
    print("0. Sair")

while True:
    menu()
    op = input("Escolha: ")

    if op == "1":
        nome = input("Nome do grupo: ")
        agenda.adicionar_grupo(nome)
        print("✅ Grupo adicionado sucesso.")

    elif op == "2":
        grupo_nome = input("Qual é o grupo: ")
        grupo = agenda.buscar_grupo(grupo_nome)
        if grupo:
            nome = input("Nome: ")
            tel = input("Telefone: ")
            email = input("Email: ")
            cat = input("Categoria: ")
            grupo.adicionar_contato(Contato(nome, tel, email, cat))
            print("✅ Contato adicionado sucesso.")
        else:
            print("❌ Grupo não encontrado.")

    elif op == "3":
        grupo_nome = input("Nome do grupo: ")
        grupo = agenda.buscar_grupo(grupo_nome)
        if grupo:
            print(f"\n📁 Contatos do grupo {grupo_nome}:")
            for c in grupo.listar_contatos():
                print(f"{c.id} - {c.nome} - {c.telefone} - {c.email} - {c.categoria}")
        else:
            print("❌ Grupo não encontrado.")

    elif op == "4":
        nome_busca = input("Nome do contato: ")
        achou = False
        for grupo in agenda.grupos:
            for c in grupo.contatos:
                if c.nome.lower() == nome_busca.lower():
                    print(f"{c.id} - {c.nome} - {c.telefone} - {c.email} - {c.categoria} (Grupo: {grupo.nome})")
                    achou = True
        if not achou:
            print("❌ Contato não encontrado.")

    elif op == "5":
        grupo_nome = input("Nome do grupo: ")
        grupo = agenda.buscar_grupo(grupo_nome)
        if grupo:
            try:
                contato_id = int(input("ID do contato a ser removido: "))
            except ValueError:
                print("ID inválido. Use apenas números.")
                continue
            grupo.remover_contato(contato_id)
            print("✅ Removido sucesso.")
        else:
            print("❌ Grupo não encontrado.")

    elif op == "6":
        print("\n📋 Todos os contatos:")
        achou = False
        for grupo in agenda.grupos:
            for c in grupo.contatos:
                print(f"{c.id} - {c.nome} - {c.telefone} - {c.email} - {c.categoria} (Grupo: {grupo.nome})")
                achou = True
        if not achou:
            print("⚠️ Nenhum contato encontrado.")

    elif op == "0":
        agenda.salvar("dados.json")
        #add
        parar_thread.set() #Para a thread
        #add

        print("💾 Dados salvos. Até logo!")
        break
    else:
        print("❌ Opção inválida.")    
