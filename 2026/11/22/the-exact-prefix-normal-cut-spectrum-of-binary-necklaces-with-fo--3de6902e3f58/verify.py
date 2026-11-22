#!/usr/bin/env python3
"""Exact rational certificates and direct tests for weight-four prefix-normal cuts.
Pure Python standard library. This computes the symbolic finite weak-order table,
not a numerical fit, and separately enumerates literal substring inequalities.
"""
from collections import Counter, defaultdict
from itertools import product


def mul(p, q):
    out = [0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):
            out[i+j] += a*b
    return out


def add(p,q):
    out = [0]*max(len(p),len(q))
    for i,a in enumerate(p): out[i]+=a
    for j,b in enumerate(q): out[j]+=b
    return out


def short(p):
    p=list(p)
    while p and p[-1]==0: p.pop()
    return p


def fac(s):
    p=[0]*(s+1); p[0]=1; p[s]=-1
    return p


def root_count(g):
    return sum(g[i]<=g[(i+1)%4] and g[i]<=g[(i+2)%4] for i in range(4))


def classes():
    for k in range(1,5):
        for h in product(range(k),repeat=4):
            if set(h)==set(range(k)):
                yield h


def cert():
    # For each surjective relative-order pattern h, the gap tuple has
    # distinct levels t0<...<t_{k-1}; t0>=0, t_j-t_{j-1}>=1.
    # Hence sum of four gaps = 4*t0 + sum_{j=1}^{k-1} b_j*(1+e_j),
    # with b_j the population in levels j,...,k-1.
    # Multiply each contribution by D=(1-z)(1-z^2)(1-z^3)(1-z^4).
    table=Counter(); P={j:[] for j in range(1,5)}
    for h in classes():
        table[root_count(h)]+=1
        k=max(h)+1
        b=[sum(x>=j for x in h) for j in range(1,k)]
        den={4,*b}
        assert len(den)==len(b)+1
        poly=[1]
        for s in (1,2,3,4):
            if s not in den: poly=mul(poly,fac(s))
        poly=[0]*sum(b)+poly
        j=root_count(h)
        P[j]=add(P[j],poly)
    assert sum(table.values())==75
    assert table==Counter({1:28,2:42,3:4,4:1}),table
    expected={
       1:mul([0,0,0,0,4],mul([1,1],[1,1])),
       2:mul([0,0,2],mul([1,1],[3,2,0,-3])),
       3:mul([0,4],mul(mul([1,-1],[1,-1]),mul([1,1],[1,1,1]))),
       4:mul(mul(mul([1,-1],[1,-1]),[1,-1]),mul([1,1],[1,1,1])),
    }
    for j in range(1,5):
        assert short(P[j])==short(expected[j]),(j,short(P[j]),short(expected[j]))
    return table, {j:short(P[j]) for j in P}


def cyc(g):
    return min(g[i:]+g[:i] for i in range(4))


def pn(word):
    n=len(word)
    prefix=0
    for ell in range(1,n+1):
        prefix += word[ell-1]
        if prefix < max(sum(word[i:i+ell]) for i in range(n-ell+1)):
            return False
    return True


def coefficient_D_inverse(cap):
    arr=[1]+[0]*cap
    for j in (1,2,3,4):
        for i in range(j,cap+1):
            arr[i]+=arr[i-j]
    return arr


def GF_count(j,n,P,inv):
    m=n-4
    S=sum(a*inv[m-i] for i,a in enumerate(P[j]) if i<=m)
    # Shift 2 invariant tuple (a,b,a,b). Non-constant pairs have 2 roots;
    # a=b has four roots. One tuple per a+b=(n-4)/2.
    sh2=0
    if n%2==0:
        t=(n-4)//2
        if j==2: sh2=t+1-int(t%2==0)
        if j==4: sh2=int(t%2==0)
    sh13=2*int(j==4 and n%4==0)
    value=S+sh2+sh13
    assert value%4==0,(j,n,value)
    return value//4


def test():
    table,P=cert()
    print('WEAK_ORDER_TABLE',dict(sorted(table.items())))
    print('RATIONAL_CERTIFICATE_NUMERATORS',P)
    cap=22; inv=coefficient_D_inverse(cap)
    bysize=[]
    for n in range(4,21):
        m=n-4
        cnt=Counter(); tested=0
        for a in range(m+1):
            for b in range(m-a+1):
                for c in range(m-a-b+1):
                    d=m-a-b-c
                    g=(a,b,c,d)
                    if g!=cyc(g):continue
                    w=[]
                    for x in g: w.extend([1]+[0]*x)
                    brute=sum(pn(w[i:]+w[:i]) for i,s in enumerate(w) if s==1)
                    assert brute==root_count(g),(n,g,brute,root_count(g))
                    cnt[brute]+=1; tested+=1
        rhs={r:GF_count(r,n,P,inv) for r in range(1,5)}
        assert all(cnt[r]==rhs[r] for r in range(1,5)),(n,cnt,rhs)
        bysize.append((n, tuple(cnt[j] for j in range(1,5))))
    print('NECKLACE_COUNTS_N4_TO20',bysize)
    assert bysize[0]==(4,(0,0,0,1))
    assert bysize[1]==(5,(0,0,1,0))
    assert bysize[-1][0]==20
    print('VERIFY_OK: 75 exhaustive weak orders, exact polynomial identity, and every four-one necklace length 4..20 checked by literal factor inequalities')

if __name__=='__main__':test()
