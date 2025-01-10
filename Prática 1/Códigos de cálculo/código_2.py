
def calibracao_10(tensoes, r_2):
    a0, a1 = tensoes
    data = {'a0': a0, 'a1': a1}

    
    ddp_r_2 = data['a1']
    corrente = ddp_r_2/r_2

    ddp_r_1 =  data['a0'] - data['a1']

    return ddp_r_1/corrente

tensao_A = [5.000, 4.823 ]
tensao_B = [5.000, 4.765 ]
tensao_C = [5.000, 4.765 ]

r_1A =  calibracao_10(tensao_A, 200)
r_1B =  calibracao_10(tensao_B, 200)
r_1C =  calibracao_10(tensao_C, 200)

print(r_1A, r_1B, r_1C)
