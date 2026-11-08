import numpy as np
from scipy.integrate import quad
from scipy.special import gammaln, betainc
from math import sqrt, pi, exp

def c(n):
    return exp(gammaln(n/2)-gammaln((n-1)/2)-0.5*np.log(pi))

def p_integral(d):
    c_d, c_w = c(d), c(d-1)
    def inner(u,w):
        z = (u*w)**2/(1+(u*w)**2)
        return 0.5*betainc(0.5,(d-1)/2,z)
    def outer(t):
        u = np.tan(t)
        return c_d*np.cos(t)**(d-2)*quad(lambda w:c_w*(1-w*w)**((d-4)/2)*inner(u,w),0,1,epsabs=1e-10)[0]
    return 0.125 - 2*quad(outer,0,pi/2,epsabs=1e-8)[0]

DIMENSIONS=[3,4,5,8,16,32,64,128,256]
p = {d:p_integral(d) for d in DIMENSIONS}
assert abs(p[3]-(1/(2*pi)-1/8))<1e-9
for d,value in p.items():
    assert 0<value<.125
    if d>=5:
        lead=2*c(d)**2*c(d-1)/(d-2)**2
        defect=.125-value
        assert lead*(1-2/(3*(d-4)))-1e-8 <= defect <= lead+1e-8
assert abs(sqrt(256)*(.125-p[256])-1/(sqrt(2)*pi**1.5))<0.001

# Independently sample points in R^d and normalize; check exact tangent signs.
rng=np.random.default_rng(41)
for d in [3,5,16,128]:
    n=450000
    hits=0
    for _ in range(n//9000):
        x=rng.normal(size=(9000,3,d))
        x/=np.linalg.norm(x,axis=-1,keepdims=True)
        a=np.einsum('ij,ij->i',x[:,0,:],x[:,1,:])
        b=np.einsum('ij,ij->i',x[:,0,:],x[:,2,:])
        z=np.einsum('ij,ij->i',x[:,1,:],x[:,2,:])
        hits+=np.count_nonzero((z>a*b)&(b>a*z)&(a>b*z))
    observed=hits/n
    # Conservatively allow >8 standard deviations of sampling uncertainty.
    tolerance=8*sqrt(p[d]*(1-p[d])/n)+0.0005
    assert abs(observed-p[d])<tolerance,(d,observed,p[d])
    print('dimension',d,'integral',p[d],'direct_MC',observed)
print('ACUTE_SPHERICAL_ALL_DIMENSION_FORMULA_CHECK_OK')
