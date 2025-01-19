import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

e = np.exp(1)

# Dictionary with portable file paths
data_path = {
    'C1': "ZIP_FINAL/Dados (csv)/RC - Circuito 1.csv",
    'C2': "ZIP_FINAL/Dados (csv)/RC - Circuito 2.csv",
    'C3': "ZIP_FINAL/Dados (csv)/RC - Circuito 3.csv",
    'C4': "ZIP_FINAL/Dados (csv)/RC - Circuito 4.csv"
}

# Print the paths to check
print(data_path)

df_c1 = pd.read_csv(data_path['C1'])
df_c2 = pd.read_csv(data_path['C2'])
df_c3 = pd.read_csv(data_path['C3'])
df_c4 = pd.read_csv(data_path['C4'])

def encontrar_tau_metodo1(intervalo_inicio, intervalo_fim, df):
    # Método 1: encontra o ponto onde V = V_inicial / e
    valor_procurado = df.at[intervalo_inicio, 'CH2V'] / e
    intervalo = df['CH2V'].iloc[intervalo_inicio: intervalo_fim + 1]
    
    # Calcula a diferença absoluta e encontra o índice do valor mais próximo
    id_valor_procurado = (intervalo - valor_procurado).abs().idxmin()

    # Calcula delta_t usando o tempo correspondente ao índice encontrado
    delta_t = df.at[id_valor_procurado, 'Time(s)'] - df.at[intervalo_inicio, 'Time(s)']
    
    return delta_t
def encontrar_tau_metodo2(intervalo_inicio, intervalo_fim, df, plot=True):
    # Ajuste exponencial
    x = df['Time(s)'].iloc[intervalo_inicio: intervalo_fim + 1].to_numpy()
    y = df['CH2V'].iloc[intervalo_inicio: intervalo_fim + 1].to_numpy()
    p = np.polyfit(x, np.log(y), 1)
    a = np.exp(p[1])
    b = p[0]

    if plot:
        plt.figure(figsize=(8, 5))
        # Dados experimentais
        plt.plot(x, y, "o", label="Dados experimentais", color="blue")
        # Ajuste exponencial
        y_fit = a * np.exp(b * x)
        plt.plot(x, y_fit, color="red", label=f"Ajuste: $y = {a:.2f} e^{{{b:.2f}x}}$")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Tensão (V)")
        plt.title("Ajuste Exponencial")
        plt.legend()
        plt.grid(True)
        plt.show()

    return -1 / b

def encontrar_tau_metodo3(intervalo_inicio, intervalo_fim, df):
    dt = df.at[intervalo_fim, "Time(s)"] -  df.at[intervalo_inicio, "Time(s)"]
    ln_VminVmax = np.log(df.at[intervalo_fim, 'CH2V']/df.at[intervalo_inicio, 'CH2V'])
    
    return -dt/ln_VminVmax
def encontrar_tau_metodo4(R,C):
    return R*C
#Caso 1

print('Caso 1')
print(df_c1.head())

R1, C1 = 10*10**3, 100*10**(-9) 

#cortando a base de dadoos



max_ddp_id1 = df_c1['CH2V'].idxmax()
min_ddp_id1 = df_c1['CH2V'].idxmin()
print(max_ddp_id1)
print(min_ddp_id1)


print(encontrar_tau_metodo1(max_ddp_id1,min_ddp_id1, df_c1))
print(encontrar_tau_metodo2(max_ddp_id1,min_ddp_id1, df_c1))
print(encontrar_tau_metodo3(max_ddp_id1,min_ddp_id1, df_c1))
print(encontrar_tau_metodo4(R1,C1))
print('\n','-=-'*10,'\n')
capacitor_calibrado_m1 = encontrar_tau_metodo1(max_ddp_id1, min_ddp_id1, df_c1) / R1
#--------------------------------------------------
print('Caso 2')
#Caso 2

print(df_c2.head())

R2, C2 = 20*10**3, 100*10**(-9)
max_ddp_id2 = df_c2['CH2V'].idxmax()
min_ddp_id2 = df_c2['CH2V'].idxmin()
print(max_ddp_id2)
print(min_ddp_id2)

print(encontrar_tau_metodo1(max_ddp_id1,min_ddp_id1, df_c2))
print(encontrar_tau_metodo2(max_ddp_id1,min_ddp_id1, df_c2))
print(encontrar_tau_metodo3(max_ddp_id1,min_ddp_id1, df_c2))
print(encontrar_tau_metodo4(R2,C2))
print('\n','-=-'*10,'\n')
#--------------------------------------------------
print('Caso 3')
#Caso 3

print(df_c3.head())

R3, C3 = 10*10**3, 200*10**(-9)
max_ddp_id3 = df_c3['CH2V'].idxmax()
min_ddp_id3 = df_c3['CH2V'].idxmin()
print(max_ddp_id3)
print(min_ddp_id3)

print(encontrar_tau_metodo1(max_ddp_id1,min_ddp_id1, df_c2))
print(encontrar_tau_metodo2(max_ddp_id1,min_ddp_id1, df_c2))
print(encontrar_tau_metodo3(max_ddp_id1,min_ddp_id1, df_c2))
print(encontrar_tau_metodo4(R3,C3))
print('\n','-=-'*10,'\n')
#--------------------------------------------------
print('Caso 4')
#Caso 4
#Como todos os datos foram retirados usando a mesma frequência e stup do ociloscopio, vamos usar o pico em todos na posição 475

print(df_c4.head())

R4, C4 = 10*10**3, 50*10**(-9)
max_ddp_id4 = 475
min_ddp_id4 = df_c4['CH2V'].idxmin()
print(max_ddp_id4)
print(min_ddp_id4)

print(encontrar_tau_metodo1(max_ddp_id1,min_ddp_id1, df_c2))
print(encontrar_tau_metodo2(max_ddp_id1,min_ddp_id1, df_c2))
print(encontrar_tau_metodo3(max_ddp_id1,min_ddp_id1, df_c2))
print(encontrar_tau_metodo4(R4,C4))
print('\n','-=-'*10,'\n')


#--------------------------------------------------

#===================================================================
#Crescimento========================================================
#===================================================================

# Vamos econtrar ums subida olhadno os gráficos

# Caso 1

min_ddp_sid1 = df_c1['CH2V'].iloc[490: 875+1].idxmin()
max_ddp_sid1 = df_c1['CH2V'].iloc[490: 875+1].idxmax()


def encontrar_tau_método1_cresce(intervalo_inicio, intervalo_fim, df):
    # Encontra a tensão no intervalo definido
    tensao = df['CH1V'].loc[intervalo_inicio:intervalo_fim].idxmax() # 5V da fonte
    print(tensao)
    
    valor_procurado = df.at[tensao,'CH1V'] * (1 - e**(-1))  # e foi definido como e = np.exp(1) 
    
   
    intervalo = df['CH2V'].iloc[intervalo_inicio:intervalo_fim + 1]
    diferença = (intervalo - valor_procurado).abs()
    id_valor_procurado = diferença.idxmin()
    
    # Calcula delta_t
    delta_t = df.at[id_valor_procurado, 'Time(s)'] - df.at[intervalo_inicio, 'Time(s)']
    return delta_t


def exponencial_crescente(t, Tensão, tau):
    return Tensão*(1 - np.exp(-t/tau))

def encontrar_tau_metodo2_crescimento(intervalo_inicio, intervalo_fim, df, plot=False):
    x = df['Time(s)'].iloc[intervalo_inicio:intervalo_fim + 1].to_numpy()
    y = df['CH2V'].iloc[intervalo_inicio:intervalo_fim + 1].to_numpy()
    x_adjusted = x - x[0]  # Ajusta o referencial do tempo

    try:
        parametros, _ = curve_fit(exponencial_crescente, x_adjusted, y, p0=[y.max(), 1])
        V_max, tau = parametros
    except RuntimeError as e:
        print(f"Erro no ajuste: {e}")
        return None

    if plot:
        plt.figure(figsize=(8, 5))
        plt.scatter(x_adjusted, y, label='Dados experimentais', color='blue')
        t_fit = np.linspace(x_adjusted.min(), x_adjusted.max(), 500)
        y_fit = exponencial_crescente(t_fit, V_max, tau)
        plt.plot(t_fit, y_fit, label=f'Ajuste: $V_{{max}}={V_max:.2f}, \\tau={tau:.5f}$', color='red')
        plt.xlabel('Tempo (s)')
        plt.ylabel('Tensão (V)')
        plt.legend()
        plt.show()

    return tau

# Função para calcular e imprimir os resultados de cada caso
def calcular_capacitor_calibrado(df, R, C, max_ddp_id, min_ddp_id, caso):
    print(f'Caso {caso}')
    print(df.head())
    print(f'Máximo índice: {max_ddp_id}, Mínimo índice: {min_ddp_id}')
    
    # Calcular tau para os diferentes métodos
    tau1 = encontrar_tau_metodo1(max_ddp_id, min_ddp_id, df)
    tau2 = encontrar_tau_metodo2(max_ddp_id, min_ddp_id, df)
    tau3 = encontrar_tau_metodo3(max_ddp_id, min_ddp_id, df)
    tau4 = encontrar_tau_metodo4(R, C)
    
    # Calcular o capacitor calibrado para cada método
    capacitor_calibrado_m1 = tau1 / R
    capacitor_calibrado_m2 = tau2 / R
    capacitor_calibrado_m3 = tau3 / R
    capacitor_calibrado_m4 = tau4 / R
    
    # Imprimir resultados
    print(f'Tau Método 1: {tau1}, Capacitor Calibrado: {capacitor_calibrado_m1}')
    print(f'Tau Método 2: {tau2}, Capacitor Calibrado: {capacitor_calibrado_m2}')
    print(f'Tau Método 3: {tau3}, Capacitor Calibrado: {capacitor_calibrado_m3}')
    print(f'Tau Método 4: {tau4}, Capacitor Calibrado: {capacitor_calibrado_m4}')
    print('\n', '-=-' * 10, '\n')
    
    return {
        'tau1': tau1,
        'tau2': tau2,
        'tau3': tau3,
        'tau4': tau4,
        'capacitor_calibrado_m1': capacitor_calibrado_m1,
        'capacitor_calibrado_m2': capacitor_calibrado_m2,
        'capacitor_calibrado_m3': capacitor_calibrado_m3,
        'capacitor_calibrado_m4': capacitor_calibrado_m4,
    }
result_caso1 = calcular_capacitor_calibrado(df_c1, R1, C1, max_ddp_id1, min_ddp_id1, caso=1)
result_caso2 = calcular_capacitor_calibrado(df_c2, R2, C2, max_ddp_id2, min_ddp_id2, caso=2)
result_caso3 = calcular_capacitor_calibrado(df_c3, R3, C3, max_ddp_id3, min_ddp_id3, caso=3)
result_caso4 = calcular_capacitor_calibrado(df_c4, R4, C4, max_ddp_id4, min_ddp_id4, caso=4)
print(result_caso1)
print(result_caso2)
print(result_caso3)
print(result_caso4)
# Parte do crescimento para o caso 2
# Ajuste do intervalo de dados para o caso 2


min_ddp_sid1 = df_c1['CH2V'].iloc[490: 875+1].idxmin()
max_ddp_sid1 = df_c1['CH2V'].iloc[490: 875+1].idxmax()

print(encontrar_tau_método1_cresce(min_ddp_sid1, max_ddp_sid1, df_c1))  # Método 1 para crescimento
print(encontrar_tau_metodo2_crescimento(min_ddp_sid1, max_ddp_sid1, df_c1, True))  # Método 2 para crescimento (com gráfico)


min_ddp_sid2 = df_c2['CH2V'].iloc[490: 875+1].idxmin()
max_ddp_sid2 = df_c2['CH2V'].iloc[490: 875+1].idxmax()


print('Caso 2 - Crescimento')
print(encontrar_tau_método1_cresce(min_ddp_sid2, max_ddp_sid2, df_c2))  # Método 1 para crescimento
print(encontrar_tau_metodo2_crescimento(min_ddp_sid2, max_ddp_sid2, df_c2, True))  # Método 2 para crescimento (com gráfico)

# Parte do crescimento para o caso 3
# Ajuste do intervalo de dados para o caso 3
min_ddp_sid3 = df_c3['CH2V'].iloc[490: 875+1].idxmin()
max_ddp_sid3 = df_c3['CH2V'].iloc[490: 875+1].idxmax()

print('Caso 3 - Crescimento')
print(encontrar_tau_método1_cresce(min_ddp_sid3, max_ddp_sid3, df_c3))  # Método 1 para crescimento
print(encontrar_tau_metodo2_crescimento(min_ddp_sid3, max_ddp_sid3, df_c3, True))  # Método 2 para crescimento (com gráfico)

# Parte do crescimento para o caso 4
# Ajuste do intervalo de dados para o caso 4
min_ddp_sid4 = df_c4['CH2V'].iloc[490: 875+1].idxmin()
max_ddp_sid4 = df_c4['CH2V'].iloc[490: 875+1].idxmax()

print('Caso 4 - Crescimento')
print(encontrar_tau_método1_cresce(min_ddp_sid4, max_ddp_sid4, df_c4))  # Método 1 para crescimento
print(encontrar_tau_metodo2_crescimento(min_ddp_sid4, max_ddp_sid4, df_c4, True))  # Método 2 para crescimento (com gráfico)



plt.show()

def salvar_em_txt(nome_arquivo, conteudo):
    caminho_completo = os.path.join('Resultados txt', nome_arquivo)
    with open(caminho_completo, 'w') as f:
        f.write(conteudo)

def salvar_resultados(df_c1, df_c2, df_c3, df_c4, R1, C1, R2, C2, R3, C3, R4, C4):
    casos = {
        "Caso 1": {
            "header": str(df_c1.head()),
            "max_ddp_id": df_c1['CH2V'].idxmax(),
            "min_ddp_id": df_c1['CH2V'].idxmin(),
            "tau_metodo_1": encontrar_tau_metodo1(df_c1['CH2V'].idxmax(), df_c1['CH2V'].idxmin(), df_c1),
            "tau_metodo_2": encontrar_tau_metodo2(df_c1['CH2V'].idxmax(), df_c1['CH2V'].idxmin(), df_c1),
            "tau_metodo_3": encontrar_tau_metodo3(df_c1['CH2V'].idxmax(), df_c1['CH2V'].idxmin(), df_c1),
            "tau_metodo_4": encontrar_tau_metodo4(R1, C1),
            "tau_crescimento_metodo_1": encontrar_tau_método1_cresce(min_ddp_sid1, max_ddp_sid1, df_c1),
            "tau_crescimento_metodo_2": encontrar_tau_metodo2_crescimento(min_ddp_sid1, max_ddp_sid1, df_c1, False),
        },
        "Caso 2": {
            "header": str(df_c2.head()),
            "max_ddp_id": df_c2['CH2V'].idxmax(),
            "min_ddp_id": df_c2['CH2V'].idxmin(),
            "tau_metodo_1": encontrar_tau_metodo1(df_c2['CH2V'].idxmax(), df_c2['CH2V'].idxmin(), df_c2),
            "tau_metodo_2": encontrar_tau_metodo2(df_c2['CH2V'].idxmax(), df_c2['CH2V'].idxmin(), df_c2),
            "tau_metodo_3": encontrar_tau_metodo3(df_c2['CH2V'].idxmax(), df_c2['CH2V'].idxmin(), df_c2),
            "tau_metodo_4": encontrar_tau_metodo4(R2, C2),
            "tau_crescimento_metodo_1": encontrar_tau_método1_cresce(min_ddp_sid2, max_ddp_sid2, df_c2),
            "tau_crescimento_metodo_2": encontrar_tau_metodo2_crescimento(min_ddp_sid2, max_ddp_sid2, df_c2, False),
        },
        "Caso 3": {
            "header": str(df_c3.head()),
            "max_ddp_id": df_c3['CH2V'].idxmax(),
            "min_ddp_id": df_c3['CH2V'].idxmin(),
            "tau_metodo_1": encontrar_tau_metodo1(df_c3['CH2V'].idxmax(), df_c3['CH2V'].idxmin(), df_c3),
            "tau_metodo_2": encontrar_tau_metodo2(df_c3['CH2V'].idxmax(), df_c3['CH2V'].idxmin(), df_c3),
            "tau_metodo_3": encontrar_tau_metodo3(df_c3['CH2V'].idxmax(), df_c3['CH2V'].idxmin(), df_c3),
            "tau_metodo_4": encontrar_tau_metodo4(R3, C3),
            "tau_crescimento_metodo_1": encontrar_tau_método1_cresce(min_ddp_sid3, max_ddp_sid3, df_c3),
            "tau_crescimento_metodo_2": encontrar_tau_metodo2_crescimento(min_ddp_sid3, max_ddp_sid3, df_c3, False),
        },
        "Caso 4": {
            "header": str(df_c4.head()),
            "max_ddp_id": 475,  # Supondo que o máximo seja fixo
            "min_ddp_id": df_c4['CH2V'].idxmin(),
            "tau_metodo_1": encontrar_tau_metodo1(475, df_c4['CH2V'].idxmin(), df_c4),
            "tau_metodo_2": encontrar_tau_metodo2(475, df_c4['CH2V'].idxmin(), df_c4),
            "tau_metodo_3": encontrar_tau_metodo3(475, df_c4['CH2V'].idxmin(), df_c4),
            "tau_metodo_4": encontrar_tau_metodo4(R4, C4),
            "tau_crescimento_metodo_1": encontrar_tau_método1_cresce(min_ddp_sid4, max_ddp_sid4, df_c4),
            "tau_crescimento_metodo_2": encontrar_tau_metodo2_crescimento(min_ddp_sid4, max_ddp_sid4, df_c4, False),
        },
    }

    # Criando os arquivos de texto para cada caso
    for caso, dados in casos.items():
        conteudo = f"""
{caso}
Cabeçalho do DataFrame:
{dados['header']}

Max DDP ID: {dados['max_ddp_id']}
Min DDP ID: {dados['min_ddp_id']}
Tau Método 1: {dados['tau_metodo_1']}
Tau Método 2: {dados['tau_metodo_2']}
Tau Método 3: {dados['tau_metodo_3']}
Tau Método 4: {dados['tau_metodo_4']}

Tau Crescimento Método 1: {dados['tau_crescimento_metodo_1']}
Tau Crescimento Método 2: {dados['tau_crescimento_metodo_2']}
"""
        # Definindo o nome do arquivo
        nome_arquivo = f"{caso.replace(' ', '_').lower()}.txt"
        salvar_em_txt(nome_arquivo, conteudo)
        print(f"Arquivo salvo: {nome_arquivo}")

# Chamada da função com suas variáveis
salvar_resultados(df_c1, df_c2, df_c3, df_c4, R1, C1, R2, C2, R3, C3, R4, C4)



