class Conta:
      def __init__(self,saldo: float) -> None:
            self.saldo = saldo
            
      def sacar(self,valor: float) -> float:
            if valor < 0:
                  return 0.0
            self.saldo -= valor
            return self.saldo
            
      def depositar(self,valor: float) -> None:
            if valor < 0:
                  return
            self.saldo += valor
            
      def calcularRendimento(self) -> float:
            return self.saldo * 0.1
