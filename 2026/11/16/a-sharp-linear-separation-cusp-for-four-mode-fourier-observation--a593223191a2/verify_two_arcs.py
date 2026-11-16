"""Standalone symbolic and numerical checks for four-mode two-arc observability.

Requires Python 3, sympy, numpy. Uses normalized Haar measure on the circle.
"""
import math
import numpy as np
import sympy as sp

x, c, A = sp.symbols('x c A', real=True)
B = A*c
E = (4*c*c-1)/3
b1 = A*x
b2 = A*c*(2*x*x-1)
b3 = A*E*(4*x**3-3*x)
d_plus=(B+b3)*(B+b1)-(b1+b2)**2
d_minus=(B-b3)*(B-b1)-(b1-b2)**2
assert sp.simplify((d_plus+d_minus)/2+sp.Rational(4,3)*A*A*(1-c*c)*x**4)==0

# Full Gram eigenvalues, independent of block formulas.
def gram(alpha, theta):
    m=2*alpha/math.pi
    b=[m]+[2*math.sin(k*alpha)*math.cos(k*theta/2)/(math.pi*k)
           for k in range(1,4)]
    return np.array([[b[abs(i-j)] for j in range(4)] for i in range(4)])

# Gaussian-Legendre integration of |P|^2 over the arcs, derived separately from the Fourier coefficient formula.
def direct_gram(alpha, theta, nquad=80):
    u,w=np.polynomial.legendre.leggauss(nquad)
    out=np.zeros((4,4),complex)
    for center in (-theta/2,theta/2):
        t=center+alpha*u
        mat=np.exp(1j*np.outer(t,np.arange(4)))
        out+=(alpha/(2*math.pi))*(mat.conj().T*w)@mat
    return out

n=0
for alpha in (0.03,0.13,0.31,0.52,0.74,1.2):
    m=2*alpha/math.pi
    baseline=m-math.sin(2*alpha)/math.pi
    at=gram(alpha, math.pi)
    vals=np.linalg.eigvalsh(at)
    assert np.max(np.abs(vals-np.array([baseline,baseline,m+math.sin(2*alpha)/math.pi,m+math.sin(2*alpha)/math.pi])))<5e-13
    for theta in np.linspace(2*alpha,math.pi,41):
        G=gram(alpha,theta)
        G2=direct_gram(alpha,theta)
        assert np.max(np.abs(G-G2)) < 3e-13
        lam=np.linalg.eigvalsh(G)[0]
        x0=math.cos(theta/2)
        bound=2*math.sin(alpha)**3/(3*math.pi)*x0**4
        assert baseline-lam>=bound-2e-13,(alpha,theta,baseline-lam,bound)
        n+=1
    # Slope limit computed at three decreasing angular separations.
    target=2*math.sin(alpha)**3/math.pi
    errors=[]
    for d in (1e-3,5e-4,2.5e-4):
        lam=np.linalg.eigvalsh(gram(alpha,math.pi-d))[0]
        errors.append(abs((baseline-lam)/d-target))
    assert errors[-1]<2e-3,(alpha,errors,target)
print(f'TWO_ARC_FOUR_MODE_PASS symbolic_determinant=1 independent_quadratures={n} cusp_slopes=6')
