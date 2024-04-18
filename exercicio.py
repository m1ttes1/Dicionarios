# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
informacoes_pessoa = {'nome': 'Joaquim','idade': 23,'cidade': 'São Paulo'}

# 2 - Utilizando o dicionário criado no item 1:

#  a   Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
#  b   Adicione um campo de profissão para essa pessoa;
#  c   Remova um item do dicionário.

informacoes_pessoa['idade'] = 24 #a
informacoes_pessoa['profissao'] = 'Programador' #b
del informacoes_pessoa['cidade']    # c

#3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário. 
dicionario = {'a': 1, 'b': 2, 'c': 3} # criando um dicionário
chave = 'b'     # criando uma chave
if chave in dicionario: # verificando se a chave existe no dicionario
    print("Chave existe em dicionario") # 
    print(dicionario[chave]) 
else: # se a chave não existir no dicionario
    print("Chave não existe em dicionário")

# 5 - Escreva um código que conte a frequência de cada contagem_ em uma frase utilizando um dicionário.
frase = "O rato roeu a roupa do rei de Roma"
contagem_palavras = {} # cria um dicionário vazio
palavras = frase.split() # separa as palavras da frase
for palavra in palavras: # percorre as palavras
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1 # conta a frequência de cada palavra
print(contagem_palavras) # imprime o dicionário com as frequências de cada palavra

