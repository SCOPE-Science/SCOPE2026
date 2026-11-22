"""Reproduce algebra and examples for the two softmax local-step estimators.
Requires Python 3 and sympy. Run: python verify.py
The exact theorem also uses elementary inequalities proved in RESULT.md.
"""
from fractions import Fraction as Q
from math import sqrt
import sympy as sp

checks = 0

def check(condition, label):
    global checks
    assert condition, label
    checks += 1

p, t, u = sp.symbols('p t u', real=True)
q = sp.Matrix([p, (1-p)*(1+t)/2, (1-p)*(1-t)/2])
d = sp.Matrix([1, 0, 0]) - q
H = sp.diag(*q) - q*q.T
N = sp.factor(d.dot(d))
A = sp.factor((d.T*H*d)[0])
B = sp.factor((d.T*H*H*d)[0])
R = sp.factor(N*B/A**2)
D = p*(u+3)**2 + u*(1-u)
formula = 1+3*u*(1-u)**2/D**2
check(sp.factor(R-formula.subs(u,t**2)) == 0, 'Exact ratio identity')
C = p*(u+3)*(u**2-12*u+3)-u*(1-u)**2
check(sp.factor(sp.diff(formula,u)-3*(1-u)*C/D**3)==0, 'Derivative identity')
phi = u*(1-u)**2/((u+3)*(u**2-12*u+3))
P=7*u**3 + 75*u**2 - 27*u + 9
check(sp.factor(sp.diff(phi,u) - (1-u)*P/((u+3)**2*(u**2-12*u+3)**2))==0, 'Uniqueness derivative identity')
check(27**2-4*75*9<0, 'Positive quadratic discriminant')

# Raw exact-rational softmax-covariance expression compared to the simplified formula.
for denominator in (3, 4, 5, 7, 11, 17, 31, 101):
    for a in range(1, denominator):
        pp = Q(a,denominator)
        for b in range(1, denominator):
            tt = Q(2*b-denominator,denominator)
            qq = [pp, (1-pp)*(1+tt)/2, (1-pp)*(1-tt)/2]
            dd = [1-qq[0],-qq[1],-qq[2]]
            mu = sum(qq[i]*dd[i] for i in range(3))
            Hd = [qq[i]*(dd[i]-mu) for i in range(3)]
            dot = sum(dd[i]*Hd[i] for i in range(3))
            rr = sum(v*v for v in dd)*sum(v*v for v in Hd)/dot**2
            uu=tt*tt
            rhs=1+3*uu*(1-uu)**2/(pp*(uu+3)**2+uu*(1-uu))**2
            check(rr==rhs, 'Rational softmax identity')
            check(rr>=1, 'Cauchy inequality')
            check((rr==1) == (tt==0), 'Equality criterion')

# A rational, strictly positive ternary witness with an approximately 833-fold ratio.
pp=Q(1,10000); tt=Q(3,100); uu=tt*tt
rr=1+3*uu*(1-uu)**2/(pp*(uu+3)**2+uu*(1-uu))**2
check(rr == Q(99940045013498380243,119964013498380243), 'Rational witness')
check(833 < rr < 834, 'Witness magnitude')

# Numerical root-isolation confirms the explicit optimizer description.
for pp in (0.00001, 0.001, 0.03, 0.1, 0.5, 0.99):
    left, right = 0.0, 6-sqrt(33)
    def cc(x):
        return pp*(x+3)*(x*x-12*x+3)-x*(1-x)**2
    check(cc(left)>0 and cc(right)<0, 'Root bracketing')
    for _ in range(100):
        mid=(left+right)/2
        if cc(mid)>0: left=mid
        else:right=mid
    star=(left+right)/2
    check(abs(cc(star)) < 1e-11, 'Root consistency')
    def r(x):
        return 1+3*x*(1-x)**2/(pp*(x+3)**2+x*(1-x))**2
    peak=r(star)
    for k in range(1, 100):
        x=k/100
        check(peak+1e-10>=r(x), 'Sampled maximum')

# Asymptotic analytical constants tested at decreasing p (not a substitute for proof).
for pp in (1e-5,1e-6,1e-7):
    left,right=0.0,6-sqrt(33)
    for _ in range(100):
        mid=(left+right)/2
        c=pp*(mid+3)*(mid*mid-12*mid+3)-mid*(1-mid)**2
        if c>0:left=mid
        else:right=mid
    star=(left+right)/2
    check(abs(star/pp-9)<0.02, 'Optimizer asymptotic')
    rmax=1+3*star*(1-star)**2/(pp*(star+3)**2+star*(1-star))**2
    check(abs(pp*rmax-1/12)<0.0001, 'Sharp constant asymptotic')
print('VERIFY_OK', checks)
