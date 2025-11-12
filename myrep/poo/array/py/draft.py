class Foo:
    def __init__(self, x: int):
        self.x = x

    def __str__(self):
        return f'Foo({self.x})'
    


lista_vazia: list[int] = [1,2,3]

lista_p: list[int] = [1,2,3,4,5]


lista_v: list[Foo] = [Foo(1), Foo(2), Foo(3), Foo(4), Foo(5)]

lista_vazia.append(1)




print(lista_p)

print(lista_vazia)


nova_lista = [ "maça", "banana", " pera", "abacate", "uva"]

formatada = "    " .join(nova_lista)

print(formatada)



for fruta in nova_lista:
    print(fruta)


a = [1,2,3,4,5,6,7]
destruir = a.remove(1)

print(destruir)











