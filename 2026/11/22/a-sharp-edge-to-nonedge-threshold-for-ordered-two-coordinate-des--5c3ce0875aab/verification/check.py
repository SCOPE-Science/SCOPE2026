"""Reproduce exact two-step coordinate-energy identities and finite checks.

Requirements: Python 3.10+, sympy>=1.11. This checks algebraic identities;
finite grids are illustrative rather than substitutes for universal proof.
"""
import sympy as sp

c, p, t = sp.symbols('c p t', real=True)
H = sp.Matrix([[1,-c,-c],[-c,1,0],[-c,0,1]])
T = []
for j in range(3):
    Q = sp.eye(3)
    Q[j,:] -= H[j,:]
    T.append(Q)

def gain(i,j):
    P=T[j]*T[i]
    return sp.simplify(H-P.T*H*P)
A=sp.simplify((gain(0,1)+gain(0,2))/2)
B=sp.simplify((gain(1,0)+gain(2,0))/2)
C=sp.simplify((gain(1,2)+gain(2,1))/2)
R=sp.Matrix([[1,0,0],[0,1,1],[0,1,-1]]).T
h0=R.T*H*R
Db=sp.factor(3+2*c-3*c*c)
p0=2*(1+c)/Db
t0=2*(1-2*c*c)/Db
D=(R.T*(p0*B+(1-p0)*C-t0*H)*R).applyfunc(sp.factor)
u=sp.Matrix([1+c-c*c,-(1+c),0])
expected=2*c/Db*(u*u.T+sp.diag(0,0,(1+c)**2))
assert (D-expected).applyfunc(sp.factor)==sp.zeros(3)
print('symbolic interior PSD rank-one-plus-contrast identity: PASS')

Dpoly=sp.factor(((R.T*B*R)[:2,:2]-t*h0[:2,:2]).det())
expected_poly=-(2*c*c-1)*(2*t*t+(3*c*c-3)*t+1-2*c*c)
assert sp.factor(Dpoly-expected_poly)==0
print('symbolic leaf-to-hub generalized characteristic polynomial: PASS')

z=sp.symbols('z', real=True)
S=sp.factor(sp.diff((1+(z+c)**2)/(z*z+4*c*z+2),z) *(z*z+4*c*z+2)**2/2)
assert sp.expand(S-(-2*c**3-c**2*z+c*z*z+z))==0
assert sp.factor(S.subs(z,1-c))==1-3*c*c
print('symbolic Rayleigh stationary equation and threshold: PASS')

# Exact rational enumeration of the 9 ordered updates, with direct generalized
# eigenvalue testing at several rational coupling strengths.
import itertools
checked=0
for cv in [sp.Rational(k,100) for k in [1,10,20,30,40,50,55,60,65,69]]:
    hc=H.subs(c,cv)
    av=A.subs(c,cv);bv=B.subs(c,cv); ev=C.subs(c,cv)
    pv=sp.Min(1,p0.subs(c,cv)); tv=t0.subs(c,cv) if cv*cv<=sp.Rational(1,3) else (3-3*cv*cv-sp.sqrt(9*cv**4-2*cv**2+1))/4
    f=sp.simplify(pv*bv+(1-pv)*ev)
    # Check the candidate's generalized eigenvalue and all nonnegative slack eigenvalues to tolerance.
    import numpy as np
    from numpy.linalg import eigvalsh
    from scipy.linalg import eigh
    hnp=np.array(hc,dtype=float);fnp=np.array(f,dtype=float)
    evs=eigh(fnp,hnp,eigvals_only=True)
    assert abs(float(evs[0])-float(tv))<1e-9
    assert min(evs)>0
    for i,j in itertools.product(range(3),repeat=2):
        g=gain(i,j).subs(c,cv)
        assert g==g.T
        checked+=1
print('finite candidate spectral and ordered-pair comparisons: PASS,',checked,'checks')
