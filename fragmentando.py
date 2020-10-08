#%%
# Autor: Ícaro Gabriel Paiva Bastos
# Última modificação: 07/10/2020

#%% Definição da função splitter
def splitter(str):
    for i in range(1, len(str)):
        start = str[0:i]
        end = str[i:]
        yield (start, end)
        for split in splitter(end):
            result = [start]
            result.extend(split)
            yield result

#%% Lendo a frase de entrada
entrada = input("Olá, seja bem-vindo!\nO nosso sistema é capaz de gerar todas as combinações possíveis de quebra de uma frase\nDigite uma frase:\n")
frase = entrada

#%% Mapeando cada palavra em um número correspondente
dicionario = {}
aux = 0
for i in frase.split():
    dicionario[str(aux)] = i
    frase = frase.replace(i, str(aux))
    aux += 1
    
frase= frase.replace(' ', '')
#%%
