import math
""" https://www.disfrutalasmatematicas.com/numeros/binario-decimal-hexadecimal-conversor.html """
ListBinary = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"]
ListHexadecimal = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"] 
ListDecimal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#link de prueba [https://www.disfrutalasmatematicas.com/numeros/binario-decimal-hexadecimal-conversor.html]
#print(f"{bin(214)} {hex(214)}" )
while True:
  #  try:
    eleccion = input("Seleccione una conversión: \n a.)Decimal a hexadecimal y binario \n b.)Hexadecimal a decimal y binario \n c.)Binario a hexadecimal y decimal \n d.)Salir \n")
 #   except:
#        print("Ingrese uno de los valores: a, b, c, d")
    ### DECIMAL A BINARIO ###
    def ConvertDecimalToBinary(NumDecimal):
        ConvertedNumBinario = []
        while NumDecimal > 0:
            ConvertedNumBinario.append(NumDecimal % 2)
            print(f"{NumDecimal} / 2 = {ConvertedNumBinario}") 
            NumDecimal = math.floor(NumDecimal / 2)
        print(f"Su numero convertido a decimal es: {ConvertedNumBinario}")
        return

    ### DECIMAL A HEXADECIMAL ###
    def ConvertDecimalToHexadecimal(NumDecimal):
        ConvertedNumHexadecimal = []
        while NumDecimal > 0:
            #se saco el valor absoluto del flotante y se le resto el numero entero, para tener el valor decimal despues del punto con el 0.
            NumDecimal = abs(float(NumDecimal / 16))
            Operacion = math.floor((NumDecimal - (int(NumDecimal)))* 16) #(str(Num % 1)[2:]) #esto era para conseguir el valor despues del punto
            if Operacion == 0: # si el valor recibido ya tiene un 0 en el valor entero entonces se detiene el loop
                    break
            ConvertedNumHexadecimal.append(hex(Operacion)) #no quiero depender del metodo hex asi que luego lo cambio
        ConvertedNumHexadecimal.reverse()
        print(f"Su numero Hexadecimal es: {ConvertedNumHexadecimal}")
        return
    ### Hexadecimal a Decimal ###
    def ConvertHexadecimalToDecimal(NumHexadecimal):
        Contador = 0
        Resultado = 0 #tengo que inicializar la variable o me marca error
        ListaOperacion = []
        for Contador, Digito in enumerate(str(NumHexadecimal)[::-1]) : #el [::-1 es para que lo recorra inversamente]
            if Digito == "A":
                Digito = 10
            elif Digito == "B":
                Digito = 11
            elif Digito == "C":
                Digito = 12
            elif Digito == "D":
                Digito = 13
            elif Digito == "E":
                Digito = 14
            elif Digito == "F":
                Digito = 15
            Operacion = int(Digito) * 16 ** Contador
            ListaOperacion.append(Operacion)
            Resultado = Resultado + Operacion
        print(f"Numeros sumados: {ListaOperacion[::-1]}")
        print(f"Su numero en decimal es: {Resultado}")
        return
    ###HEXADECIMAL A BINARIO###
    def ConvertHexadecimalToBinary(NumHexadecimal):
        contador = 0
        listBinario = []
        for contador, Digito in enumerate(str(NumHexadecimal)):
            if Digito == "0":
                Digito = ListBinary[0]
            elif Digito == "1":
                Digito = ListBinary[1]
            elif Digito == "2":
                Digito = ListBinary[2]
            elif Digito == "3":
                Digito = ListBinary[3]
            elif Digito == "4":
                Digito = ListBinary[4]
            elif Digito == "5":
                Digito = ListBinary[5]
            elif Digito == "6":
                Digito = ListBinary[6]
            elif Digito == "7":
                Digito = ListBinary[7]
            elif Digito == "8":
                Digito = ListBinary[8]
            elif Digito == "9":
                Digito = ListBinary[9]
            elif Digito == "A":
                Digito = ListBinary[10]
            elif Digito == "B":
                Digito = ListBinary[11]
            elif Digito == "C":
                Digito = ListBinary[12]
            elif Digito == "D":
                Digito = ListBinary[13]
            elif Digito == "E":
                Digito = ListBinary[14]
            elif Digito == "F":
                Digito = ListBinary[15]
            listBinario.append(Digito)
        print(f"Su numero en binario es: {listBinario}")
        return
    ###BINARIO A DECIMAL###
    def ConvertBinaryToDecimal(NumBinary): 
        Contador = 0
        Resultado = 0
        NumConvertedBinaryDecimal = 0
        print("Proceso de conversion a decimal: ")
        #leer en reversa el binario para entonces hacer la operacion de potencia, digito toma el valor del 0 o 1
        for Contador, Digito in enumerate(str(NumBinary)[::-1]):
            if Digito == "1":
                Resultado = 2 **Contador
                NumConvertedBinaryDecimal = NumConvertedBinaryDecimal + Resultado
                print(f"{Digito}: 2 ^ {Contador} = {Resultado}")
            elif Digito == "0":
                Resultado = 0
                print(f"{Digito}: 2 ^ {Contador} = {Resultado}")
        print(f"Su numero convertido a decimal es: {NumConvertedBinaryDecimal}")
        return

    ###BINARIO A DECIMAL ###
    #idea sacada de [https://hackernoon.com/how-to-split-string-every-nth-character-in-python]
    #otra referencia [https://stackoverflow.com/questions/1388818/how-can-i-compare-two-lists-in-python-and-return-matches]
    def ConvertBinaryToHexadecimal(NumBinary, n):
        iguales = []
        c=0
        split = [NumBinary[i:i+n] for i in range(0, len(NumBinary), n)]
        for c, valor in enumerate(ListBinary):
            if valor in split:
                iguales.append(ListHexadecimal[int(c)])
        print(f"Su numero en hexadecimal es: {iguales}")
        return

    match eleccion: 
        case "a":
            NumDecimal = int(input("Ingrese el valor decimal: "))
            ConvertDecimalToBinary(NumDecimal)
            ConvertDecimalToHexadecimal(NumDecimal)
        case "b":
            NumHexadecimal = input(f"Ingrese el numero Hexadecimal: ")
            ConvertHexadecimalToDecimal(NumHexadecimal)
            ConvertHexadecimalToBinary(NumHexadecimal)
        case "c":
            NumBinary = input(f"Ingrese el numero binario: ")
            ConvertBinaryToDecimal(NumBinary)
            ConvertBinaryToHexadecimal(NumBinary, 4)
        case "d":
            break




    #el codigo de abajo sirve pero para imprimir si salio residuo 0 o 1, guardar de momento esto estaba en decimal a binario
    """ Num =  input("ingrese el valor: ")
        for i in Num:
            residuo = int(i) % 2
            if residuo > 0:
                NumBinario.append(1)
            elif residuo == 0:
                NumBinario.append(0)
        print(NumBinario) """