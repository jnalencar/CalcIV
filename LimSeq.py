#1. Implemente uma função chamada limite para determinar o limite de uma sequência.
#Observação: Existe uma implementação na biblioteca sympy do Python chamada
#limit_seq (Clique aqui ). A construção da sua função pode ser feita de maneira
#similar.

#(a) Caso lim an = L ∈ R, a função deve retornar o valor com aproximação de 2 casas decimais.

#(b) Caso lim an = ∞, a função deve retornar “infinito”.

#(c) Caso lim an não existir, a função deve retornar “não existe”.

import sympy as sp
from sympy.abc import n, k, m
#Tentei as bibliotecas math e cmath para usar funções trigonométricas, mas não consegui,
#no momento o programa funciona apenas com a variavel "n" no calculo do limite.
#import math
#import cmath

def limite(an):
    try:
        lim = sp.limit_seq(an)
        print("limite: ", end=' ')
        if lim == sp.oo:
            return "infinito"
        elif lim == -sp.oo:
            return "-infinito"
        else:
            return round(float(lim), 2)
    except:
        return "não existe, ou a função não é compativel"
    
# Teste
print(limite(1/n))          #0
print(limite(n/(n+1)))      #1
print(limite(-n/(n+1)))     #-1
print(limite(n))            #infinito
print(limite(-n))           #-infinito
print(limite((-1)**n))      #não existe