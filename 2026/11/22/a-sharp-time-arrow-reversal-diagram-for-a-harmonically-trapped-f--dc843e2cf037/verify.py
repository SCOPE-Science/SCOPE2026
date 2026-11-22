"""Independent polynomial-generator and positive-kernel checks for the finite-tumble position arrow.
Scientific reproducibility; requires SymPy, NumPy and SciPy.
"""
from fractions import Fraction
from math import isclose
import sympy as sp
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq

z,a,b,c,v,D=sp.symbols('z a b c v D', positive=True)
p=c/(a+c)
XS=v*p/(a+b)
X2=(v*XS+D)/b
X2S2=(c*X2+2*v*XS+2*D*p)/(2*b+a+c)
X3S=(3*v*X2S2+6*D*XS)/(3*b+a)
X4=(v*X3S+3*D*X2)/b
# Columns encode generators of [x^3,x^2 S,x S^2,x,S] in the same basis.
L=sp.zeros(5)
L[:,0]=sp.Matrix([-3*b,3*v,0,6*D,0])
L[:,1]=sp.Matrix([0,-2*b-a,2*v,0,2*D])
L[:,2]=sp.Matrix([0,0,-b-a-c,c,v])
L[:,3]=sp.Matrix([0,0,0,-b,v])
L[:,4]=sp.Matrix([0,0,0,0,-a])
M=sp.Matrix([X4,X3S,X2S2,X2,XS])
R=(z*sp.eye(5)-L).inv()
arrow=sp.factor(X4*R[3,3]+X3S*R[4,3]-(M.T*R[:,0])[0])
K=6*a*c*v**4/((a+b)*(a+3*b)*(a+c)*(a+2*b+c))
expected=sp.factor(K*((a-b-2*c)*(z+a+b+c)+(a+3*b)*(a-c))/((z+a)*(z+b)*(z+3*b)*(z+a+2*b)*(z+a+b+c)))
assert sp.factor(arrow-expected)==0
assert sp.factor(sp.diff(arrow,D))==0
checks=2

def approx_mom(aa,bb,cc,vv,dd):
    pp=cc/(aa+cc)
    xs=vv*pp/(aa+bb)
    x2=(vv*xs+dd)/bb
    x2s2=(cc*x2+2*vv*xs+2*dd*pp)/(2*bb+aa+cc)
    x3s=(3*vv*x2s2+6*dd*xs)/(3*bb+aa)
    x4=(vv*x3s+3*dd*x2)/bb
    return np.array([x4,x3s,x2s2,x2,xs]),x4,x3s

def semigroup_arrow(aa,bb,cc,vv,dd,t):
    mm,x4,x3s=approx_mom(aa,bb,cc,vv,dd)
    mat=np.zeros((5,5))
    mat[:,0]=[-3*bb,3*vv,0,6*dd,0]
    mat[:,1]=[0,-2*bb-aa,2*vv,0,2*dd]
    mat[:,2]=[0,0,-bb-aa-cc,cc,vv]
    mat[:,3]=[0,0,0,-bb,vv]
    mat[:,4]=[0,0,0,0,-aa]
    e=expm(t*mat)
    return x4*e[3,3]+x3s*e[4,3]-mm@e[:,0]

def kernel_arrow(aa,bb,cc,vv,t):
    rates=[aa,bb,3*bb,aa+2*bb,aa+bb+cc]
    mat=np.diag(-np.array(rates,dtype=float))
    for i in range(1,5):mat[i,i-1]=1.
    h=expm(t*mat)[:,0]
    kk=6*aa*cc*vv**4/((aa+bb)*(aa+3*bb)*(aa+cc)*(aa+2*bb+cc))
    return kk*((aa-bb-2*cc)*h[3]+(aa+3*bb)*(aa-cc)*h[4]), h[3],h[4]

# Non-resonant, resonant, low/high propulsion duty, and finite thermal diffusion.
for aa,bb,cc,vv,dd in [(2.,1.,1.,1.,0.),(2.,1.,1.,1.,.7),(.5,1.,2.,2.,.4),
                        (5.,2.,.5,1.2,1.1),(1.,1.,1.,1.,3.),(3.,1.,.01,2.,.1),
                        (.8,2.,.3,1.3,0.),(7.,3.,4.,.5,.2)]:
    for t in [.04,.2,.7,1.5,3.,5.]:
        lhs=semigroup_arrow(aa,bb,cc,vv,dd,t)
        rhs,h,j=kernel_arrow(aa,bb,cc,vv,t)
        assert np.isclose(lhs,rhs,rtol=2e-8,atol=1.5e-12),(aa,bb,cc,t,lhs,rhs)
        assert h>0 and j>0
        checks+=2
    # Direct numerical monotonicity of R(t)=J(t)/H(t) and limiting value.
    ratios=[kernel_arrow(aa,bb,cc,vv,t)[2]/kernel_arrow(aa,bb,cc,vv,t)[1] for t in [.02,.07,.15,.3,.6,1.2]]
    assert all(q2>q1 for q1,q2 in zip(ratios,ratios[1:])),(aa,bb,cc,ratios)
    assert ratios[-1] < 1/(max(aa,bb)+cc)+1e-8
    checks+=2

# Explicit sharp sign reversal for (a,b,c)=(2,1,1) with arbitrary thermal strength.
root=brentq(lambda t:kernel_arrow(2,1,1,1,t)[0],.01,5.,xtol=1e-12)
assert abs(root-1.1329066090521283)<2e-8
for dd in [0.,.1,1.,5.]:
    assert semigroup_arrow(2,1,1,1,dd,.6)<0
    assert semigroup_arrow(2,1,1,1,dd,2.)>0
    checks+=2
checks+=1
print(f'PASS {checks} algebraic / finite-dimensional consistency checks; unique-root example {root:.12f}')
