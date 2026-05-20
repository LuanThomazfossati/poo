from conta import Conta
obj = Conta(1000)
print("(1) sacar")
print("(2) depositar")
print("(3) calcular rendimento")
opc = input("Qual opção você vai escolher?")
if opc == "1":
  valor_sacar = int(input("Qual o valor do saque?"))
  obj.sacar(valor_sacar)
elif opc == "2":
  valor_depositar = int(input("Qual o valor do depósito?"))
  obj.depositar(valor_depositar)
elif opc == "3":
  print(obj.calcularRendimento())
  
