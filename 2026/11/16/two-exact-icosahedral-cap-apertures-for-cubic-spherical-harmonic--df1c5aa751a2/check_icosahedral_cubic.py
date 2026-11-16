"""Reproducibility checks for cubic harmonic sampling by icosahedral cap mixtures.
Run: python check_icosahedral_cubic.py
Requires Python 3, NumPy and SymPy; checks exact symbolic and numerical identities.
"""
import numpy as np
import sympy as sp
from numpy.polynomial.legendre import leggauss

phi = (1+sp.sqrt(5))/2
W = sp.Matrix([[0,1,phi],[0,1,-phi],[1,phi,0], [1,-phi,0],[phi,0,1],[phi,0,-1]])
W = W / sp.sqrt(1+phi**2)
def L3(t): return (5*t**3-3*t)/2
S = sp.Matrix(6,6,lambda i,j: 0 if i==j else sp.simplify(sp.sqrt(5)*L3(sp.simplify(W.row(i).dot(W.row(j))))))
assert all(v in (-1,0,1) for v in S)
assert S*S == 5*sp.eye(6)
assert sp.simplify(S.trace())==0
# Antipodal point-orbit frame has spectrum 0 (four times), 7/3 (three times).
M = sp.Rational(7,6)*(sp.eye(6)+S/sp.sqrt(5))
assert M.eigenvals()=={sp.Integer(0):3,sp.Rational(7,3):3}

z=sp.symbols('z',real=True)
P6=sp.legendre(6,z)
acc=sp.factor(sp.integrate(P6,(z,z,1))/(1-z))
assert sp.simplify(acc-z*(1+z)*(429*z**4-390*z**2+65)/208)==0
assert sp.simplify(sp.limit(acc,z,1))==1
assert sp.simplify(sp.limit((1-acc)/(1-z),z,1))==sp.Rational(21,2)
radii=[sp.sqrt((195-sp.sqrt(15)*26)/429),sp.sqrt((195+sp.sqrt(15)*26)/429)]
for r in radii: assert sp.simplify(acc.subs(z,r))==0
for l in (2,4):
    assert sp.simplify((1+5*sp.legendre(l,1/sp.sqrt(5)))/6)==0

V=np.array(W.evalf(), dtype=float)
points=np.vstack([V,-V])

def H(X):
    x,y,z=X[:,0],X[:,1],X[:,2]
    return np.column_stack([x*(5*z*z-1),y*(5*z*z-1),z*(x*x-y*y),x*y*z,
                   x*(x*x-3*y*y),y*(3*x*x-y*y),z*(5*z*z-3)])

def integrate_caps(c):
    T,weights=leggauss(11)
    ts=(1+c)/2+(1-c)*T/2
    ws=weights/2
    angles=2*np.pi*np.arange(24)/24
    sums=np.zeros((7,7))
    for u in points:
        ref=np.array([0.,0.,1.]) if abs(u[2])<0.8 else np.array([0.,1.,0.])
        e=np.cross(u,ref); e/=np.linalg.norm(e)
        f=np.cross(u,e)
        for t,w in zip(ts,ws):
            circle=(t*u+np.sqrt(1-t*t)*(np.cos(angles)[:,None]*e+np.sin(angles)[:,None]*f))
            Z=H(circle)
            sums+=w*Z.T@Z/24/12
    return sums

# Normalize the polynomial basis from a separately integrated whole sphere.
T,w=leggauss(12)
angles=2*np.pi*np.arange(24)/24
sigma=np.zeros((7,7))
for t,weight in zip(T,w):
    X=np.column_stack([np.sqrt(1-t*t)*np.cos(angles),np.sqrt(1-t*t)*np.sin(angles),np.full(24,t)])
    Z=H(X);sigma+=weight/2*Z.T@Z/24
assert np.linalg.eigvalsh(sigma)[0]>1e-4
sigma_half=np.linalg.inv(np.linalg.cholesky(sigma))
A=sigma_half @ (H(points).T@H(points)/12) @ sigma_half.T
assert np.max(np.abs(np.linalg.eigvalsh(A)-np.array([0]*4+[7/3]*3)))<3e-11
for c in (0.05,0.25,float(radii[0]),0.60,float(radii[1]),0.93,0.995):
    G=integrate_caps(c)
    Q=sigma_half@G@sigma_half.T
    a=float(acc.subs(z,c))
    predicted=np.array([1-a]*4+[1+4*a/3]*3)
    error=np.max(np.abs(np.linalg.eigvalsh(Q)-np.sort(predicted)))
    assert error<2e-10,(c,error)
    print('CAP',format(c,'.12f'),'multiplier',format(a,'.12f'),'error',f'{error:.2e}')
print('ICOSAHEDRAL_CUBIC_CAP_PASS point_conference=6x6 moment_degrees=2,4 cap_tests=7 tight_radii=2')
