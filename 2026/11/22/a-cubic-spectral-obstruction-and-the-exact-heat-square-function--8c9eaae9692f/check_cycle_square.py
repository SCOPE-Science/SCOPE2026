"""Independent finite checks of spectral identities for heat square functions.

The proof for all cycle sizes is analytic; these calculations are diagnostics.
Requires Python 3, sympy and numpy. Run: python check_cycle_square.py.
"""
import sympy as sp
import numpy as np

x,y,a=sp.symbols('x y a',real=True)
quad=x*x/4+y*y/4+2*a*x*y
D=sp.expand((x+y)**4-16*quad**2)
expected=sp.expand(4*(1-4*a)*(x**3*y+(1+4*a)*x*x*y*y+x*y**3))
assert sp.simplify(D-expected)==0
print('PASS: universal pointwise two-eigenmode quartic identity')

# Verify the exact C4 two-eigenvalue coefficient and deficit.
lambda2,lambda4=sp.Integer(2),sp.Integer(4)
a24=lambda2*lambda4/(lambda2+lambda4)**2
assert a24==sp.Rational(2,9)
rho=4*a24
assert rho==sp.Rational(8,9)
assert sp.simplify(1-rho**2)==sp.Rational(17,81)
print('PASS: C4 coefficient rho=8/9 and 17/81 nonnegative deficit')

# Check the trigonometric witnesses with independent Fourier-diagonal formulas.
for n in range(5,501):
    j=np.arange(n)
    u=np.cos(2*np.pi*j/n)
    w=np.cos(6*np.pi*j/n)
    lam1=2-2*np.cos(2*np.pi/n)
    lam3=2-2*np.cos(6*np.pi/n)
    a=float(lam1*lam3/(lam1+lam3)**2)
    t=-1/64
    f=u+t*w
    g2=u*u/4+t*t*w*w/4+2*a*t*u*w
    assert min(g2)>-1e-12
    deficit=float(np.sum(f**4-16*g2**2))
    A=float(np.sum(u**3*w))
    B=float(np.sum(u*u*w*w))
    C=float(np.sum(u*w**3))
    predicted=4*(1-4*a)*t*(A+(1+4*a)*t*B+t*t*C)
    assert abs(deficit-predicted)<3e-10*max(1,abs(deficit))
    assert abs(A-np.sum(w*w)/4)<2e-11*n
    assert deficit<0,(n,deficit)
print('PASS: C5 through C500 have a strictly negative quartic deficit')

# Complex-valued C4: reconstruct from all eigenvectors and the integral Gram coefficients.
for k in range(200):
    rng=np.random.default_rng(k)
    A,B,C=[rng.normal(size=2)+1j*rng.normal(size=2) for _ in range(3)]
    U=np.array([A,-A,A,-A]); V=np.array([B,C,-B,-C]); F=U+V
    point=np.sum(abs(U)**2+abs(V)**2,axis=1)
    cross=2*np.real(np.sum(U*np.conj(V),axis=1))
    G2=(point+float(rho)*cross)/4
    deficit=np.sum(np.sum(abs(F)**2,axis=1)**2-16*G2**2)
    target=float(1-rho**2)*np.sum(cross**2)
    assert abs(deficit-target)<1e-9
    assert deficit>=-1e-9
print('PASS: 200 complex Hilbert-vector C4 deficit checks')
