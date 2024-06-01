global saldo
saldo = 0.0
global saques
global depositos 
saques = 0.0
depositos = 0.0

global extrato


extrato = {
  'Saques': saques,
  'Depositos': depositos,
  'Saldo': saldo
}

def menu():
  global opcao
  opcao = int(input("""
  Escolha uma opção:
    0 - Sair
    1 - Depositar
    2 - Sacar
    3 - ver extrato
  """))

menu()


def depositar():
  global depositos
  depositos = float(input("Digite o valor a ser depositado: "))
  global saldo
  saldo = saldo + depositos
  global extrato
  extrato = {f'Deposito de:  {depositos} \nSaldo: {saldo} \nSaques: {saques}'}
  return f'Deposito de: {depositos}'
  
def sacar():
  cont = 1
  global saldo
  global extrato
  global saques
  saques = float(input("Digite o valor a ser sacado"))
  
  if (cont < 4 and saldo > saques):
      
      saldo -= saques
      extrato = {f'Saque de: {saques} \nSaldo: {saldo} \nDepositos: {depositos}'}
      cont += 1
  elif (cont == 4):
    print("Não pode ser sacado mais que três vezes no dia.")
  else:
    print('Saque não pode ser maior do que o saldo.')
##  return f'Saque de: {saques}'
      
def ver_extrato():
  for extratos in extrato:
    print(f'extratos:  {extratos}')

while (opcao != 0):
  if (opcao == 1):
    depositar()
  elif (opcao == 2):
    sacar()
  elif (opcao == 3 ):
    ver_extrato()
  else: 
    print('Opção inválida')
  menu()

