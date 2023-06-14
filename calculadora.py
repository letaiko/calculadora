print("\n----♡♡♡| Menu Calculadora |♡♡♡---- \n1 - Somar \n2 - Subtrair \n3 -
Multiplicar \n4 - Dividir \n0 - Sair")
opcao = int(input("Digite sua opção: "))
while opcao != 0:
primeiro = int(input("Digite o primeiro número: "))
segundo = int(input("Digite o segundo número: "))
if opcao == 1:
soma = primeiro + segundo
print(f"{primeiro} + {segundo} = {soma}")
elif opcao == 2:
subtracao = primeiro - segundo
print(f"{primeiro} - {segundo} = {subtracao}")
elif opcao == 3:
multiplicacao = primeiro * segundo
print(f"{primeiro} * {segundo} = {multiplicacao}")
elif opcao == 4:
divisao = primeiro / segundo
print(f"{primeiro} / {segundo} = {divisao}")
print("\n----| Menu Calculadora |---- \n1 - Somar \n2 - Subtrair \n3 -
Multiplicar \n4 - Dividir \n0 - Sair")
opcao = int(input("Digite sua opção: "))
print("Encerrando a calculadora...")
