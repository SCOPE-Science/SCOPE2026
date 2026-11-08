"""Standalone reproducibility checks for a single weak link in a six-node phase ring.

These finite checks supplement, but do not replace, the all-parameter proof.
Run with Python 3, SymPy and NumPy: python VERIFY.py
"""
import math
import sympy as sp
import numpy as np

x, a, w = sp.symbols('x a w', real=True)
U4 = 16*x**4 - 12*x**2 + 1
assert sp.simplify(U4 + sp.Rational(5, 4) - (8*x**2-3)**2/4) == 0
assert sp.factor(sp.expand_trig(sp.sin(5*a)) / sp.sin(a) - (16*sp.cos(a)**4-12*sp.cos(a)**2+1)) == 0 or sp.trigsimp(sp.expand_trig(sp.sin(5*a))/sp.sin(a)-U4.subs(x,sp.cos(a))) == 0
assert sp.simplify(U4.subs(x,sp.sqrt(sp.Rational(3,8)))) == -sp.Rational(5,4)
assert sp.simplify(U4.subs(x,sp.cos(sp.pi/3))) == -1
assert sp.simplify(U4.subs(x,sp.cos(sp.pi/4))) == -1

def slope_pair(weight):
    s=math.sqrt(5-4/weight)
    lo=math.acos(math.sqrt((3+s)/8))
    hi=math.acos(math.sqrt((3-s)/8))
    return lo,hi

def laplacian(weight):
    weights=[1]*5+[weight]
    L=np.zeros((6,6))
    for j,aj in enumerate(weights):
        k=(j+1)%6
        L[j,j]+=aj; L[k,k]+=aj
        L[j,k]-=aj; L[k,j]-=aj
    return L

def potential_hessian(alpha,weight):
    edgeangles=[alpha]*5+[-5*alpha]
    edgeweights=[1]*5+[weight]
    H=np.zeros((6,6))
    for j,(ang,ww) in enumerate(zip(edgeangles,edgeweights)):
        k=(j+1)%6
        value=ww*math.cos(ang)
        H[j,j]+=value; H[k,k]+=value
        H[j,k]-=value; H[k,j]-=value
    return H

cases=0
for weight in [0.80000001,0.801,0.85,1.,1.1,2.,10.]:
    lo,hi=slope_pair(weight)
    assert math.pi/5 < lo < math.acos(math.sqrt(3/8)) < hi < 2*math.pi/5
    assert abs(math.sin(lo)+weight*math.sin(5*lo))<1e-11
    assert abs(math.sin(hi)+weight*math.sin(5*hi))<1e-11
    for branch,alpha in [('saddle',lo),('sink',hi)]:
        H=potential_hessian(alpha,weight)
        eig=np.linalg.eigvalsh(H)
        if branch=='saddle': assert eig[0]<-1e-7 and abs(eig[1])<1e-10 and eig[2]>1e-7
        else: assert abs(eig[0])<1e-10 and eig[1]>1e-7
        assert math.isclose(math.cos(alpha)+5*weight*math.cos(5*alpha),
                            (2*math.cos(alpha)+10*weight*math.cos(5*alpha))/2)
        h=.04/max(1.,weight)
        lam=np.linalg.eigvalsh(laplacian(weight))[-1]
        assert 0<h<1/lam
        y=np.arange(6)*alpha
        grad=np.zeros(6)
        aa=[1]*5+[weight]
        for j,ww in enumerate(aa):
            k=(j+1)%6
            delta=y[k]-y[j]
            val=ww*math.sin(delta)
            grad[j]-=val; grad[k]+=val
        assert max(abs(grad))<1e-10
        map_eigs=1-h*eig
        if branch=='sink': assert all(abs(t)<1-1e-8 for t in map_eigs[1:])
        else: assert max(map_eigs)>1+1e-8
        cases+=1

at=.8
alpha=math.acos(math.sqrt(3/8))
assert abs(math.sin(alpha)+at*math.sin(5*alpha))<1e-13
assert abs(math.cos(alpha)+5*at*math.cos(5*alpha))<1e-12
H=potential_hessian(alpha,at)
E=np.linalg.eigvalsh(H)
assert max(abs(E[0]),abs(E[1]))<1e-10 # rotation plus saddle-node zero
assert E[2]>1e-6
for at in [0., .05, .5, .8, 1., 2.]:
    H=potential_hessian(0,at)
    E=np.linalg.eigvalsh(H)
    if at>0:
        assert abs(E[0])<1e-10 and E[1]>0
print(f'VERIFY_OK exact_chebyshev_identity=1 threshold=4/5 branch_samples={cases} fold_nullity=2 dynamic_fixed_points=1')
