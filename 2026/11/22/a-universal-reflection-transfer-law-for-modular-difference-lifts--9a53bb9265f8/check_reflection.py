#!/usr/bin/env python3
"""Independent finite-factor check for reflection complexity of modular difference lifts.
For each tested parameter, explicit finite base-language factors are lifted independently.
This is a finite consistency check, not a proof of the infinite statement.
"""
from itertools import product
from math import gcd

def noble(p, minlen=50000):
    s='0'
    while len(s)<minlen:
        s=''.join(('0'*p+'1' if c=='0' else '0') for c in s)
    return s

def expected(q,h,p,n):
    if n==0: return 1, 1
    if n<=h:
        return q**n, (q**n+q**((n+1)//2))//2
    m=n-h
    factor=q**h*(m+1)
    f=gcd(2,h) if (n-1)%gcd(2,h)==0 else 0
    same=q**((h+f)//2)
    return factor,factor-(q**h-same)//2 if m<=p+1 else factor

def test(p,q,h,maxn):
    seq=noble(p)
    languages={m:{seq[i:i+m] for i in range(len(seq)-m+1)} for m in range(1,maxn-h+1)}
    for n in range(1,maxn+1):
        if n<=h:
            factors={''.join(w) for w in product('0123456789'[:q],repeat=n)}
        else:
            factors=set()
            m=n-h
            for s in languages[m]:
                for start in product(range(q), repeat=h):
                    out=list(start)
                    for j,c in enumerate(s):
                        out.append((out[j]+int(c))%q)
                    factors.add(''.join(str(t) for t in out))
        reflected={min(w,w[::-1]) for w in factors}
        got=(len(factors),len(reflected))
        want=expected(q,h,p,n)
        assert got==want,(p,q,h,n,got,want)
    return True

if __name__=='__main__':
    count=0
    for p in (1,2,3):
      for q in (3,4):
       for h in (1,2,3):
        test(p,q,h,8)
        count+=1
    print(f'PASS {count} parameter triples, each n=1,...,8, explicit factors and reflections')
    print('Examples (p=1,q=3,h=3):', [expected(3,3,1,n)[1] for n in range(0,9)])

def test_periodic_base(period, q, h, maxn=8):
    # Exact finite language of a periodic orbit, via all cyclic starts.
    def language(m):
        if m==0: return {''}
        return {''.join(period[(j+i)%len(period)] for i in range(m)) for j in range(len(period))}
    for n in range(1,maxn+1):
        if n<=h:
            factors={''.join(w) for w in product('0123456789'[:q],repeat=n)}
            expected_f=q**n
            expected_r=(q**n+q**((n+1)//2))//2
        else:
            m=n-h
            factors=set()
            L=language(m)
            for s in L:
                for u in product(range(q),repeat=h):
                    w=list(u)
                    for i,v in enumerate(s):w.append((w[i]+int(v))%q)
                    factors.add(''.join(map(str,w)))
            expected_f=q**h*len(L)
            f=gcd(2,h) if (n-1)%gcd(2,h)==0 else 0
            expected_r=expected_f-((q**h-q**((h+f)//2))//2 if '0'*m in L else 0)
        assert (len(factors),len({min(w,w[::-1]) for w in factors}))==(expected_f,expected_r), (period,q,h,n)

if __name__=='__main__':
    periodic_cases=0
    for base in ('01','001','0001','010110','1'):
        for q in (3,4):
            for h in (1,2,3):
                test_periodic_base(base,q,h)
                periodic_cases+=1
    print(f'PASS {periodic_cases} periodic-base triples, each n=1,...,8, exact cyclic languages')
