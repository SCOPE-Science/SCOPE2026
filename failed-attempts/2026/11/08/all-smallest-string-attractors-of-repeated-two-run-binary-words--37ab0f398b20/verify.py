"""Independent direct factor-occurrence check for two-run word attractor theorem.

Run: python verify.py
No external dependencies.
"""
from collections import defaultdict
from itertools import combinations
import random


def proposed(a,b,k):
    p=a+b
    if a>=2 and b>=2:
        return {frozenset((a+(i-1)*p+eps,j*p+eps))
                for i in range(1,k+1) for j in range(1,k) for eps in (0,1)}
    if a==1:
        out={frozenset((1,j*p)) for j in range(1,k)}
        for i in range(2,k+1):
            z=1+(i-1)*p
            out.update(frozenset((z,(j-1)*p+1+t))
                       for j in range(1,k+1) for t in range(1,b+1))
        return out
    # b == 1 and a >= 2
    out={frozenset((k*p,j*p+1)) for j in range(1,k)}
    for i in range(1,k):
        one=i*p
        out.update(frozenset((one,(j-1)*p+t))
                   for j in range(1,k+1) for t in range(1,a+1))
    return out


def brute(a,b,k):
    w=('0'*a+'1'*b)*k
    n=len(w)
    factors=defaultdict(int)
    for start in range(n):
        text=[]
        for end in range(start,n):
            text.append(w[end])
            factors[''.join(text)] |= ((1<<(end-start+1))-1)<<start
    vals=list(factors.values())
    out=set()
    for i,j in combinations(range(n),2):
        mask=(1<<i)|(1<<j)
        if all(mask&cover for cover in vals):
            out.add(frozenset((i+1,j+1)))
    return out, len(factors)


def main():
    cases=0; distinct=0; matched=0
    for a in range(1,7):
        for b in range(1,7):
            for k in range(2,7):
                p=proposed(a,b,k)
                q,m=brute(a,b,k)
                assert p==q,(a,b,k, sorted(map(sorted,p-q))[:5],sorted(map(sorted,q-p))[:5])
                expected= (2*k*(k-1) if min(a,b)>=2 else (k-1)*(k*max(a,b)+1))
                assert len(p)==expected,(a,b,k,len(p),expected)
                cases+=1;distinct+=m;matched+=len(q)
    rng=random.Random(20261105)
    for _ in range(180):
        a=rng.randint(1,12);b=rng.randint(1,12);k=rng.randint(2,8)
        p=proposed(a,b,k)
        q,m=brute(a,b,k)
        assert p==q,(a,b,k)
        cases+=1;distinct+=m;matched+=len(q)
    print('PASS: parameter cases',cases,'distinct factor patterns checked',distinct,
          'exact optimal attractor pairs compared',matched)

if __name__=='__main__':main()
