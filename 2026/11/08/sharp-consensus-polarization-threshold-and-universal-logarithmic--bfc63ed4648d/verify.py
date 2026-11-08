"""Exact algebraic checks and bounded diagnostics for the symmetric two-voter feedback map."""
from fractions import Fraction
import sympy as sp

x,u,c=sp.symbols('x u c', real=True)
t=1-u
nx=t*x
nu=u*(1-c*t*x)
w=u-c*x
nw=nu-c*nx
assert sp.factor(nw-w-c*u*u*x)==0
assert sp.factor((x-nx)-u*x)==0
assert sp.factor((u-nu)-c*t*(x-nx))==0
# Check the order-two invariant-curve coefficient without claiming finite tests prove convergence.
a,b=sp.symbols('a b')
h=c*x+a*x*x+b*x**3
residual=sp.series(h*(1-c*(1-h)*x)-h.subs(x,(1-h)*x),x,0,4).removeO().expand()
assert sp.factor(residual.coeff(x,3)) == c*(2*a+c*c)
assert sp.solve(residual.coeff(x,3),a)==[-c*c/2]


def decision(start_gap,start_theta,feedback,limit=24):
    q=Fraction(start_gap)
    th=Fraction(start_theta)
    cc=Fraction(feedback)
    for k in range(limit):
        v=1-th
        if v>cc*q:
            return ('consensus',k)
        if v<cc*th*q:
            return ('disagreement',k)
        nq=th*q
        th=th+cc*v*nq
        q=nq
    return ('undetermined',limit)

assert decision(Fraction(2,5),Fraction(13,20),1)[0]=='consensus'
assert decision(Fraction(2,5),Fraction(7,10),1)[0]=='disagreement'
assert decision(Fraction(1,5),Fraction(0,1),1)[0]=='consensus'

def classify_float(initial_theta,initial_gap=.4,feedback=1.,maximum=50000):
    xx=initial_gap
    tt=initial_theta
    for _ in range(maximum):
        uu=1-tt
        if uu>feedback*xx:return -1
        if uu<feedback*tt*xx:return 1
        nx=tt*xx
        tt+=feedback*uu*nx
        xx=nx
    return 0

lo,hi=.65,.70
assert classify_float(lo)==-1 and classify_float(hi)==1
for _ in range(26):
    mid=(lo+hi)/2
    side=classify_float(mid)
    if side==-1:lo=mid
    elif side==1:hi=mid
    else:break
assert .6777<lo<hi<.6780
print('VERIFY_OK')
