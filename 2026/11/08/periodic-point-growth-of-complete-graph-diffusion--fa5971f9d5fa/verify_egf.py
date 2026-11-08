#!/usr/bin/env python3
"""Check composition census against a formal power-series identity exactly."""
from fractions import Fraction as F
from math import factorial

N=13
exp=[F(1,factorial(i)) for i in range(N+1)]
num=[F(0)]+[(-1)**(i+1)*exp[i] for i in range(1,N+1)]
D=[F(0) for _ in range(N+1)]
D[0]=F(1)
D[1]=F(-2)
for k in range(2,N+1):
    D[k] = (F(1) if k==2 else F(0)) - exp[k-1]
coeff=[F(0) for _ in range(N+1)]
for k in range(1,N+1):
    coeff[k]=num[k]-sum(D[j]*coeff[k-j] for j in range(1,k+1))
    assert coeff[k].denominator > 0

def compositions(k):
    if k==0:
        yield ()
    else:
        for a in range(1,k+1):
            for rest in compositions(k-a):
                yield (a,)+rest

def count(k):
    s=0
    for groups in compositions(k):
        mult=factorial(k)
        for x in groups:mult//=factorial(x)
        for a,b in zip(groups,groups[1:]):mult*=a+b-1
        s+=mult
    return s

for k in range(1,N+1):
    value=coeff[k]*factorial(k)
    assert value.denominator==1
    independent=count(k)
    assert value==independent, (k,value,independent)
    print(f'n={k} C_n={value} primitive_two_orbits={(value-1)//2}')
print('EGF_OK')
