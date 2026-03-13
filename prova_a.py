"""
PROVA A - Fundamentos de Python para IA
Duração: 90 minutos | Valor Total: 100 pontos

Instruções:
- Preencha as funções abaixo implementando a lógica solicitada.
- Você é responsável por testar o seu próprio código. Sinta-se à vontade para 
  criar chamadas de teste no final do arquivo para garantir que a lógica funciona.
- Quando terminar, faça o commit e o push para o repositório.
"""

# ==============================================================================
# Questão 1: Manipulação de Dicionário (20 pontos)
# ==============================================================================
# Dado um texto (string), retorne um dicionário onde as chaves são as palavras 
# e os valores são o número de vezes que cada palavra aparece no texto.
def contar_frequencia(texto):
    
    palavras = texto
    frequencia = {}
    
    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1
            
    return frequencia

texto = "A carteira enviou uma carta e depois sentou na carteira mas percebeu que perdeu a carteira"
resultado = contar_frequencia(texto)
print(resultado)

#eu só consigui fazer as letras contarem

# ==============================================================================
# Questão 2: Funções Lambda e Map (20 pontos)
# ==============================================================================
# Dada uma lista de números inteiros, utilize a função `map` em conjunto com 
# uma função `lambda` para criar e retornar uma nova lista onde cada elemento 
# é o quadrado do valor original.
numeros = [2, 5, 6, 8, 9]
def elevar_ao_quadrado(numeros):
    return list(map(lambda x: x ** 2, numeros))

print(elevar_ao_quadrado(numeros))


# ==============================================================================
# Questão 3: Funções Lambda e Filter (20 pontos)
# ==============================================================================
# Dada uma lista de nomes, utilize a função `filter` e uma função `lambda` 
# para retornar uma lista apenas com os nomes que possuem 3 letras ou menos.
nomes = ["rafael", "jon", "bruno", "teo", "leo"]

def filtrar_nomes_curtos(nomes):
    return list(filter(lambda nome : len(nome) <= 3, nomes))

print(filtrar_nomes_curtos(nomes))

# ==============================================================================
# Questão 4: Recursão (20 pontos)
# ==============================================================================
# Crie uma função recursiva que calcule a soma de todos os números numa lista.
numeros2 = [5, 5, 10, 20, 30]

def soma_recursiva(lista):
    soma = 0
    for x in lista:
        soma += x
    return soma

print(soma_recursiva(numeros2)) 

def soma_lista(lista, quantidade):

    if quantidade < 1:
        return 0
    return lista[quantidade-1] + soma_lista(lista, quantidade-1)

# ==============================================================================
# Questão 5: Teoria aplicada à IA (20 pontos)
# ==============================================================================
# "Na preparação de dados para modelos de Machine Learning, é comum evitarmos 
# o uso extensivo de laços `for` tradicionais em Python, dando preferência a 
# abordagens funcionais (como map/filter) ou bibliotecas vetorizadas. 
# Explique, com as suas palavras, por que essa prática é adotada e qual a vantagem 
# das funções lambda nesse contexto."

RESPOSTA_Q5 = """
Essa prática é adotada para aumentar a eficiência e o desempenho, pois operações vetorizadas 
são processadas muito mais rápido que o for tradicional, 
e também torna o código mais legível, sendo as funções lambda vantajosas nesse caso 
por permitirem criar transformações rápidas de 
forma compacta, sem precisar declarar uma função completa pra fazer tarefas simples. 

"""

if __name__ == "__main__":
    # Área livre para testes locais do aluno.
    # Exemplo: print(contar_frequencia("teste de mesa teste"))
    pass
