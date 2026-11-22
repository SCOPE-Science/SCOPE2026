"""Independent finite tests of a two-dimensional damped-Jordan orbit-frame formula.

The continuum statements are proved analytically; these are reproducibility tests,
not a proof by enumeration. Python 3 standard library only.
"""
import cmath
import math
import random


def moments(a, T):
    lam = 2.0 * a
    e = math.exp(-lam * T)
    m0 = -math.expm1(-lam * T) / lam
    m1 = (1.0 - e * (1.0 + lam * T)) / lam**2
    m2 = (2.0 - e * (2.0 + 2.0 * lam * T + (lam * T)**2)) / lam**3
    return m0, m1, m2


def rho(a, b, T):
    x = a*T
    return (b/(2*a))**2 * (1.0-(x/math.sinh(x))**2)


def analytic_gram(a, b, T, x, y):
    m0, m1, m2 = moments(a, T)
    mu = m1/m0
    var = m2/m0 - mu**2
    z = x/y + b*mu
    sc = m0*abs(y)**2
    return (sc*(abs(z)**2 + b*b*var), sc*z, sc, sc*sc*b*b*var)


def simpson_gram(a,b,T,x,y,n=1000):
    assert n%2==0
    xx=0.0; xy=0j; yy=0.0
    h=T/n
    for i in range(n+1):
        t=h*i
        weight=1 if (i==0 or i==n) else (4 if i%2 else 2)
        ex=math.exp(-a*t)
        s=ex*(x+b*t*y); r=ex*y
        xx += weight*abs(s)**2
        xy += weight*s*r.conjugate()
        yy += weight*abs(r)**2
    return h*xx/3,h*xy/3,h*yy/3


def cond(matrix):
    xx,xy,yy=matrix
    tr=xx+yy
    disc=math.sqrt((xx-yy)**2+4*abs(xy)**2)
    return (tr+disc)/(tr-disc) if tr>disc else math.inf


def main():
    random.seed(20261115)
    checks=0
    for i in range(120):
        a=random.uniform(0.25,2.0)
        b=random.uniform(0.4,5.0)
        T=random.uniform(0.45,3.0)
        x=complex(random.uniform(-2,2),random.uniform(-2,2))
        y=complex(random.uniform(-2,2),random.uniform(-2,2))
        g=analytic_gram(a,b,T,x,y)
        h=simpson_gram(a,b,T,x,y)
        for j in range(3):
            assert abs(g[j]-h[j]) < 3e-8 * max(1,abs(g[j]));checks+=1
        assert abs(g[0]*g[2]-abs(g[1])**2-g[3]) < 2e-12*max(1,g[3]);checks+=1
        m0,m1,m2=moments(a,T)
        variance=m2/m0-(m1/m0)**2
        variance_closed=(1-(a*T/math.sinh(a*T))**2)/(4*a*a)
        assert abs(variance-variance_closed) < 5e-12;checks+=1
        besty=1+0j
        bestx=-b*m1/m0
        best=analytic_gram(a,b,T,bestx,besty)
        c0=cond(best[:3]); target=max(rho(a,b,T),1/rho(a,b,T))
        assert abs(c0-target) <= 2e-10*max(1,target); checks+=1
        assert cond(g[:3]) >= c0-1e-9*max(1,c0);checks+=1
    for a,b in ((1,1),(1,2),(1,4),(0.5,2.3),(2,3)):
        vals=[rho(a,b,k/10) for k in range(1,101)]
        assert all(u<v for u,v in zip(vals,vals[1:]));checks+=1
        assert 0<vals[0]<vals[-1] < (b/(2*a))**2;checks+=1
    for a,b in ((1,3),(1,4),(0.5,1.2),(2,6)):
        lo=0.;hi=max(10/a,20/b)
        for _ in range(120):
            mid=(lo+hi)/2
            if rho(a,b,mid)<1:lo=mid
            else:hi=mid
        T=(lo+hi)/2
        assert abs(rho(a,b,T)-1) < 1e-12;checks+=1
        assert max(rho(a,b,T/2),1/rho(a,b,T/2)) >1;checks+=1
        assert max(rho(a,b,T*2),1/rho(a,b,T*2)) >1;checks+=1
    print(f'VERIFY_OK {checks} independent numerical assertions')

if __name__=='__main__':
    main()
