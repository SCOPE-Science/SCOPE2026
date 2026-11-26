#!/usr/bin/env python3
"""Independent graph-neighborhood and inclusion-exclusion checks for total domination of 2-token bicliques."""
from itertools import combinations
from math import comb, factorial


def plus(*args):
    size=max(map(len,args)); return [sum(p[i] for p in args if i<len(p)) for i in range(size)]

def sub(a,b): return plus(a,[-v for v in b])
def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def binpoly(n):return [comb(n,k) for k in range(n+1)]

def edge_cover(t):
    p=[0]*(comb(t,2)+1)
    for i in range(t+1):
        c=(-1)**i*comb(t,i)
        for k,v in enumerate(binpoly(comb(t-i,2))):p[k]+=c*v
    return p

def nonempty_both(a,b):
    p=[0]*(a*b+1)
    for i in range(a+1):
        for j in range(b+1):
            coeff=(-1)**(i+j)*comb(a,i)*comb(b,j)
            for k,v in enumerate(binpoly((a-i)*(b-j))):p[k]+=coeff*v
    return p

def predicted(m,n):
    em,en=edge_cover(m),edge_cover(n)
    U=sub(plus(mul(em,binpoly(comb(n,2))),mul(en,binpoly(comb(m,2)))),mul(em,en))
    B=plus(nonempty_both(m,n),[m*x for x in nonempty_both(m-1,n)],
           [n*x for x in nonempty_both(m,n-1)],[m*n*x for x in nonempty_both(m-1,n-1)])
    return mul(U,B)

def actual(m,n):
    vs=list(combinations(range(m+n),2))
    U=[i for i,v in enumerate(vs) if (v[0]<m)==(v[1]<m)]
    B=[i for i in range(len(vs)) if i not in U]
    neighbors=[[] for v in vs]
    for i,p in enumerate(vs):
        for j,q in enumerate(vs):
            if i==j:continue
            diff=set(p)^set(q)
            if len(diff)==2 and (min(diff)<m<=max(diff)):
                neighbors[i].append(j)
    def counts(side,targets):
        toidx={v:i for i,v in enumerate(targets)}
        adj=[]
        for v in side:
            adj.append(sum(1<<toidx[w] for w in neighbors[v] if w in toidx))
        allmask=(1<<len(targets))-1
        coverage=[0]*(1<<len(side))
        count=[0]*(len(side)+1)
        for S in range(1,1<<len(side)):
            low=S&-S
            coverage[S]=coverage[S^low]|adj[low.bit_length()-1]
            if coverage[S]==allmask:count[S.bit_count()]+=1
        return count
    return mul(counts(U,B),counts(B,U))

def brute(m,n):
    vs=list(combinations(range(m+n),2))
    neighborhoods=[]
    for p in vs:
        mask=0
        for j,q in enumerate(vs):
            diff=set(p)^set(q)
            if len(diff)==2 and min(diff)<m<=max(diff):mask|=1<<j
        neighborhoods.append(mask)
    c=[0]*(len(vs)+1)
    for mask in range(1<<len(vs)):
        if all((neighbors & mask)!=0 for neighbors in neighborhoods):
            c[mask.bit_count()]+=1
    return c

def stirling2(n,k):
    if k<0 or k>n:return 0
    d=[[0]*(k+1) for _ in range(n+1)];d[0][0]=1
    for i in range(1,n+1):
        for j in range(1,min(i,k)+1): d[i][j]=d[i-1][j-1]+j*d[i-1][j]
    return d[n][k]

def min_edge_cover_count(t):
    if t%2==0:
        r=t//2
        return factorial(t)//(2**r*factorial(r))
    r=(t-1)//2
    return factorial(t)//(2**r*factorial(r-1))

def min_coefficient(m,n):
    s,t=max(m,n),min(m,n)
    B=s*sum(comb(t,j)*factorial(j)*stirling2(s-1,j) for j in [t-1,t])
    h=(t+1)//2
    U=sum(min_edge_cover_count(x) for x in [m,n] if (x+1)//2==h)
    return B*U

for m,n in ((2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4),(4,5)):
    p=predicted(m,n)
    q=actual(m,n)
    assert p==q,(m,n,'polynomial mismatch',p,q)
    nonzero=[i for i,x in enumerate(p) if x]
    d=min(nonzero)
    assert d==max(m,n)-1+(min(m,n)+1)//2
    assert p[d]==min_coefficient(m,n),(m,n,d,p[d],min_coefficient(m,n))
    assert p[-1]==1
    print(f'm={m} n={n} vertices={comb(m+n,2)} minimum={d} minimum_count={p[d]} total_sets={sum(p)}')
for m,n in ((2,2),(2,3),(2,4),(3,3),(3,4)):
    assert brute(m,n)==predicted(m,n),(m,n,'brute mismatch')
print('VERIFY_OK symbolic_actual=9 exhaustive=5')
