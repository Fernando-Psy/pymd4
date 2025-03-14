#Extrair coluna
def extrai_coluna_csv(nome_arquivo: str, indice_coluna: int, tipo_dado: str):
    coluna = []

    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        next(arquivo)

        for linha in arquivo:
            dados = linha.strip().split(',')

            valor = dados[indice_coluna]

            if tipo_dado == 'str':
                coluna.append(valor)
            elif tipo_dado == 'int':
                coluna.append(int(valor))
            elif tipo_dado == 'float':
                coluna.append(float(valor))
            else:
                coluna.append(valor)

    return coluna

#Extrair palavras
def extrai_linha_txt(nome_arquivo: str, numero_linha: int):
    palavras_linha = []


    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()


        if 0 <= numero_linha < len(linhas):
            palavras_linha = linhas[numero_linha].strip().split(' ')

    return palavras_linha