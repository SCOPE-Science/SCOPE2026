#!/usr/bin/env python3
"""Two exhaustive token constructions and fixed-seed reproducible diagnostics.

Tokens are the mathematical (string, split) descriptors; the terminal split is 0.
Requires Python 3.9+ standard library only.
"""
from itertools import groupby, product
from random import Random
from fractions import Fraction


def peel_tokens(word):
    x='@'+word+'$'
    lo,hi=0,len(x)
    out=[]
    while lo<hi:
        u=lo+1
        while u<hi and x[u]==x[lo]:u+=1
        if u==hi:
            out.append((x[lo:hi],0));break
        v=hi-1
        while v>u and x[v-1]==x[hi-1]:v-=1
        tok=x[lo:u]+x[v:hi]
        if u>=v:
            out.append((tok,0));break
        out.append((tok,u-lo))
        lo,hi=u,v
    return out


def pairing_tokens(word):
    runs=[(char,len(list(g))) for char,g in groupby(word)]
    output=[('@$',1)]
    r=len(runs)
    for i in range((r+1)//2):
        if i<(r+1)//2-1:
            (a,x),(b,y)=runs[i],runs[r-i-1]
            output.append((a*x+b*y,x))
        elif r%2:
            a,x=runs[i]
            output.append((a*x,0))
        else:
            (a,x),(b,y)=runs[i],runs[i+1]
            output.append((a*x+b*y,0))
    return output


def hamming_prefix(A,B):
    # Sentinel is invariant and excluded; no penalty for an unmatched final token.
    return sum(a!=b for a,b in zip(A[1:],B[1:]))


def test_exhaustive(max_n=14):
    nwords=nflips=0
    averages=[]
    for n in range(1,max_n+1):
        total=0; trials=0
        for tup in product('01',repeat=n):
            w=''.join(tup)
            a=peel_tokens(w);b=pairing_tokens(w)
            assert a==b,(n,w,a,b)
            nwords+=1
            for p in range(1,n-1):
                other=w[:p]+str(1-int(w[p]))+w[p+1:]
                c=peel_tokens(other);d=pairing_tokens(other)
                assert c==d,(n,other,c,d)
                v=hamming_prefix(a,c)
                r=len(list(groupby(w)));s=len(list(groupby(other)))
                assert abs(s-r) in (0,2)
                if r==s: assert v<=2,(w,p,v)
                total+=v;trials+=1;nflips+=1
        if trials:averages.append((n,Fraction(total,trials)))
    print('Exact test: verified both token implementations on',nwords,'binary source words')
    print('Exact test: verified',nflips,'directed interior bit-flip pairs')
    print('Exact mean discrepancies at lengths 8,10,12,14:',
          [(n,str(v)) for n,v in averages if n in (8,10,12,14)])


def test_simulation(seed=20261121):
    rng=Random(seed)
    for n,trials in ((256,3000),(1024,3000),(4096,3000)):
        total=0; bad=0; values=[]
        for _ in range(trials):
            w=''.join('1' if rng.getrandbits(1) else '0' for _ in range(n))
            p=rng.randrange(1,n-1)
            a=pairing_tokens(w)
            z=w[:p]+('0' if w[p]=='1' else '1')+w[p+1:]
            b=pairing_tokens(z)
            v=hamming_prefix(a,b)
            total+=v
            if len(a)!=len(b):
                bad+=1;values.append(v/n)
        values.sort()
        med=values[len(values)//2]
        print('Monte Carlo n=',n,'trials=',trials,
              'mean H/n=',round(total/(n*trials),7),
              'skeleton-change fraction=',round(bad/trials,5),
              'conditional median H/n=',round(med,6))
    print('Analytical prediction: mean H/n -> 1/24 =',1/24,
          '; conditional change-law median -> 1/12 =',1/12)

if __name__=='__main__':
    test_exhaustive()
    test_simulation()
