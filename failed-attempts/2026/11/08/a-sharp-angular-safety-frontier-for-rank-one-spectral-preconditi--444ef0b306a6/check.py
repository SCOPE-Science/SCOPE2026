"""Independent finite checks of analytic spiked-preconditioner identities (not an infinite proof)."""
from fractions import Fraction
from math import sqrt, isclose
import random
import numpy as np
from scipy.special import betainc, erfc
from scipy.stats import f as f_dist

random.seed(147)
rng=np.random.default_rng(147)
count=0
# exact rational matrix characteristic polynomial in two-coordinate basis.
for kap in [Fraction(3,2),Fraction(2),Fraction(5),Fraction(17),Fraction(101)]:
    for w in [Fraction(j,10) for j in range(1,10)]:
        for p in [Fraction(1,12),Fraction(1,3),Fraction(1,2),Fraction(3,4),Fraction(1)]:
            # In basis {u,z}, v=(sqrt(w),sqrt(1-w)), determinant/traces calculated algebraically.
            T=kap+p+(p-1)*(kap-1)*w
            # trace of PA from H=diag(kap,1) and P=I+(p-1)vvT
            direct = kap*(1+(p-1)*w)+1+(p-1)*(1-w)
            assert T==direct
            assert T*T>=4*kap*p
            # characteristic polynomial roots are >=? use numeric for crossing
            lo=(float(T)-sqrt(float(T*T-4*kap*p)))/2
            hi=(float(T)+sqrt(float(T*T-4*kap*p)))/2
            assert lo<=1+1e-10 and hi>=1-1e-10
            count+=1
# numeric real matrix, several random dimensions
for n in [2,3,5,10]:
  for _ in range(500):
    kap=float(np.exp(rng.uniform(.01,7)))
    u=rng.standard_normal(n);u/=np.linalg.norm(u)
    v=rng.standard_normal(n);v/=np.linalg.norm(v)
    w=float((u@v)**2);p=float(np.exp(rng.uniform(-10,0)))
    H=np.eye(n)+(kap-1)*np.outer(u,u)
    S=np.eye(n)+(sqrt(p)-1)*np.outer(v,v)
    eigen=np.linalg.eigvalsh(S@H@S)
    T=kap+p+(p-1)*(kap-1)*w
    lo=(T-np.sqrt(max(0,T*T-4*kap*p)))/2
    hi=(T+np.sqrt(max(0,T*T-4*kap*p)))/2
    assert np.isclose(eigen[0],lo,rtol=1e-6,atol=1e-8)
    assert np.isclose(eigen[-1],hi,rtol=1e-6,atol=1e-8)
    pc=(kap-(kap-1)*w)/(1+(kap-1)*w)
    best=min(1,pc)
    def cond(p):
      t=kap+p+(p-1)*(kap-1)*w
      discr=max(0,t*t-4*kap*p)
      return (t+sqrt(discr))**2/(4*kap*p)
    grid=np.linspace(.01,1,1000)
    assert cond(best) <= min(cond(x) for x in grid)+1e-6
    if w<=.5:
      assert isclose(cond(best),kap,rel_tol=1e-8)
    else:assert cond(best)<kap+1e-7
    count+=1
# numeric distribution tests q=0,1,2 and Gaussian exact distribution
for n,k,q in [(3,2,0),(4,2,1),(7,4,1),(16,3,2),(32,3,1)]:
    g=rng.normal(size=(150000,n))
    data=(k**(2*q))*g[:,0]**2 > np.sum(g[:,1:]**2,axis=1)
    exact=float(f_dist.sf((n-1)/(k**(2*q)),1,n-1))
    assert abs(data.mean()-exact)<.007, (n,k,q,data.mean(),exact)
    count+=1
# q=0 isotropic special + high-dimensional tail
for n in [3,5,12,50]:
    exact=float(1-betainc(.5,(n-1)/2,.5))
    other=float(f_dist.sf(n-1,1,n-1))
    assert abs(exact-other)<1e-13
    count+=1
print('VERIFY_OK',count,'exact-rational/numeric configurations, 5 Gaussian distribution checks')
# fixed nominal inverse-scale safety frontier and optimized closed form
for kap in [1.1, 2., 4., 16., 100., 1.e4]:
    r=sqrt(kap)
    threshold=1-r/(1+r)**2
    for w in np.linspace(0,1,101):
        p=1/kap
        T=kap+p+(p-1)*(kap-1)*w
        eigen_hi=(T+sqrt(max(0,T*T-4*kap*p)))/2
        eigen_lo=kap*p/eigen_hi
        better=eigen_hi/eigen_lo < kap-1e-9
        if abs(w-threshold)>1e-6:
            assert better==(w>threshold), (kap,w,threshold,eigen_hi/eigen_lo)
        if w>.5:
            t=(kap-1)**2/kap*w*(1-w)
            opt=(sqrt(1+t)+sqrt(t))**2
            best=(kap-(kap-1)*w)/(1+(kap-1)*w)
            s=kap+best+(best-1)*(kap-1)*w
            numerical=(s+sqrt(max(0,s*s-4*kap*best)))**2/(4*kap*best)
            assert isclose(numerical,opt,rel_tol=5e-9,abs_tol=1e-7)
# inverse scaling exact probability re-expressed through Gaussian F distribution
for n,k,q in [(3,2,0),(6,5,1),(22,10,2)]:
    r=sqrt(k)
    w0=1-r/(1+r)**2
    threshold=(n-1)*w0/(1-w0)/(k**(2*q))
    assert isclose(float(f_dist.sf(threshold,1,n-1)),
      float(f_dist.sf((n-1)*(r+1+1/r)/(k**(2*q)),1,n-1)),rel_tol=1e-12)
print('VERIFY_FIXED_SCALE_AND_OPTIMAL_FORMULA_OK')
