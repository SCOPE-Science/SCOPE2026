#!/usr/bin/env python3
"""Exact finite checks and independent Markov calculations for the two-lag tree Kemeny law.

The infinite probabilistic limits require the analytic argument in RESULT.md.
"""
from fractions import Fraction
from itertools import product
from collections import deque
from math import ceil, floor

CHECKS=0

def check(x, label=''):
    global CHECKS
    if not x:
        raise AssertionError(label)
    CHECKS+=1

def make_tree(bits):
    """bits[k-2] is 1 if vertex k attaches to k-1, else to k-2."""
    par=[-1, 0]
    for k,b in enumerate(bits,start=2):
        par.append(k-1 if b else k-2)
    return par

def kemeny_cut(par):
    n=len(par)
    sizes=[1]*n
    for k in range(n-1,0,-1):
        sizes[par[k]]+=sizes[k]
    return Fraction(sum((2*sizes[k]-1)*(2*(n-sizes[k])-1) for k in range(1,n)),2*(n-1))

def wiener_cut(par):
    n=len(par); sizes=[1]*n
    for k in range(n-1,0,-1): sizes[par[k]]+=sizes[k]
    return sum(sizes[k]*(n-sizes[k]) for k in range(1,n))

def path_k(n):
    return Fraction(2*n*n-4*n+3,6)

def one_event(n,k):
    b=[0]*(n-2); b[k-2]=1
    return make_tree(b)

def distances(par):
    n=len(par); adj=[[] for _ in range(n)]
    for i in range(1,n):
        adj[i].append(par[i]); adj[par[i]].append(i)
    d=[]
    for start in range(n):
        row=[-1]*n;row[start]=0;todo=deque([start])
        while todo:
            u=todo.popleft()
            for v in adj[u]:
                if row[v]<0:row[v]=row[u]+1;todo.append(v)
        d.append(row)
    return d

def exact_markov_k(par):
    # Independently solve hitting-time equations over the rationals.
    from sympy import Matrix, Rational
    n=len(par); adj=[[] for _ in range(n)]
    for i in range(1,n):
        adj[i].append(par[i]);adj[par[i]].append(i)
    deg=[len(s) for s in adj]
    stat=[Fraction(d,2*(n-1)) for d in deg]
    total=Fraction(0)
    for dest in range(n):
        allowed=[i for i in range(n) if i!=dest]
        row={v:i for i,v in enumerate(allowed)}
        a=Matrix.zeros(n-1,n-1)
        rhs=Matrix.ones(n-1,1)
        for i in allowed:
            a[row[i],row[i]]=1
            for j in adj[i]:
                if j!=dest:
                    a[row[i],row[j]]-=Rational(1,deg[i])
        h=a.inv()*rhs
        if dest!=0:
            total+=stat[dest]*Fraction(h[row[0]])
    return total

def check_one_case(bits):
    n=len(bits)+2
    p=make_tree(bits)
    mat=distances(p)
    w=sum(mat[i][j] for i in range(n) for j in range(i+1,n))
    check(w==wiener_cut(p),'wiener direct vs edge cut')
    k=kemeny_cut(p)
    check(k==Fraction(2*w,n-1)-n+Fraction(1,2),'K-W relation')
    deg=[0]*n
    for i in range(1,n):deg[i]+=1;deg[p[i]]+=1
    for j in range(n-1):
        expected=2*(j+1)-(bits[j] if j<=n-3 else 1)
        # For prefix j, crossing edge j+2 uses bits[(j+2)-2]=bits[j].
        check(sum(deg[:j+1])==expected,'degree-prefix identity')
    depth=[0]*n
    for i in range(1,n):depth[i]=depth[p[i]]+1
    # The quantitative pathwise bound applies to any chosen mu in [1,2].
    for mu in (Fraction(1),Fraction(3,2),Fraction(2)):
        Delta=max(abs(Fraction(depth[j])-Fraction(j,1)/mu) for j in range(n))
        mx=1
        for j in range(1,n):mx=max(mx,mat[j][j-1])
        err=abs(k/Fraction(n*n)-Fraction(1,3)/mu)
        check(err <= (1+2*Delta+2*mx)/n,'deterministic K error bound')
    if n<=6:
        check(k==exact_markov_k(p),'independent rational hitting systems')

def main():
    for n in range(2,12):
        for bits in product((0,1),repeat=n-2):
            check_one_case(bits)
    for n in range(3,100):
        for k in range(2,n):
            a=k-1; b=(n-k+1)//2; c=(n-k)//2
            v=one_event(n,k)
            exact=path_k(n)-kemeny_cut(v)
            check(exact==Fraction(2*a*b*c,n-1),'one-event tripod exact penalty')
    # Direct finite triple-armed formula, also covering degenerate arm lengths.
    for a in range(0,12):
        for b in range(0,12):
            for c in range(0,12):
                if a+b+c<1:continue
                n=1+a+b+c
                W=sum(t*(n-t) for l in (a,b,c) for t in range(1,l+1))
                check(Fraction(2*W,n-1)-n+Fraction(1,2)==path_k(n)-Fraction(2*a*b*c,n-1),'tripod identity')
    # Non-asymptotic finite comparison to its critical limit; these are diagnostics.
    for n in (100,200,500,1000):
        for fraction in (Fraction(1,5),Fraction(1,3),Fraction(1,2),Fraction(4,5)):
            k=max(2,min(n-1,n*fraction.numerator//fraction.denominator))
            v=one_event(n,k)
            x=Fraction(k,n)
            limit=Fraction(1,3)-x*(1-x)**2/2
            check(abs(kemeny_cut(v)/Fraction(n*n)-limit)<Fraction(4,n),'critical conditional finite approximation')
    print('VERIFICATION_OK assertions='+str(CHECKS))

if __name__=='__main__': main()
