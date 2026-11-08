"""Independent finite-state checks for a weak-link tripartite dimer model.

Run: python3 verify.py
Pure standard-library rational arithmetic, finite graphs only.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb, exp
import random


def reduced_distribution(n, weight):
    """Exact Markov recursion on aggregate unoccupied part sizes."""
    w = Fraction(weight)
    @lru_cache(None)
    def rec(a, b, c):
        assert c >= a+b
        if a+b == 0:
            return (Fraction(1),)
        rates = ((w*a*b, (a-1,b-1,c), 1),
                 (a*c, (a-1,b,c-1), 0),
                 (b*c, (a,b-1,c-1), 0))
        z = sum(x for x,_,_ in rates)
        ans = [Fraction(0)]*(min(a,b)+1)
        for r, state, k in rates:
            if r:
                sub = rec(*state)
                for i, v in enumerate(sub):
                    ans[i+k] += r*v/z
        return tuple(ans)
    return rec(n,n,2*n)


def vertex_distribution(n, weight):
    """Independent recursion on labelled available vertex subsets."""
    w=Fraction(weight)
    size=4*n
    edges=[]
    for a in range(n):
        for b in range(n,2*n):
            edges.append((a,b,w,1))
        for c in range(2*n,4*n):
            edges.append((a,c,Fraction(1),0))
    for b in range(n,2*n):
        for c in range(2*n,4*n):
            edges.append((b,c,Fraction(1),0))
    @lru_cache(None)
    def rec(mask):
        eligible=[(a,b,rate,k) for a,b,rate,k in edges if rate and (mask>>a)&1 and (mask>>b)&1]
        if not eligible:
            assert mask.bit_count()%2==0
            return (Fraction(1),)
        total=sum(e[2] for e in eligible)
        out=[Fraction(0)]*(n+1)
        for a,b,rate,k in eligible:
            sub=rec(mask & ~(1<<a) & ~(1<<b))
            for j,p in enumerate(sub):
                if p:
                    out[j+k]+=rate*p/total
        return tuple(out)
    return rec((1<<size)-1)


def simulate(n, weight, trials=2000, seed=81491):
    rng=random.Random(seed)
    out=[]
    for _ in range(trials):
        a=b=n;c=2*n;k=0
        while a+b:
            r_ab=weight*a*b
            r_ac=a*c
            r_bc=b*c
            z=r_ab+r_ac+r_bc
            u=rng.random()*z
            if u<r_ab:
                a-=1;b-=1;k+=1
            elif u<r_ab+r_ac:
                a-=1;c-=1
            else:
                b-=1;c-=1
        assert c==2*k
        out.append(k)
    return out


def main():
    checks=0
    for n in (1,2,3):
        for weight in (Fraction(0),Fraction(1,2),Fraction(2),Fraction(5,3)):
            p=reduced_distribution(n,weight)
            q=vertex_distribution(n,weight)
            assert p==q, (n,weight,p,q)
            assert sum(p)==1 and all(a>=0 for a in p)
            checks+=3
    for n in (4,5,6,7,8):
        p=reduced_distribution(n,Fraction(2,n))
        assert sum(p)==1 and all(a>=0 for a in p)
        assert sum(i*val for i,val in enumerate(p))<=Fraction(2*n)*Fraction(2,n)/4
        checks+=2
    for lam in (0.5,2.0,4.0):
        n=2000
        samples=simulate(n,lam/n,trials=1000,seed=81491+int(lam*10))
        avg=sum(samples)/len(samples)
        p0=sum(k==0 for k in samples)/len(samples)
        assert abs(avg-lam/2)<0.20, (lam,avg)
        assert abs(p0-exp(-lam/2))<0.08, (lam,p0)
        checks+=2
    print('PASS',checks,'exact-rational identities and seeded statistical smoke checks')
    print('Limitation: finite-state checks and simulations do not prove the asymptotic theorem.')

if __name__=='__main__':
    main()
