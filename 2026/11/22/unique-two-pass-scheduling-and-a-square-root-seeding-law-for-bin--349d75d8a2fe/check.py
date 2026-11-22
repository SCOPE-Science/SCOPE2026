import numpy as np,itertools,math

def idist(lam,d):
 r=lam**d
 return .5*((1+r)*math.log1p(r)+(1-r)*math.log1p(-r))
def predicted(lam,p,L):
 z=1-p; I=lambda d:idist(lam,d); i1=I(1)
 C=lambda ell:(ell+1)*i1-2*sum(I(k) for k in range(1,ell+1))+(ell-1)*I(ell+1)
 Ce=lambda ell:ell*i1-sum(I(k) for k in range(1,ell+1))
 return sum((L-d)*p*p*z**(d-1)*I(d) for d in range(1,L))+sum((L-e-1)*p*p*z**e*C(e) for e in range(1,L-1))+2*p*sum(z**e*Ce(e) for e in range(1,L))+z**L*(L-1)*i1

def enumerated(lam,p,L):
 states=list(itertools.product((-1,1),repeat=L));partitions=list(itertools.product((0,1),repeat=L)); f=(1-lam)/2
 dist={s:.5*math.prod((1-f) if s[i]==s[i+1] else f for i in range(L-1)) for s in states}
 ans=0
 for bits in partitions:
  prior=tuple(i for i,b in enumerate(bits) if b);late=tuple(i for i,b in enumerate(bits) if not b)
  qmask=p**len(prior)*(1-p)**len(late)
  joint_cond={}; marg={}
  for state in states:
   denom=sum(v for st,v in dist.items() if all(st[i]==state[i] for i in prior))
   for i in late:
    num=sum(v for st,v in dist.items() if all(st[k]==state[k] for k in prior) and st[i]==state[i])
    marg[(state,i)]=num/denom
  for state,w in dist.items():
   q=math.prod(.5 for i in prior)*math.prod(marg[(state,i)] for i in late)
   ans+=qmask*w*math.log(w/q)
 return ans
for L in [2,3,4,5,6]:
 for lam,p in [(.6,.4),(.2,.2),(.9,.13)]:
  a=predicted(lam,p,L);b=enumerated(lam,p,L)
  print(L,lam,p,a,b,a-b)
  assert abs(a-b)<1e-9
from scipy.optimize import brentq

def spectral(lam,p,n=25000):
    import numpy as np
    k=np.arange(1,n+1,dtype=float)
    t=np.exp(2*k*math.log(lam)); a=1/(2*k*(2*k-1)); z=1-p; q=1-z*t
    b=1-2*p*z/q+p*p*z*t/q**2
    db=(p**3*t**2 - 3*p**2*t**2 + 3*p**2*t+4*p*t**2-8*p*t+4*p-2*t**2+4*t-2)/q**3
    ddb=2*(1-t)**2*(2+t-p*t)/q**4
    return float(np.sum(a*t*b)),float(np.sum(a*t*db)),float(np.sum(a*t*ddb))
for lam in (.1,.3,.8,.95,.99):
    for p in (.05,.2,.5,.75):
        v,d,d2=spectral(lam,p)
        assert d2>0
        eps=1e-5
        dv=(spectral(lam,p+eps)[0]-spectral(lam,p-eps)[0])/(2*eps)
        assert abs(d-dv)<1e-6
    r=brentq(lambda q:spectral(lam,q)[1],.00001,.5)
    assert 0<r<.5
for delta in (1e-4,1e-5,1e-6):
    r=brentq(lambda q:spectral(1-delta,q)[1],1e-8,.4)
    ratio=r/math.sqrt(delta/(2*math.log(2)))
    assert abs(ratio-1)<.15
    print('delta',delta,'root',r,'sqrt-law-ratio',ratio)
print('all analytical-numerical consistency tests passed')
