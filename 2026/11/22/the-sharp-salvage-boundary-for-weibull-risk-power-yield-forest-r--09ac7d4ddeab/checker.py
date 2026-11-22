"""Reproducibility checks for a Weibull-fire renewal-harvest model."""
import math, random
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import gammainc, gamma

def model(T,p,m,eta,s):
    x=T/eta
    S=math.exp(-x**m)
    I=eta*gamma(1/m)*gammainc(1/m,x**m)/m
    J=eta**p*gamma(1+p/m)*gammainc(1+p/m,x**m)
    N=T**p*S+s*J
    g=T**(p-1)*(p-(1-s)*m*x**m)
    return N/I, I*g-N

def optimum(p,m,eta,s):
    if s==1: return float('inf')
    x_peak=(p*(p-1)/((1-s)*m*(p+m-1)))**(1/m)
    x_zero=(p/((1-s)*m))**(1/m)
    return brentq(lambda T:model(T,p,m,eta,s)[1],x_peak*eta,x_zero*eta,xtol=1e-12)

random.seed(20261115)
checks=0
for i in range(900):
    p=random.uniform(1.15,3.5)
    m=random.uniform(.8,4)
    eta=10**random.uniform(-.3,.6)
    s=random.uniform(0,.95)
    t=optimum(p,m,eta,s)
    v,h=model(t,p,m,eta,s)
    assert abs(h)<=1e-8*(1+abs(v)*eta), (p,m,eta,s,t,v,h)
    checks+=1
    a=(p*(p-1)/((1-s)*m*(p+m-1)))**(1/m)*eta
    b=(p/((1-s)*m))**(1/m)*eta
    assert a<t<b
    checks+=1
    for frac in (.2,.4,.7,.9):
        T=frac*t
        assert model(T,p,m,eta,s)[0] < v*(1+1e-10)
        checks+=1
    for fac in (1.1,1.5,2,4):
        T=fac*t
        assert model(T,p,m,eta,s)[0] < v*(1+1e-10)
        checks+=1
    # Independent quadrature on numerically well-conditioned cases.
    if t/eta<20 and m>=.7:
        S=lambda x:math.exp(-(x/eta)**m)
        numerator=t**p*S(t)+s*quad(lambda y:y**p*(m/eta)*(y/eta)**(m-1)*S(y),0,t,epsabs=1e-10)[0]
        denominator=quad(S,0,t,epsabs=1e-10)[0]
        assert abs(numerator/denominator-v)<2e-7*max(1,v), (p,m,eta,s,t,v,numerator/denominator)
        checks+=1
    s2=(s+1)/2
    assert optimum(p,m,eta,s2)>t
    checks+=1
for m in (.5,1,2,4):
    p=2.0;eta=1
    C=gamma(1+p/m)/gamma(1+1/m)
    for delta in (1e-2,1e-3,1e-4):
        t=optimum(p,m,eta,1-delta)
        x0=(p/(m*delta))**(1/m)
        # signed correction must approach C/(m*p)
        correction=(x0-t)/(x0**(2-p))
        if delta<=1e-4 and m>=1:
            assert abs(correction-C/(m*p))<.03
            checks+=1
print('checks_passed',checks)
print('example (p=2,m=2,eta=20 years)')
for s in (0,.5,.9,.99,.999,1):
    if s<1:
        t=optimum(2,2,20,s)
        print(f'salvage={s}: T*={t:.8f}yr, reward/time={model(t,2,2,20,s)[0]:.8f}')
    else:print('salvage=1: T*=infinity')
