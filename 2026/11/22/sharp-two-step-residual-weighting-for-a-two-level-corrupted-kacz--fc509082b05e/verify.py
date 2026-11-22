"""Exact elementary verification of the two-state Kaczmarz theorem's algebra.
Run: python verify.py. The infinite-parameter claims require the accompanying proof.
"""
from fractions import Fraction as Q
from math import isclose

# Two-variable polynomial algebra on (z,t). Exponent pairs are keys.
def add(a,b):
    c=dict(a)
    for k,v in b.items(): c[k]=c.get(k,0)+v
    return {k:v for k,v in c.items() if v}
def mul(a,b):
    c={}
    for (i,j),u in a.items():
        for (k,l),v in b.items(): c[(i+k,j+l)]=c.get((i+k,j+l),0)+u*v
    return {k:v for k,v in c.items() if v}
def deriv_t(a): return {(i,j-1):j*v for (i,j),v in a.items() if j}
def scale(a,s): return {k:s*v for k,v in a.items()}
ONE={(0,0):1}; Z={(1,0):1}; T={(0,1):1}
Z2=mul(Z,Z); ZT=add(Z,T); ZT2=mul(ZT,ZT)
U=mul(T,add(scale(Z,2),mul(add(ONE,Z2),T)))
V=mul(ZT2,add(ONE,mul(Z,T)))
N=add(add(scale(Z,2),scale(mul(Z2,T),2)),add(mul(add(mul(Z,Z2),scale(Z,-3)),mul(T,T)),scale(mul(add(ONE,Z2),mul(mul(T,T),T)),-1)))
assert add(mul(deriv_t(U),V),scale(mul(U,deriv_t(V)),-1))==mul(mul(Z,N),ZT), 'derivative identity'


def walk(p,t):
    p=Q(p);t=Q(t);q=1-p
    alpha=p*t/(q+p*t)
    beta=q*t/(p+q*t)
    lam=1-alpha-beta
    stationary=alpha/(alpha+beta)
    assert stationary==(p*p+p*q*t)/(p*p+q*q+2*p*q*t)
    assert lam==(p*q*(1-t*t))/((q+p*t)*(p+q*t))
    assert Q(0)<=lam<Q(1)
    # P^2 from both states; B-to-B is worst since the eigenvalue is nonnegative.
    p_bb=beta*alpha+(1-beta)*(1-beta)
    p_gb=(1-alpha)*alpha+alpha*(1-beta)
    assert p_bb==1-beta*(1+lam)
    assert p_bb-p_gb==lam*lam
    z=p/q
    gain=(t*(2*z+(1+z*z)*t))/((z+t)*(z+t)*(1+z*t))
    assert 1-p_bb==gain
    assert p_bb==stationary+(1-stationary)*lam*lam
    return p_bb

checks=0
for m in range(2,36):
    for k in range(1,m):
        for a,b in [(1,10),(1,3),(1,2),(3,4),(1,1)]:
            walk(Q(k,m),Q(a,b));checks+=1
assert walk(Q(1,10),Q(1,2))==Q(175,2299)
assert walk(Q(1,10),Q(1,1))==Q(1,10)

# Root signs and uniqueness are proved analytically; test crossing for a finite mesh.
def npoly(z,t):
    return 2*z+2*z*z*t+z*(z*z-3)*t*t-(1+z*z)*t*t*t
for m in range(2,55):
    for k in range(1,m):
        z=Q(k,m-k)
        assert npoly(z,Q(0))>0
        if k<m-k:
            assert npoly(z,z)>0 and npoly(z,Q(1))<0
            left=z;right=Q(1)
            for _ in range(30):
                h=(left+right)/2
                if npoly(z,h)>0:left=h
                else:right=h
            assert 0<right-left<Q(1,10**8)
            assert walk(Q(k,m),left)<walk(Q(k,m),Q(1))
        else:
            assert all(npoly(z,Q(i,20))>=0 for i in range(20))
        checks+=1

# Cubic leading scale; numerical tests are diagnostics only.
for p in [1e-4,1e-6,1e-8]:
    z=p/(1-p);lo=0.;hi=1.
    for _ in range(120):
        mid=(lo+hi)/2
        if npoly(z,mid)>0:lo=mid
        else:hi=mid
    t=(lo+hi)/2
    al=p*t/(1-p+p*t);be=(1-p)*t/(p+(1-p)*t);la=1-al-be
    risk=1-be*(1+la)
    print('p, opt_t, opt_risk, scaled_t, scaled_risk:',p,t,risk,t/(2*p)**(1/3),risk/(3*2**(-2/3)*p**(4/3)))
print('PASS: symbolic derivative polynomial, exact two-step rational identities, and',checks,'parameter cases')
