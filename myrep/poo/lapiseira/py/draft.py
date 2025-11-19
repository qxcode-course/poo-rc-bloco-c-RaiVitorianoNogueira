class Lapiseira:
    def __init__(self, calibre : float):
        self.calibre =  calibre
        self.bico =  None
        self.tambor:list[Grafite] = []



        def __str__(self):
            


    def insert(self, grafite: Grafite):
        if not self.calibre:
            print("fail: calibre incompatível")
            return 
        self.tambor.append(grafite)












class Grafite:
    def __init__(self, calibre : float, dureza: str, tamanho: int):
        self.calibre = calibre
        self.dureza = dureza
        self.tamanho = tamanho



        





















def main():
    lapiseira = Lapiseira(0)

    While True:
        line = input()
    

        args = line.split()
        print("$" + line)
    
        if args[0] == "init":
            
    
    
    









main()


