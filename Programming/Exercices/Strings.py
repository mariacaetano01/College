# Lista de exercícios 2 - Estruturas (strings, listas, tuplas e dicionários)
# Resolva os problemas utilizando apenas os métodos das estruturas de dados e funções nativas (embutidas).
# Não utilize estruturas de decisão (if, elif, else) ou repetição(for e while).

def palindromo(texto):

        #Faça uma função que verifique se uma texto é palíndromo;
        #argumento: texto (string) = um texto qualquer;
        #retorna bool true ou false dependendo se o texto for ou não palíndromo.

    texto = texto.lower()
    texto = texto.replace(" ","")
    texto = texto.replace("!","")
    palin = texto [::-1]
    return palin == texto

def trocaletras(texto):

        #vogais ficam maiúsculas e consoantes minúsculas;
        #argumento: texto (string) = um texto qualquer;
        #retorna texto convertido, conforme enunciado.
    texto = texto.lower()
    texto = texto.replace("a","A")
    texto = texto.replace("e","E")
    texto = texto.replace("i","I")
    texto = texto.replace("o","O")
    texto = texto.replace("u","U")
    return texto

def mesporextenso (data):

        #faça um programa que solicite data de nascimento (dd/mm/aaaa);
        #imprima com o nome do mes por extenso ("dia 99 de mês de 9999");
        #argumeento: data(string) = uma data no formato"dd/mm/aaaa";
        #retorna: string, a data no formato "99 de mês de 9999".

    dia,mes,ano = data.split('/')
    mes = mes.replace ("01","janeiro")
    mes = mes.replace ("02","fevereiro")
    mes = mes.replace("03","março")
    mes = mes.replace("04","abril")
    mes = mes.replace("05","maio")
    mes = mes.replace("06","junho")
    mes = mes.replace("07","julho")
    mes = mes.replace("08","agosto")
    mes = mes.replace("09","setembro")
    mes = mes.replace("10","outubro")
    mes = mes.replace("11","novembro")
    mes = mes.replace("12","dezembro")
    texto = (f"{dia} de {mes} de {ano}")
    return texto

def encontra_caracter(texto, caracter):

        #receba um texto e retorna a a localização da primeira aparição-
        #de um caractere solicitado;
        #argumento: texto (string) = texto qualquer;
        #argumento: caracter_procurado (string) = um caracter;
        #retorna: int = a posição do caracter.

    pos = texto.index(caracter)
    return pos

def é_azarado(num):
   
        #o útimo número não pode ser igual ao primeiro;
        #(porque isso da azar);
        #argumento: numero (string) = um numero em formato string;
        #retorna: bool true ou false, segundo enunciado.

    num = num.endswith(num[0])
    return num

def ordenamento_contrario(lista):
   
        #inverta a ordem de elementos de uma lista;
        #argumento: lista(list) = uma lista de elementos float;
        #retorna: lista, uma lista com elementos em ordem resersa.
   
    lista = lista[::-1]
    return lista

def maximo(lista):
    
        #retorna maior elemento da lista;
        #argumento: lista(list) = uma lista de elementos float;
        #retorna: o maior elemento da lista.
   return max(lista)

def minimo(lista):

        #retorna menor elemento da lista;
        #argumento: lista (list) = uma lista de elementos float;
        #retorna: o menor elemento da lista.
    return min(lista)
    
def maior_menor(lista):
        #calcule o maior e menor número da lista;
        #argumento: lista(list) = uma lista de elementos float;
        #retorna: uma tupla com dois numeros int, o maior e o menor da lista.
    return max(lista), min(lista)

def media_saltos_lista(saltos):

        #receba uma lista com saltos de um atleta e calcule a media-
        #dos seus saltos, sendo a melhor e pior posições desconsideradas;
        #argumento: saltos(list) = uma lista com saltos floar de um atleta;
        #retorna: a media de saltos de acordo com o enunciado.

    saltos.sort()
    saltos = saltos[1:-1]
    media = sum(saltos) / len(saltos)
    return media

def contem(lista, item_procurado):
        #verifica se na lista tem o item procurado e devolve em valor bool;
        #argumento: lista(list) = uma lista de elementos qualquer;
        #argumento: item_procurado(qualquer) = um item procurado na lista;
        #retorna: bool true ou false de acordo com o enunciado
    return item_procurado in lista

def conta(lista, item_procurado):
        #informa quantas ocorrências de um item ocorre em uma lista;
        #argumento: lista(list) = uma lista de elementos qualquer;
        #retorna: a quantidade de ocorrencias do item procurado.
    conta = lista.count(item_procurado)
    return conta

def mes_extenso(mes):

        #Receba um numero correspondente ao mês e devolva por extenso;
        #use abreviatura do mes com 3 letras;
        #use uma lista com os nomes dos meses;
        #argumento: mes(list) = uma lista de 1 a 12 correspondente aos meses;
        #retorna: string a abreviatura do mês;

    lista = [
            "jan",
            "fev",
            "mar",
            "abr",
            "mai",
            "jun",
            "jul",
            "ago",
            "set",
            "out",
            "nov",
            "dez"
            ]
    mes = lista[mes-1]
    return mes
    
def media_temperaturas(temperaturas):

        #retorna media de temperaturas da lista;
        #argumento: temperaturas (lista) = lista de temperaturas float;
        #retorna: float, a media de temperaturas.

    soma = sum(temperaturas)
    media = soma / len(temperaturas)
    return media 

def leet(texto):

        #converte um texto em leet. Veja os testes para exemplo:
        #dicionário para usar na conversão:

    dictionary = {
        "a":"4",
        "A":"4",
        "e":"3",
        "E":"3",
        "g":"9",
        "G":"9",
        "i":"1",
        "I":"1",
        "s":"5",
        "S":"5",
        "t":"7",
        "T":"7",
        "o":"0",
        "O":"0"
        }

        #argumento: texto(string) = um texto qualquer;
        #retorna: string, texto convertido conforme enunciado.

    texto = texto.replace("a","4")
    texto = texto.replace("A","4")
    texto = texto.replace("e","3")
    texto = texto.replace("E","3")
    texto = texto.replace("i","1")
    texto = texto.replace("I","1")
    texto = texto.replace("o","0")
    texto = texto.replace("O","0")
    texto = texto.replace("g","9")
    texto = texto.replace("G","9")
    texto = texto.replace("t","7")
    texto = texto.replace("T","7")
    texto = texto.replace("s","5")
    texto = texto.replace("S","5")
    return texto

def apaga(texto, n):

        #seja string ou int, devolve nova string sem a posiçção n;
        #argumento: texto(string) = um texto qualquer;
        #retorna: o texto convertido conforme enunciado.

    texto = texto[:n] + texto[n + 1:]
    return texto

# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0

def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = "\033[31m%s" % "Falhou"
    else:
        prefixo = "\033[32m%s" % "Passou"
        acertos += 1
    print(
        "%s Esperado: %s \tObtido: %s\033[1;m" % (prefixo, repr(esperado), repr(obtido))
    )

def main():
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista2 = [-1, 0]
    lista3 = [-10, 0, 10, 2, 100, -100, -100.1]
    lista4 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

    print(" Palíndromo:")
    test(palindromo("ovo"), True)  # normal
    test(palindromo("Ovo"), True)  # mudança de caixa
    test(palindromo("Ovo "), True)  # espaço no final
    test(palindromo(" Ovo "), True)  # espaço no início
    test(palindromo("Assam a massa"), True)  # frases (espaços em branco)
    test(palindromo("Ame o poema!"), True)  # frases com pontuação

    
    print(" Troca caixa:")
    test(trocaletras("Araquari"), "ArAqUArI")  # normal
    test(trocaletras("Caxias do Sul"), "cAxIAs dO sUl")  # com espaços
    test(trocaletras("joinville"), "jOInvIllE")  # com espaços
    test(trocaletras("ITAJAI"), "ItAjAI")  # com espaços

    print(" Mês por extenso:")
    test(mesporextenso("19/05/2014"), "19 de maio de 2014")
    test(mesporextenso("25/12/2016"), "25 de dezembro de 2016")


    print(" Encontra caracter:")
    test(encontra_caracter("--*--", "*"), 2)
    test(encontra_caracter("19/05/2014", "/"), 2)


    print(" É azarado:")
    test(é_azarado("213452"), True)
    test(é_azarado("213451"), False)

    print(" Listas invertidas:")
    test(ordenamento_contrario(lista1), ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    test(ordenamento_contrario(lista2), ([0, -1]))
    test(ordenamento_contrario(lista3), ([-100.1, -100, 100, 2, 10, 0, -10]))

    print(" Maior elemento da lista:")
    test(maximo(lista1), 10)
    test(maximo(lista2), 0)
    test(maximo(lista3), 100)
    test(maximo(lista4), -1)

    print(" Maior elemento da lista:")
    test(minimo(lista1), 1)
    test(minimo(lista2), -1)
    test(minimo(lista3), -100.1)
    test(minimo(lista4), -10)

    print(" Maior e o menor elementos da lista:")
    test(maior_menor(lista1), (10, 1))
    test(maior_menor(lista2), (0, -1))
    test(maior_menor(lista3), (100, -100.1))
    test(maior_menor(lista4), (-1, -10))

    print(" Média dos saltos em lista:")
    test(media_saltos_lista([10, 10, 10, 10, 10]), 10)
    test(media_saltos_lista([9, 9.1, 8, 7, 6.9]), 8)
    test(media_saltos_lista([1, 1, 3, 5, 5]), 3)
    test(media_saltos_lista([10, 10, 9.9, 10, 10]), 10)
    test(media_saltos_lista([1, 4.5, 0, 7, 5]), 3.5)

    print("Possui item:")
    test(contem([1, 2, 3, 4, 5], 6), False)
    test(contem([1, 2, 3, 4, 5], 3), True)
    test(contem(["b", "s", "i"], "i"), True)
    test(contem(["b", "s", "i"], "S"), False)

    print("Conta itens:")
    test(conta([1, 2, 3, 4, 5], 6), 0)
    test(conta([1, 2, 3, 4, 5], 1), 1)
    test(conta([1, 2, 1, 4, 1], 1), 3)
    test(conta(["b", "s", "i"], "i"), 1)
    test(conta(["b", "s", "i"], "S"), 0)
    test(conta(["b", "s", "i", "i", "f", "c"], "i"), 2)

    print("Mês por extenso:")
    test(mes_extenso(1), "jan")
    test(mes_extenso(2), "fev")
    test(mes_extenso(12), "dez")

    print("Média das temperaturas:")
    test(media_temperaturas([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 10.0)
    test(media_temperaturas([10, 12, 9, 13, 12, 10, 9, 13, 10, 12, 9, 13]), 11.0)

    print("leet")
    test(leet("ifc"), "1fc")
    test(leet("fisl2013"), "f15l2013")
    test(leet("deco"), "d3c0")
    test(leet("EMO"), "3M0")
    test(leet("restart"), "r3574r7")
    test(leet("infeliz"), "1nf3l1z")
    test(leet("The Cure"), "7h3 Cur3")
    test(leet("Eu te amo"), "3u 73 4m0")

    print("Apaga")
    test(apaga("kitten", 1), "ktten")
    test(apaga("kitten", 0), "itten")
    test(apaga("kitten", 2), "kiten")
    test(apaga("kitten", 4), "kittn")
    test(apaga("Hi", 0), "i")
    test(apaga("Hi", 1), "H")
    test(apaga("code", 0), "ode")
    test(apaga("code", 1), "cde")
    test(apaga("code", 2), "coe")
    test(apaga("code", 3), "cod")
    test(apaga("chocolate", 8), "chocolat")


if __name__ == "__main__":
    main()
    print(
        "\n%d Testes, %d Ok, %d Falhas: Nota %.1f"
        % (total, acertos, total - acertos, float(acertos * 10) / total)
    )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")