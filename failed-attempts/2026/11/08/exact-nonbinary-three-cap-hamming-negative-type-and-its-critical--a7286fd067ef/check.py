#!/usr/bin/env python3
"""Independent checks for cubic-saturated Hamming negative-type theorem.
Run: python3 check.py
Only uses the Python 3 standard library.
"""
from itertools import product
from math import comb, cos, sin, pi, log, sqrt, isclose


def krawtchouk(n,q,j,k):
    """Direct independent coefficient formula for the jth Hamming sphere."""
    return sum((-1)**h * (q-1)**(j-h) * comb(k,h) * comb(n-k,j-h)
               for h in range(max(0,j-(n-k)), min(j,k)+1))


def analytic(n,q,k,p):
    t = (q-1)*n-q*k
    z = (t*t-(q-2)*t-(q-1)*n)//2
    assert z == krawtchouk(n,q,2,k)
    return -3**p + (1-3**p)*t+(2**p-3**p)*z


def bisect(n,q,k):
    a,b=0.,1.
    assert analytic(n,q,k,a)<0<analytic(n,q,k,b)
    for _ in range(90):
        m=(a+b)/2
        if analytic(n,q,k,m)>0:b=m
        else:a=m
    return (a+b)/2


def exact_character_enumeration(q,n,p):
    """Character sum over Z/qZ; nothing uses field structure or a Krawtchouk identity."""
    words=list(product(range(q), repeat=n))
    root=[complex(cos(2*pi*j/q),sin(2*pi*j/q)) for j in range(q)]
    representatives={k:(1,)*k+(0,)*(n-k) for k in range(n+1)}
    byweight={k:[] for k in range(n+1)}
    for x in words:byweight[sum(v!=0 for v in x)].append(x)
    for k in range(1,n+1):
        w=representatives[k]
        measured=0j
        for j in range(1,n+1):
            mag=min(j,3)**p
            for x in byweight[j]:
                measured+=mag*root[sum(a*b for a,b in zip(w,x))%q]
        expected=analytic(n,q,k,p)
        assert abs(measured-expected)<1e-7*(1+abs(expected)),(q,n,k,p,measured,expected)


def run():
    total=0
    for q,n in [(3,4),(3,5),(4,4),(5,4)]:
        for p in [0.125,0.6,1.0]:
            exact_character_enumeration(q,n,p)
            total+=1
    for q in [3,4,5,6,7,8,10,11,16,31,101,503]:
        for n in [4,5,6,7,8,9,10,11,20,41,71,125]:
            k=((q-1)*n+3)//q
            assert 1<=k<n
            t=(q-1)*n-q*k
            assert -3<=t<=q-4
            b=bisect(n,q,k)
            for pp in [0.0001,0.17*b,0.87*b,0.99*b,0.5*(b+1),0.99]:
                val=analytic(n,q,k,pp)
                others=[analytic(n,q,j,pp) for j in range(1,n+1)]
                if pp<=1:
                    assert val>max(v for j,v in enumerate(others,1) if j!=k)-1e-6, (n,q,k,pp)
            assert analytic(n,q,k,b*.99)<0
            assert analytic(n,q,k,(b+1)/2)>0
    # Both asymptotic orders numerically, with slow n=4,q -> infinity convergence.
    for q in [3,4,5,11]:
        n=20000
        k=((q-1)*n+3)//q
        p=bisect(n,q,k)
        target=2/((q-1)*log(3/2))
        assert abs(n*p/target-1)<0.003
    for n in [4,5,8,12]:
        q=100000
        k=((q-1)*n+3)//q
        p=bisect(n,q,k)
        target=1/((n-2)*log(3)-(n-1)*log(2))
        assert abs(q*p/target-1)<0.006
    print('QARY_CAP3_INDEPENDENT_FOURIER_CHECKS_PASS')
    print('direct_character_enumerations',total)
    print('analytic_parameter_cases',12*12)
    print('sample_thresholds',[(q,n,round(bisect(n,q,((q-1)*n+3)//q),10)) for q,n in [(3,4),(4,5),(5,10),(7,20)]])

if __name__=='__main__':run()
