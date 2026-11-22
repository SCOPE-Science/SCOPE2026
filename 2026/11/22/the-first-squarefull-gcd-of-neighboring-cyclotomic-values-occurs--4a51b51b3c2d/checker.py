"""Exact finite certificate for first squarefull neighboring cyclotomic gcd.
Requires Python 3 and SymPy >=1.12. Run from the directory containing certificate.json.
"""
import json
from math import isqrt
from pathlib import Path
import sympy as sp


def prime_by_trial(p):
    if p < 2:
        return False
    return all(p % d for d in range(2, isqrt(p) + 1))


def horner(coeff, x, mod):
    y = 0
    for c in reversed(coeff):
        y = (y*x + c) % mod
    return y


def shifted_coeff(coeff):
    # Coefficients of f(X+1), computed over the integers.
    return [sum(coeff[j]*int(sp.binomial(j,i)) for j in range(i,len(coeff))) for i in range(len(coeff))]


def certify():
    data=json.loads(Path('certificate.json').read_text(encoding='utf8'))
    assert data['range']==[1,28]
    total_roots=0
    for m in range(1,29):
        x=sp.Symbol('x')
        f=sp.Poly(sp.cyclotomic_poly(m,x),x,domain='ZZ')
        cf=[int(v) for v in reversed(f.all_coeffs())]
        sf=sp.Poly(sum(cf[i]*(x+1)**i for i in range(len(cf))),x,domain='ZZ')
        result=abs(int(sp.resultant(f,sf,x)))
        factors={int(p):int(k) for p,k in data['factorizations'][str(m)].items()}
        assert all(prime_by_trial(p) and k>0 for p,k in factors.items()),m
        product=1
        for p,k in factors.items(): product*=p**k
        assert product==result,(m,product,result)
        cshift=shifted_coeff(cf)
        for p in factors:
            for a in range(p):
                if horner(cf,a,p)!=0 or horner(cshift,a,p)!=0: continue
                total_roots+=1
                # Every lift modulo p^2 has form a+p*t, t in [0,p-1].
                # First-order Taylor formula gives two exact linear congruences.
                # An explicit modular loop is exhaustive even for singular roots.
                dp=[i*cf[i] for i in range(1,len(cf))]
                dq=[i*cshift[i] for i in range(1,len(cshift))]
                u=(horner(cf,a,p*p)//p)%p
                v=(horner(cshift,a,p*p)//p)%p
                c=horner(dp,a,p); d=horner(dq,a,p)
                sols=[t for t in range(p) if (u+t*c)%p==0 and (v+t*d)%p==0]
                assert not sols,('unexpected lift',m,p,a,sols)
    p=59; modulus=p*p; a=298
    ff=[1]*29
    assert all(horner(ff,n,modulus)==0 for n in (a,a+1))
    print('PASS: complete indices 1..28,',total_roots,'common roots checked; 29 witness at n=298, p=59.')

if __name__=='__main__': certify()
