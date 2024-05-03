# Esse arquivo contém todas as funções para fazer o sistema funcionar 

class SistemaBiblioteca:
    # Função init da classe
    def __init__(self):
        self.livros = []
        self.usuarios = []

    # Função para cadastro de livros
    def cadastrar_livro(self, livro):
        self.livros.append(livro)

    # Função para cadastro de usuários
    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    # Função para empréstimos de livros para usuário x
    def emprestar_livro(self, titulo_livro, usuario):
        livro_encontrado = None
        for livro in self.livros: # Loop para buscar o livro solicitado
            if livro.titulo.lower() == titulo_livro.lower():
                livro_encontrado = livro
                break
        
        # Estrutura de decisão para emprestar caso seja encontrado
        if livro_encontrado:  
            if livro_encontrado.emprestar():
                print("Livro emprestado com sucesso!")
            else:
                print("Este livro não está disponível no momento.")
        else:
            print("Livro não encontrado.")

    # Função para devolver o livro 
    def devolver_livro(self, titulo_livro):
        livro_encontrado = None
        for livro in self.livros:
            if livro.titulo.lower() == titulo_livro.lower():
                livro_encontrado = livro
                break

        if livro_encontrado:
            livro_encontrado.devolver()
            print("Livro devolvido com sucesso!")
        else:
            print("Livro não encontrado.")

    # Função para consultar o livro
    def consultar_livros(self, termo):
        resultados = []
        for livro in self.livros:
            if termo.lower() in livro.titulo.lower() or termo.lower() in livro.autor.lower() or termo == str(livro.ano_publicacao):
                resultados.append(livro)
        return resultados
    
    # Função para gerar o relatório 
    def gerar_relatorio(self, tipo):
        if tipo == "livros_disponiveis":
            return [livro for livro in self.livros if livro.num_copias_disponiveis > 0]
        elif tipo == "livros_emprestados":
            return [livro for livro in self.livros if livro.num_copias_disponiveis < livro.num_copias]
        elif tipo == "usuarios_cadastrados":
            return self.usuarios
