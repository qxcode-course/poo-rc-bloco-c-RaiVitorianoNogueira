class Market:
    def __init__(self, caixas: int):
        self.counters: list[Cliente|None]  = []
        self.wait: list[Cliente] = []
        for _ in range(caixas):
            self.counters.append(None)

    

    def __str__(self):
        caixas = ", ".join([str(cliente) if cliente else "-----" for  cliente in self.counters])
        espera = ", ".join([str(cliente) for cliente in self.wait])

        return f"Caixas: {caixas}\nEspera: {espera}"
    
    




        
        















class Cliente:
    def __init__(self:)