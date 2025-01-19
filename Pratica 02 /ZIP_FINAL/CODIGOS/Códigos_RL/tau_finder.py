import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

data_path = {'C3':'/home/carlos/Documentos/Laborat-rio-1/Pratica 02 /DadosRL/Dados 3/RigolDS0.csv', 'C5':'/home/carlos/Documentos/Laborat-rio-1/Pratica 02 /DadosRL/Dados 5/RigolDS0.csv'}

df_3, df_5 = pd.read_csv(data_path['C3']), pd.read_csv(data_path['C5'])

# Descida
# Vamos encontrar a período de dados corespondente a uma descida

contencao_esq_id, contencao_dir_id = 72, 511 # Aqui escolhemos um dado que isola dois picos, um máximo e um mínimo, e vamos usar esses para determinar os intervalo de descida
def func(t, V_max, tau):
    return -V_max*(1- np.exp(-t/tau))

def ajuste( df, esq_id = contencao_esq_id,dir_id = contencao_dir_id, plot = True):
    esq = df['CH1V'].loc[esq_id:dir_id+1].idxmin()
    dir = df['CH1V'].loc[esq_id:dir_id+1].idxmax()
    print(esq, dir)
    x = df['Time(s)'].iloc[esq:dir+1].to_numpy()
    y = df['CH2V'].iloc[esq:dir+1].to_numpy()
    x_adjusted = x - x[0]

    parametros, _ = curve_fit(func, x_adjusted, y, p0 = [1,0.04])
    V_max, tau  = parametros
    if plot:
        plt.figure(figsize=(8, 5))
        plt.scatter(x_adjusted, y, label='Dados experimentais', color='blue')
        t_fit = np.linspace(x_adjusted.min(), x_adjusted.max(), 500)
        y_fit = func(t_fit, V_max, tau)
        plt.plot(t_fit, y_fit, label=f'Ajuste: $V_{{max}}={V_max:.2f}, \\tau={tau:.5f}$', color='red')
        plt.xlabel('Tempo (s)')
        plt.ylabel('Tensão (V)')
        plt.legend()
        plt.show()
    return tau
    

resistencia_indutores = np.array([21.46, 21.906, 21.19, 21.2, 21.41])
resistencia_100 = 100


#tau = L/R


print('Caso 3 indutores')

tau_3 =ajuste(df_3)
resistencia_eq_sem_impedancia_3 = np.sum(resistencia_indutores[:3]) + resistencia_100
tau_3_nominal = 3*10**(-3)/resistencia_eq_sem_impedancia_3
# Note que a impedância deve ser um valor somado 
resistencia_impedancia_3 = 3*10**(-3)/tau_3 - resistencia_eq_sem_impedancia_3

print(tau_3)
print(tau_3_nominal)
print(resistencia_impedancia_3)
print(tau_3/tau_3_nominal)


print('Caso 5 indutores')
tau_5 = ajuste(df_5)

resistencia_eq_sem_impedancia_5 = np.sum(resistencia_indutores) + resistencia_100
tau_5_nominal = 5*10**(-3)/resistencia_eq_sem_impedancia_5
resistencia_impedancia_5 = 5*10**(-3)/tau_5 - resistencia_eq_sem_impedancia_5
print(tau_5)
print(tau_5_nominal)
print(resistencia_impedancia_5)

# Save the results to a text file
results = f"""Resultados para Caso 3 (Indutores):
Tau (ajustado): {tau_3}
Tau (nominal): {tau_3_nominal}
Impedância: {resistencia_impedancia_3}
Razão Tau ajustado / Tau nominal: {tau_3/tau_3_nominal}

Resultados para Caso 5 (Indutores):
Tau (ajustado): {tau_5}
Tau (nominal): {tau_5_nominal}
Impedância: {resistencia_impedancia_5}
Razão Tau ajustado / Tau nominal: {tau_3/tau_3_nominal}
"""

# Save to file
file_path = "/home/carlos/Documentos/Laborat-rio-1/Pratica 02 /DadosRL/ Casos.txt"
with open(file_path, "w") as f:
    f.write(results)

print(f"Resultados salvos em {file_path}")