import pandas as pd



data_path = {'C1': "/home/al.carlos.pereira/Laborat-rio-1/Pratica 02 /DadosRC/RC-onda quadrada/circuito1/wave/RigolDS0.csv",
             'C2': "/home/al.carlos.pereira/Laborat-rio-1/Pratica 02 /DadosRC/RC-onda quadrada/circuito2/data0.csv",
             'C3': "/home/al.carlos.pereira/Laborat-rio-1/Pratica 02 /DadosRC/RC-onda quadrada/circuito3/circuito30.csv",
             'C4': "/home/al.carlos.pereira/Laborat-rio-1/Pratica 02 /DadosRC/RC-onda quadrada/circuito4/circuito40.csv"}

#Caso 1
df_c1 = pd.read_csv(data_path['C1'])
print(df_c1.head())

max_ddp_id = df_c1['CH2V'].idxmax()
min_ddp_id = df_c1['CH2V'].idxmin()


print(df_c1.at[max_ddp_id,'CH2V'])



print(min_ddp_id)

