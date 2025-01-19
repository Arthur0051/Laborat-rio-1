import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

# Definir os caminhos para os arquivos de dados
data_path = {
    'C0': "ZIP_FINAL/Dados (csv)/RLC - 0 Ohm.csv", 
    'C300': "ZIP_FINAL/Dados (csv)/RLC - 300 Ohm.csv", 
    'C600': "ZIP_FINAL/Dados (csv)/RLC - 600 Ohm.csv"
}

# Carregar os dados
dataframes = {key: pd.read_csv(path) for key, path in data_path.items()}

def calculate_alfa_omega(R, L, C):
    omega = np.sqrt(1 / (L * C))
    alfa = R / (2 * L)
    return alfa, omega

# Valores iniciais dos componentes
resistencia_indutores = np.array([21.46, 21.906, 21.19, 21.2, 21.41])
R1 = np.sum(resistencia_indutores)
L1 = 5 * 10**(-3)
C1 = 25 * 10**(-9)
print(np.sqrt(1/(L1*C1)))


alfa, omega = calculate_alfa_omega(R1, L1, C1)
print(f"Alfa calculado: {alfa}, Omega calculado: {omega}")
print(omega)
# Função de ajuste
def func(t, Voff, V_max, alfa, omega):
    beta = np.sqrt(omega**2 - alfa**2)
    return V_max * np.exp(-alfa * t) * (np.cos(beta * t) + (alfa / beta) * np.sin(beta * t)) + Voff

output_file = "/home/carlos/Documentos/Laborat-rio-1/Pratica 02 /DadosRLC/dados.txt"
# Abrir o arquivo para escrita
with open(output_file, 'w') as f:
    
    f.write("Resultados dos Parâmetros Ajustados e Calculados:\n")
    f.write("Arquivo\t\t\tV_off (V)\t±\tV_max (V)\t±\tAlfa_ajustado (1/s)\t±\tOmega_ajustado (rad/s)\t±\tAlfa_calculado (1/s)\tOmega_calculado (rad/s)\n")
    f.write("="*160 + "\n")
    i = 0
    # Ajustar os dados e salvar os resultados
    for key, df in dataframes.items():
        id_min, id_max = 0, 100
        tempo = df['Time(s)'].loc[id_min:id_max + 1].values
        ddv = df['CH2V'].loc[id_min:id_max + 1].values

        alfa, omega = calculate_alfa_omega(R1 + 300*i, L1, C1)
        # Ajustar o tempo para começar em zero
        tempo = tempo - tempo[0]
        i+=1
        # Parâmetros iniciais para o ajuste
        p0 = [0, 2.5, alfa, omega]

        # Ajuste de curva
        params, cov = curve_fit(func, tempo, ddv, p0=p0, maxfev=10000)
        Voff_fit, V_max_fit, alfa_fit, omega_fit = params

        # Calcular incertezas (desvios padrão)
        uncertainties = np.sqrt(np.diag(cov))
        Voff_err, V_max_err, alfa_err, omega_err = uncertainties


        print(f"{key} - Parâmetros ajustados: Voff={Voff_fit} ± {Voff_err}, V_max={V_max_fit} ± {V_max_err}, alfa={alfa_fit} ± {alfa_err}, omega={omega_fit} ± {omega_err}")

        # Escrever os resultados no arquivo
        f.write(f"Arquivo: {key}\n")
        f.write(f"V_off (V): {Voff_fit:.6e} ± {Voff_err:.6e}\n")
        f.write(f"V_max (V): {V_max_fit:.6e} ± {V_max_err:.6e}\n")
        f.write(f"Alfa ajustado (1/s): {alfa_fit:.6e} ± {alfa_err:.6e}\n")
        f.write(f"Omega ajustado (rad/s): {omega_fit:.6e} ± {omega_err:.6e}\n")
        f.write(f"Alfa calculado (1/s): {alfa:.6e}\n")
        f.write(f"Omega calculado (rad/s): {omega:.6e}\n")
        f.write("="*50 + "\n\n")  # Linha separadora para organizar
        # Gerar curva ajustada
        ddv_ajustada = func(tempo, Voff_fit, V_max_fit, alfa_fit, omega_fit)

        # Plot dos dados e da curva ajustada
        plt.figure(figsize=(10, 6))
        plt.plot(tempo, ddv, 'o', label=f'Dados experimentais {key}')
        plt.plot(tempo, ddv_ajustada, '-', label=f'Curva ajustada {key}', color='red')
        plt.xlabel('Tempo (s)')
        plt.ylabel('Tensão (V)')
        plt.title(f'Ajuste de Oscilação Sub-Amortecida - {key}')
        plt.legend()
        plt.grid(True)
        plt.show()

print(f"Resultados salvos em: {output_file}")
