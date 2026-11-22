"""Independent numerical checks for the finite-size polar-fluctuation theorem."""
import math
from itertools import product
import numpy as np
from scipy.integrate import quad
from scipy.special import i0e,i1e


def mean_nematic_sq(n, c):
    # Exact Gaussian decoupling of fully-connected planar XY Gibbs law.
    scale=n**0.25
    def log_i0(x): return math.log(i0e(x))+x
    def mu(x): return i1e(x)/i0e(x)
    def kernel(u):
        r=u/scale
        return u*math.exp(n*(log_i0(r)-r*r/(2*c)))
    # At critical c_N these tails are dominated by exp(-u^4/64).
    z=quad(kernel,0,14,epsabs=1e-11,epsrel=1e-11,limit=200)[0]
    m2=quad(lambda u: kernel(u)*mu(u/scale)**2,0,14,
            epsabs=1e-11,epsrel=1e-11,limit=200)[0]/z
    return 1/n+(1-1/n)*m2

def checks():
    for n in range(3,9):
        for j in range(5):
            phi = 0.17+np.arange(n)*0.93 + j*.24*np.arange(n)**2
            b = np.exp(.5j*phi)
            vals=[]; vals2=[]
            for signs in product((-1,1),repeat=n):
                p=np.dot(np.array(signs),b)/math.sqrt(n)
                vals.append(abs(p)**4)
                vals2.append(p*p)
            m=np.exp(1j*phi).mean()
            assert np.isclose(np.mean(vals),2+abs(m)**2-2/n,rtol=2e-12,atol=2e-12)
            assert np.isclose(np.mean(vals2),m,rtol=2e-12,atol=2e-12)
    target=2/math.sqrt(math.pi)
    values=[]
    for n in (64,256,1024,4096):
        c=2*(n-2)/n
        m2=mean_nematic_sq(n,c)
        values.append(math.sqrt(n)*m2)
    assert abs(values[-1]-target)<0.09,(values,target)
    assert all(values[k]<values[k+1] for k in range(3)),(values,target)
    print('finite-sign fourth moment and mixed second moment: 30 tests passed')
    print('critical sqrt(N)*E|m_N|²:',[(n,round(v,8)) for n,v in zip((64,256,1024,4096),values)])
    print('theoretical limit 2/sqrt(pi):',target)
    # The one-component excess kurtosis of the limiting distribution is 3*rho^2/2.
    for rho in (.01,.25,.65,.99):
        t=1.8
        # Integral over the uniform director of anisotropic Gaussian characteristic function.
        from scipy.special import i0
        vals=[math.exp(-t*t*(1+rho*math.cos(a))/4)
              for a in np.linspace(0,2*math.pi,10001)[:-1]]
        exact=math.exp(-t*t/4)*i0(rho*t*t/4)
        assert abs(np.mean(vals)-exact)<1e-12
    print('Gaussian-mixture directional characteristic functions: 4 tests passed')

if __name__=='__main__':checks()
