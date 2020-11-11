def leiaint():
    try:
        try:
            numero=int(input("Insira um numero: "))
        except ValueError:
            print("O houve o erro")
        print(numero)
    except UnboundLocalError:
        print("O numero foi invalido")

def leiafloat():
    try:
        try:
            numero=int(input("Insira um numero: "))
        except ValueError:
            print("O houve o erro")
        print(numero)
    except UnboundLocalError:
        print("O numero foi invalido")
leiaint()
leiafloat()