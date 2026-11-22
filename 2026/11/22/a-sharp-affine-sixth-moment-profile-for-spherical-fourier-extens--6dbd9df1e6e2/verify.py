#!/usr/bin/env python3
"""Reproduce exact sixth moments and the affine spherical-extension deficit.

No external packages required for the exact rational portion. Optional scipy/numpy
quadrature is used solely as a numerical diagnostic, not as a proof.
"""
from collections import defaultdict
from fractions import Fraction as F
from math import factorial, pi

# b_{a,k}(t)=(t-a)_+^k/k!, with b_{a,p}*b_{b,q}=b_{a+b,p+q+1}.
# The delta at zero is encoded by (0,-1).
u = {(-1,0):1,(1,0):-1}                    # indicator [-1,1]
v = {(-1,1):1,(-1,0):-1,(1,1):-1,(1,0):-1} # t indicator [-1,1]
def conv(A,B):
    C=defaultdict(int)
    for (a,p),x in A.items():
        for (b,q),y in B.items(): C[a+b,p+q+1]+=x*y
    return {k:z for k,z in C.items() if z}
def second_at_origin(A):
    return sum((F(x*(-a)**(p-2),factorial(p-2)) for (a,p),x in A.items() if a<0 and p>=2),F(0))

# sinc r = integral_{-1}^1 exp(irt)dt/2. Even powers of sinc' carry (-1)^k.
# R_k=4pi int_0^infty r^2 sinc(r)^(6-2k) sinc'(r)^(2k)dr.
# Distribution identity int_R r^2 exp(irs)dr=-2*pi*delta''(s).
R=[]
expected=[F(1,2),F(1,10),F(29,630),F(107,1890)]
for k in range(4):
    C={(0,-1):1}
    for x in [u]*(6-2*k)+[v]*(2*k): C=conv(C,x)
    h=second_at_origin(C)
    moment=(-1)**(k+1)*h/F(16) # R_k / pi^2
    assert moment==expected[k], (k,moment)
    R.append(moment)
print('Exact radial moment ratios R_k/pi^2:',*[str(x) for x in R])

# Angular spherical moments in R^3 and all Rk yield exact sextic polynomial.
# Let a>=0, v=p+i q with P=|p|^2, Q=|q|^2, h=p dot q, s=P+Q.
# The expression below is integral |T(a+v dot omega)|^6 divided by pi^2.

def moment(a,P,Q,h):
    s=P+Q
    tr2=P*P+Q*Q+2*h*h
    tr3=P**3+Q**3+3*s*h*h
    return (R[0]*a**6 + R[1]*a**4*(s+4*Q)
            +R[2]*a*a/F(5)*(s*s+2*tr2+4*Q*s+8*Q*Q+8*h*h)
            +R[3]/F(105)*(s**3+6*s*tr2+8*tr3))
def upper(a,s):
    return R[0]*a**6+5*R[1]*a**4*s+3*R[2]*a*a*s*s+R[3]/7*s**3
def deficit(a,P,Q,h):
    s=P+Q; D=P*Q-h*h
    return (P*(4*R[1]*a**4+F(12,5)*R[2]*a*a*s)
            +D*(F(12,5)*R[2]*a*a+F(12,35)*R[3]*s))

import sympy as S
a,P,Q,h=S.symbols('a P Q h',real=True)
assert S.expand(upper(a,P+Q)-moment(a,P,Q,h)-deficit(a,P,Q,h))==0
b=S.symbols('b',real=True)
profile=S.factor(upper(S.sqrt(1-b),3*b))
assert S.expand(profile-(F(1,2)-F(9,35)*b*b-F(6,245)*b**3))==0
print('Sharp profile /pi^2:',profile)
print('Exact polarization deficit /pi^2:',S.factor(deficit(a,P,Q,h)))

# Non-proof diagnostic checks: independently integrate angular and radial variables.
try:
    import numpy as np
    from scipy.integrate import quad
    from numpy.polynomial.legendre import leggauss
    mu,wt=leggauss(24)
    angles=np.arange(32)*2*pi/32
    nvec=np.array([(np.sqrt(1-z*z)*np.cos(t),np.sqrt(1-z*z)*np.sin(t),z) for z in mu for t in angles])
    w=np.repeat(wt,32)*(2*pi/32)
    cases=[(0.8,np.array([1+0.7j, -0.4+0.6j,0.2-0.2j])),
           (0.3,np.array([0.0+0.9j,0.0j,0.0j])),
           (0.0,np.array([1+0.5j,-0.4+0.1j,0.9-0.7j]))]
    for alpha,V in cases:
        pc=np.real(V);qc=np.imag(V)
        Fexact=float(pi*pi*moment(alpha,float(pc@pc),float(qc@qc),float(pc@qc)))
        def radial(r):
            ph=np.sinc(r/pi)
            dp=(r*np.cos(r)-np.sin(r))/r**2 if r>1e-6 else -r/3+r**3/30
            values=alpha*ph+1j*dp*(nvec@V)
            return r*r*np.sum(w*np.abs(values)**6)
        N=quad(radial,0,150,epsabs=1e-7,limit=1000)[0]
        assert abs(N-Fexact)<0.0003,(N,Fexact)
        print('Quadrature check:',round(N,8),round(Fexact,8))
except ImportError:
    print('Optional scipy/numpy numeric diagnostics not performed.')
print('ALL EXACT CHECKS PASS')
