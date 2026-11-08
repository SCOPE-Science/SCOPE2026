#!/usr/bin/env python3
"""Independent algebra and finite-matrix checks for a two-habitat survival theorem.

Requires Python 3, SymPy and SciPy. Exact symbolic checks and numerical
matrix-exponential checks are ancillary to the analytic stochastic-order proof.
"""
from fractions import Fraction as F
import math
import sympy as sp
import numpy as np
from scipy.linalg import expm

checks = 0

def ok(value, message):
    global checks
    if not bool(value):
        raise AssertionError(message)
    checks += 1

a,b,c,d,z,t=sp.symbols('a b c d z t',positive=True)
S=a+b; P=a*b; C=c+d; q=c*d
Q=sp.Matrix([[-S,b,a],[c,-(a+c),0],[d,0,-(b+d)]])
r=sp.Matrix([0,a,b])
D=z**3+(2*S+C)*z**2+(S**2+P+S*C+q)*z+P*(S+C)
N=P*(S+C+2*z)

ok(sp.factor((z*sp.eye(3)-Q).det()-D)==0,'determinant')
Fz=sp.factor((z*sp.eye(3)-Q).inv()[0,:].dot(r))
ok(sp.factor(Fz-N/D)==0,'absorption Laplace transform')
ok(sp.factor(Fz.subs(z,0)-1)==0,'full extinction')
E=(S**2-P+S*C+q)/(P*(S+C))
ok(sp.factor(-sp.diff(Fz,z).subs(z,0)-E)==0,'exact mean')
# Direct z-dependent derivative with c variable at fixed C: substitute d=C0-c.
C0=sp.symbols('C0',positive=True)
q0=sp.symbols('q0',positive=True)
D0=z**3+(2*S+C0)*z**2+(S**2+P+S*C0+q0)*z+P*(S+C0)
N0=P*(S+C0+2*z)
Lsurv=(1-N0/D0)/z
ok(sp.factor(sp.diff(Lsurv,q0)-N0/D0**2)==0,'survival derivative LT')

# Taylor coefficient of finite-deadline extinction by Q-powers.
# P(extinct by t)=sum_{k>=1} (e11^T Q^(k-1) r) t^k/k!.
M=sp.eye(3)
coefs=[]
for k in range(1,7):
    coefs.append(sp.factor((M*r)[0]/sp.factorial(k)))
    M=M*Q
    checks += 1
ok(sp.factor(coefs[0])==0,'CDF first coefficient')
ok(sp.factor(coefs[1]-P)==0,'CDF second coefficient')
ok(sp.factor(coefs[2]+P*(C+3*S)/6)==0,'CDF third coefficient')
# Compare the fourth coefficient after fixing C=c+d.
u=sp.symbols('u')
co4=sp.factor(coefs[3].subs({c:u,d:C0-u}, simultaneous=True))
ok(sp.factor(sp.diff(co4,u,2)-P/6)==0,'fourth order product curvature')
ok(sp.factor(sp.diff(co4,u)-P*(2*u-C0)/12)==0,'fourth order product derivative')
# Exact fourth-order coefficient of survival difference per increment of product.
# Since extinction CDF fourth coefficient has derivative -P/12 with respect to q,
# survival gains +P*t**4/12 per increment of q.
co4q=sp.factor(co4.subs(u, (C0+sp.sqrt(C0**2-4*q0))/2))
ok(sp.factor(sp.diff(co4q,q0)+P/12)==0,'fourth order extinction coefficient product derivative')


# Independent, direct matrix-exponential survival probabilities.
# Intentionally includes zero directional rate boundaries.
ps=[(1.,1.,2.),(1.,2.,2.),(.25,3.,1.5),(2.,.7,5.),(4.,5.,.5)]
times=[.025,.1,.25,.5,1.,2.,5.,10.]
for aa,bb,cc in ps:
    prev=None
    for yy in [0.,cc*.1,cc*.25,cc*.4,cc*.5]:
        QQ=np.array([[-aa-bb,bb,aa],[yy,-aa-yy,0],[cc-yy,0,-bb-(cc-yy)]],float)
        for tt in times:
            survival=float(expm(QQ*tt)[0,:].sum())
            ok(0.<survival<1.,'probability boundaries')
            if prev is not None:
                ok(survival>prev[tt],'strict ordered survival')
        if prev is None:
            prev={tt:float(expm(QQ*tt)[0,:].sum()) for tt in times}
        else:
            prev={tt:float(expm(QQ*tt)[0,:].sum()) for tt in times}

# Invariance on reversing colonization rate allocation even with unequal local extinctions.
for aa,bb,cc in ps:
    for frac in [0.,.13,.27,.49]:
        y=cc*frac
        QA=np.array([[-aa-bb,bb,aa],[y,-aa-y,0],[cc-y,0,-bb-(cc-y)]],float)
        QB=np.array([[-aa-bb,bb,aa],[cc-y,-aa-(cc-y),0],[y,0,-bb-y]],float)
        for tt in times:
            ok(abs(float(expm(QA*tt)[0,:].sum())-float(expm(QB*tt)[0,:].sum()))<1e-11,'reflection invariance')

# Verify rational mean values on exact parameters from first-step equations.
for aa,bb,cc,yy in [(F(1),F(1),F(2),F(0)),(F(1),F(1),F(2),F(1)),(F(1),F(2),F(2),F(1)),(F(1),F(2),F(2),F(1,2))]:
    mat=sp.Matrix([[-(aa+bb),bb,aa],[yy,-(aa+yy),0],[cc-yy,0,-(bb+cc-yy)]])
    mean=-mat.inv()[0,:].dot(sp.Matrix([1,1,1]))
    predicted=((aa+bb)**2-aa*bb+(aa+bb)*cc+yy*(cc-yy))/(aa*bb*(aa+bb+cc))
    ok(mean==predicted,'rational mean direct inverse')

print('PASS:',checks,'algebraic/numerical assertions')
print('Example a=b=1,C=2: mean(end)=7/4, mean(balanced)=2')
for yy in (0,1):
    QQ=np.array([[-2,1,1],[yy,-1-yy,0],[2-yy,0,-3+yy]],float)
    print('survival at t=1, allocation',yy,':',float(expm(QQ)[0,:].sum()))
