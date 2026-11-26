"""Reproduce exact two-patch pulse-timing identities and the threshold witness.

Standard-library only. Independent algebraic proof is in RESULT.md.
"""
from fractions import Fraction as F
from math import exp, sqrt, sinh, cosh, log, isclose


def mul(X,Y):
    return tuple(tuple(sum(X[i][k]*Y[k][j] for k in range(2)) for j in range(2)) for i in range(2))

def tr(X):
    return X[0][0]+X[1][1]

def det(X):
    return X[0][0]*X[1][1]-X[0][1]*X[1][0]

def expA(a,b,c,d,t):
    theta=(a+d)/2.0
    delta=(a-d)/2.0
    chi=sqrt(delta*delta+b*c)
    co=cosh(chi*t)*exp(theta*t)
    si=sinh(chi*t)*exp(theta*t)/chi
    return ((co+si*delta,si*b),(si*c,co-si*delta))

def Q(a,b,c,d,T,p,q,t):
    D1=((p,0),(0,1))
    D2=((1,0),(0,q))
    return mul(mul(mul(expA(a,b,c,d,T-t),D2),expA(a,b,c,d,t)),D1)

def rho(X):
    return (tr(X)+sqrt(tr(X)**2-4*det(X)))/2

# All matrix entries and stability certificates rational; no float tolerances.
p=F(12,25)
M=((F(3),F(1)),(F(1),F(3)))
D1=((p,F(0)),(F(0),F(1)))
D2=((F(1),F(0)),(F(0),p))
H=mul(mul(mul(M,D2),M),D1)
H=tuple(tuple(x/F(8) for x in row) for row in H)
assert H==((F(711,1250),F(111,200)),(F(333,1250),F(133,200)))
assert tr(H)==F(6169,5000)
assert det(H)==F(144,625)
assert F(1)-tr(H)+det(H)==-F(17,5000)
assert F(24,25)<1
print('EXACT CERTIFICATE: midpoint entries, trace, determinant, negative det(I-Q) and synchronized rho=24/25 verified')

# Each of these parameter/offset checks is separate from the rational witness.
choices=[(0.,1.,1.,0.,log(2),.48,.48),(.8,2.,.3,-.7,.9,.32,.71),(-.2,.15,1.7,.4,1.3,.9,.26),(.5,2.2,1.1,.9,.6,.51,.4)]
checks=0
for a,b,c,d,T,p,q in choices:
    theta=(a+d)/2
    chi=sqrt(((a-d)/2)**2+b*c)
    coef=(1-p)*(1-q)*b*c*exp(theta*T)/chi**2
    B=Q(a,b,c,d,T,p,q,0.)
    mid=Q(a,b,c,d,T,p,q,T/2)
    for f in [0.,.07,.18,.29,.42,.5,.58,.71,.82,.93,1.]:
        t=T*f
        X=Q(a,b,c,d,T,p,q,t)
        right=coef*sinh(chi*t)*sinh(chi*(T-t))
        assert isclose(tr(X)-tr(B),right,abs_tol=2e-12)
        assert isclose(det(X),p*q*exp((a+d)*T),abs_tol=2e-12)
        assert rho(B)-2e-12<=rho(X)<=rho(mid)+2e-12
        checks+=1
print(f'FLOAT STRESS CHECKS: {checks} matrix trace, determinant and ordering checks passed')

# Exact comparison between H and the observed rational witness.
C=(1-float(F(12,25)))**2
assert isclose(C*sinh(log(2)/2)**2,float(F(1)-tr(mul(expA(0,1,1,0,log(2)),((float(F(12,25)),0),(0,float(F(12,25))))))+(tr(H)-1)),rel_tol=0,abs_tol=2e-12)
print('HYPERBOLIC MIDPOINT EXCESS: passed')
