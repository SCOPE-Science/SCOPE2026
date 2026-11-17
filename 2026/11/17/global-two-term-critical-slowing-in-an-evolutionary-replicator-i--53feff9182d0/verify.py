#!/usr/bin/env python3
"""Independent algebraic and finite-trajectory checks for a scalar replicator map.
Run with Python 3 and SymPy; finite checks are not a substitute for proof.
"""
import math
from fractions import Fraction
import sympy as s

def polys_mul(v,w,N=5):
    return [sum(v[j]*w[k-j] for j in range(k+1)) for k in range(N+1)]

b=s.symbols('b',real=True)
B=b*(1-b)
a=2/B
N=5
expo=[a**j/s.factorial(j) for j in range(N+1)]
ep=polys_mul([1-b,-1,0,0,0,0],expo)
den=[1,ep[1]+1]+ep[2:]
num=[b,1,0,0,0,0]
t=[]
for k in range(N+1):
    t.append(s.factor(num[k]-sum(den[j]*t[k-j] for j in range(1,k+1))))
C=2*(1-3*B)/(3*B**2)
D=2*(2*b-1)*(1-3*B)/(3*B**3)
E=2*(30*B**2-20*B+3)/(15*B**4)
assert all(s.factor(t[i]-v)==0 for i,v in enumerate([b,-1,0,C,D,E]))
K=s.factor((6*C**2+4*E)/(4*C))
Kexpected=(2-5*B)*(4-15*B)/(5*B**2*(1-3*B))
assert s.factor(K-Kexpected)==0
assert s.factor(3*C**2-2*E - (3*C**2-2*E))==0

def iterate(bval,x0,n):
    alpha=2/(bval*(1-bval))
    x=x0
    for _ in range(n):
        x=x/(x+(1-x)*math.exp(alpha*(x-bval)))
    return x

for bv in [0.2,0.3,0.5,0.7]:
    q=bv*(1-bv)
    Cn=2*(1-3*q)/(3*q*q)
    n=180_000
    x=iterate(bv,bv+0.07 if bv<.5 else bv-0.07,n)
    leading=n*(x-bv)**2
    target=1/(2*Cn)
    assert abs(leading/target-1)<0.005,(bv,leading,target)
# Slow convergence of the logarithmic coefficient is expected; use two fairly long ranges.
for bv in [.3,.5]:
    q=bv*(1-bv)
    Cn=2*(1-3*q)/(3*q*q)
    Kn=(2-5*q)*(4-15*q)/(5*q*q*(1-3*q))
    def U(n):
        x=iterate(bv,bv+0.05,n)
        return 1/(x-bv)**2
    n=200_000
    estim=(U(2*n)-U(n)-2*Cn*n)/math.log(2)
    assert abs(estim-Kn)<0.09,(bv,estim,Kn)
print('VERIFY_OK critical_taylor=1 inverse_square_log_coefficient=1 global_rate_cases=4 log_coefficient_cases=2')
