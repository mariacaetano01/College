# ShuffleWords (Embaralha Palavras)
Projeto apresentado como requisito na disciplina de Algorítmos e Programação II do curso de Bacharelado em Sistemas da Informação, 
do Instituto Federal Catarinense - Campus Araquari.

### Métodos do Jogo
O arquivo "gamefuncs.py" contém os métodos utilizados para desenvolvimento do jogo, utilizados nos demais arquivos. Ele não foi 
desenvolvido com nenhum método de testes, portanto, as funções não seguem padrões.

### O Embaralhador
O arquivo "ShuffleWords.py" é o principal arquivo no projeto, nele há o código principal do jogo de palavras sem interface
gráfica. Nele, o usuário
seleciona uma categoria (tema) de palavras e o nível de dificuldade, então tem um número limitado de tentativas para descobrir qual
a palavra, cujo próprio jogo verificará e mostrará a usuário a verificação.

### O Embaralho: Interface Gráfica
O arquivo "ShuffleWordsTkinter.py" é o arquivo que contém a estrutura do jogo dentro de uma interface gráfica para o usuário,
baseadas nas funções do "gamefuncs.py". (A interface ainda não está finalizada).

### Categorias
O arquivos "categories.JSON" é um arquivo JSON em python que contém as palavra usadas pelo algorítmo principal para que o jogo
funcione, separando tais palavras em categorias e dificuldades dentro de cada categoria.

### Instalação do Projeto
Este projeto foi desenvolvido em um ambiente virtual com poetry https://python-poetry.org/docs/#installing-with-the-official-installer
