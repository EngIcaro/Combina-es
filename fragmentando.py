#%%
# Autor: Ícaro Gabriel Paiva Bastos
# Última modificação: 07/10/2020

entrada = "icaro meu querido icaro rato oi"

def splitter(str):
    for i in range(1, len(str)):
        start = str[0:i]
        end = str[i:]
        yield (start, end)
        for split in splitter(end):
            result = [start]
            result.extend(split)
            yield result

