Text = input(" Digite um texto para inverter: ")

TextInverso = ""

for Inv in range(len(Text) - 1,-1,-1):
    TextInverso += Text[Inv]

print(f"{TextInverso}")