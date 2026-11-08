"""Reproducibility checks for exact prime-two census in adaptive-belief MWU dynamics.
Run with Python 3 and sympy; numerical samples only corroborate the analytic proof.
"""
from fractions import Fraction as Q
from math import log, exp, sqrt, isclose
import random
import sympy as sp

# Exact matrix identities for one-step Jacobians and the two-step orbit.
su, sv, a, r = sp.symbols('s_u s_v a r', positive=True)
# Scale c=1 and p1=r for a symbolic gauge, without changing the product cp1.
Ju=sp.Matrix([[sv*(1/su-a), -a*sv], [r, 0]])
Jv=sp.Matrix([[su*(1/sv-a), -a*su], [r, 0]])
P=sp.simplify(Jv*Ju)
T=1-a*(1+r)*(su+sv)+a*a*su*sv
D=(a*r)**2*su*sv
assert sp.simplify(sp.trace(P)-T)==0
assert sp.simplify(P.det()-D)==0
assert sp.simplify(1-T+D-a*(1+r)*su*sv*(1/su+1/sv-a*(1-r)))==0
# Fixed point characteristic polynomial; flip boundary and second eigenvalue.
s=sp.symbols('s',positive=True)
Jfix=sp.Matrix([[1-a*s,-a*s],[r,0]])
flip=sp.Rational(2,1)/(s*(1-r))
assert sp.simplify((Jfix+sp.eye(2)).det().subs(a,flip))==0
assert sp.simplify(Jfix.det().subs(a,flip)-2*r/(1-r))==0

# Exact symmetric witness: b=3/5, c=2, p0=1/20, p1=1/10,
# k=1, a=15 log(2), two cycle ((1/2,1/12),(1/3,1/10)).
p0,p1,c,b=Q(1,20),Q(1,10),Q(2),Q(3,5)
u,v=Q(1,2),Q(1,3)
q0=p0+p1*v; q1=p0+p1*u
assert q0==Q(1,12) and q1==Q(1,10)
assert u-b+c*q0==Q(1,15)
assert v-b+c*q1==-Q(1,15)
assert u/(u+(1-u)*2)==v
assert v/(v+(1-v)*Q(1,2))==u
m=(b-c*p0)/(1+c*p1)
assert m==Q(5,12)
assert Q(2)/(m*(1-m)*(1-c*p1))==Q(72,7)
assert 15*log(2)>float(Q(72,7))
# Check genuine two-step attraction via exact Schur inequalities involving log 2.
av=15*log(2); rv=float(c*p1); suv=float(u*(1-u)); svv=float(v*(1-v))
tr=1-av*(1+rv)*(suv+svv)+av*av*suv*svv
det=(av*rv)**2*suv*svv
assert 1-det>0 and 1-tr+det>0 and 1+tr+det>0
# Exact rational enclosure: log(2)=2*atanh(1/3).
N=12
log2_lo=sum((Q(2, (2*j+1)*3**(2*j+1)) for j in range(N+1)), Q(0))
log2_hi=log2_lo+Q(2, (2*N+3)*3**(2*N+3))*Q(9,8)
a_lo=15*log2_lo; a_hi=15*log2_hi
assert a_lo>Q(72,7)
assert 1-a_hi*a_hi/Q(450)>0
assert Q(17,30)*a_lo-Q(4,75)*a_hi*a_hi>0
assert 2-Q(17,30)*a_hi+Q(13,225)*a_lo*a_lo>0

rng=random.Random(20261104)
cases=0
for i in range(650):
    m0=0.08+0.84*rng.random()
    rr=0.01+0.93*rng.random()
    bd=min(m0,1-m0)
    aa=(2/(m0*(1-m0)))*(1+0.05+3*rng.random())/(1-rr)
    def logit(x):
        return log(x/(1-x))
    def H(d):
        return (logit(m0+d)-logit(m0-d))/d
    lo,hi=0.,bd*(1-1e-12)
    assert H(hi)>aa*(1-rr)
    for _ in range(72):
        mid=(lo+hi)/2
        if H(mid)<aa*(1-rr):lo=mid
        else:hi=mid
    d=(lo+hi)/2
    x1,x2=m0+d,m0-d
    # Set c=1, p1=rr, p0=0, b=(1+rr)m0 to reconstruct the
    # model without insisting b<1; adjust c,p0 to ensure original bounds below.
    # Instead choose c=2, p1=rr/2, p0=0, b=(1+rr)m0 if b<1.
    if (1+rr)*m0>=1:continue
    p0_=0.; p1_=rr/2; c_=2.; b_=(1+rr)*m0
    q1_=p1_*x1; q2_=p1_*x2
    def first(x,q):
        t=aa*(x-b_+c_*q)
        return 1/(1+(1-x)/x*exp(t))
    assert abs(first(x1,q2_)-x2)<2e-10
    assert abs(first(x2,q1_)-x1)<2e-10
    cases+=1
assert cases>350
# Sharp amplitude onset d^2 ~ 3(1-r)(a-a_*)/L'''(m).
m0=Q(5,12); r0=Q(1,5); amin=float(Q(72,7)); L3=2/float(m0)**3+2/(1-float(m0))**3
for step in (1e-3,1e-4,1e-5):
    target=(amin+step)*(1-float(r0))
    left,right=0.,min(float(m0),1-float(m0))*0.99
    for _ in range(90):
        d=(left+right)/2
        x,y=float(m0)+d,float(m0)-d
        h=(log(x/(1-x))-log(y/(1-y)))/d if d else 2/(float(m0)*(1-float(m0)))
        if h<target:left=d
        else:right=d
    d=(left+right)/2
    assert abs(d*d/(step*3*(1-float(r0))/L3)-1)<0.02
print('VERIFY_OK symbolic_identities=5 exact_rational_witness=8 numerical_two_cycles=',cases,'attracting_witness=1')
