"""Reproducible checks for Ritz-gap and eigenvector-conditioning formulas.

The asymptotic theorem is established analytically in RESULT.md; this script
checks finite-dimensional identities, exact constants, and a local area limit.
"""
from fractions import Fraction
from math import sqrt, pi, isclose
import random
import cmath

try:
    import numpy as np
except ImportError as exc:
    raise SystemExit('This checker requires numpy for finite-matrix replay') from exc

OMEGA=complex(-0.5, sqrt(3)/2)
SPEC=np.array([1,OMEGA,OMEGA.conjugate()], dtype=complex)
N=0

def ensure(v,why):
    global N
    N+=1
    if not v:
        raise AssertionError(why)

# Exact-real rational polynomial tests on barycentric weights.  Imaginary parts
# of u, u-bar handled by the quadratic extension Q(sqrt(-3)).
for den in (7,11,17,31):
    for a in range(1,den):
        for b in range(1,den-a):
            c=den-a-b
            w1,w2,w3 = Fraction(a,den),Fraction(b,den),Fraction(c,den)
            # u = x + i sqrt(3) y; x=(3w1-1)/2, y=(w2-w3)/2.
            x=(3*w1-1)/2
            y=(w2-w3)/2
            # F=u^2-4 conjugate(u): real=x^2-3y^2-4x,
            # sqrt(3)*imag=(2xy+4y)
            f_re=x*x-3*y*y-4*x
            f_im=2*x*y+4*y
            ensure((f_re==0 and f_im==0)==(w1==w2==w3),'unique defect')
            # Equivalent cubic compression char: z^2+u*z+u-bar.
            # Determinant constant = w1+omega^2*w2+omega*w3: (x,-y)
            const_re=w1-(w2+w3)/2
            const_im=(w3-w2)/2
            ensure((x,y)==(const_re,-const_im),'constant coefficient')

# Matrix replay for Haar normals including nonreal/real orthogonal complements.
rng=np.random.default_rng(20261107)
for field in ('complex','real'):
    for _ in range(350):
        g=rng.normal(size=3)+(1j*rng.normal(size=3) if field=='complex' else 0)
        v=np.asarray(g, dtype=complex)/np.linalg.norm(g)
        P=np.eye(3,dtype=complex)-np.outer(v,v.conj())
        eigv,eigvec=np.linalg.eigh(P)
        Q=eigvec[:,1:]
        B=Q.conj().T@np.diag(SPEC)@Q
        w=np.abs(v)**2
        u=w[0]+OMEGA*w[1]+OMEGA.conjugate()*w[2]
        F=u*u-4*u.conjugate()
        roots=np.linalg.eigvals(B)
        D=abs(roots[0]-roots[1])
        ensure(abs(np.trace(B)+u)<3e-12,'trace')
        ensure(abs(np.linalg.det(B)-u.conjugate())<3e-12,'det')
        ensure(abs(D**2-abs(F))<4e-12,'discriminant gap')
        frob=np.linalg.norm(B,'fro')**2
        ensure(abs(frob-(1+abs(u)**2))<4e-12,'frob')
        nu2=1+(abs(u)**2-D**2)/2
        ensure(nu2>-1e-12,'schur nu square nonnegative')
        nu=sqrt(max(0,nu2))
        k_expected=(sqrt(nu2+D*D)+nu)/D
        ew,ev=np.linalg.eig(B)
        ev=ev/np.linalg.norm(ev,axis=0)
        k_actual=np.linalg.cond(ev)
        ensure(abs(k_actual/k_expected-1)<3e-9,'unit-column eig cond')

# Approximate density at zero by uniform barycentric area sampling and independent
# squared-normal (real Haar) sampling; finite epsilon is NOT the proof.
for field in ('complex','real'):
    for eps in (0.38,0.48,0.62):
        count=0
        batch=150000
        g=rng.normal(size=(batch,3))
        if field=='complex':
            g=(g+1j*rng.normal(size=(batch,3)))/sqrt(2)
        w=np.abs(g)**2
        w=w/w.sum(axis=1,keepdims=True)
        u=w[:,0]+OMEGA*w[:,1]+OMEGA.conjugate()*w[:,2]
        event=np.abs(u*u-4*np.conj(u))<=eps**2
        rate=float(np.mean(event))
        predicted=(pi/(12*sqrt(3)) if field=='complex' else 1/16)*eps**4
        # Loose sanity for a finite epsilon and empirical sample; not certification.
        ensure(0.55<rate/predicted<1.6, f'local area sanity: {field},{eps},{rate},{predicted}')

# Exact Jacobian at barycenter 16; constants from barycentric Dirichlet densities.
area_T=3*sqrt(3)/4
assert isclose((pi/16)/area_T, pi/(12*sqrt(3)),rel_tol=1e-14)
assert isclose((pi/16)*(1/pi),1/16,rel_tol=1e-14)
assert isclose(16*pi/(12*sqrt(3)),4*pi/(3*sqrt(3)),rel_tol=1e-14)
assert isclose(16*(1/16),1,rel_tol=1e-14)
print(f'PASS: {N} finite symbolic, matrix, and simulation checks; proof is analytic')
