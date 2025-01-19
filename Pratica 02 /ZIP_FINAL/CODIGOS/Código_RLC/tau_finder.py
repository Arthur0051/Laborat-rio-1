import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

# Definir os caminhos para os arquivos de dados
data_path = {
    'C0': "Pratica 02 /ZIP_FINAL/Dados (csv)/RLC - 0 Ohm.csv", 
    'C300': "Pratica 02 /ZIP_FINAL/Dados (csv)/RLC - 300 Ohm.csv", 
    'C600': "Pratica 02 /ZIP_FINAL/Dados (csv)/RLC - 600 Ohm.csv"
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
L1 = 3 * 10**(-3)
C1 = 25 * 10**(-9)

alfa, omega = calculate_alfa_omega(R1, L1, C1)
print(f"Alfa calculado: {alfa}, Omega calculado: {omega}")

# Função de ajuste
def func(t, Voff, V_max, alfa, omega):
    beta = np.sqrt(omega**2 - alfa**2)
    return V_max * np.exp(-alfa * t) * (np.cos(beta * t) + (alfa / beta) * np.sin(beta * t)) + Voff

# Ajustar os dados e plotar
for key, df in dataframes.items():
    id_min, id_max = 0, 100
    tempo = df['Time(s)'].loc[id_min:id_max + 1].values
    ddv = df['CH2V'].loc[id_min:id_max + 1].values

    # Ajustar o tempo para começar em zero
    tempo = tempo - tempo[0]

    # Parâmetros iniciais para o ajuste
    p0 = [0, 2.5, alfa, omega]

    # Ajuste de curva
    params, _ = curve_fit(func, tempo, ddv, p0=p0, maxfev=10000)
    Voff_fit, V_max_fit, alfa_fit, omega_fit = params
    print(f"{key} - Parâmetros ajustados: Voff={Voff_fit}, V_max={V_max_fit}, alfa={alfa_fit}, omega={omega_fit}")

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

output_file = "/home/carlos/Documentos/Laborat-rio-1/Pratica 02 /DadosRLC/dados.txt"

# Abrir o arquivo para escrita
with open(output_file, 'w') as f:
    
    f.write("Resultados dos Parâmetros Ajustados e Calculados:\n")
    f.write("Arquivo\t\t\tV_off (V)\tV_max (V)\tAlfa_ajustado (1/s)\tOmega_ajustado (rad/s)\tAlfa_calculado (1/s)\tOmega_calculado (rad/s)\n")
    f.write("="*120 + "\n")
    
    # Ajustar os dados e salvar os resultados
    for key, df in dataframes.items():
        id_min, id_max = 0, 100
        tempo = df['Time(s)'].loc[id_min:id_max + 1].values
        ddv = df['CH2V'].loc[id_min:id_max + 1].values

        # Ajustar o tempo para começar em zero
        tempo = tempo - tempo[0]

        # Parâmetros iniciais para o ajuste
        p0 = [0, 2.5, alfa, omega]

        # Ajuste de curva
        params, _ = curve_fit(func, tempo, ddv, p0=p0, maxfev=10000)
        Voff_fit, V_max_fit, alfa_fit, omega_fit = params
        print(f"{key} - Parâmetros ajustados: Voff={Voff_fit}, V_max={V_max_fit}, alfa={alfa_fit}, omega={omega_fit}")

        # Escrever os resultados no arquivo
        f.write(f"{key}\t\t{Voff_fit:.6e}\t{V_max_fit:.6e}\t{alfa_fit:.6e}\t{omega_fit:.6e}\t{alfa:.6e}\t{omega:.6e}\n")

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


