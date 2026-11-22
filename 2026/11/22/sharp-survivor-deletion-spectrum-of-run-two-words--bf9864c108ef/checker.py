#!/usr/bin/env python3
"""Independent exhaustive and finite-state checks for a run-limited deletion theorem.

No third-party dependencies; run: python checker.py
"""
from collections import Counter, defaultdict
from itertools import product
from math import ceil


def allowed(x):
    return all(not (x[i] == x[i+1] == x[i+2]) for i in range(len(x)-2))


def actual_degree(x):
    return len({x[:i]+x[i+1:] for i in range(len(x)) if allowed(x[:i]+x[i+1:])})


def run_degree(x):
    runs=[]
    for a in x:
        if runs and runs[-1][0]==a:
            runs[-1]=(a,runs[-1][1]+1)
        else:
            runs.append((a,1))
    if not x:
        raise ValueError('nonempty input needed')
    assert all(length <= 2 for _,length in runs)
    ans=0
    for i,(a,length) in enumerate(runs):
        bad=(0<i<len(runs)-1 and length==1 and
             runs[i-1][0]==runs[i+1][0] and
             (runs[i-1][1]==2 or runs[i+1][1]==2))
        ans+=int(not bad)
    return ans


def transfer_polynomials(q,n_max):
    """Exact coefficient enumeration using 4 run-pair transfer states."""
    out=[Counter() for _ in range(n_max+1)]
    for a in (1,2):
        if a<=n_max:
            out[a][1]+=q
    states=defaultdict(int)
    for a,b in product((1,2),repeat=2):
        if a+b<=n_max:
            states[(a+b,a,b,2)]+=q*(q-1)
    for length in range(2,n_max+1):
        current=[(key,coef) for key,coef in states.items() if key[0]==length]
        for (_,a,b,d),coef in current:
            out[length][d]+=coef
            for c in (1,2):
                if length+c>n_max:continue
                risky=(b==1 and (a==2 or c==2))
                if risky:
                    states[(length+c,b,c,d)]+=coef
                    if q>2:states[(length+c,b,c,d+1)]+=coef*(q-2)
                else:
                    states[(length+c,b,c,d+1)]+=coef*(q-1)
    return out


def witness(d,short=0):
    """Length 4d-2 canonical extremal, or one of its shortened variants."""
    if d==1:
        return (0,)*max(1,2-short)
    lengths=[2]+[v for _ in range(d-1) for v in (1,1,2)]
    if short==1:
        # Delete the last singleton in the final (1,1,2) block.
        lengths.pop(-2)
    else:
        return tuple(i%2 for i,l in enumerate(lengths) for _ in range(l))[:4*d-2-short]
    return tuple(i%2 for i,l in enumerate(lengths) for _ in range(l))


def run():
    cases=((2,16),(3,10),(4,8))
    count=0
    for q,maximum in cases:
        expected=transfer_polynomials(q,maximum)
        for n in range(1,maximum+1):
            counts=Counter()
            for x in product(range(q),repeat=n):
                if not allowed(x):continue
                assert run_degree(x)==actual_degree(x), (q,n,x)
                counts[actual_degree(x)]+=1
                count+=1
            assert counts==+expected[n],(q,n,counts,expected[n])
            minimum=ceil((n+2)/4)
            assert min(counts)==minimum,(q,n,counts)
            assert max(counts)==n,(q,n,counts)
            assert counts[n]==q*(q-1)**(n-1),(q,n,counts)
            if n>=2 and (n+2)%4==0:
                assert counts[minimum]==q*(q-1)**(minimum-1),(q,n,counts)
        print(f'q={q}, lengths=1..{maximum}: exact transfer law and all claimed extrema OK')
    for d in range(1,18):
        for short in range(4):
            n=4*d-2-short
            if n<1:continue
            x=witness(d,short)
            assert len(x)==n,(d,short,n,x)
            assert allowed(x) and actual_degree(x)==d,(d,short,x,actual_degree(x))
    print('Canonical extremal/shortened witnesses: degrees 1..17 OK')
    print('Exhaustive source words checked:',count)


if __name__=='__main__':
    run()
