"""Numerical crosschecks for two-query Brownian-bridge barrier detection.

Requires Python 3 standard library only. Numerical tests do not replace the
analytic proof of the optimization rule and the cusp derivative.
"""
from math import sqrt, exp, erfc, pi, gamma, isclose


def Phi(z):
    return 0.5*erfc(-z/sqrt(2))


def phi(z):
    return exp(-z*z/2)/sqrt(2*pi)


def integrate(f, hi, n=16000):
    assert n%2==0
    h=hi/n
    total=f(0)+f(hi)
    for j in range(1,n):
        total+=(4 if j%2 else 2)*f(j*h)
    return h*total/3


def J(c,s):
    v=s*(1-s)
    z0=-c/sqrt(v)
    k=c/max(s,1-s)
    den=1/sqrt(2*pi*v)
    def f(u):
        y=u*u
        return 2*u*den*exp(-(y-c)**2/(2*v))*Phi(-2*u*sqrt(k))
    hi=sqrt(max(8, c+9*sqrt(v)))
    return Phi(z0)+integrate(f,hi)


def conditional_detection(a,b,length,t):
    r=t/length
    assert 0<r<1
    m=a+(b-a)*r
    return Phi(-m/sqrt(length*r*(1-r)))


def run():
    count=0
    for a,b,length in [(0.1,0.7,0.4),(0.5,0.3,0.75),(3,1,2)]:
        t=length*a/(a+b)
        optimum=conditional_detection(a,b,length,t)
        formula=Phi(-2*sqrt(a*b/length))
        assert abs(optimum-formula)<1e-14
        for i in range(1,100):
            test_t=length*i/100
            assert conditional_detection(a,b,length,test_t)<=optimum+1e-13
            count+=1
    for c in (0.05, 0.2, 0.5, 1, 2):
        middle=J(c,0.5)
        h=0.0001
        right=J(c,0.5+h)
        left=J(c,0.5-h)
        slope=gamma(.75)*sqrt(c)*exp(-2*c*c)/(2**.25*pi)
        assert right>middle and left>middle
        assert abs(right-left)<2e-11
        assert abs((right-middle)/h-slope)<0.02*slope
        assert middle>Phi(-2*c)
        count+=5
    c=0.5
    improvement=J(c,1/3)-J(c,1/2)
    assert 0.0106<improvement<0.0109
    print('PASS',count,'deterministic checks; J(1/2)=',format(J(.5,.5),'.12f'),
          'J(1/3)=',format(J(.5,1/3),'.12f'),
          'slope=',format(gamma(.75)*sqrt(.5)*exp(-.5)/(2**.25*pi),'.12f'))


if __name__=='__main__':
    run()
