"""Reproduce finite harmonic spectra for uniform independent sets on cycle prisms.
Only Python standard library. Direct enumeration is intentionally limited to n<=9.
"""
import cmath
import itertools
from math import cos, pi, sqrt

def analytic(n):
    assert n >= 3
    alpha, beta = 1 + sqrt(2), 1 - sqrt(2)
    epsilon = (-1)**n
    Z = alpha**n + beta**n + epsilon
    out_s, out_a = [], []
    for k in range(n):
        c = cos(2*pi*k/n)
        val_s = sqrt(2)*(alpha**n-beta**n)/(4*Z*(3+c))
        if k == 0:
            val_s += n*(epsilon*Z-1)/(8*Z**2)
        val_a = ((alpha**n-epsilon)/(sqrt(2)+c)
                 + epsilon*(1-alpha**(-n))/(sqrt(2)-c))/(4*Z)
        out_s.append(val_s)
        out_a.append(val_a)
    return Z, out_s, out_a

def direct(n):
    # Vertices (j,0) and (j,1); each rung is empty, occupied top, or occupied bottom.
    configurations = []
    for w in itertools.product((0,1,2), repeat=n):
        if all(w[j] == 0 or w[(j+1)%n] == 0 or w[j] != w[(j+1)%n]
               for j in range(n)):
            configurations.append(w)
    q = len(configurations)
    p = sum(w[0] == 1 for w in configurations)/q
    TT, TB = [], []
    for d in range(n):
        tt = sum(w[0] == 1 and w[d] == 1 for w in configurations)/q
        tb = sum(w[0] == 1 and w[d] == 2 for w in configurations)/q
        TT.append(tt-p*p)
        TB.append(tb-p*p)
    S, A = [], []
    for k in range(n):
        S.append(sum(cos(2*pi*k*d/n)*(TT[d]+TB[d]) for d in range(n)))
        A.append(sum(cos(2*pi*k*d/n)*(TT[d]-TB[d]) for d in range(n)))
    return q,S,A

for n in range(3,10):
    z, ss, aa = analytic(n)
    cnt, s0, a0 = direct(n)
    assert abs(z-cnt)<1e-7
    assert max(abs(x-y) for x,y in zip(ss,s0))<1e-10
    assert max(abs(x-y) for x,y in zip(aa,a0))<1e-10
    assert min(ss+aa)>0
    print('PASS n=%d independent sets=%d maxerror=%.3g' % (n,cnt,max(abs(x-y) for x,y in zip(ss+aa,s0+a0))))
for n in (100,150,200,300):
    _,s,a=analytic(n)
    ratio=max(s+a)/min(s+a)
    assert abs(ratio-(4+2*sqrt(2)))<1.0 if n==100 else abs(ratio-(4+2*sqrt(2)))<0.06
    print('large-n check',n,'condition=',round(ratio,9))
print('PASS. Direct enumeration is finite evidence; the all-n theorem uses transfer diagonalization.')
