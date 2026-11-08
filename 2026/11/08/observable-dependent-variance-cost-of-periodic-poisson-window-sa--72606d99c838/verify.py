#!/usr/bin/env python3
"""Finite algebraic and numerical diagnostics for periodic Poisson window sampling.

Standard-library-only; not a substitute for the infinite-dimensional proof.
"""
from fractions import Fraction as F
from math import comb, factorial, cos, pi

checks=0

def test(ok,label):
    global checks
    assert ok, label
    checks += 1

# Sparse multivariate polynomials in independent Poisson variables A,B,C.
def const(c): return {(0,0,0): F(c)} if c else {}
def add(p,q):
    r=dict(p)
    for k,v in q.items():r[k]=r.get(k,F(0))+v
    return {k:v for k,v in r.items() if v}
def scale(p,c):return {k:v*c for k,v in p.items() if v*c}
def mul(p,q):
    r={}
    for (i,j,k),v in p.items():
      for (a,b,c),w in q.items():
        key=(i+a,j+b,k+c);r[key]=r.get(key,F(0))+v*w
    return {k:v for k,v in r.items() if v}
def fall(p,n):
    r=const(1)
    for j in range(n):r=mul(r,add(p,const(-j)))
    return r

def charlier(p,n,lam):
    res={}
    for j in range(n+1):
      res=add(res,scale(fall(p,j),F(comb(n,j))*(-lam)**(n-j)))
    return res

def stirling2(n,k):
    if n==0:return int(k==0)
    if k==0:return 0
    return stirling2(n-1,k-1)+k*stirling2(n-1,k)

def pois_raw(k,mu):return sum(F(stirling2(k,j))*mu**j for j in range(k+1))
def expectation(poly,means):
    return sum(v*pois_raw(i,means[0])*pois_raw(j,means[1])*pois_raw(k,means[2])
               for (i,j,k),v in poly.items())

A={(1,0,0): F(1)};B={(0,1,0): F(1)};C={(0,0,1):F(1)}
X=add(A,B);Y=add(A,C)
for lam in [F(1,2),F(1),F(5,2)]:
  for overlap in [F(0),F(1,7),F(1,2),F(1)]:
    means=[lam*overlap,lam*(1-overlap),lam*(1-overlap)]
    for r in range(4):
      for s in range(4):
        got=expectation(mul(charlier(X,r,lam),charlier(Y,s,lam)),means)
        exp=F(factorial(r))* (lam*overlap)**r if r==s else F(0)
        test(got==exp,f'cross Charlier r={r} s={s} lam={lam} overlap={overlap}: {got}!={exp}')
    p=fall(X,2);q=fall(Y,2)
    covariance=expectation(mul(p,q),means)-lam**4
    test(covariance==4*lam**3*overlap+2*lam**2*overlap**2,'factorial moment covariance')

# Fourier diagnostics using independently integrated covariance kernels.
def Fkernel(r,k,steps=16000):
    # midpoint integration of even triangular-power kernel
    sm=0.0
    for i in range(steps):
        x=(i+0.5)/steps
        sm+=(1-x)**r*cos(2*pi*k*x)
    return 2*sm/steps
for k in range(1,9):
    test(abs(Fkernel(1,k))<4e-9,f'first-chaos Fourier zero k={k}')
    test(abs(Fkernel(2,k)-1/(pi*pi*k*k))<4e-9,f'second-chaos Fourier k={k}')
    for r in range(3,8):
        test(Fkernel(r,k)>0,f'positive higher-chaos spectrum r={r} k={k}')
for r in range(1,8):
    # zero-frequency integral of (1-|v|)^r is 2/(r+1)
    test(abs(Fkernel(r,0)-2/(r+1))<4e-9,f'zero frequency r={r}')

# Auxiliary spectral check using the sinusoidal arrival-density autocorrelation.
# eta(u)=1+eps*cos(2*pi*harmonic*u), whose periodic autocorrelation is
# 1+(eps^2/2)*cos(2*pi*harmonic*v).
for lam in [0.5,1.0,2.5]:
  for eps in [0.2,0.6,0.9]:
    for harmonic in [1,2,4]:
      baseline=4*lam**3+4*lam**2/3
      explicit=baseline+lam**2*eps**2/(pi*pi*harmonic**2)
      steps=32000; integral=0.0
      for i in range(steps):
          v=(i+0.5)/steps
          covariance=4*lam**3*(1-v)+2*lam**2*(1-v)**2
          phase=1+eps**2/2*cos(2*pi*harmonic*v)
          integral+=2*covariance*phase/steps
      test(abs(integral-explicit)<2e-8,
           f'physical-time asymptotic variance lambda={lam}, eps={eps}, harmonic={harmonic}')
      # For h(x)=x, all nonzero harmonics cancel, so variance = lambda.
      linear=0.0
      for i in range(steps):
          v=(i+0.5)/steps
          linear+=2*lam*(1-v)*(1+eps**2/2*cos(2*pi*harmonic*v))/steps
      test(abs(linear-lam)<2e-8,'linear phase immunity')
print(f'PASS {checks} finite exact-algebra and numerical diagnostics')

# Independent physical-time overlap check for sinusoidal arrival intensities
# eta(t)=1+eps*cos(2*pi*ell*t), evaluated directly in physical time.
# J_v(t)=integral from t+v-1 to t of eta(s) ds.
from math import sin
for lam,eps,ell in [(F(1,2),F(1,3),1),(F(3,2),F(1,2),2),(F(3),F(2,3),3)]:
    lam=float(lam);eps=float(eps)
    Nv=1000; Nt=300
    total=0.
    for j in range(Nv):
        v=(j+0.5)/Nv
        phaseavg=0.
        for i in range(Nt):
            t=(i+0.5)/Nt
            J=(1-v)+eps/(2*pi*ell)*(sin(2*pi*ell*t)-sin(2*pi*ell*(t+v-1)))
            phaseavg+=4*lam**3*J+2*lam**2*J*J
        total+=phaseavg/Nt
    total*=2/Nv
    want=4*lam**3+4*lam**2/3+lam**2*eps**2/(pi*pi*ell*ell)
    test(abs(total-want)<3e-6, f'physical-clock overlap and Fourier law {lam},{eps},{ell}')
print(f'PASS final total {checks} algebraic and numerical diagnostics')
