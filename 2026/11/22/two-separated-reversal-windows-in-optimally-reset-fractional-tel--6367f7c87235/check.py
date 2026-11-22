#!/usr/bin/env python3
"""Independent numerical checks for fractional-telegrapher optimized search comparisons."""
import math
from scipy.optimize import brentq

def h(kind,x,mu):
    return x**(mu/2)*math.sqrt(1+x**(mu if kind=='I' else 1))
def eta(kind,x,mu):
    w=x**(mu if kind=='I' else 1)
    return (mu/2)+((mu if kind=='I' else 1)/2)*w/(1+w)
def phi(z):
    return z/(-math.expm1(-z)) if z>1e-8 else 1+z/2+z*z/12
def zeta(q):
    return brentq(lambda z:q*phi(z)-1,1e-12,200,xtol=1e-13)
def optimum(kind,a,mu):
    fun=lambda lx:eta(kind,math.exp(lx),mu)*phi(a*h(kind,math.exp(lx),mu))-1
    lx=brentq(fun,-100,100,xtol=1e-12)
    x=math.exp(lx)
    return x, math.expm1(a*h(kind,x,mu))/x

def tests():
    n=0
    for mu in (.2,.4,.5,.7,.9):
        b1=zeta(3*mu/4)/math.sqrt(2)
        b2=zeta((2*mu+1)/4)/math.sqrt(2)
        xe=brentq(lambda x:mu*x**(mu-1)-1-(1-mu)*x**mu,1e-12,1)
        be=zeta(eta('I',xe,mu))/h('I',xe,mu)
        assert 0<b2<b1<be;n+=1
        for a in (b2*.1,b2,b2*.7+b1*.3,(b1+b2)/2,b1,b1*1.05,(b1+be)/2,be,be*1.5,be*10):
            x1,m1=optimum('I',a,mu)
            x2,m2=optimum('II',a,mu)
            assert abs(eta('I',x1,mu)*phi(a*h('I',x1,mu))-1)<5e-10;n+=1
            assert abs(eta('II',x2,mu)*phi(a*h('II',x2,mu))-1)<5e-10;n+=1
            if a<=b2+1e-10:assert m1<m2;n+=1
            if a>=b1-1e-10:assert m1>m2;n+=1
            if a<=b1+1e-10:assert x1>x2;n+=1
            if a>=be-1e-10:assert x1<x2;n+=1
        a_cost=brentq(lambda a:math.log(optimum('I',a,mu)[1]/optimum('II',a,mu)[1]),b2,b1)
        a_rate=brentq(lambda a:math.log(optimum('I',a,mu)[0]/optimum('II',a,mu)[0]),b1,be)
        assert b2<a_cost<b1<a_rate<be;n+=1
        if mu==.5:
            print('mu',mu,'b2',b2,'cost_cross',a_cost,'b1',b1,'rate_cross',a_rate,'be',be,'xe',xe)
        z=zeta(mu/2)
        for a in (1000,10000):
            x1,m1=optimum('I',a,mu)
            x2,m2=optimum('II',a,mu)
            x0=(z/a)**(2/mu)
            assert x1<x2;n+=1
            predicted=(math.exp(z)*z/2)*(x0**(mu-1))
            relative=(m1-m2)/predicted
            assert relative>0 and relative<2;n+=1
            print(f'mu={mu} a={a} far_relative={relative:.4f} x1/x0={x1/x0:.5f}')
        zI=zeta(mu); zII=zeta((mu+1)/2)
        a=1e-6
        x1,m1=optimum('I',a,mu)
        x2,m2=optimum('II',a,mu)
        assert x1>x2 and m1<m2;n+=1
        assert .80<x1/(zI/a)**(1/mu)<1.2;n+=1
        assert .80<x2/(zII/a)**(2/(1+mu))<1.2;n+=1
    print('PASS',n,'checks')

if __name__=='__main__':tests()
