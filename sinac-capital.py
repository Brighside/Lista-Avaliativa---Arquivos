from sys import implementation


import struct 

registo = struct.Struct("6s7s6s8s2s1s4s8s")

with open("sinasc-sp-capital-2018.dat", "rb") as arq:
    linha = arq.read(registo.size)
    cont = 0
    while len(linha) > 0: 
        cont += 1
        linha = arq.read(registo.size) 
 
    print(cont)