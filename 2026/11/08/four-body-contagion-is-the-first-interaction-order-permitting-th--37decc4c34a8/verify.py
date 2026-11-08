"""Reproduce exact finite checks for stationary mode bounds in cooperative SIS.
Uses Python's rational arithmetic; no third-party dependencies.
This code is a finite check, not a substitute for the algebraic proof.
"""
from fractions import Fraction as Q
from math import comb
from itertools import product


def choose(k, j):
    return comb(k, j) if k >= j else 0


def inc(k, eps, rates):
    return eps + sum(rate * choose(k, j) for j, rate in enumerate(rates, 1))


def birth(n, k, eps, rates):
    return (n-k) * inc(k, eps, rates)


def weights(n, eps, rates, mu=Q(1)):
    out=[Q(1)]
    for k in range(n):
        out.append(out[-1] * birth(n,k,eps,rates)/(mu*(k+1)))
    return out


def strict_modes(ws):
    return [k for k in range(len(ws)) if
            (k==0 or ws[k]>ws[k-1]) and
            (k==len(ws)-1 or ws[k]>ws[k+1])]


def edge_detailed_balance(n, eps, rates, mu=Q(1)):
    w=weights(n,eps,rates,mu)
    for mask in range(1 << n):
        k=mask.bit_count()
        weight=w[k]/comb(n,k)
        for v in range(n):
            if mask & (1 << v):
                continue
            m2=mask | (1 << v)
            other=w[k+1]/comb(n,k+1)
            assert weight*inc(k,eps,rates)==other*mu


def check():
    # Every infection route is strictly positive, including pair, triangle, tetrahedron.
    n=4; mu=Q(1); eps=Q(1,8)
    rates=(Q(5,8),Q(1,16),Q(3))
    w=weights(n,eps,rates,mu)
    den=8192
    assert [int(v*den) for v in w]==[8192,4096,4608,4416,5727]
    assert strict_modes(w)==[0,2,4]
    assert sum(int(v*den) for v in w)==27039
    edge_detailed_balance(n,eps,rates,mu)
    assert [birth(n,k,eps,rates)/(k+1) for k in range(n)] == [Q(1,2),Q(9,8),Q(23,24),Q(83,64)]
    tested=0; edges=0
    for n in range(2,11):
        for eps,beta,eta,delta in product([Q(1,4*n),Q(1,2*n),Q(3,4*n)],
                                          [Q(0),Q(1,2*n),Q(1,n),Q(2,n)],
                                          [Q(0),Q(1,2*n*n),Q(5,n*n)],
                                          [Q(0),Q(1,n**3),Q(10,n**3)]):
            for r in ((beta,), (beta,eta), (beta,eta,delta)):
                if any(birth(n,k,eps,r)<0 for k in range(n)):
                    raise AssertionError('negative birth')
                ww=weights(n,eps,r)
                maxm=1+(len(r)+1)//2
                mm=strict_modes(ww)
                assert 0 in mm
                assert len(mm)<=maxm,(n,eps,r,mm)
                if n <= 6 and tested%17==0:
                    edge_detailed_balance(n,eps,r)
                    edges+=(1<<n)*n
                tested+=1
    # Uniform sharpness construction: every population size n >= 4 has modes 0,2,n.
    for n in range(4,201):
        t=Q(n-5,(n-1)*(n-2))
        eps=(t+Q(1,n))/2
        lower=Q(2,n-1)-eps
        upper=Q(3,2*(n-2))-eps/2
        beta=(lower+upper)/2
        eta=(upper-lower)/2
        delta=Q(n+1)
        assert 0<eps<Q(1,n) and 0<lower<beta<upper and eta>0
        probs=weights(n,eps,(beta,eta,delta))
        assert strict_modes(probs)==[0,2,n],(n,strict_modes(probs))
    # Direct N=4 necessity/sufficiency of the zero / two / four modal chamber.
    for eps,beta,delta in product([Q(1,20),Q(1,8),Q(1,5)],
                                  [Q(v,40) for v in range(10,41)],
                                  [Q(v,4) for v in range(0,25)]):
        r=(beta,Q(0),delta)
        m=strict_modes(weights(4,eps,r))
        chamber=(4*eps<1 and 3*(eps+beta)>2 and
                 2*(eps+2*beta)<3 and eps+3*beta+delta>4)
        assert (m==[0,2,4])==chamber,(eps,beta,delta,m)
    print('VERIFY_OK exact stationary distribution, generator edge-balance, root mode ceilings, 4-person chamber and rational witness',tested,'parameter/case checks',edges,'edge comparisons attempted')

if __name__=='__main__':
    check()
