#!/usr/bin/env python3
"""Exact F_2 elimination certificate for lines on the space-filling K3 quartic.

Requires sympy. Recomputes all six Grassmannian RREF charts from the
homogeneous quartic; no point-sampling is used for the algebraic-closure claim.
"""
from itertools import combinations, product
from sympy import Poly, expand, groebner, symbols

s,t=symbols('s t')

def quartic(x):
    x0,x1,x2,x3=x
    phi=lambda i,j:x[i]**2*x[j]+x[i]*x[j]**2
    return x1*phi(0,1)+x2*phi(1,2)+x3*phi(2,3)+(x0+x3)*phi(3,0)

expected={
 (0,1):['v0 + v2','v1 + v2 + v3','v2**2 + v2','v2*v3 + v2 + v3 + 1','v3**2 + v3'],
 (0,2):['v0','v1','v2'],
 (0,3):['1'],
 (1,2):['1'],
 (1,3):['v0'],
 (2,3):['1'],
}
count=0
for a,b in combinations(range(4),2):
    freedoms=[(r,j) for r,p in enumerate((a,b)) for j in range(p+1,4) if j not in (a,b)]
    v=symbols('v0:'+str(len(freedoms))) if freedoms else ()
    M=[[0]*4 for _ in range(2)]
    M[0][a]=M[1][b]=1
    for (r,j),z in zip(freedoms,v): M[r][j]=z
    x=[s*M[0][j]+t*M[1][j] for j in range(4)]
    f=Poly(expand(quartic(x)),s,t)
    equations=[f.coeff_monomial(s**i*t**(4-i)) for i in range(5)]
    if not v:
        basis=['1'] if any(int(z)%2 for z in equations) else []
    else:
        basis=[str(z.as_expr()) for z in groebner(equations,*v,order='lex',modulus=2).polys]
    assert basis==expected[(a,b)], (a,b,basis)
    if '1' in basis: chartpoints=0
    elif (a,b)==(0,1):
        # F_2[v2,v3]/(v2^2+v2,v3^2+v3,(v2+1)(v3+1)) = F_2^3.
        chartpoints=3
    else:
        # Explicit maximal ideal in all variables: F_2.
        chartpoints=1
    count+=chartpoints
    print('chart',a,b,'basis:',basis,'geometric-points:',chartpoints)
assert count==5
print('PASS: F_1(X) has exactly five geometric F_2-rational points; total =',count)
print('Scheme reducedness: use N_{L/X} = O(-2) and H0(N) = 0 on the smooth K3 quartic.')
