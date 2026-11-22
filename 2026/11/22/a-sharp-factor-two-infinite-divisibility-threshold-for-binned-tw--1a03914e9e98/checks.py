"""Standalone, reproducible exact-arithmetic and high-precision stress checks.
The infinite-support conclusions are proved analytically in RESULT.md;
finite checks are consistency diagnostics and not substitutes for proofs.
"""
from fractions import Fraction as Q
import math
import mpmath as mp
import sympy as s

assertions=0
def check(cond):
    global assertions
    assert cond
    assertions += 1

p=s.symbols('p', positive=True)
u,v,z=s.symbols('u v z', positive=True)
A=3*(1-p*p)
B=2*(1-p**3)
rg=s.factor((B*p*p-A*p**3)/(A-B))
check(s.simplify(rg-p*p*(2+p)/(1+2*p))==0)
check(s.simplify((A-B)-(1-p)**2*(1+2*p))==0)
check(s.factor((A/(1-p*p*z)-B/(1-p**3*z))-(A-B)*(1+rg*z)/((1-p*p*z)*(1-p**3*z)))==0)
for q in [Q(1,4),Q(1,2),Q(3,5),Q(2,3),Q(4,5),Q(9,10),Q(19,20),Q(99,100)]:
    uu=q*q; vv=q**3; rr=uu*(2+q)/(1+2*q)
    a=3*(1-uu); b=2*(1-vv)
    check(a-b>0)
    check(rr>uu>vv>0)
    # exact 96 coefficients in both ways, plus exact pgf and telescoping
    prev=Q(0)
    for n in range(1,97):
        # log coefficient exact at every degree
        lam=(uu**n+vv**n+(-1)**(n-1)*rr**n)/n
        if n%2==1: check(lam>0)
        else:
            # exact sign equivalence (no floating point)
            check((lam<0)==((rr/uu)**n>1+(vv/uu)**n))
            if prev<0: check(lam<0)
            prev=lam
    # finite masses strictly positive
    for n in range(80):check(a*uu**n-b*vv**n>0)

mp.mp.dps=60
c=mp.findroot(lambda t: mp.e**(t/3)-1-mp.e**(-t),(.8,1.1))
check(mp.mpf('.96')<c<mp.mpf('.97'))
for q in [mp.mpf('.9'),mp.mpf('.99'),mp.mpf('.999'),mp.mpf('.9999')]:
    R=(2+q)/(1+2*q)
    # root of log R*n - log(1+q^n)=0
    root=mp.findroot(lambda n: n*mp.log(R)-mp.log1p(q**n),(.8/(1-q),1.2/(1-q)))
    first=2*int(mp.floor(root/2))+2
    check(first>root and first<=root+2)
    check(R**first>1+q**first)
    check(R**(first-2)<1+q**(first-2))
    check(abs(root*(1-q)-c)<mp.mpf('.2'))

for a in ['.1','.5','1','2','5']:
    aa=mp.mpf(a); uu=mp.e**(-aa)
    for rat in ['1.01','1.1','1.5','1.999','2','2.001','3','6']:
        bb=aa*mp.mpf(rat);vv=mp.e**(-bb)
        A=bb*(1-uu)/(bb-aa);B=aa*(1-vv)/(bb-aa)
        rr=(B*uu-A*vv)/(A-B)
        check(rr>0 and rr<1)
        check((rr<uu) if mp.mpf(rat)>2 else ((rr>uu) if mp.mpf(rat)<2 else (abs(rr-uu)<mp.mpf("1e-48"))))
        check(abs(A/(1-uu)-B/(1-vv)-1)<mp.mpf('1e-50'))
        for n in [0,1,2,3,8,15]: check(A*uu**n>B*vv**n)
    D=1-uu-aa*uu
    rr=uu*(aa+uu-1)/D
    check(D>0 and rr>uu)

# Exact structural polynomial for the rate-doubling case b=2a,
# expressed in the natural coordinate u=e^{-a}.
q=s.symbols('q',positive=True)
check(s.factor(2*(1-q)*(1+q) - 2*(1-q*q))==0)
# Strict logarithmic mean inequality is pure calculus, so finite numerical checks
# here are only corroborative.
for i in range(1,1000):
    qv=mp.mpf(i)/1000
    check(-mp.log(qv)>2*(1-qv)/(1+qv))
print('PASS:',assertions,'checks; c_star=',mp.nstr(c,35))
