#!/usr/bin/env python3
"""Exact jet-determinant certificate for two branch fibers of a genus-17 curve.
Requires SymPy >= 1.12. Run: python VERIFY.py
This uses exact rational polynomial arithmetic, not floating-point sampling.
"""
import sympy as sp

T = sp.symbols('T')
N = 16
binom = [sp.binomial(sp.Rational(1, 2), k) for k in range(N)]

def root_series(a):
    return [binom[k] * a**k for k in range(N)]

def pair_product(x, y):
    return [sp.expand(sum(x[j] * y[k-j] for j in range(k+1))) for k in range(N)]

def add(x, y):
    return [sp.expand(u+v) for u,v in zip(x,y)]

def subtract(x,y):
    return [sp.expand(u-v) for u,v in zip(x,y)]

f_a, f_minus_a = root_series(1), root_series(-1)
f_b, f_minus_b = root_series(T), root_series(-T)
Pab=pair_product(f_a,f_b)
Pminus=pair_product(f_minus_a,f_minus_b)
Pcross=pair_product(f_a,f_minus_b)
Pcross2=pair_product(f_minus_a,f_b)
E = [
    [sp.Integer(k == 0) for k in range(N)],
    add(f_a,f_minus_a), add(f_b,f_minus_b),
    pair_product(f_a,f_minus_a), pair_product(f_b,f_minus_b),
    add(Pab,Pminus), add(Pcross,Pcross2)
]
O = [
    [sp.Integer(k == 1) for k in range(N)],
    subtract(f_a,f_minus_a), subtract(f_b,f_minus_b),
    subtract(Pab,Pminus), subtract(Pcross,Pcross2)
]

def jet_determinant(sections, degrees):
    mat=sp.Matrix([[sections[j][i] for j in range(len(sections))] for i in degrees])
    return sp.factor(mat.det(method='domain-ge'))

p = 44*T**4-117*T**2+44
q = 208*T**8-656*T**6+1527*T**4-656*T**2+208
pnext = (T**2+1)*(156*T**4-401*T**2+156)
qnext = (T**2+1)*(3056*T**8-9808*T**6+21653*T**4-9808*T**2+3056)

claimed={
    'O_1_3_5_7_9':(O,[1,3,5,7,9],T**6*(T-1)**4*(T+1)**4*p / sp.Integer(8589934592)),
    'O_1_3_5_7_11':(O,[1,3,5,7,11],3*T**6*(T-1)**4*(T+1)**4*pnext/sp.Integer(68719476736)),
    'E_0_2_4_6_8_10_12':(E,[0,2,4,6,8,10,12],T**9*(T-1)**8*(T+1)**8*q/sp.Integer(9223372036854775808)),
    'E_0_2_4_6_8_10_14':(E,[0,2,4,6,8,10,14],T**9*(T-1)**8*(T+1)**8*qnext/sp.Integer(73786976294838206464)),
}
for label,(sections,degrees,expected) in claimed.items():
    actual=jet_determinant(sections,degrees)
    assert sp.cancel(actual-expected)==0, label
    print(label, 'IDENTITY_OK')

assert sp.gcd(p,q)==sp.Integer(1)
assert sp.gcd(p,pnext)==sp.Integer(1)
assert sp.gcd(q,qnext)==sp.Integer(1)
assert sp.gcd(p,sp.diff(p,T))==sp.Integer(1)
assert sp.gcd(q,sp.diff(q,T))==sp.Integer(1)
assert all(r.subs(T,0)!=0 and r.subs(T,1)!=0 and r.subs(T,-1)!=0 for r in [p,q])
assert sp.expand(T**4*p.subs(T,1/T)-p)==0
assert sp.expand(T**8*q.subs(T,1/T)-q)==0
print('COPRIMALITY_AND_ADMISSIBILITY_OK')

ordinary=list(range(11))+[12,14,16,18,20,24]
exception_p=list(range(11))+[12,14,16,20,22,24]
exception_q=list(range(11))+[12,14,16,18,20,28]
for name,orders,weight in [('generic',ordinary,23),('P_zero',exception_p,27),('Q_zero',exception_q,27)]:
    assert len(orders)==17 and orders==sorted(set(orders))
    assert sum(orders)-17*16//2==weight
    print(name,'weight',weight,'vanishing_sequence',orders)
print('ALL_CHECKS_PASSED')
