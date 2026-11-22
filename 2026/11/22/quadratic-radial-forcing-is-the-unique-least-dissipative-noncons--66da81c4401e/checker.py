"""Exact rational checker for radial-force dissipation in a driven OU trap.

Independent routes: (i) stationary polynomial moment equations for (S,Z),
and (ii) orthogonal Laguerre spectral weights. Run with Python 3.
"""
from fractions import Fraction as F
from math import factorial, comb
from itertools import product

def mul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):r[i+j]+=a*b
    return r

def laguerre(n):
    return [F((-1)**j*comb(n,j),factorial(j)) for j in range(n+1)]

def normal_expect(poly):
    return sum(c*factorial(k) for k,c in enumerate(poly))

def direct_sigma(coeffs,eta):
    # Polynomial f(S)=sum a_m L_m(S); s=(x^2+y^2)/2 ~ Exp(1).
    deg=len(coeffs)
    p=[F(0)]*(deg+1)
    for m,a in enumerate(coeffs,1):
        for k,c in enumerate(laguerre(m)):p[k]+=a*c
    assert normal_expect(p)==0
    # Stationary generator: L S^k=2*k^2 S^(k-1)-2*k S^k.
    z_sk=[F(0)]*(deg+1)
    for k in range(deg+1):
        fs=normal_expect([F(0)]*k+p)  # E[f(S) S^k]
        z_sk[k]=(fs+(2*k*k*z_sk[k-1] if k else 0))/(eta+2*k)
    fz=sum(c*v for c,v in zip(p,z_sk))
    force_var=normal_expect(mul(p,p))
    return (force_var-eta*fz)/eta,force_var,fz

def spectrum_sigma(coeffs,eta):
    return sum(a*a*F(2*m,1)/(eta*(eta+2*m)) for m,a in enumerate(coeffs,1))

checks=0
for eta in [F(1,3),F(1),F(2),F(7,2),F(11)]:
    for n in range(1,7):
        coeffs=[F(0)]*n
        coeffs[-1]=F(1)
        s,v,fz=direct_sigma(coeffs,eta)
        assert v==1 and s==spectrum_sigma(coeffs,eta)
        assert s==F(2*n)/(eta*(eta+2*n))
        checks+=3
    for co in [[F(1),F(2)],[F(-2),F(1),F(3)],[F(3,2),F(0),F(-4,3),F(5,2)], [F(1),F(-2),F(3),F(-4),F(5)]]:
        s,v,fz=direct_sigma(co,eta)
        ref=spectrum_sigma(co,eta)
        assert s==ref
        assert v==sum(x*x for x in co)
        assert eta*s>=F(2)*v/(eta+2)
        tail=sum(a*a for a in co[1:])
        assert s-F(2)*v/(eta*(eta+2))>=F(2)*tail/((eta+2)*(eta+4))
        checks+=4
    # Equality witness for sharp stability gap: only Laguerre degrees 1 and 2.
    s,v,_=direct_sigma([F(3),F(-2)],eta)
    assert s-F(2)*v/(eta*(eta+2))==F(2)*F(4)/((eta+2)*(eta+4))
    checks+=1
# Nonattained upper bound and its approach by normalized higher degrees.
for n in [1,2,5,10,25,100,1000]:
    eta=F(3)
    s=spectrum_sigma([F(0)]*(n-1)+[F(1)],eta)
    assert s < F(1,eta) and F(1,eta)-s==F(1,eta+2*n)
    checks+=2
print('PASS:',checks,'exact rational assertions; generator/moment and spectral methods agree')
