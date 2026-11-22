"""Reproducibility checks for the repeated-complex-pole subnormality threshold.
Uses only Python 3 standard library. Finite tests do not replace the proof.
"""
from fractions import Fraction
from math import cos, sin, exp, sqrt, pi, isclose

def P(n, a, b, c):
    return (n+a)*((n+b)**2+c*c)**2 / (a*(b*b+c*c)**2)

def g(z):
    return sin(z)-z*cos(z)

def bisect(fn, lo, hi, n=100):
    vlo = fn(lo)
    assert vlo * fn(hi) < 0, (lo, hi, vlo, fn(hi))
    for _ in range(n):
        mid=(lo+hi)/2
        if fn(mid) * vlo > 0:
            lo, vlo = mid, fn(mid)
        else:
            hi = mid
    return (lo+hi)/2

def F(d, u):
    s,c=sin(u),cos(u)
    return (2+exp(-d*u)*((d**3*u+d*u)*c -(d**3+d*d*u+3*d+u)*s-2*c))/(1+d*d)**2

def Q(d,z):
    return exp(-d*z)*((1+d*d)*z*z+2*d*z+2)/sqrt(1+z*z)

def quad_simpson(fn, lo, hi, steps=12000):
    if steps%2: steps+=1
    h=(hi-lo)/steps
    ans=fn(lo)+fn(hi)
    ans+=4*sum(fn(lo+j*h) for j in range(1,steps,2))
    ans+=2*sum(fn(lo+j*h) for j in range(2,steps,2))
    return h*ans/3

def test():
    checks=0
    z2=bisect(g,2*pi,2.5*pi)
    threshold=bisect(lambda d:Q(d,z2)-2,0,1)
    assert 7.7252518369<z2<7.7252518370;checks+=1
    assert .18825293387<threshold<.18825293389;checks+=1
    assert threshold>1/z2;checks+=1
    assert abs(F(threshold,z2))<2e-14;checks+=1
    roots=[]
    for j in range(1,22):
        lo=j*pi
        hi=(j+.5)*pi
        if j==1: lo=pi
        if (j%2)==1:
            root=bisect(g,lo,hi)
        else:
            root=bisect(g,lo,hi)
        roots.append(root)
    # Positivity is proved for all t in the manuscript; check stationary values.
    for d in [threshold,threshold+.001,.2,.4,1.0,2.0]:
        for j,z in enumerate(roots):
            assert F(d,z)>-5e-12,(d,j,z,F(d,z));checks+=1
        for z in [.02,.2,.8,2.0,4,6,9,12,17,24,31,50]:
            assert F(d,z)>-5e-12,(d,z,F(d,z)); checks+=1
    for d in [-.7,-.1,0,.07,.15,threshold-.0001]:
        assert F(d,z2)<0,(d,F(d,z2)); checks+=1
    # Exact polynomial 6-isometry and strict non-5-isometry; rational cases.
    for a,b,c in [(Fraction(1),Fraction(6,5),Fraction(1)),
                  (Fraction(2),Fraction(3),Fraction(1)),
                  (Fraction(1),Fraction(1),Fraction(3,2))]:
        for k in range(5):
            sixth=sum((-1)**(6-j)*__import__('math').comb(6,j)*P(k+j,a,b,c) for j in range(7))
            fifth=sum((-1)**(5-j)*__import__('math').comb(5,j)*P(k+j,a,b,c) for j in range(6))
            assert sixth==0;checks+=1
            assert fifth>0;checks+=1
            for n in range(1,7):
                prod=Fraction(1)
                for j in range(n):prod*=P(k+j+1,a,b,c)/P(k+j,a,b,c)
                assert prod==P(k+n,a,b,c)/P(k,a,b,c);checks+=1
    # Verify inversion of Laplace transform at integer arguments in the positive zone.
    for a,b,c in [(1.0,1.3,1.0),(2.0,2.4,1.0),(1.2,1.2+.22*1.1,1.1)]:
        d=(b-a)/c
        factor=a*(b*b+c*c)**2/(2*c**4)
        for n in range(5):
            approx=quad_simpson(lambda v:factor*exp(-(n+a)*v)*F(d,c*v),0,55)
            exact=1/P(n,a,b,c)
            assert abs(approx-exact)<3e-10,(a,b,c,n,approx,exact);checks+=1
    # Derivative identities verified by a small centered-difference diagnostic.
    d=.3; z=10.0;h=1e-5
    dp=(Q(d+h,z)-Q(d-h,z))/(2*h)
    dp_exact=-exp(-d*z)*(1+d*d)*z**3/sqrt(1+z*z)
    assert abs(dp-dp_exact)<3e-6;checks+=1
    print('PASS', checks, 'checks; z2=',repr(z2),'rho*=',repr(threshold))

if __name__=='__main__':test()
