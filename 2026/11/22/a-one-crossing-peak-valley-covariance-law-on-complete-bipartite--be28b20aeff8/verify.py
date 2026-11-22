"""Exact checks for the covariance of counts of local extrema on complete bipartite graphs."""
from fractions import Fraction
from itertools import combinations
from math import comb
import sympy as sp


def formula(a: int, b: int) -> Fraction:
    assert 1 <= a <= b
    mean = Fraction(a, b + 1) + Fraction(b, a + 1)
    product = (Fraction(a * (a - 1), (b + 1) * (b + 2))
               + Fraction(b * (b - 1), (a + 1) * (a + 2))
               + 2 - Fraction(2, comb(a+b, a)))
    return product - mean * mean


def enumerate_words(a: int, b: int) -> Fraction:
    n = a+b
    hsum = ts = pts = 0
    for apos in combinations(range(n), a):
        letters = [0] * n
        for pos in apos: letters[pos] = 1
        h = 1
        while h < n and letters[h] == letters[0]: h += 1
        t = 1
        while t < n and letters[n-1-t] == letters[-1]: t += 1
        hsum += h
        ts += t
        pts += h*t
    N = comb(n,a)
    assert hsum == ts
    return Fraction(pts,N) - Fraction(hsum * ts,N*N)


def symbolic_certificates():
    a,b,u,v=sp.symbols('a b u v', integer=True, nonnegative=True)
    f = (a*(a-1)/((b+1)*(b+2)) + b*(b-1)/((a+1)*(a+2))
         + 2-(a/(b+1)+b/(a+1))**2)
    D = sp.factor(f-f.subs(b,b+1))
    n=a+b
    rhs=12*a/((n+1)*n*(n-1)*(n-2))
    W=sp.cancel(D-rhs)
    num,den=sp.fraction(W)
    assert sp.simplify(W-num/den)==0
    # For all a>=3 and b>=a, u=a-3 and v=b-a; the denominator is positive.
    p=sp.Poly(sp.expand(num.subs(b,a+v).subs(a,u+3)),u,v)
    assert len(p.terms())==65
    assert all(c>0 for _,c in p.terms())
    # Case a=2: the exact decrement has a positive shifted numerator.
    f2=sp.factor(f.subs(a,2) - 4/((b+1)*(b+2)))
    d2=sp.factor(f2-f2.subs(b,b+1))
    numerator2, denominator2=sp.fraction(d2)
    p2=sp.Poly(sp.expand(numerator2.subs(b,v+2)),v)
    assert p2.degree()==6 and all(c>0 for _,c in p2.terms())
    # Fixed-shift asymptotic regime b=a+c*sqrt(a).
    c,t=sp.symbols('c t',positive=True)
    fscale=sp.cancel(f.subs(b,t**(-2)+c/t).subs(a,t**(-2)))
    leading=sp.limit(fscale/t**4,t,0)
    assert sp.simplify(leading-8*(1-c*c))==0
    return p,p2,leading

if __name__=='__main__':
    assertions=0
    for a in range(1,8):
        for b in range(a,11-a+1):
            assert enumerate_words(a,b)==formula(a,b), (a,b)
            assertions+=1
    for a in range(2,80):
        assert formula(a,a)>0
        for b in range(a,a+25):
            assert formula(a,b)>formula(a,b+1)
            assertions+=1
    for b in range(2,80):
        assert formula(1,b)<0
        assertions+=1
    p,p2,lead=symbolic_certificates()
    assertions+=3
    print('PASS',assertions,'exact tests; positive symbolic coefficients:',len(p.terms()), len(p2.terms()),'scaling',lead)
    for a in [2,3,4,5,6,9,13,21,32,50,100,300]:
        bstar=max(b for b in range(a,a+int(a**.5)+8) if formula(a,b)>0)
        print('boundary',a,bstar, 'gap',bstar-a)
