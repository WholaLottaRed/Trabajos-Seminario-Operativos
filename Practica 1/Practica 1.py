"""Practica 1
Ruben Gamaliel Reyes Gómez
218744554
Seminario de Sistemas Operativos
"""

with open("prueba2.txt","r") as archivo:

    archivo2=open("archivo.txt","w")
    for linea in archivo:
        decimal=[]
        cadenas=[]
        hexadecimal=[]
        nueva_linea=""
        renglon=linea.split(",")
        cadenas = renglon[1:-1]
        hexs_a_decimales=renglon[0]
        hexs_a_decimales = hexs_a_decimales.split(":")
        hexadecimales = renglon[-1]
        hexadecimales = hexadecimales[0:-1]
        decimales_a_hex = hexadecimales.split(".")
        for submascara in hexs_a_decimales:
            if not submascara.isalnum():
                if submascara.find("/") == -1:
                    submascara = submascara[3:]
                else:
                    submascara = submascara[0:submascara.find("/")]
            decimal_convertido = int(submascara,16)
            decimal.append(decimal_convertido)
        for submascara in decimales_a_hex:
            try:
                submascara = int(submascara)
            except:
                submascara = 0
            hex_convertido = hex(submascara).lstrip("0x")
            hexadecimal.append(hex_convertido)
        nueva_linea = cadenas[1] + ':'
        nueva_linea = nueva_linea + ':'.join(map(str,decimal)) + ':'
        nueva_linea = nueva_linea + '.'.join(map(str,hexadecimal))
        archivo2.write(nueva_linea + '\n')

archivo2.close()
