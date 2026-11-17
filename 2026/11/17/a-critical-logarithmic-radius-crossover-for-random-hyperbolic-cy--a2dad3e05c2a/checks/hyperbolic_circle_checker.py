"""Independent numerical diagnostics for hyperbolic random inscribed polygon area.
Use: python hyperbolic_circle_checker.py. Requires numpy and scipy.
"""
import numpy as np
from scipy.integrate import quad
from math import pi


def limit_stats(lam):
    c=2*pi/lam
    f=lambda x: 2*np.arctan(c*x)
    df=lambda x:2*c/(1+(c*x)**2)
    I=lambda fun:quad(lambda x: np.exp(-x)*fun(x),0,np.inf,epsabs=1e-11)[0]
    mu=I(f); a=I(lambda x:x*df(x))
    var=I(lambda x:(f(x)-a*x)**2)-(mu-a)**2
    return mu,a,var

def finite_mean(n,lam):
    r=1-lam/n
    fun=lambda x: 2*np.arctan2(r*np.sin(2*pi*x/n),1-r*np.cos(2*pi*x/n))*(n-1)/n*(1-x/n)**(n-2)
    return quad(fun,0,n,epsabs=1e-10)[0]

def exact_area(exponentials,lam):
    n=exponentials.shape[-1]
    angles=2*pi*exponentials/exponentials.sum(axis=-1,keepdims=True)
    q2=1-lam/n
    return 2*np.arctan2(q2*np.sin(angles),1-q2*np.cos(angles)).sum(axis=-1)

def independent_gauss_bonnet(q2,theta):
    z=np.sqrt(q2)*np.exp(1j*np.sort(theta))
    angles=[]
    for i in range(len(z)):
        u=(z[i-1]-z[i])/(1-np.conj(z[i])*z[i-1])
        v=(z[(i+1)%len(z)]-z[i])/(1-np.conj(z[i])*z[(i+1)%len(z)])
        angles.append(np.arccos(np.clip((u.conjugate()*v).real/abs(u*v),-1,1)))
    return (len(z)-2)*pi-sum(angles)

def main():
    rng=np.random.default_rng(826781)
    for n in (3,5,8,30):
        for lam in (.1,1,2):
            if n<=lam:continue
            theta=np.sort(rng.uniform(0,2*pi,n))
            gaps=np.diff(np.r_[theta,theta[0]+2*pi]); q2=1-lam/n
            a=2*np.arctan2(q2*np.sin(gaps),1-q2*np.cos(gaps)).sum()
            b=independent_gauss_bonnet(q2,theta)
            assert abs(a-b)<1e-9, (n,lam,a,b)
    for lam in (.8,5.,20.):
        mu,a,var=limit_stats(lam)
        ratio=mu*lam/(4*pi)
        assert 0<ratio<1 and var>0
        print('lambda',lam,'mu',mu,'sigma2',var,'coverage',ratio)
        for n in (600,2400):
            m=2500
            gaps=rng.exponential(size=(m,n))
            arr=exact_area(gaps,lam)/n
            mu_n=finite_mean(n,lam)
            z=np.sqrt(n)*(arr-mu_n)/np.sqrt(var)
            print(' n',n,'mean',arr.mean(),'finite-theory',mu_n,'std of centered',np.std(z,ddof=1),'normalized bias',np.mean(z))
            assert abs(np.mean(z))<0.16 and abs(np.std(z,ddof=1)-1)<0.12
    print('HYPERBOLIC_CYCLIC_CRITICAL_AREA_CHECK_OK')
if __name__=='__main__':main()
