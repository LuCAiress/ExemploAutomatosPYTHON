#ALUNOS
#Lucas Lima Aires
#Rafael de Queiroz Lavoyer
#Pedro Paulo de Avelar Fioresi Gadioli

opc = input("\n<<SELECIONE A EXPRESSÃO REGULAR DESEJADA>>\n<<1. PALAVRAS DE A E B COMEÇANDO EM A E TERMINANDO EM B>>\n<<2. SEQUÊNCIAS DE 1 E 0 COM OCORRÊNCIAS PARES>>\n<<3. SEQUÊNCIAS DE 1 E 0 COM OCORRÊNCIAS IMPARES>>\n")

#SWITCH PARA ESCOLHER AS GRAMÁTICAS

match opc:
    case '1':
        #FUNÇÕES PARA ABRIR OS ARQUIVOS
        
        entrada = open("entrada1.txt", "r")
        saida = open("saida.txt", "w")

        #EXPRESSÃO REGULAR QUE ACEITA SOMENTE PALAVRAS COM A OU B COMEÇADAS EM A E TERMINADAS EM B
        
        def valida(palavra):
            if palavra == "":
                return False
            for letra in palavra:
                if letra not in "ab":
                    return False
            if palavra[-1] == "b" and palavra[0] == "a":
                return True
            else:
                return False
            if palavra == "a" * len(palavra) or palavra == "b" * len(palavra):
                return True
            else:
                return False
            if "ab" in palavra:
                return True
            else:
                return False
                
        for linha in entrada:
            linha = linha.strip()
            if valida(linha):
                saida.write(linha +" SIM\n")
            else:
                saida.write(linha +" NÃO\n")

        entrada.close()
        saida.close()
        
    case '2':
        #FUNÇÕES PARA ABRIR OS ARQUIVOS
        
        entrada = open("entrada2.txt", "r")
        saida = open("saida.txt", "w")
        
        #EXPRESSÃO REGULAR QUE ACEITA SOMENTE ENTRADAS COM 1 E 0 E SUAS OCORRÊNCIAS DEVEM SER PARES
        
        def valida(sequencia):
            if sequencia == "":
                return False
            for num in sequencia:
                if num not in "10":
                    return False
            cont0 = 0
            cont1 = 0
            for caractere in sequencia:
                if caractere == "0":
                    cont0 += 1
                elif caractere == "1":
                    cont1 += 1
                else:
                    return False
            if cont0 % 2 == 0 and cont1 % 2 == 0:
                return True
            else:
                return False
            if sequencia == "1" * len(sequencia) or sequencia == "0" * len(sequencia):
                return True
            else:
                return False
            if "10" in sequencia:
                return True
            else:
                return False
                
        for linha in entrada:
            linha = linha.strip()
            if valida(linha):
                saida.write(linha +" SIM\n")
            else:
                saida.write(linha +" NÃO\n")

        entrada.close()
        saida.close()
    
    case '3':
        #FUNÇÕES PARA ABRIR OS ARQUIVOS
        
        entrada = open("entrada3.txt", "r")
        saida = open("saida.txt", "w")
        
        #EXPRESSÃO REGULAR QUE ACEITA SOMENTE ENTRADAS COM 1 E 0 E SUAS OCORRÊNCIAS DEVEM SER IMPARES
        
        def valida(sequencia):
            if sequencia == "":
                return False
            for num in sequencia:
                if num not in "10":
                    return False
            cont0 = 0
            cont1 = 0
            for caractere in sequencia:
                if caractere == "0":
                    cont0 += 1
                elif caractere == "1":
                    cont1 += 1
                else:
                    return False
            if cont0 % 2 != 0 and cont1 % 2 != 0:
                return True
            else:
                return False
            if sequencia == "1" * len(sequencia) or sequencia == "0" * len(sequencia):
                return True
            else:
                return False
            if "10" in sequencia:
                return True
            else:
                return False
                
        for linha in entrada:
            linha = linha.strip()
            if valida(linha):
                saida.write(linha +" SIM\n")
            else:
                saida.write(linha +" NÃO\n")

        entrada.close()
        saida.close()
