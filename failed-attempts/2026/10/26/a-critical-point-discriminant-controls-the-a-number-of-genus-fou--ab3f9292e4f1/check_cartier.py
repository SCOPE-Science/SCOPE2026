#!/usr/bin/env python3
"""Exact finite characteristic-five diagnostic for the cubic Artin-Schreier Cartier computation."""
from itertools import product
P=5

def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            z[i+j]=(z[i+j]+x*y)%P
    return z

def translated(a,b,c,u):
    # alpha*(x+u)^3 + beta*(x+u)^2 + gamma*(x+u) + delta
    return a%P, (b+3*a*u)%P, (c+2*b*u+3*a*u*u)%P

count=0
superspecial=0
for alpha,beta,gamma in product(range(1,5),range(5),range(5)):
    poly=[0,gamma,beta,alpha]
    squared=mul(poly,poly)
    H=(beta*beta+2*alpha*gamma)%P
    assert squared[4]==H
    ddisc=(4*beta*beta-12*alpha*gamma)%P
    assert ddisc==(4*H)%P
    for u in range(P):
        A,B,C=translated(alpha,beta,gamma,u)
        assert (B*B+2*A*C)%P==H
    if H==0:
        superspecial+=1
        inv3=2
        u=(-beta*inv3*pow(alpha,-1,P))%P
        A,B,C=translated(alpha,beta,gamma,u)
        assert B==0 and C==0
    count+=1
assert count==100
assert superspecial==20
print('VERIFY_OK: 100 cubic coefficient triples, 20 superspecial, 500 translations; exact characteristic-five identities hold')
