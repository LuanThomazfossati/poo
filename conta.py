class conta:
      def __init__(self,saldo)
          self.saldo = saldo  
      def saca(self,valor)
          self.saldo -= valor
      def depositar(self,deposita) 
          self.saldo += deposita
      def calcularRendimento(self)
          self.saldo *= 0,1
          
