#!/usr/bin/env python3
"""Standalone exact checks of threshold-graph sibling/tuft distributions."""
from itertools import product
from collections import Counter
from fractions import Fraction

def geometric(n):
    # lists of coefficients through z^n
    return [1]*(n+1)

def conv(a,b,n):
    c=[0]*(n+1)
    for i,u in enumerate(a[:n+1]):
        if u:
            for j,v in enumerate(b[:n-i+1]):
                if v:c[i+j]+=u*v
    return c

def gf_formula(S,T,N):
    z=lambda k: [int(i==k) for i in range(N+1)]
    def j(h):return [int(1<=i<=h) for i in range(N+1)]
    def r(h):return [int(2<=i<=h) for i in range(N+1)]
    def mul(a,b):return conv(a,b,N)
    def add(*polys):return [sum(p[i] for p in polys) for i in range(N+1)]
    def shift(p,k):return [0]*k+p[:N+1-k] if k<=N else [0]*(N+1)
    zz=geometric(N)
    A=add(shift(j(S),1),shift(mul(zz,j(S+1)),2))
    B=shift(mul(zz,j(S+1)),1)
    C=add(shift(mul(zz,r(S+1)),1),shift(j(T),1))
    Aend=add(shift(r(S),1),shift(mul(zz,r(S+1)),2),shift(r(T),1))
    # A*C*(1+B+B^2+...)
    q=[1]+[0]*N
    den=[0]*(N+1); den[0]=1
    # inverse 1/(1-B), B[0]=0
    for i in range(1,N+1):den[i]=sum(B[j]*den[i-j] for j in range(1,i+1))
    return add(Aend,mul(mul(A,C),den))

def graph_stats(bits):
    n=len(bits);adj=[set() for _ in range(n)]
    for j in range(1,n):
        if bits[j]:
            for i in range(j):adj[i].add(j);adj[j].add(i)
    sibling=max(sum(adj[i]|{i}==adj[j]|{j} for j in range(n))-1 for i in range(n))
    leaves=[i for i in range(n) if len(adj[i])==1]
    tuft=max(sum(j in leaves for j in adj[i]) for i in range(n))
    return sibling,tuft

def runs_stats(bits):
    runs=[]
    for b in bits:
        if runs and runs[-1][0]==b:runs[-1]=(b,runs[-1][1]+1)
        else:runs.append((b,1))
    q=len(runs)//2
    s=max(runs[2*i+1][1]-1+int(i==0 and runs[0][1]==1) for i in range(q))
    t=runs[-2][1] if runs[-1][1]==1 else 0
    return s,t

def main():
    all_stats={}
    for n in range(3,14):
        d=Counter()
        for mid in product((0,1),repeat=n-2):
            bits=(0,)+mid+(1,)
            a=graph_stats(bits);b=runs_stats(bits)
            assert a==b,(n,bits,a,b)
            d[a]+=1
        all_stats[n]=d
        assert sum(d.values())==2**(n-2)
        assert sum(c for (s,t),c in d.items() if t==0)==2**(n-3)
        assert sum(t*c for (s,t),c in d.items())==2**(n-2)
        assert sum((t-1)**2*c for (s,t),c in d.items())==2**(n-2)*(Fraction(2)-Fraction(1,2**(n-3)))
    # coefficient-accurate independent dynamic composition checks all (S,T) small
    for S in range(0,7):
        for T in range(0,7):
            coeff=gf_formula(S,T,13)
            for n,d in all_stats.items():
                want=sum(c for (s,t),c in d.items() if s<=S and t<=T)
                assert coeff[n]==want,(n,S,T,coeff[n],want)
    f0,f1=0,1
    fib=[0,1]
    for i in range(2,20):fib.append(fib[-1]+fib[-2])
    for n,d in all_stats.items():
        assert sum(c for (s,t),c in d.items() if s==0)==fib[n-2]
    print('GRAPH_NEIGHBORHOOD_AND_RUN_STATISTICS_PASS n=3..13 graphs=',sum(2**(n-2) for n in range(3,14)))
    print('BOUNDED_JOINT_GENERATING_FUNCTION_PASS S,T=0..6 n=3..13 cases=',49*11)
    print('EXACT_MARGINAL_AND_TUFT_MOMENT_IDENTITIES_PASS n=3..13')
    print('VERIFY_OK')

if __name__=='__main__':main()
