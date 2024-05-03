class Livro:
    # Função init da classe livro
    def __init__(self, titulo, autor, ano_publicacao, num_copias):
        self.titulo = titulo # Variável para o título
        self.autor = autor # Variável para o autor
        self.ano_publicacao = ano_publicacao # Variável para o ano de publicação
        self.num_copias = num_copias # Variável para o número de cópias do livro no acervo
        self.num_copias_disponiveis = num_copias # Variável para a quantidade de livros que é atualizada de acordo com os empréstimos

    # Função para emprestar livros
    def emprestar(self):
        if self.num_copias_disponiveis > 0:
            self.num_copias_disponiveis -= 1 # Retira 1 cópia da quantidade total de livros do estoque caso for emprestado
            return True
        else:
            return False

    # Função para devolver livros
    def devolver(self):
        self.num_copias_disponiveis += 1 # Adiciona 1 cópia ao número total de acordo com a devolução dos livros que foram emprestados