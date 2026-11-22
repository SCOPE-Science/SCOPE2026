"""Independent algebraic identities and finite numerical checks for the two-observation Jordan model."""
import math
import random
import sympy as sp

u, d, q, z1 = sp.symbols('u d q z1', real=True, positive=True)
V = sp.Matrix([[sp.exp(-z1), q*z1*sp.exp(-z1)],
               [sp.exp(-z1-d), q*(z1+d)*sp.exp(-z1-d)]])
B = sp.Matrix([[1, 0], [sp.exp(-d), q*d*sp.exp(-d)]])
S = sp.Matrix([[1, q*z1], [0, 1]])
assert sp.simplify(V - sp.exp(-z1)*B*S) == sp.zeros(2)
assert sp.simplify(V.det() - q*d*sp.exp(-2*z1-d)) == 0
assert sp.simplify(sp.trace(V.T*V) - sp.exp(-2*z1)*sp.trace(B.T*B)
                   - q*q*sp.exp(-2*z1)*(z1*z1+sp.exp(-2*d)*(2*z1*d+z1*z1))) == 0

K = q*q*d*d*sp.exp(-2*d)
Tr = 1+sp.exp(-2*d)*(1+q*q*d*d)
v = q*q*d*(d-1)
c = v/(1+v)
assert sp.simplify((1+v)**2*(c*c-Tr*c+K)-q*q*d*(sp.exp(-2*d)*(1+v)-(d-1))) == 0
lam = sp.symbols('lam', real=True)
assert sp.simplify(sp.diff(K,d)-sp.diff(Tr,d)*lam
                   -2*sp.exp(-2*d)*((1+v)*lam-v)) == 0
print('6 symbolic identities passed')

def croot():
    lo, hi = 1.0, 2.0
    for _ in range(100):
        mid=(lo+hi)/2
        if (mid-1)*math.exp(2*mid)>1:hi=mid
        else:lo=mid
    return (lo+hi)/2

C=croot()
def g(z):
    return math.exp(2*z)/z-1/(z*(z-1))

def zstar(q0):
    lo=C
    hi=2
    while g(hi)<q0*q0:
        hi*=2
    for _ in range(100):
        mid=(lo+hi)/2
        if g(mid)>q0*q0:hi=mid
        else:lo=mid
    return (lo+hi)/2

def information(q0,zlo,zhi):
    # Return smallest eigenvalue, determinant and inverse-trace.
    rr=[]
    for z in (zlo,zhi):
        decay=math.exp(-z)
        rr.append((decay,q0*z*decay))
    aa=rr[0][0]**2+rr[1][0]**2
    bb=rr[0][0]*rr[0][1]+rr[1][0]*rr[1][1]
    cc=rr[0][1]**2+rr[1][1]**2
    determinant=max(0,aa*cc-bb*bb)
    tr=aa+cc
    lambdamin=2*determinant/(tr+math.sqrt(max(0,(aa-cc)**2+4*bb*bb))) if tr else 0
    return lambdamin, determinant, tr/determinant if determinant>0 else math.inf

rng=random.Random(20261116)
comparisons=0
for q0 in (0.05,0.1,0.5,1,2,4,10,50):
    ze=zstar(q0)
    for horizon in (0.15,0.65,1.05,1.3,2.0,3.5,6.5):
        tD=min(horizon,1)
        tA=min(horizon,C)
        tE=min(horizon,ze)
        eopt=information(q0,0,tE)[0]
        dopt=information(q0,0,tD)[1]
        aopt=information(q0,0,tA)[2]
        for _ in range(700):
            lo=rng.uniform(0,horizon)
            hi=rng.uniform(lo,horizon)
            val,det,invtr=information(q0,lo,hi)
            assert val<=eopt+5e-12,(q0,horizon,lo,hi,val,eopt)
            assert det<=dopt+5e-12,(q0,horizon,lo,hi,det,dopt)
            assert invtr>=aopt-5e-10,(q0,horizon,lo,hi,invtr,aopt)
            comparisons+=3
    assert ze>C
    assert 0<information(q0,0,ze)[0]<1
    v0=q0*q0*ze*(ze-1)
    assert abs(information(q0,0,ze)[0]-v0/(1+v0)) <1e-12
print('finite designs:',comparisons,'criterion comparisons passed')
print('c=',f'{C:.12f}')
for q0 in (1,4,10):
    zz=zstar(q0)
    print('q=',q0,'z_E=',f'{zz:.12f}','lambda_E=',f'{information(q0,0,zz)[0]:.12f}')
