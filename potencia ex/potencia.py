b = int(input("Base: "))
exp = int(input("Expoente: "))

p = 1
c = 1

while c <= exp:
    p *= b
    c += 1

print(b, "^", exp, "=", p)
