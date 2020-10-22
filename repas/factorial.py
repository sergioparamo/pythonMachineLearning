#L'usuari escriu un enter i s'imprimeix el seu factorial
#Pista: for, range()

#num = int(input("Escriu un num i s'imprimira el factorial"))

# Python code to demonstrate naive method
# to compute factorial
n = int(5) #num
fact = 1
current = 2

for current in range(2, n + 1):
    fact = fact * current

print("bucle for: ")
print(fact)

fact = 1
current = 2

while fact <= n:
    n *= current
    current + current+1

print("bucle while: ")
print(n)