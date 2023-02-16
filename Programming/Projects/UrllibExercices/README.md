# StarbuzzUrllib
Projeto apresentado como requisito na disciplina de Algorítmos e Programação II do curso de Bacharelado em Sistemas da Informação, 
do Instituto Federal Catarinense - Campus Araquari.

### Funções
O arquivo "MessageFunctions" contém os métodos de envio de mensagem utilizado no arquivo principal.  Ele não foi 
desenvolvido com nenhum método de testes, portanto, as funções não seguem padrões.

### Projeto
O arquivo "URLProject" contém o projeto princial, nele há o código principal de verificação de preço do café no site fictício do Starbuzz
e envio de mensagem quando o mesmo estiver de acordo com os padrões estipulados.

### Testes
O arquivo "UrllibTests" contém um código semelhante ao do projeto principal. Este arquivo é usado para eventuais modificações futuras.

# Instalação do Projeto

---

### Requisitos
- Poetry - [Tutorial de instalação](https://python-poetry.org/docs/#installation)

### Instalação

Abra um terminal e clone este repositório:
```bash
git clone https://github.com/jhonathasmoura/Validador_CPF.git
```

Entre na pasta do projeto:
```bash
cd Validador_CPF
```

Instale as dependências:
```bash
poetry install
```

Inicie um novo shell e ative o ambiente virtual:
```bash
poetry shell
```

### Testes

```bash
python test_validador_cpf.py
```

### Execução

```bash
python validador_cpf.py
```
