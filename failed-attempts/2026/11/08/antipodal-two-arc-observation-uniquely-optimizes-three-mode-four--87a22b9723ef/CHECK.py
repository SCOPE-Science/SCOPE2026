"""Reproducibility checks for three-mode observation on equal circular arcs."""
import math
import numpy as np
import sympy as sp

PI=math.pi

def coeffs(beta,alpha):
    a=2*beta/PI
    u=2*math.sin(beta)*math.cos(alpha)/PI
    v=math.sin(2*beta)*math.cos(2*alpha)/PI
    return a,u,v

def matrix(beta,alpha):
    a,u,v=coeffs(beta,alpha)
    return np.array([[a,u,v],[u,a,u],[v,u,a]],dtype=float)

def exact_eigs(beta,alpha):
    a,u,v=coeffs(beta,alpha)
    h=math.hypot(v,math.sqrt(8)*u)
    return sorted([a-v,a+v/2-h/2,a+v/2+h/2])

def matrix_from_endpoints(beta,alpha):
    """Directly integrate exponentials over two disjoint arcs (not using Toeplitz formulas)."""
    endpoints=[(-alpha-beta,-alpha+beta),(alpha-beta,alpha+beta)]
    M=np.zeros((3,3),dtype=complex)
    freq=[-1,0,1]
    for i,m in enumerate(freq):
        for j,n in enumerate(freq):
            k=n-m
            M[i,j]=sum((hi-lo if k==0 else (np.exp(1j*k*hi)-np.exp(1j*k*lo))/(1j*k)) for lo,hi in endpoints)/(2*PI)
    return M

def expected_gap(beta,alpha):
    t=math.cos(alpha)
    B=math.sin(2*beta)/PI
    D=math.sqrt((2*t*t-1)**2+8*t*t/(math.cos(beta)**2))
    return 4*B*(math.tan(beta)**2)*t*t/(D+1+2*t*t)

rng=np.random.default_rng(20261106)
checks=0
for beta in np.linspace(0.03,1.52,71):
    for frac in [0.0,0.001,0.08,0.25,0.51,0.83,0.98,1.0]:
        alpha=float(beta+(PI/2-beta)*frac)
        M=matrix_from_endpoints(beta,alpha)
        assert np.max(np.abs(M-matrix(beta,alpha)))<3e-14
        e=np.linalg.eigvalsh(M)
        model=exact_eigs(beta,alpha)
        assert max(abs(x-y) for x,y in zip(e,model))<3e-14
        Aopt=(2*beta-math.sin(2*beta))/PI
        assert abs(Aopt-e[-3]-expected_gap(beta,alpha))<3e-12
        assert e[0]<=Aopt+3e-13
        if frac<1:
            assert e[0]<Aopt-1e-13 if expected_gap(beta,alpha)>1e-12 else e[0]<Aopt
        checks+=6
# Independent direct-integration test of quadratic-form sampling norm.
for i in range(180):
    beta=float(rng.uniform(0.04,1.45))
    alpha=float(rng.uniform(beta,PI/2))
    c=rng.normal(size=3)+1j*rng.normal(size=3)
    form=float(np.real(np.vdot(c,matrix(beta,alpha)@c)))
    x1=np.linspace(-alpha-beta,-alpha+beta,4001)
    x2=np.linspace(alpha-beta,alpha+beta,4001)
    f=lambda t:c[0]*np.exp(-1j*t)+c[1]+c[2]*np.exp(1j*t)
    integ=(np.trapezoid(abs(f(x1))**2,x1)+np.trapezoid(abs(f(x2))**2,x2))/(2*PI)
    assert abs(form-integ)<3e-7
    checks+=1
# Nonstandard determinant certificate exactly: symmetric shifted block determinant.
b,t=sp.symbols('b t',positive=True,real=True)
B=sp.sin(2*b)/sp.pi
A=2*sp.sin(b)/sp.pi
assert sp.trigsimp(sp.expand((2*B*t**2)*B-2*(A*t)**2)+2*t*t*(A*A-B*B))==0
checks+=1
# Small-arc series of optimal value and contiguous observation comparator.
opt=(2*b-sp.sin(2*b))/sp.pi
u=sp.sin(2*b)/sp.pi
v=sp.sin(4*b)/(2*sp.pi)
contig=2*b/sp.pi+v/2-sp.sqrt(v**2+8*u**2)/2
assert sp.simplify(sp.limit(opt/b**3,b,0)-sp.Rational(4,3)/sp.pi)==0
assert sp.simplify(sp.limit(contig/b**5,b,0)-sp.Rational(64,135)/sp.pi)==0
checks+=2
print('TWO_ARC_FOURIER_CHECKS_PASSED',checks)
