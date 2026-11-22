"""Independent deterministic checks of a short-distance law for an astroid.
Python 3 standard library only; no external files or services required.
"""
from math import gamma, sqrt

L = 6.0
C = (2.0 ** (1/3) / 9.0) * gamma(1/3) * gamma(3/2) / gamma(11/6)
c = (2.0/3.0) ** 1.5
u_max = 3.0 / (2.0 ** (5/3))
I = C * (L*L)/8.0


def f(a):
    return (1.0-2.0*a/3.0)**1.5


def d2(a,b):
    return (f(a)-f(b))**2+c*c*(a**1.5+b**1.5)**2


def min_b(a, upper):
    """Independent golden-section minimization of squared branch separation."""
    q=(sqrt(5)-1)/2
    lo,hi=0.0,upper
    x=hi-q*(hi-lo); y=lo+q*(hi-lo)
    fx=d2(a,x);fy=d2(a,y)
    for _ in range(80):
        if fx<fy:
            hi=y;y=x;fy=fx;x=hi-q*(hi-lo);fx=d2(a,x)
        else:
            lo=x;x=y;fx=fy;y=lo+q*(hi-lo);fy=d2(a,y)
    return .5*(lo+hi)


def cross_width(a,eps):
    upper=min(1.5,a+4*eps)
    bmid=min_b(a, upper)
    if d2(a,bmid)>=eps*eps:
        return 0.0
    if d2(a,0)<=eps*eps:
        left=0.0
    else:
        lo,hi=0.0,bmid
        for _ in range(55):
            m=(lo+hi)/2
            if d2(a,m)>eps*eps:lo=m
            else:hi=m
        left=(lo+hi)/2
    lo,hi=bmid,upper
    assert d2(a,hi)>eps*eps
    for _ in range(55):
        m=(lo+hi)/2
        if d2(a,m)<eps*eps:lo=m
        else:hi=m
    return (lo+hi)/2-left


def cross_area(eps,n=1800):
    assert n%2==0
    # Upper a bound follows from the vertical coordinate c*a^(3/2) <= eps.
    amax=(eps/c)**(2/3)
    h=amax/n
    total=cross_width(0.0,eps)+cross_width(amax,eps)
    for i in range(1,n):
        total+=(4 if i%2 else 2)*cross_width(h*i,eps)
    return total*h/3


def main():
    assert abs(2**(-2/3)*gamma(1/3)*gamma(3/2)/gamma(11/6)-I)<1e-12
    # 8 ordered branch-pairs (4 cusps x 2 orientations), normalized by 6^2.
    estimates=[]
    for eps in (0.012,0.006,0.003,0.0015):
        area=cross_area(eps)
        estimate=(8*area/L**2)/eps**(5/3)
        estimates.append(estimate)
        print(f'eps={eps:.4g}, coefficient={estimate:.9f}, limit={C:.9f}')
    assert all(0<e<C for e in estimates)
    assert all(estimates[i]<estimates[i+1] for i in range(3))
    assert abs(estimates[-1]-C)/C<0.045
    # Beta(1/3, 3/2) and independent uniform mark for the limiting cusp domain.
    assert abs((1/3)/(1/3+3/2)-2/11)<1e-14
    assert abs(u_max-3/2**(5/3))<1e-14
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':
    main()
