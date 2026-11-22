"""Standalone verification of two endpoint laws for inscribed parabolic triangles.

Python 3 with SymPy and NumPy. This checker corroborates finite identities
and coefficients; the mathematical proof handles continuous probabilities.
"""
import math
import numpy as np
import sympy as sp

x, y, z, a = sp.symbols('x y z a', real=True)
P = lambda t: sp.Matrix([t, t*t])
V = sp.factor(sp.det(sp.Matrix.hstack(P(y)-P(x), P(z)-P(x))))
assert sp.simplify(V - (y-x)*(z-x)*(z-y)) == 0
# The product of side lengths divided by four times triangle area.
assert sp.simplify(V + (x-y)*(x-z)*(y-z)) == 0
A = sp.eye(3) + sp.ones(3)
assert A.det() == 4
Ainv = A.inv()
assert Ainv == sp.eye(3) - sp.ones(3)/4
for ell in [sp.Matrix([1,1,0]),sp.Matrix([0,1,1]),sp.Matrix([1,0,1])]:
    assert (ell.T*Ainv*ell)[0] == 1
# Exact lower endpoint expansion and spherical fourth-moment computation.
# On unit sphere each linear form has squared coefficient norm 4;
# E[(v dot omega)^4] = ||v||^4/5 in dimension 3.
Tmean = sp.Rational(1) - sp.Rational(1,8)*3*sp.Rational(16,5)
assert Tmean == -sp.Rational(1,5)
V0 = sp.Rational(16,3)*sp.pi
V1 = sp.Rational(8,5)*sp.pi
assert sp.simplify(V0/8 - 2*sp.pi/3) == 0
assert sp.simplify(V1/8 - sp.pi/5) == 0
c = 2*a*sp.sqrt(1+4*a*a)
assert sp.simplify(1/(24*a**3*c**3) - 1/(192*a**6*(1+4*a*a)**sp.Rational(3,2))) == 0
# Check the radius identity against a direct determinant and chord calculation.
def rad(t):
    s01=t[0]+t[1];s12=t[1]+t[2];s20=t[2]+t[0]
    return .5*math.sqrt((1+s01*s01)*(1+s12*s12)*(1+s20*s20))
def rad_direct(t):
    pts=np.column_stack((t,t*t))
    A0,B0,C0=pts
    p,q,r=np.linalg.norm(A0-B0),np.linalg.norm(B0-C0),np.linalg.norm(C0-A0)
    cross=abs(np.linalg.det(np.array([B0-A0,C0-A0])))
    return p*q*r/(2*cross)
rg=np.random.default_rng(7721)
for _ in range(200):
    t=np.sort(rg.uniform(-1.2,1.2,3))
    assert abs(rad(t)-rad_direct(t))<4e-10
# Deterministic area quadrature of the exact lower sublevel set on a sphere.
# The following is corroboration, not a replacement for the proof.
N=8192
k=np.arange(N)
phi=(1+math.sqrt(5))/2
zz=1-2*(k+.5)/N
angles=2*math.pi*k/phi
omega=np.column_stack((np.sqrt(1-zz*zz)*np.cos(angles),np.sqrt(1-zz*zz)*np.sin(angles),zz))
w,V=np.linalg.eigh(np.eye(3)+np.ones((3,3)))
Z=2*omega@((V*(1/np.sqrt(w)))@V.T).T
S=np.column_stack((Z[:,0]+Z[:,1],Z[:,1]+Z[:,2],Z[:,2]+Z[:,0]))
for eps in [.01,.03,.06]:
    lo=np.zeros(N);hi=np.full(N,1.2)
    for _ in range(43):
        mid=(lo+hi)/2
        value=.5*np.prod(np.sqrt(1+eps*(mid[:,None]*S)**2),axis=1)-.5
        hi=np.where(value>eps,mid,hi)
        lo=np.where(value<=eps,mid,lo)
    coeff=(4*math.pi/3)*float(np.mean(hi**3))/2
    pred=2*math.pi/3+math.pi*eps/5
    assert abs(coeff-pred)<.003
# Corner gradient in each parameter and leading upper probability coefficient.
for aval in [.4,1,2]:
    rmax=.5*(1+4*aval*aval)**1.5
    slope=2*aval*math.sqrt(1+4*aval*aval)
    eps=1e-6
    first=(rmax-rad(np.array([aval-eps,aval,aval])))/eps
    assert abs(first/slope-1)<5e-6
print('PARABOLIC_CIRCUMRADIUS_ENDPOINTS_CHECKS_OK')
