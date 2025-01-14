import pandas as pd 
import altair as alt
import numpy

#ainda não tenho a base de dados bas ela virá em um formato csv com 3 colunas.
chanel_time_name = 'time'
chanel_01_name = 'ch_01'
chanel_02_name = 'ch_02'

df = pd.DataFrame(data ={chanel_time_name:[0.001, 0.003], chanel_01_name: [1,2], chanel_02_name:[3,4]})
print(df)

df['Ddp resitor 10kohms'] = df[chanel_01_name] - df[chanel_02_name]

print(df)

#Seque da equação diferencial que a constante de decaimento tau é dada por resistência (10kohms) vezes capacitância (0,1uF)
#Segundo o chat gpt, ter um outro circuito em paralelo pode gerar impedância de modo que a médida de tau seja na verdade a Req do circuito vezes a capacitância

R1 = 10000  #10 kohms
C1 = 0.1 * 10**(-6) #0,1 uF

tau = R1*C1

print(tau)
