"""Independent numerical consistency checks for an explicit two-cost diffusion frontier.
Python 3, standard library only. Finite tests do not prove the continuous claim.
"""
from math import sqrt, log, sin, pi
from fractions import Fraction


def simpson(f, n=12000):
    assert n % 2 == 0
    return (f(0.) + f(1.) + sum((4 if k%2 else 2)*f(k/n) for k in range(1,n)))/(3*n)


def profile(r):
    assert r > 1.
    h = r**4-r
    d = 3*r/(2*r**3+1)
    def u(x):
        target = (1-x)*h
        lo,hi=1.,r
        for _ in range(54):
            mid=(lo+hi)/2
            if mid**4-mid < target:lo=mid
            else:hi=mid
        return (lo+hi)/2
    def D(x):return d*u(x)**2
    f=(4*(r**3-1)/3-log(r))/(h*sqrt(d))
    m=((2*r**6-5*r**3+3)/3+log(r))/(d*h*h)
    lam=2/(sqrt(d)*h)
    mu=lam/(2*d**1.5)
    return D,f,m,lam,mu


def endpoint_laplace(discount):
    """Exact singular-endpoint transform as reciprocal 0F1(;2/3;8s/27)."""
    z=8*discount/27
    term=1.
    total=term
    for k in range(1,150):
        term*=z/(k*(k-1+2/3))
        total+=term
        if abs(term)<1e-16*total:break
    return 1./total


def main():
    checks=0
    def near(x,y,tol=1e-6):
        nonlocal checks
        assert abs(x-y)<tol, (x,y)
        checks+=1
    assert Fraction(2,3)**2 == Fraction(4,9)
    assert Fraction(4,3)**2 * Fraction(2,3) == Fraction(32,27)
    checks+=2
    for s in (1e-5,1e-4,1e-3):
        # Expansion: E T=4/9 and E T^2=128/405.
        near(endpoint_laplace(s),1-4*s/9+64*s*s/405,2e-9)
    near(endpoint_laplace(1.),0.6731995082652709,2e-12)
    last_f,last_m=1.,.5
    for r in (1.01,1.06,1.2,1.5,2.,3.,5.,10.,30.):
        D,f,m,lam,mu=profile(r)
        near(D(1),3*r/(2*r**3+1))
        h=r**4-r;d=3*r/(2*r**3+1)
        def sint(g):
            return (r-1)*simpson(lambda x:g(1+(r-1)*x))
        near(sint(lambda u:d*u*u*(4*u**3-1)/h),1.)
        near(sint(lambda u:(4*u**3-1)/(u*h*sqrt(d))),f)
        near(sint(lambda u:((u**4-u)*(4*u**3-1))/(d*h*h*u*u)),m)
        if r<=3:
            near(simpson(D,24000),1.)
            near(simpson(lambda x:1/sqrt(D(x)),24000),f,3e-6)
            near(simpson(lambda x:(1-x)/D(x),24000),m)
        assert last_f<f and m<last_m
        checks+=1
        last_f,last_m=f,m
        for x in (.01,.05,.2,.4,.6,.8,.95,.99):
            value=D(x)
            near((1-x)/value**2+lam/(2*value**1.5),mu,3e-9)
        for amp in (.05,.2,.35,.5):
            comp=lambda x:1+amp*sin(2*pi*x)
            score=simpson(lambda x: (1-x)/comp(x)+lam/sqrt(comp(x)))
            assert score>=m+lam*f-1e-7
            checks+=1
    print('PASS:',checks,'deterministic formula, stationarity, ordering and competitor checks')

if __name__ == '__main__':main()
