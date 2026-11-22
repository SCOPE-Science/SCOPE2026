#!/usr/bin/env python3
"""Independent exact finite checks of Fibonacci power-index residue theorem.
This program supplies finite tests, not proof of the infinite claim.
"""
from collections import Counter

Q = ((1, 1), (1, 0))

def mm(a, b, p):
    return tuple(tuple(sum(a[i][t]*b[t][j] for t in range(2)) % p for j in range(2)) for i in range(2))

def mpow(a, n, p):
    ans=((1,0),(0,1))
    while n:
        if n&1: ans=mm(ans,a,p)
        a=mm(a,a,p)
        n//=2
    return ans

def fiblist(m):
    out=[]; a,b=0,1
    for j in range(4*m):
        out.append(a);a,b=b,(a+b)%m
    assert (a,b)==(0,1)
    return out

def expected(d,k):
    m=5**k
    counts={0:4*5**(k-(k+d-1)//d)}
    for y in range(1,m):
        t=y;v=0
        while t%5==0:t//=5;v+=1
        if v%d:continue
        if d%4==0 and t%5 not in (1,2):continue
        a=v//d
        counts[y]=(8 if d%4==0 else 4)*5**((d-1)*a)
    return counts

def run():
    checks=0; maxperiod=0
    B=((4,3),(3,1))
    q20=mpow(Q,20,25)
    assert q20==((21,15),(15,6));checks+=1
    assert mm(mpow(Q,4,5),B,5)==B;checks+=1
    slopes=[mm(mpow(Q,r,5),B,5)[0][1] for r in range(4)]
    assert slopes==[3,4,2,1];checks+=1
    c=[2,1,3,4]
    fib=fiblist(5)
    for n in range(20):
        assert fib[n] == c[n%4]*n%5;checks+=1
    scenarios=[(d,k) for d in range(1,19) if d%5 for k in range(1,5)] + [(d,5) for d in (1,2,3,4,6,7,8,9,11,12)]
    for d,k in scenarios:
        mod=5**k; cycle=4*mod;seq=fiblist(mod)
        obs=Counter(seq[pow(n,d,cycle)] for n in range(cycle))
        exp=expected(d,k)
        assert obs==exp,('fiber mismatch',d,k,[(y,obs.get(y),exp.get(y)) for y in range(mod) if obs.get(y)!=exp.get(y)][:5]);checks+=mod
        period=(4 if d%2 else 2)*mod
        for i in range(cycle):
            assert seq[pow(i,d,cycle)]==seq[pow((i+period)%cycle,d,cycle)];checks+=1
        if k<=3:
            for t in range(1,period):
                # A single failure disproves t as a period.
                if all(seq[pow(n,d,cycle)] == seq[pow((n+t)%cycle,d,cycle)] for n in range(min(60,period))):
                    # Exhaust all positions, to preclude a false short-period claim.
                    assert any(seq[pow(n,d,cycle)] != seq[pow((n+t)%cycle,d,cycle)] for n in range(cycle)),('short period',d,k,t)
                checks+=1
        maxperiod=max(maxperiod,period)
    print('PASS: %s exact assertions across %s (exponent, depth) scenarios; maximum tested period %s' %(checks,len(scenarios),maxperiod))

if __name__=='__main__':run()
