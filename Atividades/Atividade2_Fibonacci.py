    #Primeiros números de Fibonacci
Fibo1 = int(0)
Fibo2 = int(1)

    #Variável para próximo número
Next = int(0)

    #Valor Final
Value = int(0)

    #Valor Digitado
Number = int(input("Detector Fibonacci!\n digite o número para verificar se está na sequência de Fibonacci.\n\n"))

    #Calcular valor até que Number esteja o mais próximo da sequência de Fibonacci
while Value == 0 and Next <= Number:
    Next = Fibo1 + Fibo2
    Fibo1 = Next
    if Number == Next:
        Value = Next
        
    Next = Fibo1 + Fibo2
    Fibo2 = Next
    if Number == Next:
        Value = Next

    #Concluir se está ou não na sequência de Fibonacci
print(f"{Number} está na Fibonacci!") if Number == Value else print(f"{Number} não está na Fibonacci.")