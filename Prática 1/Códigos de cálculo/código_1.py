import numpy as np
from matplotlib import pyplot as plt


tensao = 4.9707
resistencia_r5x = 1500
corrente = tensao/resistencia_r5x
correnteA0A1 = (5 - tensao)/9.87
# incerteza calculada usando a teoria proposta no material
erro_x = [np.sqrt((0.05*10)**2 + (0.02*1500)**2), 30, 1200*0.05/np.sqrt(4), 900*0.05/np.sqrt(3), 600*0.05/np.sqrt(2), 300, 0 ]
erro_y = [0.0049]*7

print(f'Tensão medida (V) : {tensao} \n Resistência_1500 (Ω) : {resistencia_r5x} \n corrente resitor 1500 (A): {corrente} \n queda resitor de 10 (A): {correnteA0A1}')
print(f'Erros na medição da resistência (Ω): {erro_x} \n Erros na medição da tensão (V): f{erro_y}  ' )
voltage = [5.00, tensao, 3.96, 2.96, 1.98, 0.98,0]
resistencia_lista = [1510, 1500, 1200,900, 600, 300,0]


plt.errorbar(resistencia_lista, voltage,erro_y, erro_x,'8', ecolor ='red', label="Dados experimentais", color = 'green')
plt.xlabel("Resistência (Ω)")
plt.ylabel("Tensão (V)")


x_r = np.linspace(0, 1510, 100)
y_u = x_r*corrente
plt.plot(x_r, y_u, label="Ajuste linear (V = I * R)", color='blue')
plt.legend()
plt.show()

def valor_real_resistor(ddp):
    resistencia = []
    for U in ddp:
        
        resistencia.append(U/corrente)
    return resistencia

voltage1 = []
for j in range(len(voltage)-1):
    
    voltage1.append(voltage[j]-voltage[j+1])
print( 'resistores calibrados:' ,end = '\t')  
print(valor_real_resistor(voltage1))
        

    
A
