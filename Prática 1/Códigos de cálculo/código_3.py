import numpy as np
from matplotlib import pyplot as plt

Data = {'A0': 5.0000, 'A1':2.1408, 'A2':1.8573, 'A3':1.7400,'A4': 1.6862, 'A5':0.0000}
r_A, r_B, r_C = (10,10 ,10)
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

#Percentual da corrente medida e soma 
print(corrente_total/corrente_nominal, (corrente_braço_56 + corrente_braço_234)/corrente_nominal)

##################################################################################



