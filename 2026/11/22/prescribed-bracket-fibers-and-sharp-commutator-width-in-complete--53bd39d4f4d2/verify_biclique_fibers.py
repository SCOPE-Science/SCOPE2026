#!/usr/bin/env python3
"""Direct finite-field verification for complete bipartite graphical Lie brackets."""
from itertools import product
from collections import Counter


def multiply(a,b,q):
    if q==4:
        # GF(2)[t]/(t*t+t+1), elements represented by binary coefficients.
        z=0
        for i in range(2):
            if (b>>i)&1:
                z ^= a<<i
        if z&8:
            z ^= 0b1100
        if z&4:
            z ^= 0b111
        return z
    return (a*b)%q

def add(a,b,q):
    return (a^b) if q==4 else (a+b)%q

def negate(a,q):
    return a if q==4 else (-a)%q

def inv(a,q):
    if not a: raise ZeroDivisionError
    return next(i for i in range(1,q) if multiply(a,i,q)==1)

def rank(M,a,b,q):
    # Reduced elimination independent of the counting formulas.
    rows=[list(M[i*b:(i+1)*b]) for i in range(a)]
    r=0
    for j in range(b):
        k=next((k for k in range(r,a) if rows[k][j]),None)
        if k is None: continue
        rows[r],rows[k]=rows[k],rows[r]
        t=inv(rows[r][j],q)
        rows[r]=[multiply(t,z,q) for z in rows[r]]
        for k in range(a):
            if k!=r and rows[k][j]:
                t=rows[k][j]
                rows[k]=[add(x,negate(multiply(t,y,q),q),q) for x,y in zip(rows[k],rows[r])]
        r+=1
        if r==a: break
    return r

def rank_count(a,b,r,q):
    if r==0: return 1
    if r>min(a,b): return 0
    numerator=1
    denominator=1
    for i in range(r):
        numerator*= (q**a-q**i)*(q**b-q**i)
        denominator*=q**r-q**i
    assert numerator%denominator==0
    return numerator//denominator

def predicted(a,b,r,q):
    if r>2: return 0
    if r==2: return (q*q-1)*(q*q-q)
    if r==1: return (q*q-1)*(q**a+q**b-q)
    return q**(2*b)+(q+1)*(q**a-1)*q**b+(q**a-1)*(q**a-q)

def direct(a,b,q):
    out=Counter()
    # For input x and y, bracket coefficient of (i,j) is x_U[i]*y_W[j]-y_U[i]*x_W[j].
    for x in product(range(q),repeat=a+b):
        for y in product(range(q),repeat=a+b):
            M=tuple(add(multiply(x[i],y[a+j],q),negate(multiply(y[i],x[a+j],q),q),q)
                for i in range(a) for j in range(b))
            out[M]+=1
    return out

def check(a,b,q):
    f=direct(a,b,q)
    counts=Counter()
    for M in product(range(q),repeat=a*b):
        r=rank(M,a,b,q)
        counts[r]+=1
        assert f[M]==predicted(a,b,r,q), (a,b,q,M,r,f[M],predicted(a,b,r,q))
    assert sum(f.values())==q**(2*(a+b))
    assert all(counts[r]==rank_count(a,b,r,q) for r in range(min(a,b)+1))
    assert sum(rank_count(a,b,r,q)*predicted(a,b,r,q) for r in range(min(a,b)+1))==q**(2*(a+b))
    print('PASS',a,b,q,'targets',sum(counts.values()),'ranks',dict(counts),'fibers',dict((r,predicted(a,b,r,q)) for r in sorted(counts)),'vertex_pairs',sum(f.values()))

if __name__=='__main__':
    for args in [(2,2,2),(2,3,2),(3,2,2),(3,3,2),(2,2,3),(2,3,3),(2,2,4)]:
        check(*args)
    print('BICLIQUE_LIE_BRACKET_FIBERS_OK 7')
