"""Reproduce exact algebra and numerical instances of a three-delay FNN law.
Only standard Python, SymPy and NumPy/SciPy for optional orbit checks.
The proof of the infinite-time limit is analytic, not numerical.
"""
import math
import sympy as sp

z, lam = sp.symbols('z lam', real=True)
L=(8*z*z-2*z+1)/(2*z+1)
detA=2*(1-z)*(1+2*z)
zstar=(sp.sqrt(2)-1)/2
assert sp.simplify(L.subs(z,zstar)-(4*sp.sqrt(2)-5))==0
assert sp.simplify(sp.diff(L,z)-4*(4*z*z+4*z-1)/(2*z+1)**2)==0
assert sp.simplify((L-1)-(8*z*z-4*z)/(2*z+1))==0

# Exact polynomial certificate using rational Chebyshev recurrence.
C = sp.symbols('C',real=True) # C = cos(theta)
S=sp.symbols('S',real=True)
V0=sp.Matrix([1,0]);V1=sp.Matrix([C,S])
V2=sp.Matrix([2*C*C-1,2*C*S]);V3=sp.Matrix([4*C**3-3*C,S*(4*C*C-1)])
A=V0*V0.T+V1*V1.T+V2*V2.T
q=lambda e:sp.factor(sp.together(e).subs(S*S,1-C*C))
# Reduce with sin^2 + cos^2 = 1 directly via Groebner basis.
gb=sp.groebner([S*S+C*C-1],S,C)
assert gb.reduce(sp.expand(A.det()-detA.subs(z,C*C)))[1]==0
poly=sp.expand((V3.T*A.adjugate()*V3)[0]-L.subs(z,C*C)*detA.subs(z,C*C))
assert gb.reduce(poly)[1]==0

# Numerical nearest-neighbor values need no probabilistic sampling.
import numpy as np
from scipy.spatial import cKDTree

def prediction(alpha, R):
    theta=2*math.pi*alpha
    zz=math.cos(theta)**2
    E=(8*zz*zz-2*zz+1)/(2*zz+1)
    la=R*R
    if la>=E:return 0.0
    tr=1-3*la
    de=2*(1-zz)*(1+2*zz)*la*(la-E)
    dd=math.sqrt(tr*tr-4*de)
    return 2/math.pi*math.atan(math.sqrt((tr+dd)/(dd-tr)))

def empirical(alpha,phase,n,R,A_tol=1.0):
    theta=2*math.pi*alpha
    u=np.mod(phase+theta*np.arange(n+3),2*math.pi)
    x=np.cos(u)
    Y=np.column_stack([x[:n],x[1:n+1],x[2:n+2]])
    distances,indices=cKDTree(Y).query(Y,k=2)
    j=indices[:,1]
    dy=np.abs(x[3:n+3]-x[j+3])
    noise=np.std(x)
    return np.mean((dy/distances[:,1]>R)|(dy/noise>A_tol))

alpha=(math.sqrt(5)-1)/2
for R in (0.6,0.9,1.25):
    expected=prediction(alpha,R)
    seen=empirical(alpha,0.37,18000,R)
    print('alpha',alpha,'tolerance',R,'prediction',round(expected,8),'observed',round(seen,8))
    assert abs(expected-seen)<0.015
opt_alpha=math.acos(math.sqrt(float(zstar)))/(2*math.pi)
for R in (0.7,0.8,0.83):
    expected=prediction(opt_alpha,R)
    seen=empirical(opt_alpha,0.14,15000,R)
    print('opt alpha',opt_alpha,'tolerance',R,'prediction',round(expected,8),'observed',round(seen,8))
    assert abs(expected-seen)<0.015
print('ALL CHECKS PASSED')
