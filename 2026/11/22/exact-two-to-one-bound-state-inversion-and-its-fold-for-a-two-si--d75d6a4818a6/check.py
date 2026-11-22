"""Reproducible symbolic and finite-section checks for two-defect Jacobi inverse fibers.
All infinite-dimensional assertions in the paper are analytic, not established by this checker.
"""
from fractions import Fraction
from math import sqrt
import numpy as np
import sympy as S

def jost(a,b,z):
    return 1-(a+b)*z+a*b*z*z-b*z*z*z

def eigen_roots(a,b):
    q=np.roots([-b,a*b,-(a+b),1])
    return np.sort([float(z.real) for z in q if abs(z.imag)<1e-9 and 0<z.real<1])

z=S.symbols('z')
r=S.Rational(1,10); s=S.Rational(2,5)
q=S.factor(r*s*z*z-(r+s)*(1-r*s)*z+1-r*s)
assert S.factor(q/S.Rational(1,25)) == z*z-12*z+24
for t in [6-2*S.sqrt(3),6+2*S.sqrt(3)]:
    a=S.simplify(r+s+t)
    b=S.simplify(1/(r*s*t))
    polynomial=S.expand(jost(a,b,z))
    for x in (r,s,t):assert S.simplify(polynomial.subs(z,x))==0
    assert float(a)>2 and float(b)>0
    assert float(b*(a-2)-a+1)>0
    assert np.allclose(eigen_roots(float(a),float(b)), [0.1,0.4],atol=1e-10)
    for N in (60,100,160):
        mat=np.diag(np.array([float(a),float(b)]+[0.]*(N-2)))+np.diag(np.ones(N-1),1)+np.diag(np.ones(N-1),-1)
        top=np.linalg.eigvalsh(mat)[-2:][::-1]
        assert np.max(abs(top-np.array([10.1,2.9])))< (0.14 if N==60 else 0.09)

# For independently sampled strictly two-bound-state potentials, reconstruct both roots.
checks=0
for a in np.linspace(2.1,12.0,23):
    for b in np.linspace((a-1)/(a-2)+0.1,16,31):
        if b<=0:continue
        R=np.sort(np.roots([-b,a*b,-(a+b),1]).real)
        if not (0<R[0]<R[1]<1<R[2]):
            raise AssertionError((a,b,R))
        r,s,t=R
        t_other=b-1/t
        assert t_other>1
        aa=r+s+t_other;bb=1/(r*s*t_other)
        assert abs(jost(aa,bb,r))<1e-8 and abs(jost(aa,bb,s))<1e-8
        assert np.allclose(eigen_roots(aa,bb),[r,s],atol=1e-8)
        assert abs(aa-a)<1e-7 and abs(bb-b)<1e-7 or abs(t_other-t)>1e-8
        checks+=1

# Fold equations and exact boundary of two-bound region.
t=S.symbols('t',positive=True)
a=t+2/t;b=t+1/t
assert S.factor(b*(a-2)-a+1)==(t-1)*(t**3-2*t**2+2*t-2)/t**2
print('All checks passed; sampled inverse cases:',checks)
