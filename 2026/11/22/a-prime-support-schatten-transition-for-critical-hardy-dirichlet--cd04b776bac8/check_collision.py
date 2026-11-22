from math import comb, sqrt, pi, log, exp, lgamma
import numpy as np

def collision(n,theta):
    if len(theta)==2:
        u,v=theta
        return sum((comb(n,k)*u**k*v**(n-k))**2 for k in range(n+1))
    if len(theta)==3:
        u,v,w=theta
        return sum((comb(n,a)*comb(n-a,b)*u**a*v**b*w**(n-a-b))**2 for a in range(n+1) for b in range(n-a+1))

def hdiag(n):return comb(2*n,n)/4**n
for theta in ((.3,.7),(.5,.5),(.2,.3,.5)):
    r=len(theta)
    coeff= (4*pi)**(-(r-1)/2)/sqrt(np.prod(theta))
    for n in (12,36,80):
        c=collision(n,theta)
        ratio=c*n**((r-1)/2)/coeff
        print('r',r,'n',n,'asymptotic ratio',ratio,'trace diag',c*hdiag(n))
        assert .95<ratio<1.08 if n>=36 else .85<ratio<1.1
for theta in ((.5,.5),(.3,.7)):
    N=40
    cs=np.array([sqrt(collision(n,theta)) for n in range(N)])
    H=np.array([[comb(n+m,n)/2.**(n+m) for m in range(N)] for n in range(N)])
    B=cs[:,None]*H*cs[None,:]
    lam=np.linalg.eigvalsh(B)
    assert min(lam)>-1e-12
    assert all(np.diff(lam)>=-1e-12)
    print('eigen-max:',lam[-1], 'trace',sum(lam), 'trace-formula',sum(cs**2*np.diag(H)))
print('ALL CHECKS PASSED')
