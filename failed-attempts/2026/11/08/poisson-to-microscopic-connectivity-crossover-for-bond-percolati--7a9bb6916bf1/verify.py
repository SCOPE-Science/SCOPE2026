"""Finite-state and continuum checks for wheel bond percolation."""
from fractions import Fraction
from math import exp, sqrt, cosh
import random


def exact_connected_formula(n, p, q):
    s = 2*p + q - 2*p*q
    u = p*p*(1-q)
    z0, z1 = Fraction(2), s
    if n == 0:
        z = z0
    elif n == 1:
        z = z1
    else:
        for _ in range(2, n + 1):
            z0, z1 = z1, s*z1 - u*z0
        z = z1
    return z - 2*(p*(1-q))**n


def exact_root_mean_formula(n, p, q):
    r = 1-q
    total = (p**n + n*(1-p)*p**(n-1))*r**n
    for s in range(1, n):
        total += s*(1-p)**2*p**(s-1)*r**s
    return 1-total


def enumerate_exact(n):
    # Rim edge open probability 2/3; spoke open probability 2/5.
    denom = 15**n
    connected_count, root_weight = 0, 0
    for rim in range(1<<n):
        wr = 2**rim.bit_count()
        for spoke in range(1<<n):
            weight = wr * 2**spoke.bit_count()*3**(n-spoke.bit_count())
            par = list(range(n+1))
            def find(a):
                while par[a] != a:
                    a=par[a]
                return a
            def union(a,b):
                aa,bb=find(a),find(b)
                par[aa]=bb
            for i in range(n):
                if rim>>i & 1:
                    union(i,(i+1)%n)
                if spoke>>i & 1:
                    union(i,n)
            if len({find(i) for i in range(n+1)})==1:
                connected_count+=weight
            root_weight+=weight*sum(find(i)==find(n) for i in range(n))
    return Fraction(connected_count,denom),Fraction(root_weight,n*denom)


def continuum_conn(lam,mu):
    delta = sqrt(mu*mu+4*lam*mu)
    lead = 0.0 if lam == 0 and mu == 0 else -2*lam*lam/(delta+mu+2*lam)
    return exp(lead) + exp(-lam-mu/2-delta/2) - 2*exp(-lam-mu)


def continuum_mean(lam,mu):
    if lam+mu == 0:
        return 0.0
    a=lam+mu
    return 1-exp(-a)*(1+lam)-lam*lam/(a*a)*(1-(1+a)*exp(-a))


def sample_continuum(rng,lam,mu):
    # Knuth's Poisson sampler works well for the modest test parameters.
    def poisson(rate):
        prod=1.0; k=0; target=exp(-rate)
        while True:
            prod*=rng.random()
            if prod<=target:
                return k
            k+=1
    cuts=sorted(rng.random() for _ in range(poisson(lam)))
    spoke=sorted(rng.random() for _ in range(poisson(mu)))
    if len(cuts)<2:
        x=float(bool(spoke))
        return x,x==1
    # Each arc from cut_i to next cut is active iff any spoke is inside.
    lengths=[cuts[i+1]-cuts[i] for i in range(len(cuts)-1)]
    lengths.append(1-cuts[-1]+cuts[0])
    selected=[False]*len(cuts)
    for s in spoke:
        # first cut strictly to the right of s, cyclically
        j=0
        while j<len(cuts) and cuts[j]<s:
            j+=1
        selected[(j-1)%len(cuts)]=True
    x=sum(a for a,yes in zip(lengths,selected) if yes)
    return x,all(selected)


def run():
    checks=0
    p,q=Fraction(2,3),Fraction(2,5)
    for n in range(3,8):
        a,b=enumerate_exact(n)
        assert a==exact_connected_formula(n,p,q),(n,a,exact_connected_formula(n,p,q))
        assert b==exact_root_mean_formula(n,p,q),(n,b,exact_root_mean_formula(n,p,q))
        checks+=2
    for n in (50,200,1000,5000,20000):
        lam,mu=1.4,0.9
        p=1-lam/n;q=mu/n
        rf=exact_connected_formula(n,p,q)
        mf=exact_root_mean_formula(n,p,q)
        assert abs(rf-continuum_conn(lam,mu)) < 15/n
        assert abs(mf-continuum_mean(lam,mu)) < 15/n
        checks+=2
    for lam,mu in ((0.,0.),(0.,1.4),(2.1,0.),(1.4,.9),(3.,2.)):
        r=continuum_conn(lam,mu);m=continuum_mean(lam,mu)
        assert 0<=r<=m+1e-9<=1+1e-9
        checks+=1
    for lam in (10.0, 50.0, 200.0):
        for ratio in (.5, 1.0, 2.0):
            target=exp(-1/ratio)
            assert abs(continuum_conn(lam,ratio*lam*lam)-target)<4/lam
            checks+=1
    rng=random.Random(314159)
    lam,mu=1.4,.9
    samples=[sample_continuum(rng,lam,mu) for _ in range(50000)]
    empirical_conn=sum(c for x,c in samples)/len(samples)
    empirical_mean=sum(x for x,c in samples)/len(samples)
    assert abs(empirical_conn-continuum_conn(lam,mu))<0.012
    assert abs(empirical_mean-continuum_mean(lam,mu))<0.012
    checks+=2
    print('PASS',checks,'checks')
    print('continuum parameters',lam,mu,'Pconn',continuum_conn(lam,mu),'Efrac',continuum_mean(lam,mu))

if __name__=='__main__':
    run()
