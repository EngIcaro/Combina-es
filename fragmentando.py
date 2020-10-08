#%%
# Autor: Ícaro Gabriel Paiva Bastos
# Última modificação: 07/10/2020

#%% Definição da função splitter
def splitter(frase):
    for i in range(1, len(frase)):
        start = frase[0:i]
        end = frase[i:]
        yield (start, end)
        for split in splitter(end):
            result = [start]
            result.extend(split)
            yield result

#%% Lendo a frase de entrada
entrada = input("Olá, seja bem-vindo!\nO nosso sistema é capaz de gerar todas as combinações possíveis de quebra de uma frase\nDigite uma frase:")
frase = entrada
frase = frase.split()
#%% Chamando a função splitter e passando como parâmetro a frase correspondente
combinations = list(splitter(frase))       
combinations = [list(x) for x in combinations]

#%% Convertando as listas em string
for i in range(0,len(combinations)):
    for y in range(0, len(combinations[i])):
        combinations[i][y] = ' '.join(combinations[i][y])

#%% Printando o resultado final
print('[')
entrada = '[\'' + entrada +'\']'
print(entrada)
for i in combinations:
    print(i)
print(']')
    



