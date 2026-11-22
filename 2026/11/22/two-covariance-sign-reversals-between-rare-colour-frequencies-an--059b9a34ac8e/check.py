"""Exact checks for the frequency–switch covariance in a symmetric Polya scheme."""
from fractions import Fraction
from itertools import product
from math import comb

def rising(a,k):
    z=Fraction(1)
    for i in range(k):z*=a+i
    return z

def formula(q,a,n,r):
    a=Fraction(a)
    d=Fraction((q-1)*a,q*a+1)
    b=Fraction((q-2)*a,(q-1)*a+1)
    p=Fraction(comb(n,r))*rising(a,r)*rising((q-1)*a,n-r)/rising(q*a,n)
    F=2*r*(n-r)+(n-r)*(n-r-1)*b-n*(n-1)*d
    return q*p*F/n, F, p

def brute(q,a,n,r):
    a=Fraction(a)
    normalizer=rising(q*a,n)
    ER=EC=ERC=Fraction(0)
    for seq in product(range(q), repeat=n):
        counts=[seq.count(j) for j in range(q)]
        prob=Fraction(1,1)
        for c in counts: prob*=rising(a,c)
        prob/=normalizer
        R=sum(seq[i]!=seq[i+1] for i in range(n-1))
        C=sum(c==r for c in counts)
        ER+=prob*R; EC+=prob*C; ERC+=prob*R*C
    return ERC-ER*EC

cases=0
for q in (2,3):
    for a in (Fraction(1,2),Fraction(1),Fraction(2)):
        for n in range(2,8 if q==3 else 9):
            for r in range(1,n+1):
                f,F,p=formula(q,a,n,r)
                b=brute(q,a,n,r)
                assert f==b,(q,a,n,r,f,b)
                if r==1:
                    assert F==Fraction((n-1)*(a+1),a*(q-1)+1)*(2-Fraction(n*a,q*a+1))
                if r>=2:
                    _,Fs,_=formula(q,a,r,r)
                    _,Fm,_=formula(q,a,q*r,r)
                    assert Fs<0 and Fm>0
                cases+=1
print('All exact word enumerations and quadratic sign checkpoints passed:',cases)

# Symbolic derivations, including all positivity identities.
import sympy as s
q,a,n,r=s.symbols('q a n r',positive=True)
d=(q-1)*a/(q*a+1)
b=(q-2)*a/((q-1)*a+1)
F=2*r*(n-r)+(n-r)*(n-r-1)*b-n*(n-1)*d
assert s.simplify(s.diff(F,n,2)-2*(b-d))==0
assert s.simplify((b-d)+a*(a+1)/((q*a+1)*(a*(q-1)+1)))==0
assert s.simplify(F.subs(n,r)+r*(r-1)*d)==0
assert s.simplify(F.subs(n,q*r)-r*(a+r)*(q-1)*(a*q+2)/((a*q+1)*(a*(q-1)+1)))==0
assert s.simplify(F.subs(r,1)-(n-1)*(a+1)/(a*(q-1)+1)*(2-n*a/(q*a+1)))==0
T=s.symbols('T',real=True)
f=s.factor(s.limit(F.subs(n,T*r)/r**2,r,s.oo))
tplus=q+1/a+s.sqrt(a*a*q*q-a*a*q+2*a*q-a+1)/(a*s.sqrt(a+1))
tminus=q+1/a-s.sqrt(a*a*q*q-a*a*q+2*a*q-a+1)/(a*s.sqrt(a+1))
assert s.simplify(f.subs(T,tminus))==0
assert s.simplify(f.subs(T,tplus))==0
print('Symbolic identities, concavity, and limiting roots passed.')
