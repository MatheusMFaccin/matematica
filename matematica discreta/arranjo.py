#n!/(n-k)!
def calculaPermuta(valor):
    permuta = 1
    while valor > 1:
        permuta = permuta*valor
        valor = valor -1
    return permuta

n = float(input("digite o valor de n"))
k = float(input("digite o valor de k"))
print(calculaPermuta(n))

resposta = calculaPermuta(n)/calculaPermuta(n-k)
print(resposta)

