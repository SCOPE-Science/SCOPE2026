#!/usr/bin/env python3
"""Supplementary checks for the sharp quartic two-coset projection theorem."""
import cmath, math
from sympy import primerange, primitive_root
n=0
for p in primerange(5, 1000):
    if p % 8 != 5:
        continue
    g=int(primitive_root(p)); m=(p-1)//4
    C=[{pow(g,j+4*k,p) for k in range(m)} for j in range(4)]
    cl={x:j for j,S in enumerate(C) for x in S}
    J=sum(1j**((cl[x]+cl[(1-x)%p])%4) for x in range(2,p))
    a,b=round(J.real),round(J.imag)
    assert a*a+b*b==p and a%2 and b%2==0 and b!=0
    eta=[sum(cmath.exp(2j*math.pi*x/p) for x in S) for S in C]
    L=[]
    for i,j in [(0,1),(0,2)]:
        E=C[i]|C[j]
        actual=(len(E)+m*sum(abs(eta[(r+i)%4]+eta[(r+j)%4]) for r in range(4)))/p
        L.append(actual)
    A=p+1-b*math.sqrt(p); B=p+1+b*math.sqrt(p)
    adjacent=m/p*(2+math.sqrt(A)+math.sqrt(B))
    opposite=m/p*(2+2*math.sqrt(p))
    assert abs(L[0]-adjacent)<1e-8
    assert abs(L[1]-opposite)<1e-8
    assert adjacent<=opposite+1e-8
    assert (abs(adjacent-opposite)<1e-8)==(abs(b)==2)
    n+=1
assert n==43,n
print('PASS: 43 prime cases; exact Jacobi arithmetic, both norms, ordering and ties')
