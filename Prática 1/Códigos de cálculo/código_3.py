import numpy as np
from matplotlib import pyplot as plt

Data = {'A0': 5.0000, 'A1':2.1408, 'A2':1.8573, 'A3':1.7400,'A4': 1.6862, 'A5':0.0000}
r_A, r_B, r_C = (9.86,9.86 ,9.86)
r_2,r_3,r_4,r_5,r_6 = (304.997284084736
,301.768362604864
,295.732995352767
,301.768362604864
,295.732995352767)

r_234 = 1/(1/r_2+1/r_3+1/r_4)
r_56 = 1/(1/r_5 + 1/r_6)

ddp_A = Data['A1'] - Data['A2']

##################################################################################

data_calibracao_100 =  {'a0': 4.9951, 'a1': 0.4497}	

corrente_calibracao = data_calibracao_100['a1']/r_A

r_100_1 = (data_calibracao_100['a0']-data_calibracao_100['a1'])/corrente_calibracao


##################################################################################



corrente_total = ddp_A/r_A




ddp_braço_56 = Data['A2'] - Data['A3']
corrente_braço_56 = ddp_braço_56/r_B

ddp_braço_234 = Data['A2'] - Data['A4']
corrente_braço_234 = ddp_braço_234/r_C

resistencia_eq_nominal = 100 + 10 + 1/((1/110)+(1/160))

corrente_nominal = 5/resistencia_eq_nominal
soma = corrente_braço_56 + corrente_braço_234
#Percentual da corrente medida e soma
print('='*10 , 'correntes', '='*10)
print(f'corrente total: {corrente_total}')
print(f'braço 56: {corrente_braço_56} \t braço 234: {corrente_braço_234}')
print(f'Soma:{soma}')
print(f'corrente nominal: {corrente_nominal}')

print(f'valor fracionário do total: {corrente_total/corrente_nominal} \n  valor fracionário da soma dos braços: {(corrente_braço_56 + corrente_braço_234)/corrente_nominal}')

print(f'corrente da calibração do resistor de 100: {corrente_calibracao}')

##################################################################################


print('='*10 , "ddp's", '='*10)
print(f'ddp A:{ddp_A}')
print(f'ddp 56:{ddp_braço_56}')
print(f'ddp 234:{ddp_braço_234}')

print('='*10 , "resistencias's", '='*10)
print(f'r 234: {r_234}')
print(f'r 56: {r_56}')
print(f'r100 1 = {r_100_1}')
print(f'resistência nominal: {resistencia_eq_nominal}')
