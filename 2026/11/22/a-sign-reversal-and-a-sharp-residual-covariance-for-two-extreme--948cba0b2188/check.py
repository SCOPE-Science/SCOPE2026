"""Exact identities and numerical consistency tests for adjacent extreme spacings."""
import itertools
import math
from fractions import Fraction


def no_adjacent_cycle(n, p):
    discr = math.sqrt((1-p)*(1+3*p))
    return ((1-p+discr)/2)**n + ((1-p-discr)/2)**n


def brute_no_adjacent(n, p):
    z = 0.0
    for bits in itertools.product((0, 1), repeat=n):
        if all(not (bits[j] and bits[(j+1)%n]) for j in range(n)):
            k = sum(bits)
            z += p**k * (1-p)**(n-k)
    return z


def covariance_exponential(n, mesh=440):
    # u=log(n)+x, v=(log(n)+y)/2; Jacobian exactly 1/2.
    lo, hi = -11.0, 13.0
    step = (hi-lo)/mesh
    xgrid = [lo+i*step for i in range(mesh+1)]
    ygrid = [lo+j*step for j in range(mesh+1)]
    total = 0.0
    logn = math.log(n)
    for i,x in enumerate(xgrid):
        u = logn+x
        if u<=0: continue
        q = math.exp(-u)
        fa = (1-q)**n
        outer_weight = 0.5 if i in (0,mesh) else 1
        for j,y in enumerate(ygrid):
            v = (logn+y)/2
            if v<=0: continue
            p = math.exp(-v)
            rp = no_adjacent_cycle(n,p)
            if u<v:
                difference = fa*(1-rp)
            else:
                pp = (p-q)/(1-q)
                difference = fa*(no_adjacent_cycle(n,pp)-rp)
            inner_weight = 0.5 if j in (0,mesh) else 1
            total += outer_weight*inner_weight*difference
    return 0.5*total*step**2


def expected_pair_minimum_exponential(n, mesh=10000):
    # E[B_n] = integral from 0 to infinity of (1-R_n(exp(-v))) dv.
    top = math.log(n)/2+22
    h = top/mesh
    acc=0.
    for j in range(mesh+1):
        v=j*h
        val=1-no_adjacent_cycle(n,math.exp(-v))
        acc+=(0.5 if j in (0,mesh) else 1)*val
    return acc*h


def main():
    count=0
    for n in range(3,11):
        for p in (.03,.11,.3,.5,.77):
            a,b=no_adjacent_cycle(n,p),brute_no_adjacent(n,p)
            assert abs(a-b)<2e-12,(n,p,a,b)
            count+=1
    ea=Fraction(11,6); eb=Fraction(5,6)
    cab=Fraction(1,9)+Fraction(1,4)
    cnormalized=(cab-ea*eb/3)/12
    assert cnormalized==Fraction(-1,81)
    count+=1
    for n in (80,250,1000,3000):
        cov=covariance_exponential(n)
        eb=expected_pair_minimum_exponential(n)
        ea=sum(1/j for j in range(1,n+1))
        normalized=(cov-ea*eb/n)/(n*(n+1))
        if n==80: assert math.isfinite(normalized)
        if n==3000: assert normalized>0
        if n==3000:
            assert abs(math.sqrt(n)*cov-math.sqrt(math.pi))<.13
            assert abs(n**2.5*normalized-math.sqrt(math.pi))<1.2
        print('n=',n,'sqrt(n)Cov(exp extremes)=',round(math.sqrt(n)*cov,7),
              'n^(5/2)Cov(normalized)=',round(n**2.5*normalized,7))
        count+=4
    print('PASS',count,'checks')

if __name__=='__main__':
    main()
