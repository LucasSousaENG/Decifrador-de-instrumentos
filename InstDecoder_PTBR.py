import unidecode
import os


#Decifrador de símbolos
############################################################################
def decsymbol():      #Esta função filtra a pesquisa de símbolos no dicionário
    symb = []

    #O numeral presente ao final da variável dic indica a posição da letra (1 = primeiro)
    dicsym = {"ARC": "Controlador registrador de análise", "AIC": "Controlador indicador de análise", "AC": "Controlador de análise", "AR": "Leitor registrador de análise", "AI": "Leitor indicador de análise", "ASH": "Chave e alarme de alta de análise", "ASL": "Chave e alarme de baixa de análise", "ASHL": "Chave e alarme de alta e baixa de análise", "ART": "Transmissor registrador de análise", "AIT": "Transmissor indicador de análise", "AT": "Transmissor de análise", "AY": "Relé de análisador", "AE": "Elemento primário de análise", "AP": "Ponto de teste de análise", "AW": "Prova de análise", "BG": "Dispositivo visual de análise ou queima", "AV": "Elemento final de análise",
    "BRC": "Controlador registrador de queima", "BIC": "Controlador indicador de queima", "BC": "Controlador de queimador", "BR": "Leitor registrador de queimador", "BI": "Leitor indicador de queima",  "BSH": "Chave e alarme de alta de queimador", "BSL": "Chave e alarme de baixa de queimador", "BSHL": "Chave e alarme de alta e baixa de queimador", "BRT": "Transmissor registrador de queimador", "BIT": "Transmissor indicador de queimador", "BT": "Transmissor de queimador", "BY": "Relé de queimador", "BE": "Elemento primário de queimador", "BW": "Prova de queimador", "BG": "Dispositivo de visualização de queimador", "BZ": "Elemento final de queimador", 
    "ERC": "Controlador registrador de voltagem", "EIC": "Controlador indicador de voltagem", "EC": "Controlador de voltagem", "ER": "Leitor registrador de voltagem", "EI": "Leitor indicador de voltagem","ESH": "Chave e alarme de alta de voltagem", "ESL": "Chave e alarme de baixa de voltagem", "ESHL": "Chave e alarme de alta e baixa de voltagem","ERT": "Transmissor registrador de voltagem", "EIT": "Transmissor indicador de voltagem", "ET": "Transmissor de voltagem", "EY": "Relé de voltagem", "EE": "Elemento primário de voltagem", "EZ": "Elemento final de voltagem",
    "FRC": "Controlador registrador de vazão", "FIC": "Controlador indicador de vazão", "FC": "Controlador de vazão", "FCV": "Controlador de válvula de controle auto atuada de vazão","FICV": "Controlador de válvula de controle auto atuada de vazão", "FR": "Leitor registrador de vazão", "FI": "Leitor indicador de vazão","FSH": "Chave e alarme de alta de vazão", "FSL": "Chave e alarme de baixa de vazão", "FSHL": "Chave e alarme de alta e baixa de vazão", "FRT": "Transmissor registrador de vazão", "FIT": "Transmissor indicador de vazão", "FT": "Transmissor de vazão", "FY": "Relé de vazão", "FE": "Elemento primário de vazão", "FP": "Ponto de teste de vazão", "FG": "Dispositivo de visualização de vazão", "FV": "Elemento final de vazão",
    "FQRC": "Controlador registrador de quantidade de vazão", "FQIC": "Controlador indicador de quantidade de vazão", "FQR": "Leitor registrador de quantidade de vazão", "FQI": "Leitor indicador de quantidade de vazão","FQSH": "Chave e alarme de alta de quantidade de vazão", "FQSL": "Chave e alarme de baixa de quantidade de vazão", "FQIT": "Transmissor indicador de quantidade de vazão", "FQT": "Transmissor de quantidade de vazão", "FQY": "Relé de quantidade de vazão", "FQE": "Elemento primário de quantidade de vazão", "FQV": "Elemento final de quantidade de vazão",
    "FFRC": "Controlador registrador de flow ratio", "FFIC": "Controlador indicador de flow ratio", "FFC": "Controlador de flow ratio", "FFR": "Leitor registrador de flow ratio", "FFI": "Leitor indicador de flow ratio","FFSH": "Chave e alarme de alta de flow ratio", "FFSL": "Chave e alarme de baixa de flow ratio", "FFE": "Elemento primário de flow ratio", "FFV": "Elemento final de flow ratio",
    "HIC": "Controlador indicador de hand", "HC": "Controlador de hand", "HS": "Chave de alarme de alta e baixa de hand", "HV": "Elemento final de hand",
    "IRC": "Controlador registrador de corrente", "IIC": "Controlador indicador de corrente", "IR": "Leitor registrador de corrente", "II": "Leitor indicador de corrente", "ISH": "Chave e alarme de alta de corrente", "ISL": "Chave e alarme de baixa de corrente", "ISHL": "Chave e alarme de alta e baixa de corrente", "IRT": "Transmissor registrador de corrente", "IIT": "Transmissor indicador de corrente", "IT": "Transmissor de corrente", "IY": "Relé de corrente", "IE": "Elemento primário de corrente", "IZ": "Elemento final de corrente",
    "JRC": "Controlador registrador de potência", "JIC": "Controlador indicador de potência", "JR": "Leitor registrador de potência", "JI": "Leitor indicador de potência", "JSH": "Chave e alarme de alta de potência", "JSL": "Chave e alarme de baixa de potência", "JSHL": "Chave e alarme de alta e baixa de potência", "JRT": "Transmissor registrador de potência", "JIT": "Transmissor indicador de potência", "JT": "Transmissor de potência", "JY": "Relé de potência", "JE": "Elemento primário de potência", "JV": "Elemento final de potência",
    "KRC": "Controlador registrador de tempo", "KIC": "Controlador indicador de tempo", "KC": "Controlador de tempo", "KCV": "Controlador de válvula de controle auto atuada temporizada", "KR": "Leitor registrador de tempo", "KI": "Leitor indicador de tempo", "KSH": "Chave e alarme de alta de tempo", "KSL": "Chave e alarme de baixa de tempo", "KSHL": "Chave e alarme de alta e baixa de tempo", "KRT": "Transmissor registrador de tempo", "KIT": "Transmissor indicador de tempo", "KT": "Transmissor de tempo", "KY": "Relé de tempo", "KE": "Elemento primário de tempo", "KV": "Elemento final de tempo",
    "LRC": "Controlador registrador de nível", "LIC": "Controlador indicador de nível", "LC": "Controlador de nível", "LCV": "Controlador de válvula de controle auto atuada nívelrizada", "LR": "Leitor registrador de nível", "LI": "Leitor indicador de nível", "LSH": "Chave e alarme de alta de nível", "LSL": "Chave e alarme de baixa de nível", "LSHL": "Chave e alarme de alta e baixa de nível", "LRT": "Transmissor registrador de nível", "LIT": "Transmissor indicador de nível", "LT": "Transmissor de nível", "LY": "Relé de nível", "LE": "Elemento primário de nível", "LW": "Prova de nível", "LG": "Dispositivo de visualização de nível", "LV": "Elemento final de nível",
    "PRC": "Controlador registrador de pressão", "PIC": "Controlador indicador de pressão", "PC": "Controlador de pressão", "PCV": "Controlador de válvula de controle auto atuade pressãorizada", "PR": "Leitor registrador de pressão", "PI": "Leitor indicador de pressão", "PSH": "Chave e alarme de alta de pressão", "PSL": "Chave e alarme de baixa de pressão", "PSHL": "Chave e alarme de alta e baixa de pressão", "PRT": "Transmissor registrador de pressão", "PIT": "Transmissor indicador de pressão", "PT": "Transmissor de pressão", "PY": "Relé de pressão", "PE": "Elemento primário de pressão", "PP": "Ponto de teste de pressão", "PSV": "Dispositivo de segurança de pressão", "PV": "Elemento final de pressão",
    "PDRC": "Controlador registrador de pressão diferencial", "PDIC": "Controlador indicador de pressão diferencial", "PDC": "Controlador de pressão diferencial", "PDCV": "Controlador de válvula de controle auto atuade pressão diferencialrizada", "PDR": "Leitor registrador de pressão diferencial", "PDI": "Leitor indicador de pressão diferencial", "PDSH": "Chave e alarme de alta de pressão diferencial", "PDSL": "Chave e alarme de baixa de pressão diferencial", "PDRT": "Transmissor registrador de pressão diferencial", "PDIT": "Transmissor indicador de pressão diferencial", "PDT": "Transmissor de pressão diferencial", "PDY": "Relé de pressão diferencial", "PE": "Elemento primário de pressão diferencial", "PP": "Ponto de teste de pressão diferencial", "PSE": "Dispositivo de segurança de pressão diferencial",
    "QRC": "Controlador registrador de quantidade", "QIC": "Controlador indicador de quantidade", "QR": "Leitor registrador de quantidade", "QI": "Leitor indicador de quantidade", "QSH": "Chave e alarme de alta de quantidade", "QSL": "Chave e alarme de baixa de quantidade", "QSHL": "Chave e alarme de alta e baixa de quantidade", "QRT": "Transmissor registrador de quantidade", "QIT": "Transmissor indicador de quantidade", "QT": "Transmissor de quantidade", "QY": "Relé de quantidade", "QE": "Elemento primário de quantidade", "QZ": "Elemento final de quantidade",
    "RRC": "Controlador registrador de radiação", "RIC": "Controlador indicador de radiação", "RC": "Controlador de radiação", "RR": "Leitor registrador de radiação", "RI": "Leitor indicador de radiação", "RSH": "Chave e alarme de alta de radiação", "RSL": "Chave e alarme de baixa de radiação", "RSHL": "Chave e alarme de alta e baixa de radiação", "RRT": "Transmissor registrador de radiação", "RIT": "Transmissor indicador de radiação", "RT": "Transmissor de radiação", "RY": "Relé de radiação", "RE": "Elemento primário de radiação", "RW": "Prova de radiação", "RZ": "Elemento final de radiação",
    "SRC": "Controlador registrador de velocidade/frequência", "SIC": "Controlador indicador de velocidade/frequência", "SC": "Controlador de velocidade/frequência", "SCV": "Controlador de válvula de controle auto atuada velocidade/frequênciarizada", "SR": "Leitor registrador de velocidade/frequência", "SI": "Leitor indicador de velocidade/frequência", "SSH": "Chave e alarme de alta de velocidade/frequência", "SSL": "Chave e alarme de baixa de velocidade/frequência", "SSHL": "Chave e alarme de alta e baixa de velocidade/frequência", "SRT": "Transmissor registrador de velocidade/frequência", "SIT": "Transmissor indicador de velocidade/frequência", "ST": "Transmissor de velocidade/frequência", "SY": "Relé de velocidade/frequência", "SE": "Elemento primário de velocidade/frequência", "SV": "Elemento final de velocidade/frequência",
    "TRC": "Controlador registrador de temperatura", "TIC": "Controlador indicador de temperatura", "TC": "Controlador de temperatura", "TCV": "Controlador de válvula de controle auto atuada temperaturarizada", "TR": "Leitor registrador de temperatura", "TI": "Leitor indicador de temperatura", "TSH": "Chave e alarme de alta de temperatura", "TSL": "Chave e alarme de baixa de temperatura", "TSHL": "Chave e alarme de alta e baixa de temperatura", "TRT": "Transmissor registrador de temperatura", "TIT": "Transmissor indicador de temperatura", "TT": "Transmissor de temperatura", "TY": "Relé de temperatura", "TE": "Elemento primário de temperatura", "TP": "Ponto de teste de temperatura", "TW": "Prova de temperatura", "TSE": "Dispositivo de segurança de temperatura", "TV": "Elemento final de temperatura",
    "TDRC": "Controlador registrador de temperatura diferencial", "TDIC": "Controlador indicador de temperatura diferencial", "TDC": "Controlador de temperatura diferencial", "TDCV": "Controlador de válvula de controle auto atuada temperatura diferencialrizada", "TDR": "Leitor registrador de temperatura diferencial", "TDI": "Leitor indicador de temperatura diferencial", "TDSH": "Chave e alarme de alta de temperatura diferencial", "TDSL": "Chave e alarme de baixa de temperatura diferencial", "TDRT": "Transmissor registrador de temperatura diferencial", "TDIT": "Transmissor indicador de temperatura diferencial", "TDT": "Transmissor de temperatura diferencial", "TDY": "Relé de temperatura diferencial", "TE": "Elemento primário de temperatura diferencial", "TP": "Ponto de teste de temperatura diferencial", "TW": "Prova de temperatura diferencial", "TDV": "Elemento final de temperatura diferencial",
    "UR": "Leitor registrador multivariável", "UI": "Leitor indicador multivariável", "UY": "Relé multivariável", "UV": "Elemento final multivariável",
    "VR": "Leitor registrador de vibração", "VI": "Leitor indicador de vibração", "VSH": "Chave e alarme de alta de vibração", "VSL": "Chave e alarme de baixa de vibração", "VSHL": "Chave e alarme de alta e baixa de vibração", "VRT": "Transmissor registrador de vibração", "VIT": "Transmissor indicador de vibração", "VT": "Transmissor de vibração", "VY": "Relé de vibração", "VE": "Elemento primário de vibração", "VZ": "Elemento final de vibração",
    "WRC": "Controlador registrador de força/peso", "WIC": "Controlador indicador de força/peso", "WC": "Controlador de força/peso", "WCV": "Controlador de válvula de controle auto atuada força/pesorizada", "WR": "Leitor registrador de força/peso", "WI": "Leitor indicador de força/peso", "WSH": "Chave e alarme de alta de força/peso", "WSL": "Chave e alarme de baixa de força/peso", "WSHL": "Chave e alarme de alta e baixa de força/peso", "WRT": "Transmissor registrador de força/peso", "WIT": "Transmissor indicador de força/peso", "WT": "Transmissor de força/peso", "WY": "Relé de força/peso", "WE": "Elemento primário de força/peso", "WZ": "Elemento final de força/peso",
    "WDRC": "Controlador registrador de força/peso diferencial", "WDIC": "Controlador indicador de força/peso diferencial", "WDC": "Controlador de força/peso diferencial", "WDCV": "Controlador de válvula de controle auto atuada força/peso diferencialrizada", "WDR": "Leitor registrador de força/peso diferencial", "WDI": "Leitor indicador de força/peso diferencial", "WDSH": "Chave e alarme de alta de força/peso diferencial", "WDSL": "Chave e alarme de baixa de força/peso diferencial", "WDSHL": "Chave e alarme de alta e baixa de força/peso diferencial", "WDRT": "Transmissor registrador de força/peso diferencial", "WDIT": "Transmissor indicador de força/peso diferencial", "WDT": "Transmissor de força/peso diferencial", "WDY": "Relé de força/peso diferencial", "WE": "Elemento primário de força/peso diferencial", "WDZ": "Elemento final de força/peso diferencial",
    "YIC": "Controlador indicador de presença/estado", "YC": "Controlador de presença/estado", "YR": "Leitor registrador de presença/estado", "YI": "Leitor indicador de presença/estado", "YSH": "Chave e alarme de alta de presença/estado", "YSL": "Chave e alarme de baixa de presença/estado", "YT": "Transmissor de presença/estado", "YY": "Relé de presença/estado", "YE": "Elemento primário de presença/estado", "YZ": "Elemento final de presença/estado",
    "ZRC": "Controlador registrador de posição/dimensão", "ZIC": "Controlador indicador de posição/dimensão", "ZC": "Controlador de posição/dimensão", "ZCV": "Controlador de válvula de controle auto atuada posição/dimensãorizada", "ZR": "Leitor registrador de posição/dimensão", "ZI": "Leitor indicador de posição/dimensão", "ZSH": "Chave e alarme de alta de posição/dimensão", "ZSL": "Chave e alarme de baixa de posição/dimensão", "ZSHL": "Chave e alarme de alta e baixa de posição/dimensão", "ZRT": "Transmissor registrador de posição/dimensão", "ZIT": "Transmissor indicador de posição/dimensão", "ZT": "Transmissor de posição/dimensão", "ZY": "Relé de posição/dimensão", "ZE": "Elemento primário de posição/dimensão", "ZV": "Elemento final de posição/dimensão",
    "ZDRC": "Controlador registrador de gauging/desvio", "ZDIC": "Controlador indicador de gauging/desvio", "ZDC": "Controlador de gauging/desvio", "ZDCV": "Controlador de válvula de controle auto atuada gauging/desviorizDada", "ZDR": "Leitor registrador de gauging/desvio", "ZDI": "Leitor indicador de gauging/desvio", "ZDSH": "Chave e alarme de alta de gauging/desvio", "ZDSL": "Chave e alarme de baixa de gauging/desvio", "ZDSHL": "Chave e alarme de alta e baixa de gauging/desvio", "ZDRT": "Transmissor registrador de gauging/desvio", "ZDIT": "Transmissor indicador de gauging/desvio", "ZDT": "Transmissor de gauging/desvio", "ZDY": "Relé de gauging/desvio", "ZDE": "Elemento primário de gauging/desvio", "ZDV": "Elemento final de gauging/desvio"}


    while True:
        print("\nInsira o símbolo de instrumentação (ex: ARC):\n")
        symb = input()
        symb = symb.upper()

        try:
            print("\n" + dicsym[symb] + "\n")
            
            print("Deseja voltar?\n [s] = Sim\n [n] = Não\n")
            voltar = input()
            voltar = voltar.upper()
            clear()
            if voltar == 'S':
                menu()
            else:
                continue

        except:
            print("\nNão foi encontrada a especificação do símbolo, por favor, tente novamente\n")


#Gerador de símbolos
############################################################################
def symbol():        #Esta função filtra a pesquisa de símbolos no dicionário
    while True:
        symb = []
        print("\nInsira a especificação da instrumentação (ex: Controlador registrador de queima):\n")

        try:

            let = input()
            let = let.upper()
            let.replace("Ç","C")
            let = unidecode.unidecode(let)
            #O numeral presente ao final da variável dic indica a posição da letra (1 = primeiro)
            dic1 = {"ANALISE":"A", "QUEIMA":"B", "QUEIMADOR":"B", "COMBUSTAO":"B", "VOLTAGEM":"E", "TENSAO":"E", "VAZAO":"F", "VAZAO QUANTIDADE": "FQ", "QUANTIDADE VAZAO": "FQ", "VAZAO DE QUANTIDADE": "FQ", "QUANTIDADE DE VAZAO": "FQ", "FLOW RATIO": "FF", "HAND": "H", "MAO": "H", "CORRENTE": "I", "POTENCIA": "J", "TEMPO": "K", "NIVEL": "L", "LEVEL": "L", "PRESSAO": "PD", "PRESSAO DIFERENCIAL": "PD", "QUANTIDADE": "Q", "RADIACAO": "R", "SPEED": "S", "VELOCIDADE": "S", "FREQUENCIA": "S", "TEMPERATURA": "T", "TEMPERATURA DIFERENCIAL": "TD", "DIFFERENTIAL": "TD", "MULTIVARIAVEL": "U", "VIBRACAO": "V", "PESO": "W", "FORCA": "W", "PESO DIFERENCIAL": "WD", "FORÇA DIFERENCIAL": "WD", "EVENTO": "Y", "ESTADO": "Y", "PRESENÇA": "Y", "POSICAO": "Z", "DIMENSAO": "Z", "GAUGING": "ZD", "DESVIO": "ZD"}
            dic2 = {"CONTROLADOR":{"REGISTRADOR":"RC", "INDICADOR":"IC", "CEGO":"C", "VALVULA": "CV", "VALVULA": "ICV", "VALVULA DE CONTROLE": "CV", "VALVULA DE CONTROLE": "ICV", "VALVULA DE CONTROLE AUTO ATUADA": "CV", "VALVULA DE CONTROLE AUTO ATUADA": "ICV"}, "LEITOR":{"REGISTRADOR": "R", "INDICADOR":"I"}, "LEITURA":{"REGISTRADOR": "R", "INDICADOR":"I"}, "CHAVE":{"ALTA":"SH", "BAIXA":"SL","ALTA E BAIXA":"SHL", "ALTA BAIXA":"SHL", "HL":"SHL", "BAIXA E ALTA":"SHL", "BAIXA ALTA":"SHL", "LH":"SHL"}, "SWITCH":{"ALTA":"SH", "BAIXA":"SL","ALTA E BAIXA":"SHL", "ALTA BAIXA":"SHL", "HL":"SHL", "BAIXA E ALTA":"SHL", "BAIXA ALTA":"SHL", "LH":"SHL"}, "TRANSMISSOR":{"REGISTRADOR":"RT", "INDICADOR":"IT", "CEGO": "T"}, "SOLENOIDE":"Y", "SOL":"Y", "RELE":"Y", "RELAY":"Y", "ELEMENTO PRIMARIO": "AE", "PONTO DE TESTE": "AP", "FORCA": "AW", "PROVA": "AW", "DISPOSITIVO DE SEGURANCA":"SV", "ELEMENTO FINAL": "V"}   #O elemento final deve ser consertado para outras variaveis
            dic3 = {"CONTROLADOR":"C", "LEITOR":"R", "LEITURA":"R", "CHAVE":"SHL", "SWITCH":"SHL", "TRANSMISSOR": "T","SOLENOIDE":"Y", "SOL":"Y", "RELE":"Y", "RELAY":"Y", "ELEMENTO PRIMARIO": "AE", "PONTO DE TESTE": "AP", "FORCA": "AW", "PROVA": "AW", "DISPOSITIVO DE SEGURANCA":"SV", "ELEMENTO FINAL": "V"}   #O elemento final deve ser consertado para outras variaveis
            

            let = let.split()
            j = 0
            i = 0
            cego = False

            while i <= len(let)-1:  #Testa se o instrumento é do tipo cego
                #print(i)
                try:
                    if not any([n in dic2[let[i]] for n in let]):
                        cego = True
                    break
                except:
                    i+=1
                    continue

            i = 0

            while i <= len(let)-1:
                #print(i)

                if let[i] in list(dic1.keys()):         #Fazer uma lista com essas strings com base na ordem
                    #print(dic1[let[i]])
                    symb.insert(0,dic1[let[i]])


                #Fazer um if para cada variavel (Controladores, chaves, etc)
                if cego == True: #Utiliza a lista 3 no caso de não especificar o tipo (Ex: controlador queimador = BC)
                    if let[i] in list(dic3.keys()):
                        j = 0
                        #print(dic3[let[i]])
                        symb.insert(0,dic3[let[i]])    #insere no final do da lista
                        j+=1



                if cego == False:
                    if let[i] in list(dic2.keys()):
                        j = 0
                        while j <= len(let)-1:
                            try:
                                #print(dic2[let[i]][let[j]])
                                symb.insert(-1,dic2[let[i]][let[j]])    #insere no final do da lista
                                j+=1
                            except:
                                j+=1


                    else:
                        i+=1
                        continue
                i+=1


            res = "".join([str(item) for item in symb])         #transforma a lista em string

            if res == "":
                print("Não foi encontrado o instrumento na base de dados\n")

            else:
                print("O símbolo do instrumento é:" ,res + "\n")

            print("Deseja voltar?\n [s] = Sim\n [n] = Não\n")
            voltar = input()
            voltar = voltar.upper()
            clear()
            if voltar == 'S':
                menu()
            else:
                continue

        except:
            print("\nNão foi encontrada a especificação do símbolo, por favor, tente novamente\n")

#Clear
############################################################################
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#Menu
############################################################################
def menu():
    clear()

    print("##########################################")
    print("#                                        #")
    print("#   Bem vindo ao Decifrador de Siglas    #")
    print("#                                        #")
    print("#                                        #")
    print("#    Digite a função que deseja usar:    #")
    print("#                                        #")
    print("# a) Decifrador de Sigla                 #")
    print("# b) Gerador de Sigla                    #")
    print("# c) Sair                                #")
    print("#                                        #")
    print("##########################################\n")

    resp = input()
    resp = resp.upper()

    if resp == 'A':
        clear()
        decsymbol()

    if resp == 'B':
        clear()
        symbol()

    if resp == "C":
        print("\n Obrigado por usar o programa\n")
        os._exit(0)



menu()