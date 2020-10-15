#L'usuari escriu un enter i s'imprimeix true si existeix un bitllet d'euros amb la quantitat entrada,
# #false en qualsevol altre cas.
#Pista: or

num = int(input("Escriu un enter i et dire si hi ha un bitllet d'euro amb aquest valor"))

if (num == 5 or num == 10 or num == 20 or num == 50 or num == 100 or num == 200 or num == 500):
    print("true")
