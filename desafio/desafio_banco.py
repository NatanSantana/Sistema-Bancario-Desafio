# %%

menu = """
------------SAINT BANK------------

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

"""

saldo = 1500
saque  = float()
depositado = float()
extrato = []


LIMITE_SAQUE = 4

while True:
    
    opcao  = input(menu)
    
    
    if opcao == "1":

        depositado = input("Insira um valor para depositar:  ")

        depositado = float(depositado)

        if depositado > 0:
            saldo + depositado
            extrato.append(f"Valor Depositado: R$ {depositado} ")


    
        if depositado < 0:
            print("Digite um número válido, POSITIVO!")
        
        
    if opcao == "2":
        saque = input("Quanto você quer sacar?: ")

        saque = float(saque)

        if (saque < 0):
            
            print("insira um valor positivo")
            continue

        if (saque > saldo):
            print("Saldo insuficiente")
            break

        if (saque < 500) and (saque < saldo):
            print("O limite diário é de 3 saques")
            extrato.append(f"Valor Sacado: R$ {saque} ")
            saldo -= saque
            LIMITE_SAQUE -= 1

        if saque > 500:
            print("O limite de saque é de R$ 500")
    
    
    if opcao == "3":
        print(f"Seu extrato: {extrato}")

    if opcao == "4":
        print("Obrigado por usar o Saint Bank, Até uma próxima")
        break
    
    
    if LIMITE_SAQUE < 1:
        print("Você atingiu o limite de saque diário")
        break
        

   
    

   
        
    
    
    
    
    

         
            

    
    


         
            
            

            





