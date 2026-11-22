"""Independent algebraic checks for parity-optimal Kemeny sampling on finite paths.

Run: python verify.py (requires SymPy). This finite verification supports, but does
not replace, the all-order multiplier proof supplied in RESULT.md.
"""
from fractions import Fraction
from math import sqrt
import sympy as sp

checks = 0

def assert_eq(a,b):
    global checks
    assert sp.simplify(a-b)==0, (a,b)
    checks += 1

r,k = sp.symbols('r k', integer=True, positive=True)
j = sp.symbols('j', integer=True, positive=True)
for n, odd in ((2*r,False),(2*r+1,True)):
    O = sp.factor(sp.summation((2*j-1)*(n-2*j+1), (j,1, r if not odd else r)))
    E = sp.factor(sp.summation((2*j)*(n-2*j), (j,1, r-1 if not odd else r)))
    Ok = sp.factor(sp.summation((2*j-1)*(n-2*j+1), (j,1,k)))
    Ek = sp.factor(sp.summation((2*j)*(n-2*j), (j,1,k)))
    assert_eq(O, r*(2*r*r+1)/3 if not odd else r*(r+1)*(2*r+1)/3)
    assert_eq(E, 2*r*(r*r-1)/3 if not odd else r*(r+1)*(2*r+1)/3)
    assert_eq(Ok,k*(-4*k*k+6*k*r+(1 if not odd else 3*k+1))/3)
    assert_eq(Ek,2*k*(k+1)*(-2*k+3*r-1)/3 if not odd else k*(k+1)*(-4*k+6*r+1)/3)
    ne = sp.factor(O*Ek-E*Ok)
    no = sp.factor(E*Ok-O*Ek.subs(k,k-1))
    if not odd:
        assert_eq(ne,2*k*r*(r-k)*(2*k+2*r*r-r+1)/3)
        assert_eq(no,2*k*r*(r-k)*(-2*k+2*r*r+r+1)/3)
    else:
        assert_eq(ne,2*k*r*(r-k)*(r+1)*(2*r+1)/3)
        assert_eq(no,2*k*r*(r+1)*(2*r+1)*(r-k+1)/3)

for n in range(3,501):
    cs = [i*(n-i) for i in range(1,n)]
    O = sum(cs[::2]); E = sum(cs[1::2])
    assert O>0 and E>0
    if n % 2 == 0:
        assert_eq(sp.Integer(O), sp.Rational(n*(n*n+2),12))
        assert_eq(sp.Integer(E), sp.Rational(n*(n*n-4),12))
    else:
        assert_eq(sp.Integer(O), sp.Integer(E))
        assert_eq(sp.Integer(O), sp.Rational(n*(n*n-1),12))
    eta = Fraction(0)
    for i,c in enumerate(cs):
        eta=Fraction(c,O if i%2==0 else E)-eta
        checks += 1
        if i<len(cs)-1: assert eta>0,(n,i,eta)
        else: assert eta==0,(n,eta)
    a=sqrt(O)/(sqrt(O)+sqrt(E)); b=1-a
    assert abs(a+b-1)<1e-14
    kvalue=sum(c/(a if i%2==0 else b) for i,c in enumerate(cs))/n
    target=(sqrt(O)+sqrt(E))**2/n
    assert abs(kvalue-target)<1e-8*(1+target)
    checks += 2

for n in range(3,11):
    cs=[i*(n-i) for i in range(1,n)]
    for a,b in ((sp.Rational(1,2),sp.Rational(1,2)),(sp.Rational(2,5),sp.Rational(3,5)),(sp.Rational(3,5),sp.Rational(2,5))):
        w=[a if i%2==0 else b for i in range(n-1)]
        L=sp.zeros(n)
        for i,v in enumerate(w):
            L[i,i]+=v;L[i+1,i+1]+=v;L[i,i+1]-=v;L[i+1,i]-=v
        J=sp.ones(n)/n
        spectral_trace=sp.trace((L+J).inv())-1
        cut_sum=sum(sp.Rational(c,1)/v for c,v in zip(cs,w))/n
        assert_eq(spectral_trace,cut_sum)

# Exact Bregman-plus-holding-penalty identity, including strict positivity.
for n in range(3,13):
    cs=[i*(n-i) for i in range(1,n)]
    O=sum(cs[::2]); E=sum(cs[1::2])
    C=(sp.sqrt(O)+sp.sqrt(E))**2
    ws=[sp.sqrt(O)/(sp.sqrt(O)+sp.sqrt(E)) if i%2==0 else sp.sqrt(E)/(sp.sqrt(O)+sp.sqrt(E)) for i in range(n-1)]
    eta=sp.Rational(0); es=[]
    for i,c in enumerate(cs):
        eta=sp.Rational(c,O if i%2==0 else E)-eta
        if i<n-2: es.append(eta)
    for t in (sp.Rational(1,4),sp.Rational(2,5),sp.Rational(1,2)):
        w=[t]*(n-1)
        lhs=sum(c*(1/z-1/zs) for c,z,zs in zip(cs,w,ws))
        sq=sum(c*(z-zs)**2/(z*zs**2) for c,z,zs in zip(cs,w,ws))
        holding=C*sum(es[j]*(1-w[j]-w[j+1]) for j in range(n-2))
        assert_eq(lhs,sq+holding)

print('PASS',checks,'algebraic, exact KKT, and resolvent-trace checks')
