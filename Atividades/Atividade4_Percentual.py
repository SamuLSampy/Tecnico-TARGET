import math

    #Estados e Valores
SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Others = 19848.53

    #Total
Total = [SP, RJ, MG, ES, Others]
Total1 = round(sum(Total),2)

    #Saída dos valores
print(f"\nValor total: R$ {Total1} (100%)\n\n- São Paulo: R$ {SP} ({round((SP/Total1)*100,2)}%)\n- Rio de Janeiro: R$ {RJ} ({round((RJ/Total1)*100,2)}%)\n- Minas Gerais: R$ {MG} ({round((MG/Total1)*100,2)}%)\n- Espírito Santo: R$ {ES} ({round((ES/Total1)*100,2)}%)\n- Outros: R$ {Others} ({round((Others/Total1)*100,2)}%)\n")
