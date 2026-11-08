#!/usr/bin/env python3
"""Exact Gaussian-integer verification of a reversible order-16 difference set
and of the finite factors in the exponent-four spectral construction.

All arithmetic is integer arithmetic. The analytic infinite product and
singularity arguments are established in RESULT.md, not by enumeration.
"""
from collections import Counter
from itertools import product

D = frozenset({(0,0), (0,1), (0,3), (1,0), (2,2), (3,0)})
Q4 = range(4)

def b(x, y):
    return -1 if (x,y) in D else 1


def assert_difference_set():
    assert len(D) == 6
    assert {(-x % 4, -y % 4) for x,y in D} == D
    counts = Counter(((x-u)%4,(y-v)%4) for x,y in D for u,v in D)
    assert counts[(0,0)] == 6
    assert all(counts[(u,v)]==2 for u,v in product(Q4, repeat=2) if (u,v)!=(0,0))


def add(a,b):
    return (a[0]+b[0],a[1]+b[1])

def sub(a,b):
    return (a[0]-b[0],a[1]-b[1])

def mul_i(a):
    return (-a[1],a[0])

def mul_minus_i(a):
    return (a[1],-a[0])


def dft4(a,b,c,d):
    # Transformation with character (-i) raised to input*frequency.
    return (add(add(a,b),add(c,d)),
            add(sub(a,c),sub(mul_i(d),mul_i(b))),
            sub(add(a,c),add(b,d)),
            add(sub(a,c),sub(mul_i(b),mul_i(d))))


def dft_power4(arr, dimension):
    n = 4**dimension
    a = arr.copy()
    for axis in range(dimension):
        step=4**axis
        for j in range(0,n,4*step):
            for offset in range(step):
                ix=[j+offset+h*step for h in range(4)]
                z=dft4(*(a[i] for i in ix))
                for i,v in zip(ix,z):
                    a[i]=v
    return a


def digits(i,dimension):
    out=[]
    for _ in range(dimension):
        out.append(i%4)
        i//=4
    return out


def run():
    assert_difference_set()
    # The size-16 seed has normalized transform entries +/- 1/4.
    f=[(b(x,y),0) for y in Q4 for x in Q4]
    tr=dft_power4(f,2)
    assert all(im==0 and abs(re)==4 for re,im in tr)
    sign=[re//4 for re,im in tr]
    assert sign[0] == 1
    assert all(sign[u+4*v] == sign[(-u)%4 + 4*((-v)%4)] for u,v in product(Q4,repeat=2))

    for j in (1,2,3):
        q=4**j
        dimension=2*j+1
        n=4**dimension
        raw=[]
        sigmas={}
        for idx in range(4**(2*j)):
            ws=digits(idx,2*j)
            sigma=1
            for k in range(j):
                sigma *= sign[ws[2*k]+4*ws[2*k+1]]
            sigmas[idx]=sigma
        for idx in range(n):
            d=digits(idx,dimension)
            t=d[0];w=d[1:]
            val=1
            for k in range(j):
                val *= b(w[2*k],w[2*k+1])
            c=(1,0,-1,0)[t]
            s=(0,1,0,-1)[t]
            localized=(q*s if all(z==0 for z in w) else 0)
            # 2f=2+b(w)cos(pi t/2)+i q 1_{w=0} sin(pi t/2).
            raw.append((2+val*c,localized))
        F=dft_power4(raw,dimension)
        nonconstant=0
        for idx,(re,im) in enumerate(F):
            d=digits(idx,dimension)
            t=d[0];z=d[1:]
            zidx=sum(x*(4**k) for k,x in enumerate(z))
            if not any(d):
                expected=(2*n,0)
            elif t== (1 if sigmas[zidx]==1 else 3):
                expected=(4*q*sigmas[zidx],0)
                nonconstant+=1
            else:
                expected=(0,0)
            assert (re,im)==expected, (j,d,(re,im),expected)
        assert nonconstant==q*q
        assert (1 if sigmas[0]==1 else 3)==1
        # Spectral antipodality follows from sign(-z)=sign(z).
        for zidx,s in sigmas.items():
            z=digits(zidx,2*j)
            negidx=sum(((-x)%4)*(4**k) for k,x in enumerate(z))
            assert sigmas[negidx]==s
    print('CHECK_OK difference_set_order=16 exact_factor_levels=3 gaussian_integer_Fourier_coefficients='+str(sum(4**(2*j+1) for j in (1,2,3))))


if __name__ == '__main__':
    run()
