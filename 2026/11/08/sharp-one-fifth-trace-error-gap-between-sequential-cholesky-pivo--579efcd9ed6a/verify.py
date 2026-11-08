"""Exact algebra tests for rank-two Nyström pivot sampling on 3x3 correlations.

Run: python verify.py
Dependencies: Python 3.10+ and sympy 1.14.0.
"""
from fractions import Fraction
from itertools import product
import sympy as sp

checks=0

def check(cond, message):
    global checks
    if not cond:
        raise AssertionError(message)
    checks += 1


def formula_ratio(u,v,w):
    U=u+v+w
    return sp.cancel(sp.Rational(2,9)*U*(1/(u+v)+1/(u+w)+1/(v+w)))


def exact_risks(M):
    M=sp.Matrix(M)
    D=M.det()
    W=sp.Integer(0)
    pair={}
    for i in range(3):
        for j in range(i+1,3):
            ij=(i,j)
            w=sp.factor(M.extract(ij,ij).det())
            pair[ij]=w
            W+=w
    T=[sp.factor(M.trace()-(M[:,i].dot(M[:,i])/M[i,i])) for i in range(3)]
    rp=sp.Integer(0)
    dp=sp.Integer(0)
    for (i,j),w in pair.items():
        p=sp.factor((M[i,i]/M.trace())*(w/M[i,i])/T[i]
                    + (M[j,j]/M.trace())*(w/M[j,j])/T[j])
        risk=D/w
        rp+=p*risk
        dp+=w/W*risk
    return sp.factor(rp),sp.factor(dp)

u,v,w,t=sp.symbols('u v w t', positive=True)
R=formula_ratio(u,v,w)
check(sp.factor(R-1)==sp.factor((sp.Rational(2,9)*(u+v+w)*(1/(u+v)+1/(u+w)+1/(v+w)))-1),'lower formula')
Rt=sp.factor(R.subs({u:(t+1)**2,v:t**2,w:1}))
Rt_expected=20*(t*t+t+1)**3/(9*(t*t+1)*(t*t+2*t+2)*(2*t*t+2*t+1))
check(sp.factor(Rt-Rt_expected)==0,'boundary exact formula')
sharp_gap=sp.Rational(6,5)-Rt
sharp_cert=2*(t-1)**2*(t+2)**2*(2*t+1)**2/(45*(t*t+1)*(t*t+2*t+2)*(2*t*t+2*t+1))
check(sp.factor(sharp_gap-sharp_cert)==0,'sharp polynomial certificate')
check(sp.factor(Rt.subs(t,1)-sp.Rational(6,5))==0,'sharp boundary endpoint')

q=sp.symbols('q',positive=True)
cosangle=(1-q*q)/(1+q*q)
cosdouble=2*cosangle*cosangle-1
jitter=q**4
F=sp.Matrix([[1,cosangle,cosdouble],[cosangle,1,cosangle],[cosdouble,cosangle,1]])
A=sp.simplify((F+jitter*sp.eye(3))/(1+jitter))
uq=sp.factor(1-A[0,1]**2)
vq=sp.factor(1-A[0,2]**2)
wq=sp.factor(1-A[1,2]**2)
check(sp.limit(uq/q**2,q,0)==4,'first sin gap')
check(sp.limit(vq/q**2,q,0)==16,'double sin gap')
check(sp.limit(wq/q**2,q,0)==4,'third sin gap')
check(sp.limit(formula_ratio(uq,vq,wq),q,0)==sp.Rational(6,5),'sharp SPD sequence')
for val in [sp.Rational(1,2),sp.Rational(1,5),sp.Rational(1,10),sp.Rational(1,50)]:
    B=A.subs(q,val)
    check(all(z>0 for z in list(B[:,:].eigenvals().keys())),'positive definite sequence')
    rp,dp=exact_risks(B)
    check(sp.factor(rp/dp-formula_ratio(uq,vq,wq).subs(q,val))==0,'Schur probabilities')
    check(1<rp/dp<sp.Rational(6,5),'two-sided strict ratio')

rho=sp.symbols('rho', real=True)
Fone=sp.Matrix([[1,rho,0],[rho,1,0],[0,0,1]])
rs,ds=exact_risks(Fone)
check(sp.factor(rs/ds-(1+rho**4/(9*(2-rho**2))))==0,'single-edge closed form')
check(sp.factor(formula_ratio(1,1,1)-1)==0,'equal correlation absolute values')

for a,b,c in [(2,3,4),(3,3,3),(5,2,1),(10,5,1),(1,10,1)]:
    B=sp.diag(a,b,c)
    rp,dp=exact_risks(B)
    check(sp.factor((rp-dp))<=0,'diagonal contrast')
check(exact_risks(sp.diag(10,5,1))==(sp.Rational(535,264),sp.Rational(30,13)),'exact unequal diagonal reversal')

# Finite checks cross-check the algebra; the continuum result is proved separately.
for x,y,z in product(range(-3,4),repeat=3):
    B=sp.Matrix([[5,x,y],[x,5,z],[y,z,5]])/5
    if B.det()<=0 or any(B.extract((i,j),(i,j)).det()<=0 for i in range(3) for j in range(i+1,3)):
        continue
    rp,dp=exact_risks(B)
    check(sp.factor(rp/dp-formula_ratio(1-B[0,1]**2,1-B[0,2]**2,1-B[1,2]**2))==0,'grid risk algebra')
    check(dp<=rp<=sp.Rational(6,5)*dp,'grid sharp bound')
print(f'PASS: {checks} exact algebraic assertions; 3x3 correlation RPCholesky/k-DPP frontier.')
print('LIMIT: finite grid assertions are cross-checks; global inequalities rely on the analytic argument in RESULT.md.')
