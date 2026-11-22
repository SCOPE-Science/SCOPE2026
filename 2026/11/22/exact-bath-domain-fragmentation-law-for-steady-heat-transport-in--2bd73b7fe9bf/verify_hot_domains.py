#!/usr/bin/env python3
"""Standalone exact checker for finite patterned-bath kinetic Ising rings.
Uses only Python standard-library rational arithmetic. The theorem for all sizes
is proved in RESULT.md; these calculations are independent finite checks.
"""
from fractions import Fraction as F
from itertools import combinations, product

def solve(A,b):
    n=len(b)
    A=[list(row)+[b[i]] for i,row in enumerate(A)]
    for j in range(n):
        p=next(i for i in range(j,n) if A[i][j])
        if p!=j:A[j],A[p]=A[p],A[j]
        v=A[j][j]
        for k in range(j,n+1):A[j][k]/=v
        for i in range(j+1,n):
            v=A[i][j]
            if v:
                for k in range(j+1,n+1):A[i][k]-=v*A[j][k]
                A[i][j]=F(0)
    x=[F(0)]*n
    for i in range(n-1,-1,-1):
        x[i]=A[i][-1]-sum((A[i][k]*x[k] for k in range(i+1,n)),F(0))
    return x

def blocks(bits):
    n=len(bits)
    if not (1 in bits and 0 in bits):return []
    return [sum(1 for k in range(1,n+1) if all(bits[(i+j)%n]==1 for j in range(1,k+1))) for i in range(n) if bits[i]==0 and bits[(i+1)%n]==1]

def alpha_l(l,g):
    a=F(0); alpha=g/4
    for _ in range(l):a=alpha/(1-alpha*a)
    return a

def flux_pred(bits,g):return 2*sum((alpha_l(l,g) for l in blocks(bits)),F(0))

def flux_full(bits,g):
    n=len(bits); count=1<<n
    rates=[F(0) if b==0 else g for b in bits]
    # Row balance: sum_{states} p(state)*Q(state, next) = 0.
    M=[[F(0) for _ in range(count)] for __ in range(count)];rhs=[F(0)]*count
    for x in range(count):
        s=[1 if x & (1<<i) else -1 for i in range(n)]
        for i in range(n):
            w=(1-rates[i]*s[i]*(s[(i-1)%n]+s[(i+1)%n])/2)/2
            y=x^(1<<i)
            M[y][x]+=w;M[x][x]-=w
    M[-1]=[F(1)]*count;rhs[-1]=F(1)
    p=solve(M,rhs)
    assert sum(p)==1 and all(t>0 for t in p)
    # Energy gain on hot-spin flips, with J=1 and rate 1/2.
    return sum((p[x]*sum((s[i]*(s[(i-1)%n]+s[(i+1)%n]) for i in range(n) if bits[i]==0),0) for x in range(count) for s in [[1 if x&(1<<i) else -1 for i in range(n)]]),F(0))

def flux_pairs(bits,g):
    n=len(bits);pairs=list(combinations(range(n),2));loc={x:i for i,x in enumerate(pairs)};m=len(pairs)
    A=[[F(0)]*m for _ in range(m)];rhs=[F(0)]*m
    gam=[g if b else F(0) for b in bits]
    for k,(i,j) in enumerate(pairs):
        A[k][k]=F(2)
        for site,other in [(i,j),(j,i)]:
            for dest in ((site-1)%n,(site+1)%n):
                if dest==other:rhs[k]+=gam[site]/2
                else:A[k][loc[tuple(sorted((dest,other)))]]-=gam[site]/2
    C=solve(A,rhs)
    def cor(i,j):
        if i==j:return F(1)
        return C[loc[tuple(sorted((i,j)))]]
    return sum((cor(i,(i-1)%n)+cor(i,(i+1)%n) for i,b in enumerate(bits) if b==0),F(0))

def main():
    g=F(3,5)
    for pattern in ['00111','01011','000111','010101','001011','00101011']:
        bits=[int(c) for c in pattern]
        if len(bits)>7: continue
        predicted=flux_pred(bits,g)
        assert flux_full(bits,g)==predicted,(pattern,flux_full(bits,g),predicted)
        assert flux_pairs(bits,g)==predicted
        print('full-state rational:',pattern,str(predicted),'PASS')
    counts=0
    for n in range(4,9):
        for h in range(2,n):
            c=n-h
            rmax=min(c,h)
            lo=2*alpha_l(c,g)
            q,rem=divmod(c,rmax)
            hi=2*((rmax-rem)*alpha_l(q,g)+rem*alpha_l(q+1,g))
            found=[]
            for hot in combinations(range(n),h):
                bits=[int(i not in hot) for i in range(n)]
                actual=flux_pairs(bits,g)
                assert actual==flux_pred(bits,g)
                found.append(actual)
                counts+=1
            assert min(found)==lo and max(found)==hi,(n,h,min(found),max(found),lo,hi)
    print('exact stationary pair solutions and all extrema:',counts,'patterns PASS')
    # Check strict discrete concavity and refinement for a rational cold bath.
    a=[alpha_l(k,F(7,9)) for k in range(16)]
    assert all(a[k+1]>a[k] for k in range(1,15))
    assert all(a[k+1]-a[k]<a[k]-a[k-1] for k in range(1,15))
    assert all(a[p+q]<a[p]+a[q] for p in range(1,8) for q in range(1,8))
    print('rational monotonicity/concavity/subadditivity through length 15 PASS')
if __name__=='__main__':main()
