from livros import Livro
from usuario import Usuario
from sistema import SistemaBiblioteca

def menu():
    print("\n=== Menu ===")
    print("1. Cadastrar livro")
    print("2. Cadastrar usuário")
    print("3. Emprestar livro")
    print("4. Devolver livro")
    print("5. Consultar livros")
    print("6. Gerar relatórios")
    print("0. Sair")

def main():
    sistema = SistemaBiblioteca()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            ano_publicacao = int(input("Ano de publicação: "))
            num_copias = int(input("Número de cópias: "))
            livro = Livro(titulo, autor, ano_publicacao, num_copias)
            sistema.cadastrar_livro(livro)

        elif opcao == "2":
            nome = input("Nome do usuário: ")
            identificacao = input("Identificação do usuário: ")
            contato = input("Contato do usuário: ")
            usuario = Usuario(nome, identificacao, contato)
            sistema.cadastrar_usuario(usuario)

        elif opcao == "3":
            titulo = input("Título do livro a ser emprestado: ")
            usuario_identificacao = input("Identificação do usuário: ")
            usuario = [u for u in sistema.usuarios if u.identificacao == usuario_identificacao]
            if usuario:
                sistema.emprestar_livro(titulo, usuario[0])
            else:
                print("Usuário não encontrado.")

        elif opcao == "4":
            titulo = input("Título do livro a ser devolvido: ")
            sistema.devolver_livro(titulo)

        elif opcao == "5":
            termo = input("Digite o termo de busca: ")
            resultados = sistema.consultar_livros(termo)
            print("\nResultados da busca:")
            for livro in resultados:
                print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano_publicacao}, Disponíveis: {livro.num_copias_disponiveis}")

        elif opcao == "6":
            tipo_relatorio = input("Tipo de relatório (livros_disponiveis, livros_emprestados, usuarios_cadastrados): ")
            relatorio = sistema.gerar_relatorio(tipo_relatorio)
            print("\nRelatório:")
            for item in relatorio:
                if isinstance(item, Livro):
                    print(f"Livro: {item.titulo}, Disponíveis: {item.num_copias_disponiveis}/{item.num_copias}")
                elif isinstance(item, Usuario):
                    print(f"Usuário: {item.nome}, Identificação: {item.identificacao}, Contato: {item.contato}")

        elif opcao == "0":
            print("Saindo do sistema. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
