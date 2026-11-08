"""Independent finite-dimensional spectral, integral and sampled checks of even spherical cycle excess."""
import math
import numpy as np
from scipy.special import eval_gegenbauer, gammaln, roots_jacobi
from scipy.integrate import quad

def P(m,D,c):
    if m==0: return 1.0
    if m==1: return c
    prev,curr=1.,float(c)
    for k in range(1,m):
        nxt=((2*k+D-2)*c*curr-k*prev)/(k+D-2)
        prev,curr=curr,nxt
    return curr

def lambda1(d,c):
    return math.exp(gammaln(d/2)-gammaln((d-1)/2)-0.5*math.log(math.pi)-math.log(d-1)+(d-1)/2*math.log1p(-c*c))

def multiplicity(k,d):
    return (2*k+d-2)*math.exp(gammaln(k+d-2)-gammaln(k+1)-gammaln(d-1))

def q_spectral(d,c,r,max_degree=100):
    l1=lambda1(d,c)
    terms=[]
    for k in range(1,max_degree+1):
        terms.append(multiplicity(k,d)*(l1*P(k-1,d+2,c))**(2*r))
    return sum(terms)

def integral_eigen(d,c,k):
    cd=math.exp(gammaln(d/2)-.5*math.log(math.pi)-gammaln((d-1)/2))
    # integrate normalised Gegenbauer as zonal spherical harmonics
    a=(d-2)/2
    norm=eval_gegenbauer(k,a,1.0)
    v,_=quad(lambda x: cd*(1-x*x)**((d-3)/2)*eval_gegenbauer(k,a,x)/norm,c,1.,epsabs=1e-11,limit=300)
    return v

for d,c in [(3,0.),(4,0.25),(7,-0.15),(20,0.05)]:
    for k in range(1,8):
        a=integral_eigen(d,c,k); b=lambda1(d,c)*P(k-1,d+2,c)
        assert abs(a-b)<1e-9,(d,c,k,a,b)
    for r in [2,3]:
        total=q_spectral(d,c,r)
        leading=d*lambda1(d,c)**(2*r)
        eta2=c*c+(1-c*c)/(d+1)
        # upper uses HS norm <= 1/4 to avoid reliance on p calculation
        bound=(lambda1(d,c)**2*eta2)**(r-1)*0.25
        assert 0 <= total-leading <= bound+1e-13,(d,c,r,total,leading,bound)
        print('spectral',d,c,r,total,leading,bound)

# Monte Carlo direct four-vertex edge data, p=1/2
rng=np.random.default_rng(50321)
for d in [3,6,12]:
    total=0; N=600000; chunk=10000
    for _ in range(N//chunk):
        z=rng.normal(size=(chunk,4,d)); z/=np.linalg.norm(z,axis=2)[:,:,None]
        isall=(np.einsum('nid,nid->ni',z,np.roll(z,-1,axis=1))>=0).all(axis=1)
        total+=int(np.sum(isall))
    diff=total/N-0.5**4
    prediction=q_spectral(d,0.,2)
    stderr=math.sqrt((prediction+.0625)*(1-prediction-.0625)/N)
    assert abs(diff-prediction)<4.5*stderr,(d,diff,prediction,stderr)
    print('sample',d, N,round(diff,7),round(prediction,7),round(stderr,7))

for d in [20,50,100,300]:
    pred=q_spectral(d,0.,2,max_degree=30)
    coefficient=1/(4*math.pi**2)
    print('asymptotic',d, 'd*q4',d*pred,'limit',coefficient)
    assert abs(d*pred-coefficient)<0.15*coefficient
print('EVEN_SPHERICAL_CYCLE_EXCESS_TESTS_OK')
