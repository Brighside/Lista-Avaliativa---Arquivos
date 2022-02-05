import struct

registo = struct.Struct("6s7s6s8s2s1s4s8s")

with open('sinasc-sp-2018.dat', 'rb') as arq:
    arq.seek(0,2)
    tamanho = arq.tell()
    quantRegistro = (tamanho/registo.size) - 1
    arq.seek(0)
    linha = arq.read(registo.size)
    arqCopia = open("sinasc-sp-capital-2018.dat", "ab")


    quantMeninasSnt = 0
    quantBebes = 0
    
   
    while len(linha) > 0: 
        record = registo.unpack(linha)
        if record[0].decode('latin1') == "355030":
            arqCopia.write(linha)

        if record[0].decode('latin1') == "354850" and record[5].decode('latin1') == "2":
            quantMeninasSnt += 1

        if record[0].decode('latin1') == "350950" and int(record[6].decode('latin1')) < 2500:
            if record[3].decode('latin1')[4:] == "2018":
                quantBebes += 1

        linha = arq.read(registo.size) 

    print(
        f"Tamanho do arquivo: {tamanho} Bytes"
        f"\nTamanho de cada registro: {registo.size} Bytes"
        f"\nQuantidade de registros: {quantRegistro}"
        f"\nQuantidade de Meninas (Santos): {quantMeninasSnt}"
        f"\nbebês com baixo peso (<2500) (Campinas): {quantBebes}"
    )

    arqCopia.close()

    