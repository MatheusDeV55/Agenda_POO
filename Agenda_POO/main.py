
from agenda import Agenda
from contato import Contato

agenda = Agenda()
agenda.carregar("dados.json")

def menu():
    print("\n==== MENU AGENDA ====")
    print("1. Adicionar grupo")
    print("2. Adicionar contato")
    print("3. Listar contatos por grupo")
    print("4. Buscar contato por nome")
    print("5. Remover contato")
    print("6. Listar todos os contatos")
    print("0. Sair")

while True:
    menu()
    op = input("Escolha: ")

    if op == "1":
        nome = input("Nome do grupo: ")
        agenda.adicionar_grupo(nome)
        print("✅ Grupo adicionado.")

    elif op == "2":
        grupo_nome = input("Nome do grupo: ")
        grupo = agenda.buscar_grupo(grupo_nome)
        if grupo:
            nome = input("Nome: ")
            tel = input("Telefone: ")
            email = input("Email: ")
            cat = input("Categoria: ")
            grupo.adicionar_contato(Contato(nome, tel, email, cat))
            print("✅ Contato adicionado.")
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
            nome = input("Nome do contato a remover: ")
            grupo.remover_contato(nome)
            print("✅ Removido (se existia).")
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
        print("💾 Dados salvos. Até logo!")
        break

    else:
        print("❌ Opção inválida.")
