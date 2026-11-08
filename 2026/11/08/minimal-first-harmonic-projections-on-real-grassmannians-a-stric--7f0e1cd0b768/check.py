"""Independent numerical checks for a Grassmann first-harmonic projection asymptotic.
Diagnostic only: numerical experiments do not establish the limiting theorem.
"""
from math import gamma,pi,exp,sqrt,lgamma
import numpy as np
from scipy.integrate import quad
from scipy.special import beta

def D(n):return (n-1)*(n+2)/2

def c(k):
    s=k*k/2
    return exp(np.log(2)-np.log(k)+s*np.log(s)-s-lgamma(s))

def rank_one_closed(n):
    return 2*(n+2)/sqrt(n)*(1-1/n)**((n-1)/2)/beta(.5,(n-1)/2)

def rank_one_integral(n):
    a,b=.5,(n-1)/2
    return n*(n+2)/2*quad(lambda t:abs(t-1/n)*t**(a-1)*(1-t)**(b-1)/beta(a,b),0,1/n,epsabs=1e-10)[0]+n*(n+2)/2*quad(lambda t:abs(t-1/n)*t**(a-1)*(1-t)**(b-1)/beta(a,b),1/n,1,epsabs=1e-10)[0]

for n in range(2,22):
    r1,r2=rank_one_closed(n),rank_one_integral(n)
    assert abs(r1-r2)<2e-8,(n,r1,r2)
print('RANK_ONE_BETA_EXACT_FORMULA_NUMERIC_CHECKS_PASSED 20')

prev=0
for k in range(1,50):
    z=c(k)
    assert z>prev,(k,z,prev)
    assert z<1/sqrt(pi)
    prev=z
print('MONOTONE_GAMMA_CONSTANT_SAMPLE_CHECKS_PASSED 49')

rng=np.random.default_rng(1706)
for n,k,N in [(5,1,20000),(8,2,30000),(15,3,30000),(30,2,30000)]:
    Q=rng.normal(size=(N,n,k))
    # QR of each n-by-k normal block, Haar Stiefel frame
    # Batched QR returns orthonormal columns; diagonal signs not needed for QQ^T.
    F=np.linalg.qr(Q,mode='reduced')[0]
    Z=np.sum(F[:,:k,:]**2,axis=(1,2))*n
    K=D(n)/(k*(n-k))*(Z-k*k)
    sample_second=np.mean(K*K)
    assert abs(sample_second-D(n))/D(n)<.10,(n,k,sample_second,D(n))
    est=np.mean(np.abs(K))
    if k==1:
        assert abs(est-rank_one_closed(n))/rank_one_closed(n)<.05
    print('GRASSMANN_HAAR_CHECK n=%d k=%d norm_est=%.6f second_est=%.6f dimension=%.0f'%(n,k,est,sample_second,D(n)))
print('ALL_GRASSMANN_PROJECTION_DIAGNOSTICS_PASSED')
