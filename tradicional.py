def ordena(array):
    keys = list(array.keys())
    values = list(array.values())
    
    
    for i in range(1, len(values)):
        chave = values[i]
        chavek = keys[i]
        k = i
        while k > 0 and chave < values[k - 1]:
            values[k] = values[k - 1]
            keys[k] = keys[k - 1]
            k -= 1
        values[k] = chave
        keys[k] = chavek


    ordenado = {}
    for i in range(len(values)):
        ordenado[keys[i]] = values[i]
    return ordenado
    

def letras(texto):
    letras = []
    for letra in texto:
        if letra not in letras:
            letras.append(letra)
    return letras

def dicionario(letras):
    dici = {}
    for i, letra in enumerate(letras):
        dici[letra] = str(bin(i)).split('0b')[1] # i em binario
    # print(dici)
    # return dici
    
    maior_str = len(str(dici[list(dici.keys())[0]]))
    for num_bin in list(dici.keys()):
        if maior_str < len(str(dici[num_bin])):
            maior_str = len(str(dici[num_bin]))
    
    for num_bin in list(dici.keys()):
        # if len(dici[num_bin]) < maior_str:
        while len(dici[num_bin]) - maior_str:
            dici[num_bin] = '0' + dici[num_bin]
    # print(dici)
    return dici

def printar(dici):
        print('{:5} | {:5}'.format('Letra', 'Code'))
        for k in list(dici.keys()):
            print('{:5} | {:5}'.format(k, dici[k]))

texto = 'The huffman code is boring'
texto_bin = ""

dici = dicionario(letras(texto))

for letra in texto:
    texto_bin += dici[letra]

printar(dici)

print("\n{} ({} bits)".format(texto_bin, len(texto_bin)))


# print(letras(texto))
# dicionario(letras(texto))