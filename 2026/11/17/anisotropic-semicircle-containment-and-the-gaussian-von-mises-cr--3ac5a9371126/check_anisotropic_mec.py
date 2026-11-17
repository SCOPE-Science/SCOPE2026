"""Numerical diagnostics for anisotropic circular sample enclosing disks.
This code is supplementary: finite computation does not prove limit laws.
Requires numpy, scipy.
"""
import math
from math import pi
import numpy as np
from scipy.integrate import quad
from scipy.special import i0
from scipy.stats import norm, kstest


def exact_probability(n, eta):
    b = 2*eta/pi
    # finite positive sum uses no quadrature
    s = sum(math.comb(n-1, 2*k)*math.comb(2*k,k)/4**k * b**(2*k)
            for k in range((n-1)//2+1))
    return n*2.0**(1-n)*s


def quadrature_probability(n, eta):
    b=2*eta/pi
    v=quad(lambda t:(1-b*math.sin(t))**(n-1)/(2*pi),0,2*pi,epsabs=1e-11)[0]
    return n*2.0**(1-n)*v


def simulate_conditional(n,eta,nrep,seed):
    rng=np.random.default_rng(seed)
    b=2*eta/pi; pmax=.5+eta/pi
    # pivot distribution: proportional to f(theta) p(theta)^(n-1)
    # rejection from uniform angle envelope (1+eta) pmax^(n-1)
    pivots=[]
    while len(pivots)<nrep:
        theta=rng.uniform(0,2*pi,size=max(nrep//2,2000))
        p=.5-eta*np.sin(theta)/pi
        keep=rng.random(len(theta)) < (1+eta*np.cos(theta))/(1+eta)*(p/pmax)**(n-1)
        pivots.extend(theta[keep].tolist())
    theta=np.array(pivots[:nrep]);
    # exact endpoint-gap law by inverse of semicircle conditional mass:
    # q(s) = integral_(theta+pi-s)^(theta+pi) f(phi)dphi
    #      = s/(2pi) + eta/(2pi)*(sin(theta+pi)-sin(theta+pi-s)).
    # q(s) = p(theta) * (1 - U^(1/(n-1)))
    p=.5-eta*np.sin(theta)/pi
    u=rng.random(nrep)
    target=p*(-np.expm1(np.log(u)/(n-1)))
    lo=np.zeros(nrep); hi=np.full(nrep,pi)
    for _ in range(45):
        mid=(lo+hi)/2
        q=(mid + eta*(-np.sin(theta)+np.sin(theta-mid)))/(2*pi)
        lo=np.where(q<target,mid,lo)
        hi=np.where(q>=target,mid,hi)
    s=(lo+hi)/2
    # MEC radius and center for endpoints subtending pi-s
    radius=np.cos(s/2)
    center=np.column_stack((np.sin(s/2)*np.cos(theta+pi/2-s/2),
                            np.sin(s/2)*np.sin(theta+pi/2-s/2)))
    return theta,s,radius,center


def test():
    for n,eta in [(3,.4),(4,.8),(8,.1),(12,.4),(30,.35),(90,.6)]:
        p=exact_probability(n,eta); q=quadrature_probability(n,eta)
        assert abs(p-q)<1e-10, (n,eta,p,q)
    print('exact polynomial matches integral: 6 cases')
    for eta in [.2,.5,.8]:
        n=250
        b=2*eta/pi
        approx=math.sqrt(n*(1+b)/(2*pi*b))*((1+b)/2)**(n-1)
        p=exact_probability(n,eta)
        print('fixed-shape Laplace ratio:',eta,p/approx)
        assert .95<p/approx<1.05
    for lam in [0.,1.,3.]:
        n=400; eta=lam/n
        ratio=exact_probability(n,eta)/(n*2.0**(1-n))
        target=i0(2*lam/pi)
        print('critical crossover ratio:',lam,ratio/target)
        assert abs(ratio/target-1)<.012
    for n,eta in [(60,.4),(140,2/140),(140,0.)]:
        th,s,r,C=simulate_conditional(n,eta,30000,11+int(n*eta))
        if eta==.4:
            E=n*s/(pi+2*eta)
            X=((th+pi/2+pi)%(2*pi)-pi)*math.sqrt(n*(2*eta/pi)/(1+2*eta/pi))
            print('fixed-marked',np.mean(E),np.mean(X),np.std(X),kstest(E,'expon').statistic,kstest(X,'norm').statistic)
            assert abs(np.mean(E)-1)<.06
            assert abs(np.mean(X))<.16
            assert abs(np.std(X)-1)<.09
            assert kstest(E,'expon').statistic<.035
        else:
            lam=n*eta
            E=n*s/pi
            actual=np.mean(np.sin(th))
            pred=quad(lambda t:np.sin(t)*np.exp(-2*lam*np.sin(t)/pi),0,2*pi)[0]/(2*pi*i0(2*lam/pi))
            print('critical-marked',lam,np.mean(E),actual,pred,kstest(E,'expon').statistic)
            assert abs(np.mean(E)-1)<.06
            assert abs(actual-pred)<.05
            assert kstest(E,'expon').statistic<.035
    print('ANISOTROPIC_MEC_WINDOW_CHECK_OK')

if __name__=='__main__':
    test()
