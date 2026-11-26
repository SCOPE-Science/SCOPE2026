"""Exact finite sanity checks for sparse scroll ruling-curve critical counts."""
import sympy as s
from functools import reduce
T=s.Symbol('t')
CASES=[(2,3),(2,4),(3,5),(2,2,3),(2,3,4)]
for ix,ns in enumerate(CASES):
    ss=[sum(T**(2*j) for j in range(n+1)) for n in ns]
    L=s.lcm_list(ss)
    f=0
    for i,n in enumerate(ns):
        # Independent rank-one orthogonal projectors in disjoint coordinate blocks.
        w=[1+(i+1)*(j+1)+(j*j+2*i)%5 for j in range(n+1)]
        q=sum(w[j]*T**j for j in range(n+1))
        f+=q*q/(sum(z*z for z in w)*ss[i])
    N=s.cancel(s.diff(f,T)); A,B=map(s.Poly,s.fraction(N)); degree=2*s.degree(L)-2
    assert A.degree()==degree, (ns,A.degree(),degree)
    assert s.gcd(A,B).degree()==0
    assert s.gcd(A,A.diff()).degree()==0, (ns,'multiple critical roots')
    print(ns,'delta',s.degree(L),'critical',A.degree(),'simple',True)
print('VERIFY_OK')
