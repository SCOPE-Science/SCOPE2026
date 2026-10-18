#!/usr/bin/env python3
from math import isqrt

def factor(n):
    out={}; d=2
    while d*d<=n:
        while n%d==0:
            out[d]=out.get(d,0)+1; n//=d
        d=3 if d==2 else d+2
    if n>1: out[n]=out.get(n,0)+1
    return out

def is_prime(n):
    return n>=2 and factor(n)=={n:1}

def omega(n): return sum(factor(n).values())

def is_sondow(mu,n):
    return all((n//p+mu)%(p**a)==0 for p,a in factor(n).items())

def classified(mu,n):
    if not (mu>0 and n>mu and omega(n)<=2): return False
    f=factor(n)
    if len(f)==1:
        p,a=next(iter(f.items()))
        return (a==1 and mu==p-1) or (a==2 and mu==p*(p-1))
    p,q=sorted(f)
    return all(a==1 for a in f.values()) and mu==p*q-p-q

def main():
    primes=[p for p in range(2,100) if is_prime(p)]
    for p in primes:
        assert is_sondow(p-1,p)
        assert is_sondow(p*(p-1),p*p)
    for i,p in enumerate(primes):
        for q in primes[i+1:]:
            mu=p*q-p-q
            if mu>0:
                assert is_sondow(mu,p*q)
                assert mu+1==(p-1)*(q-1)
    # finite regression on all low-complexity n <= 1500
    for n in range(2,1501):
        if omega(n)>2: continue
        for mu in range(1,min(n,300)):
            assert is_sondow(mu,n)==classified(mu,n), (mu,n)
    mu=673
    assert not is_prime(674)
    D=1+4*mu
    assert isqrt(D)**2!=D
    assert 674==2*337
    pairs=[]
    for d in (1,2,337,674):
        if 674%d: continue
        p=d+1; q=674//d+1
        if p<q and is_prime(p) and is_prime(q): pairs.append((p,q))
    assert pairs==[]
    print('VERIFY_OK')
    print('mu673_low_omega_witnesses=[]')
if __name__=='__main__': main()
