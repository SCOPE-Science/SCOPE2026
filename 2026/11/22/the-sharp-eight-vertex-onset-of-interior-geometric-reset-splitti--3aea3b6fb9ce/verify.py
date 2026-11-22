"""Reproducibility checks for geometric-reset splitting on short birth-death paths.
Scientific reference: arXiv:2611.01756v1. Requires SymPy (tested with 1.13+).
The theorem for arbitrary rates and the minimality statement are proved in RESULT.md;
finite checks here are supplementary and cannot replace that argument.
"""
from fractions import Fraction
from itertools import product
import sympy as S

s=S.symbols('s',real=True,positive=True)
CHECKS=0

def test(x):
    global CHECKS
    if not bool(x):
        raise AssertionError(x)
    CHECKS+=1

def one(a,z,p):
    """Direct backward-solution of discounted boundary hitting equations."""
    U=S.zeros(a-1)
    for i in range(a-1):
        v=i+1
        U[i,i]=1
        if v>1: U[i,i-1]=-s*(1-p[v])
        if v<a-1: U[i,i+1]=-s*p[v]
    r0=S.zeros(a-1,1); r1=S.zeros(a-1,1)
    r0[0]=s*(1-p[1]);r1[a-2]=s*p[a-1]
    lhs=S.factor(U.inv().multiply(r0)[z-1])
    rhs=S.factor(U.inv().multiply(r1)[z-1])
    return S.factor(lhs/(lhs+rhs)),S.factor(lhs/rhs)

p={1:S.Rational(4,5),2:S.Rational(1,5),3:S.Rational(1,2),
   4:S.Rational(1,2),5:S.Rational(1,2),6:S.Rational(1,2)}
Q,R=one(7,3,p)
q_expected=16*(2-s**2)/(32+25*s-16*s**2-16*s**3)
test(S.simplify(Q-q_expected)==0)
test(S.simplify(R-16*(2-s**2)/(s*(25-16*s**2)))==0)
P=16*s**4-71*s**2+50
test(S.simplify(S.diff(Q,s)+16*P/(32+25*s-16*s**2-16*s**3)**2)==0)
root=S.sqrt((71-S.sqrt(1841))/32)
test(bool(root>0 and root<1))
test(S.simplify(P.subs(s,root))==0)
test(bool(S.N(Q.subs(s,root),30)<S.Rational(16,25)))
test(S.simplify(Q.subs(s,1)-S.Rational(16,25))==0)
# Discrete sampling verifies the sign pattern, independent of root extraction.
for t in [S.Rational(i,200) for i in range(1,201)]:
    test(S.simplify((S.diff(Q,s).subs(s,t))*P.subs(s,t))<=0)
# Broad exact rational checks of continuant odds and no extrema on shorter paths.
for a in range(2,8):
    for z in range(1,a):
        for seed in range(4):
            pi={i:S.Rational(((i*7 + seed*3)%7)+1,9) for i in range(1,a)}
            q,r=one(a,z,pi)
            def D(l,h):
                if l>h:return S.Integer(1)
                d0=S.Integer(1); d1=S.Integer(1)
                for k in range(l+1,h+1):
                    d0,d1=d1,S.expand(d1-s*s*pi[k-1]*(1-pi[k])*d0)
                return d1
            C=S.prod(1-pi[i] for i in range(1,z+1))/S.prod(pi[i] for i in range(z,a))
            prediction=S.factor(C*s**(2*z-a)*D(z+1,a-1)/D(1,z-1))
            test(S.simplify(r-prediction)==0)
            if a<=6:
                dr=S.factor(S.diff(r,s))
                nonzero=[S.sign(dr.subs(s,S.Rational(j,25))) for j in range(1,26)]
                test(all(x>=0 for x in nonzero) or all(x<=0 for x in nonzero))

# General 7/3 polynomial and sharp threshold: rational exact grid (not an exhaustive proof).
for ib,ia in product(range(1,16), repeat=2):
    b=S.Rational(ib,16); A=S.Rational(ia,16)
    N=-1+(3*b-A)*s*s-A*b*s**4
    signs=[S.sign(N.subs(s,S.Rational(j,20))) for j in range(1,21)]
    test(not (1 in signs and -1 in signs and signs.index(1)<signs.index(-1)))
    criterion=b>(1+A)/(3-A)
    test((N.subs(s,1)>0)==criterion)

print(f'PASS: {CHECKS} exact algebraic/rational assertions; full theorem requires analytic proof.')
print('Illustrative interior minimum survival:',S.N(root,16))
print('Illustrative minimum lower-exit probability:',S.N(Q.subs(s,root),16))
