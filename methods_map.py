class MathOperations:

    def soma(x, y):
        return x + y

    def dif(x, y):
        return x - y

    def mult(x, y):
        return x * y

    def div(x, y):
        return x / y


soma_map = None
dif_map = None
mult_map = None
div_map = None

mapper = {
    soma_map: MathOperations.soma,
    dif_map: MathOperations.dif,
    mult_map: MathOperations.mult,
    div_map: MathOperations.div
}

a = mapper[soma_map](2, 3)
b = mapper[dif_map](10, 5)
c = mapper[mult_map](12, 10)
d = mapper[div_map](50, 10)

print(a)
print(b)
print(c)
print(d)
