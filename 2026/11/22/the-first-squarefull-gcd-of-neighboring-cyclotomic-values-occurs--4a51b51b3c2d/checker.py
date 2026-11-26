"""Exact certificate for the first nontrivial squarefull neighboring cyclotomic gcd.

Requires Python 3 and SymPy; run with certificate.json in the working directory.
"""
import json
from math import comb, gcd, isqrt, prod
from pathlib import Path

import sympy as sp


def prime_by_trial(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


def horner(coeff, x, modulus):
    v = 0
    for c in reversed(coeff):
        v = (v*x+c) % modulus
    return v


def derivative(coeff):
    return [i*c for i,c in enumerate(coeff) if i]


def certify():
    data = json.loads(Path('certificate.json').read_text(encoding='utf8'))
    assert data['range'] == [1,28]
    x = sp.Symbol('x')
    count, largest, roots = 0, 0, 0
    for m in range(1,29):
        f = sp.Poly(sp.cyclotomic_poly(m,x), x, domain='ZZ')
        c = [int(v) for v in reversed(f.all_coeffs())]
        g = sp.Poly(sum(c[i]*(x+1)**i for i in range(len(c))), x, domain='ZZ')
        R = abs(int(sp.resultant(f,g,x)))
        factors = {int(p):int(e) for p,e in data['factorizations'][str(m)].items()}
        assert all(prime_by_trial(p) and e>0 for p,e in factors.items())
        assert R == prod(p**e for p,e in factors.items())
        count += len(factors)
        largest = max([largest,*factors])
        s = [sum(comb(j,i)*c[j] for j in range(i,len(c))) for i in range(len(c))]
        cf, cs = derivative(c), derivative(s)
        for p in factors:
            for a in range(p):
                if horner(c,a,p) or horner(s,a,p):
                    continue
                roots += 1
                A,B = horner(c,a,p*p)//p, horner(s,a,p*p)//p
                U,V = horner(cf,a,p), horner(cs,a,p)
                assert all((A+t*U)%p or (B+t*V)%p for t in range(p)), (m,p,a)
    assert (count,largest,roots)==(97,19927,178)
    a=298
    exact = gcd(sum(a**i for i in range(29)),sum((a+1)**i for i in range(29)))
    assert prime_by_trial(59) and exact==59**2==3481
    print(f'PASS: indices 1..28, {roots} common roots, no simultaneous prime-square lifts; G_29(298)={exact}.')


if __name__ == '__main__':
    certify()
