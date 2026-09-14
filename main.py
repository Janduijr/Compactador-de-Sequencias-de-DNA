from bitarray import bitarray
def ler_documento():
    with open('arquivo.txt', 'r') as arquivo:
        linhas = arquivo.read()
    
    conteudo = bitarray()
    
    for linha in linhas:
        linha = linha.strip()
        
        if linha == '':
            continue
        
        if linha.lower() == ('a'):
            conteudo.append(0)
            conteudo.append(0)
        elif linha.lower() == ('c'):
            conteudo.append(0)
            conteudo.append(1)
        elif linha.lower() == ('g'):
            conteudo.append(1)
            conteudo.append(0)
        elif linha.lower() == ('t'):
            conteudo.append(1)
            conteudo.append(1)
        else:
            pass
        
    
    return conteudo

def compactar():
    codigo = ler_documento()
    with open('compactado.bin', 'wb') as arquivo:
        codigo.tofile(arquivo)

def descompactar():
    descompactado = bitarray()
    with open ('compactado.bin', 'rb') as arquivo:
        resultado = []
        descompactado.fromfile(arquivo)
        atual = 0
        while atual <= len(descompactado):
            if descompactado[atual] == False and descompactado[atual+1] == False:
                resultado.append('A')

            elif descompactado[atual] == False and descompactado[atual+1] == True:
                resultado.append('C')

            elif descompactado[atual] == True and descompactado[atual+1] == False:
                resultado.append('G')

            elif descompactado[atual] == True and descompactado[atual+1] == True:
                resultado.append('T')

            atual += 2

        with open('descompactado.txt', 'w') as arquivo:
            atual = 0
            while atual <= len(resultado):
                arquivo.write(resultado[atual])

descompactar()







