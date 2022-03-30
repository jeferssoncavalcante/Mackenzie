import math
vlEspetaculo = float(input())
vlconvite = float(input())

qtdCV = vlEspetaculo / vlconvite
lucro = vlEspetaculo + (vlEspetaculo * (23/100))
total = lucro / vlconvite
print (math.ceil(qtdCV))
print(math.ceil(total))
