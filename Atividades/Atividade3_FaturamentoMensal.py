import json

    #Abrir dados.json
with open("./resources/dados.json") as Arqjson:
    dados = json.load(Arqjson)

    # Valores Iniciais
SomaMes = 0.0
Media = 0
MenorValor = float('inf')
MaiorValor = float('-inf')
DiaMenor = 0
DiaMaior = 0
DiaUpMed = 0

    #Realizar a soma dos valores do mês
for linha in dados:
    if linha['valor'] > 0:
        SomaMes += linha['valor']
        Media += 1

    #Verificar menor valor e seu dia do mês
for linha in dados:
    if linha['valor'] < MenorValor and linha['valor'] > 0:
        MenorValor = linha['valor']
        DiaMenor = linha['dia']

    #Verificar maior valor e seu dia do mês
for linha in dados:
    if linha['valor'] > MaiorValor and linha['valor'] > 0:
        MaiorValor = linha['valor']
        DiaMaior = linha['dia']

MediaMes = SomaMes/Media #Armazenar a média

    #Verificar valores acima da média
for linha in dados:
    if linha['valor'] > MediaMes:
        DiaUpMed += 1

    #Saída
print(f"\nTotal do Mês: R$ {SomaMes:.2f}")
print(f"A média do mês (desconsiderando valores 0) é de: R${MediaMes:.2f}")
print(f"\n O menor valor do mês foi no dia {DiaMenor} com: R$ {MenorValor:.2f}")
print(f"O maior valor do mês foi no dia {DiaMaior} com: R$ {MaiorValor:.2f}")
print(f"\n Um total de {DiaUpMed} dias com valores superando a média!\n")