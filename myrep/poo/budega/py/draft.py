class Cliente:
    def __init__(self, nome: str):
        self.__nome =  nome



    def getNome(self,):
        return self.__nome
    

    def __str__(self):
        return self.__nome
    





class Market:
    def __init__(self, caixas: int):
        self.counters: list[Cliente|None]  = []
        self.wait: list[Cliente] = []
        for _ in range(caixas):
            self.counters.append(None)

    

    def __str__(self):
        caixas = ", ".join([str(cliente) if cliente else "-----" for  cliente in self.counters])
        espera = ", ".join([str(cliente) for cliente in self.wait])

        return f"Caixas: [{caixas}]\nEspera: [{espera}]"
    
    

    def arrive(self, cliente:Cliente):
        self.wait.append(cliente)


    def enter(self, cliente: Cliente):
        self.arrive(cliente)
        

    

    def call(self, posicao: int):
        if posicao < 0 or posicao >= len(self.counters):
            return  

        if self.counters[posicao] is not None:
            print("fail: caixa ocupado")

        elif not self.wait:
            print("fail: sem clientes")

        else:
            self.counters[posicao] = self.wait.pop(0)


        



    def finish(self, posicao: int):
        if posicao < 0 or posicao >= len(self.counters):
            print("fail: caixa inexistente")

        elif self.counters[posicao] is None:
            print("fail: caixa vazio")

        else:
            self.counters[posicao] = None
        








def main():
    market = Market(0)

    while True:
        line = input()

        args = line.split()
        print("$" + line)

        if args[0] == "init":
            market = Market(int(args[1]))
            
        elif args[0] == "show":
            print(market)

        elif args[0] == "enter":
            market.enter(Cliente(args[1]))

        
        
        elif args[0] == "arrive":
            market.arrive(Cliente(args[1]))
            

        elif args[0] == "call":
            market.call(int(args[1]))



        elif args[0] == "finish":
            market.finish(int(args[1]))



        elif args[0] == "end":
            break

    


main()