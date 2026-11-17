"""Exact moment and stochastic checks for two-block cubical free sums.
Scientific reproducibility only; no external services.
"""
from fractions import Fraction as Q
import math
import numpy as np

def rising(a,k):
    v=1
    for t in range(k):v*=a+t
    return v

def formula(p,q):
    N=p+q
    d2=rising(N+1,2); d4=rising(N+1,4)
    A=lambda n: Q(n+2,3)
    B=lambda n: A(n)**2+Q(4*(n-1),45)
    Et2=lambda n: Q(rising(n,2),d2)
    Et4=lambda n: Q(rising(n,4),d4)
    Et2t2=Q(rising(p,2)*rising(q,2),d4)
    ER2=A(p)*Et2(p)+A(q)*Et2(q)
    ER4=B(p)*Et4(p)+B(q)*Et4(q)+2*A(p)*A(q)*Et2t2
    mean=ER2/N
    var=(ER4-ER2**2)/N**2
    ec2 = (A(p)**2)*Et4(p)+(A(q)**2)*Et4(q)+2*A(p)*A(q)*Et2t2
    varc=(ec2-ER2**2)/N**2
    return mean,var,varc

# independent polynomial beta-integration for each sign/max-face cone, direct simplex monomial integrals
# For group with n coords and shell radius t, dimension n: mean squared radius on shell
# equals t^2*(n+2)/3, square mean equals t^4*((n+2)^2/9+4*(n-1)/45).

def sample(p,q,size,seed):
    rng=np.random.default_rng(seed)
    N=p+q
    z=rng.gamma(shape=np.array([p,q,1]),scale=1.,size=(size,3))
    z/=z.sum(axis=1)[:,None]
    t,u=z[:,0],z[:,1]
    e=np.ones((size,p));f=np.ones((size,q))
    if p>1:e[:,1:]=rng.uniform(-1,1,(size,p-1))
    if q>1:f[:,1:]=rng.uniform(-1,1,(size,q-1))
    R=(t*t*(e*e).sum(axis=1)+u*u*(f*f).sum(axis=1))/N
    C=((p+2)*t*t+(q+2)*u*u)/(3*N)
    return R,C

if __name__=='__main__':
    checks=0
    for p in range(1,9):
      for q in range(1,9):
        mean,var,varc=formula(p,q)
        assert mean>0 and var>0 and varc>0
        N=p+q
        assert mean == Q(p*(p+1)*(p+2)+q*(q+1)*(q+2),3*N*(N+1)*(N+2))
        checks+=4
    for p,q in [(2,3),(5,5),(10,30),(120,120),(80,240)]:
      mean,var,varc=map(float,formula(p,q))
      values,cond=sample(p,q,80000,seed=42+p*17+q)
      # sigma deviations within 6 standard errors (always generous stochastic diagnostic)
      assert abs(values.mean()-mean)<6*math.sqrt(var/len(values))
      assert abs(values.var()-var)<0.07*var
      assert abs(cond.var()-varc)<0.09*varc
      checks+=3
    for p,q in [(200,200),(200,600)]:
      N=p+q; a=p/N;b=q/N
      vtarget=4/45*(1-15*a*a*b*b)
      _,v,_=map(float,formula(p,q))
      assert abs(N*v-vtarget)<0.01
      checks+=1
    for n in [30,100,300]:
      N=2*n
      *_,vc=map(float,formula(n,n))
      assert abs(N*N*vc-1/24)<0.03
      checks+=1
    print('PASS',checks,'exact/statistical assertions')
    for p,q in [(3,4),(20,20),(100,300)]:
      print(p,q,'mean, Nvar, N²var(C)',*(float(x) for x in formula(p,q)))
