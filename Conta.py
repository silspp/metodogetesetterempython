class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
# from conta import Conta
#>>> conta = Conta(123, "Nico", 55.5, 1000.0)
#Construindo objeto ... <conta.Conta object at 0x7fc4ed132048>
#>>> conta2 = Conta(321, "Marcos", 100.0, 1000.0)
#Construindo objeto ... <conta.Conta object at 0x7fc4ed1324a8>
#>>> conta.titular
#'Nico'
#>>> conta2.titular
#'Marcos'