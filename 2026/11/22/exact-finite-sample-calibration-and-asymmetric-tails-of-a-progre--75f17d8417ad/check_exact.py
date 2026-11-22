"""Exact rational checks and independent censored-sample simulation for a spacing test.

Python 3 standard library only. Run: python check_exact.py
"""
from fractions import Fraction as Q
from math import comb, factorial, sqrt
import random


def parameters(n, m, r):
    assert isinstance(n,int) and isinstance(m,int) and isinstance(r,int)
    assert 0 <= r < m <= n and m-r >= 2
    d = m-r
    weights = [Q(d-1-j, d-1) for j in range(d)]
    c = [Q(n-r, n-j) for j in range(r+1)]
    return d, weights, c


def cdf_exact(n, m, r, t):
    d, w, cs = parameters(n, m, r)
    t = Q(t)
    if t <= 0: return Q(0)
    if t >= 1: return Q(1)
    below = [j for j in range(1, d) if w[j] < t]
    above = [j for j in range(1, d) if w[j] > t]
    ans=Q(0)
    for j in below:
        b=1/(t-w[j])
        coeff=Q(1)
        for h in below:
            if h != j:
                coeff *= (t-w[j])/(w[h]-w[j])
        for c in cs:
            coeff *= 1/(1+b*(1-t)*c)
        for h in above:
            coeff *= 1/(1+b*(w[h]-t))
        ans += coeff
    assert Q(0) <= ans <= Q(1)
    return ans


def cdf_unobserved_none(d,t):
    t=Q(t)
    if t<=0:return Q(0)
    if t>=1:return Q(1)
    x=(d-1)*t
    return sum(Q((-1)**j*comb(d-1,j),factorial(d-1))*(x-j)**(d-1)
               for j in range(d) if Q(j)<=x)


def left_coefficient(n,m,r):
    d, _, _ = parameters(n,m,r)
    c=Q(1)
    for ell in range(r+1):c*=Q(n-ell,n-r)
    return c*Q((d-1)**(d-2),factorial(d-2))


def complete_homogeneous(c,degree):
    h=[Q(0)]*(degree+1);h[0]=Q(1)
    for x in c:
        for j in range(1,degree+1):h[j]+=x*h[j-1]
    return h[degree]


def right_coefficient(n,m,r):
    d, _, c=parameters(n,m,r)
    return Q((d-1)**(d-1),factorial(d-1))*complete_homogeneous(c,d-1)


def left_formula(n,m,r,t):
    d,w,_=parameters(n,m,r)
    t=Q(t)
    assert Q(0)<t<Q(1,d-1)
    a=Q(1)
    for ell in range(r+1):
        a*=Q(n-ell)*t/(Q(n-ell)*t+Q(n-r)*(1-t))
    for j in range(1,d-1):a*=t/w[j]
    return a


def simulate_scheme(n,m,r,R,threshold,seed,N=30000):
    rng=random.Random(seed)
    d, weights, _ = parameters(n,m,r)
    assert len(R)==d and sum(R)==n-m
    hit=0
    for _ in range(N):
        lifetimes=[rng.expovariate(1) for _ in range(n)]
        unseen=set(sorted(range(n),key=lambda j:lifetimes[j])[r:])
        last=0.0;spacings=[]
        for j,remove in enumerate(R):
            risk=len(unseen)
            victim=min(unseen,key=lambda i:lifetimes[i])
            time=lifetimes[victim]
            spacings.append(risk*(time-last))
            last=time
            unseen.remove(victim)
            for ix in rng.sample(sorted(unseen),remove):unseen.remove(ix)
        stat=sum(float(weights[i])*spacings[i] for i in range(d))/sum(spacings)
        hit+= stat<=threshold
    return hit/N


def main():
    count=0
    for d in range(2,9):
        for numer in range(1, 40):
            t=Q(numer,40)
            got=cdf_exact(d+3,d,0,t)
            assert got==cdf_unobserved_none(d,t),(d,t,got)
            count+=1
    for n,m,r in [(5,3,1),(8,6,4),(10,6,2),(17,10,3),(20,10,0)]:
        d=m-r
        for den in [20,50,100]:
            t=Q(1,den*(d-1))
            assert cdf_exact(n,m,r,t)==left_formula(n,m,r,t)
            count+=1
        for den in [10000,100000]:
            t=Q(1,den)
            a=cdf_exact(n,m,r,t)/t**(m-1)
            b=(1-cdf_exact(n,m,r,1-t))/t**(d-1)
            assert abs(float(a/left_coefficient(n,m,r)-1))<0.002
            assert abs(float(b/right_coefficient(n,m,r)-1))<0.002
            count+=2
    for j in range(1,100):
        t=Q(j,100)
        assert cdf_exact(5,3,1,t)==5*t*t/(4+t)
        count+=1
    for scheme in [(4,0,0,0),(0,0,0,4)]:
        for threshold in [.35,.60,.85]:
            est=simulate_scheme(10,6,2,scheme,threshold,12345,30000)
            exact=float(cdf_exact(10,6,2,Q(str(threshold))))
            se=sqrt(exact*(1-exact)/30000)
            assert abs(est-exact)<6*se+0.002,(scheme,threshold,est,exact)
            print('scheme',scheme,'threshold',threshold,'empirical',round(est,5),'exact',round(exact,5))
            count+=1
    print('Exact rational and direct censorship simulation checks passed:',count)
    print('Example n=5,m=3,r=1 F(t)=5t^2/(4+t).')
    print('n=10,m=6,r=2 left/right constants:',float(left_coefficient(10,6,2)),float(right_coefficient(10,6,2)))


if __name__=='__main__':main()
