file = open("bits.txt", "r")

bits = []

for line in file:
    for num in line.split(','):
            bits.append(int(num))
        
expo = [] 

print(bits)

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
    
print (mantissa)

#formula geral 


expoente = int('10000101',2)
signal = 1

def toDec(mantissa, expoente, signal):
    expoente = expoente - 127
    num = ((-1**signal)*(1 + mantissa) * (2**expoente))
    return num

decNum = toDec(mantissa, expoente, signal)
print(decNum)