"""Numerical and exact-coefficient checks for random geodesic polygon parity."""
from __future__ import annotations
import math
import random


def circle_distance(t):
    u = t % 1.0
    return min(u, 1.0-u)


def sign_spectrum(m):
    # Frequencies (2k+1)*pi; both positive/negative modes have the same eigenvalue.
    return 2.0 * ((-1.0)**m) / (math.pi * (2*m+1))


def trace_power(n, terms=10000):
    return 2 * sum(sign_spectrum(k)**n for k in range(terms))


def single_edge_difference(n, u, terms=9000):
    assert n >= 4
    def primitive(w, s):
        return (1-s)*math.sin(w*s)/w-math.cos(w*s)/(w*w)
    return 8*sum(sign_spectrum(k)**(n-1) * (
        primitive((2*k+1)*math.pi, .5+u)-primitive((2*k+1)*math.pi,.5)
    ) for k in range(terms))


def chosen_parity(x0,y0,x1,y1,a,b):
    de=(x0-x1)**2 + (b*circle_distance((y0-y1)/b))**2
    do=(a-abs(x0-x1))**2 + (b*circle_distance((y0+y1)/b))**2
    return do < de


def direct_parity(x0,y0,x1,y1,a,b):
    ev=min((x0-x1-2*k*a)**2+(y0-y1-m*b)**2
           for k in range(-2,3) for m in range(-2,3))
    od=min((x0-x1-(2*k+1)*a)**2+(y0+y1-m*b)**2
           for k in range(-2,3) for m in range(-2,3))
    return od < ev


def trial(n, aspect, number, seed):
    rng=random.Random(seed)
    count=0
    for _ in range(number):
        x=[aspect*rng.random() for _ in range(n)]
        y=[rng.random() for _ in range(n)]
        v=sum(chosen_parity(x[j],y[j],x[(j+1)%n],y[(j+1)%n],aspect,1.)
              for j in range(n))
        count += v%2
    return count/number


def main():
    vals={2:1.,3:.5,4:1/3,5:5/24,6:2/15}
    for n,t in vals.items():
        got=trace_power(n)
        assert abs(got-t)<(3e-5 if n==2 else 3e-9),(n,got,t)
    for n in (4,5,6):
        delta=.004
        got=single_edge_difference(n,delta)/delta**2
        expected=-2*vals[n-2]
        assert abs(got-expected)<.055,(n,got,expected)
    rng=random.Random(55311)
    for _ in range(600):
        a=1.3+3*rng.random();b=.4+1.1*rng.random()
        x0,x1=a*rng.random(),a*rng.random()
        y0,y1=b*rng.random(),b*rng.random()
        assert chosen_parity(x0,y0,x1,y1,a,b)==direct_parity(x0,y0,x1,y1,a,b)
    for n,aspects in [(4,(1.,2.,4.)),(5,(1.,2.)),(6,(1.,2.))]:
        p0=(1-vals[n])/2
        for a in aspects:
            p=trial(n,a,180000,81515+n*101+int(a)*3)
            prediction=p0 + n*vals[n-2]/(360*a**4)
            # Finite-width remainder is not zero; conservative test for trends.
            tolerance=.012/a**5 + 0.006
            assert abs(p-prediction)<tolerance,(n,a,p,prediction)
            print('n',n,'a/b',a,'empirical',round(p,6),
                  'asymptotic',round(prediction,6))
    print('KLEIN_ALL_POLYGON_PARITY_QUARTIC_OK')

if __name__=='__main__':
    main()
