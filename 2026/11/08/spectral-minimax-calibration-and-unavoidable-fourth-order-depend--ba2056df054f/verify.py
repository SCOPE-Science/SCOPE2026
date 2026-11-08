"""Standalone rational-recursion checks for random-order OU splitting.
All functions are plain mathematical checks, not formal proof of infinite claims.
Run with python verify.py (standard library only).
"""
from fractions import Fraction as F
import math

count=0

def check(a,b,label):
    global count
    count+=1
    if a != b:
        raise AssertionError(f'{label}: {a} != {b}')

for h in [F(1,7),F(2,3),F(3,2)]:
  for p in [F(0),F(1,9),F(1,3),F(1,2),F(3,4),F(1)]:
    for ri in [F(1,6),F(1,3),F(2,3),F(4,5)]:
      ai=ri**2
      qi=2*h*(p+(1-p)*ai)
      qi2=(2*h)**2*(p+(1-p)*ai**2)
      mi=qi/(1-ai)
      closed_mi=2*h*(p+ai/(1-ai))
      check(mi,closed_mi,'scalar variance')
      m4=(6*ai*qi*mi+3*qi2)/(1-ai**2)
      kappa=m4-3*mi**2
      closed_kappa=3*(2*h)**2*p*(1-p)*(1-ai)**2/(1-ai**2)
      check(kappa,closed_kappa,'fourth cumulant')
      for rj in [F(1,8),F(2,5),F(3,4)]:
        aj=rj**2
        qj=2*h*(p+(1-p)*aj)
        mj=qj/(1-aj)
        qij=(2*h)**2*(p+(1-p)*ai*aj)
        m22=(ai*qj*mi +aj*qi*mj + qij)/(1-ai*aj)
        cross=m22-mi*mj
        closed_cross=(2*h)**2*p*(1-p)*(1-ai)*(1-aj)/(1-ai*aj)
        check(cross,closed_cross,'cross-square covariance')

# Numerical sanity check for the spectral minimax rule, not a proof.
for h in [0.01,0.1,0.4,1.0,2.0]:
    for lo,hi in [(0.3,1.0),(0.5,2.0),(1.0,10.0),(1.0,1.0)]:
        def f(t):
            return 1/(2*t)-1/math.expm1(2*t)
        fmax,fmin=f(h*lo),f(h*hi)
        pstar=(fmax+fmin)/2
        optimal=h*(fmax-fmin)
        assert 0 < pstar < 0.5
        for j in range(1001):
            p=j/1000
            error=2*h*max(abs(p-fmax),abs(p-fmin))
            assert error >= optimal-1e-12, (h,lo,hi,p)
        assert abs(2*h*max(abs(pstar-fmax),abs(pstar-fmin))-optimal)<1e-12
        count+=1003

# Exact one-step conditional fourth moment against three-step tree enumeration,
# with the geometric tail treated analytically via a deterministic quadratic recursion.
for a in [F(1,4),F(3,7)]:
    p=F(2,5);h=F(1,3)
    mean=2*h*(p+a/(1-a))
    var_v=(2*h)**2*p*(1-p)*(1-a)**2/(1-a*a)
    for K in range(1,6):
        # Random finite prefix of the stationary conditional variance.
        base=2*h*a/(1-a)
        vs=[]
        for mask in range(1<<K):
            prob=F(1)
            s=base
            for k in range(K):
                bit=(mask>>k)&1
                prob*=p if bit else 1-p
                s+=2*h*(1-a)*a**k*bit
            vs.append((s,prob))
        em=sum((v*prob for v,prob in vs),F(0))
        ev2=sum((v*v*prob for v,prob in vs),F(0))
        finite_var=ev2-em*em
        formula=(2*h)**2*p*(1-p)*(1-a)**2*(1-a**(2*K))/(1-a*a)
        check(finite_var,formula,'finite-prefix variance')
        check(em,base+2*h*p*(1-a**K),'finite-prefix mean')
        check(var_v-finite_var,var_v*a**(2*K),'exact tail variance')

print(f'PASS: {count} checks (exact rational recursion, moments, finite-prefix identities and numerical minimax grid).')
