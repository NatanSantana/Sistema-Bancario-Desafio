# %%
from abc import ABC, abstractmethod


menu = """
------------SAINT BANK------------

[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar novo usuario
[5] Criar conta
[6] Sair

"""

saldo = 1500
valor_saque  = float()
valor_depositado = float()
extrato = {"Depósito": [], "Saque": []}
LIMITE_SAQUE = 3  
cpfs = []
usuarios = []
contas = []
AGENCIA = "0001"
criar_contas = {}
senhas = []
contas_registradas = []


class depositar:
    def __init__(self,valor_depositado):
        self.valor_depositado = valor_depositado
          
    @classmethod
    def deposito(cls,valor_depositado):
        valor_depositado = input("Insira um valor para depositar: ")

        valor_depositado = float(valor_depositado)

        if (valor_depositado > 0):
            global saldo
            
            saldo += valor_depositado

            extrato["Depósito"].append(f"R${valor_depositado}")

        if valor_depositado < 0:
            print("Digite um número válido, POSITIVO!")
            
    
            
class retirada:
    def __init__(self,*,valor_saque):
        self.valor_saque = valor_saque

    @classmethod
    def sacar(self, *,valor_saque):
        global LIMITE_SAQUE
        global saldo   
        if (valor_saque <= 500) and (valor_saque < saldo) and (valor_saque > 0) and (LIMITE_SAQUE >= 1):
        
            print("O limite diário é de 3 saques")
            saldo -= valor_saque
        
            extrato["Saque"].append(f"R${valor_saque}")
         
            LIMITE_SAQUE -= 1
        
        if (saque < 0):
            
            print("insira um valor positivo")
            
        if (saque > saldo):
            print("Saldo insuficiente")
        
        if saque > 500:
            print("O limite de saque é de R$ 500")

class Historico:
    def __init__(self,saldo, extrato=None):
        self.saldo = saldo
        self.extrato = extrato

    def extratos(saldo, /,*,extrato):
        for deposito, saque in extrato.items():
            print(f"{deposito}: {", ".join(saque)}")
        print(f"Saldo: R${saldo}")

class Cliente:
    def __init__(self,usuarios=None):
        self.usuarios = usuarios

    def criar_usuario(usuarios):
        nome = input("Nome do usuario: ")
        data_de_nascimento = input("Data de nascimento: ")
        cpf = input("Insira o cpf (somente números): ")
        endereco = input("endereco: ") 
        limite = 1
        while limite >= 1:
                if cpf in cpfs:
                        print("Um usuario com esse cpf já existe")
                        limite -= 2
                else:
                    
                    cpfs.append(cpf)
                    usuarios.append(f"{nome}, {data_de_nascimento}, {cpf}, {endereco}")
                    limite -= 1
                    print(f"Usuário criado: {nome}, {data_de_nascimento}, {cpf}, {endereco}")
                    criar_contas.setdefault(f"{cpf}", f"{nome}")

class Conta_corrente:
    def __init__(self,contas=None):
        self.contas = contas

    @classmethod    
    def criar_conta(cls,contas):
        global senhas
        cpf_conta = input("Infome o cpf para criar uma conta: ")
        senha =  input("Insira uma senha: ")
    
        qtde = senhas.count(senha)

        if cpf_conta in criar_contas:
            qtde += 1
            senhas.append(senha)     
            print(f"""
            Agência: {AGENCIA}
            C/C: {qtde}
            Titular: {criar_contas[cpf_conta]}""")

        

        else:
            print("Esse cpf não existe na nossa lista de usuarios")
    
        if cpf_conta not in contas_registradas:
            contas_registradas.append(cpf_conta)
        
        

    
        
        




while True:
    
    opcao  = input(menu)
    
   
    if opcao == "1":
        depositar.deposito(valor_depositado)
        
    if opcao == "2":
        
        saque = input("Quanto você quer sacar?: ")
        
        saque = float(saque)

        retirada.sacar(valor_saque=saque)
        
    if LIMITE_SAQUE < 1:
        print("Você atingiu o limite de saque diário")
        
    if opcao == "3":
        Historico.extratos(saldo, extrato=extrato)

    if opcao == "4":
        Cliente.criar_usuario(usuarios)

    if opcao == "5":
        Conta_corrente.criar_conta(contas)
        
         
    if opcao == "6":
        print("Obrigado por usar o Saint Bank, Até uma próxima")
        break
