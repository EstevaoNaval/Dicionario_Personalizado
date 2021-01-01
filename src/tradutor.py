# Abre um arquivo para somente leitura
with open(file="mensagem.txt",mode="r", encoding="utf8") as arqvMsgOriginal:

    for linha in arqvMsgOriginal:
        # Tira os espaços nos extremos da linha do arquivo
        linha = linha.strip()

        # Aqui eu coloco uma string contendo alguns caracteres.
        stringComCaractereOriginal = "abcdefghijqlMNopqr"

        # Depois eu coloco uma string DO MESMO TAMANHO contendo os caracteres do meu próprio dicionário
        stringComCaracterePersonalizado = "%gj)}3l[x,y&n&+\?)"

        # Aqui eu uso a função maketrans() para retornar a estrutura de dados map
        dicionarioPersonalizado = linha.maketrans(stringComCaractereOriginal, stringComCaracterePersonalizado)

        # A nova linha traduzida utilizando a função translate()
        linha = linha.translate(dicionarioPersonalizado)

        with open(file="mensagemCodificada.txt",mode="a+", encoding="utf8") as arqvMsgCodificada:
            arqvMsgCodificada.write(linha+"\n")
        



        
        


