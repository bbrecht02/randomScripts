file = open("bits.txt", "r")

lines = file.readlines()

count = 0

bits = []

for line in lines:
    count = count + 1
    if (count == 1): 
        signal = int(line)
    elif (count == 2):
        expoente = line
    elif (count == 3):
        for num in line.split(' '):
            bits.append(int(num))

expo = []

#setup exponent
for i in range (24):
    if (i != 0):
        expo.append((i*-1))

mantissa = 0
aux = 0

for bit in bits: 
    for ex in expo:
        aux = bit * (2**ex)
        mantissa += aux 
    
#cast to dec
expoente = int(expoente,2)

def toDec(mantissa, expoente, signal):
    expoente = expoente - 127
    num = ((-1**signal)*(1 + mantissa) * (2**expoente))
    return num

decNum = toDec(mantissa, expoente, signal)
print(decNum)