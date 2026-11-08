"""Exact derivative identities and quantitative consistency checks for a Chialvo cusp.

Run: python checker.py
This script is corroboration; the accompanying proof supplies the infinite-time argument.
"""
import math
import sympy as sp
from mpmath import mp

x,u=sp.symbols('x u', real=True)
sq2=sp.sqrt(2)
xc=2-sq2
kc=3-2*sq2
rc=xc-sp.log(xc*(2-xc))
E0=1/(xc*(2-xc))
assert sp.simplify(xc**2*E0 +kc-xc)==0
assert sp.simplify(E0*xc*(2-xc)-1)==0
assert sp.simplify(E0*(xc**2-4*xc+2))==0

# Local fixed-point displacement series: g(u)=f(xc+u)-xc-u.
coeff={}
for j in (3,4,5):
    P=(-1)**j*(x*x-2*j*x+j*(j-1))
    coeff[j]=sp.simplify(E0*P.subs(x,xc)/sp.factorial(j))
assert coeff[3] == -(2+sq2)/6
assert coeff[4] == (5+3*sq2)/24
assert coeff[5] == -(3+2*sq2)/40

a=-coeff[3]
b=coeff[4]
c5=coeff[5]
A=2*a
B=-2*b
C=3*a*a-2*c5
H=sp.simplify(C/A-B*B/A**2)
D=2*B/sp.sqrt(A)
assert sp.simplify(A-(2+sq2)/3)==0
assert sp.simplify(H-(sp.Rational(59,160)+sq2/5))==0
assert sp.simplify(sp.diff(x-sp.log(x*(2-x)),x,2).subs(x,xc)-(2+sq2))==0
assert sp.simplify(sp.diff(x-x/(2-x),x,2).subs(x,xc)+sq2)==0
print('exact algebra: PASS; A=', A, 'D=', sp.N(D,12), 'H=', H)

mp.dps=60
xcm=mp.mpf(2)-mp.sqrt(2)
kcm=mp.mpf(3)-2*mp.sqrt(2)
rcm=xcm-mp.log(xcm*(2-xcm))
Am=mp.mpf(str(sp.N(A,55)))
Dm=mp.mpf(str(sp.N(D,55)))
Hm=mp.mpf(str(sp.N(H,55)))

def F(z):
    return z*z*mp.exp(rcm-z)+kcm

def wvar(z):
    return 1/(z-xcm)**2

for sign in (1,-1):
    z=xcm + mp.mpf(sign)/4
    vals={}
    for n in range(1,30001):
        z=F(z)
        if n in (5000,10000,15000,30000):
            vals[n]=wvar(z)
    for n in (10000,30000):
        # two-block difference filters the unknown orbit-dependent constant.
        m=n//2
        slope=(vals[n]-vals[m]-Am*(n-m)-sign*Dm*(mp.sqrt(n)-mp.sqrt(m)))/mp.log(mp.mpf(n)/m)
        print('sign',sign,'n',n,'observed log coefficient',mp.nstr(slope,14),'theory',mp.nstr(Hm,14))
        assert abs(slope-Hm) < mp.mpf('0.10')

# Fold boundaries and the predicted cubic-root cusp opening.
def foldx(alpha,left):
    low=mp.mpf('0.000001') if left else xcm
    high=xcm if left else mp.mpf('1.99')
    target=rcm+alpha
    for i in range(150):
        mid=(low+high)/2
        rv=mid-mp.log(mid*(2-mid))
        if left:
            if rv>target: low=mid
            else: high=mid
        else:
            if rv<target: low=mid
            else: high=mid
    return (low+high)/2

for alpha_text in ('0.001','0.0001'):
    alpha=mp.mpf(alpha_text)
    kboundary=[float((z:=foldx(alpha,left)) - z/(2-z)) for left in (True,False)]
    central=float(kcm - (xcm/mp.sqrt(2))*alpha)
    width=(max(kboundary)-min(kboundary))/2
    pred=float((mp.mpf(2)/3)*mp.sqrt(xcm)*alpha**mp.mpf('1.5'))
    ratio=width/pred
    print('alpha=',alpha_text,'cusp half-width ratio',ratio)
    assert abs(ratio-1)<0.05

print('ALL CHECKS PASSED')
