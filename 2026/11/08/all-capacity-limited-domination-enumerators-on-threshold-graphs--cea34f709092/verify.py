"""Exact independent tests for k-limited domination on apex joins and clique bouquets."""
from itertools import product
from math import comb
from collections import Counter

def graph_from_profile(sizes):
    m=sum(sizes)
    adj=[0]*(m+1)
    pos=1
    for size in sizes:
        verts=list(range(pos,pos+size))
        for i in verts:
            adj[0] |= 1<<i
            adj[i] |= 1
            for j in verts:
                if i!=j: adj[i]|=1<<j
        pos+=size
    return adj

def brute_poly(adj,k):
    n=len(adj); allbits=(1<<n)-1; c=Counter()
    for d in range(1<<n):
        out=allbits^d
        if any((adj[u]&out).bit_count()>k for u in range(n) if (d>>u)&1):continue
        if any((adj[u]&d)==0 for u in range(n) if (out>>u)&1):continue
        c[d.bit_count()]+=1
    return dict(c)

def formula(sizes,k):
    m=sum(sizes); c=Counter()
    for t in range(min(k,m)+1): c[m+1-t]+=comb(m,t)
    prod={0:1}
    for size in sizes:
        nxt=Counter()
        for j,x in prod.items():
            for t in range(min(k-1,size-1)+1): nxt[j+size-t]+=x*comb(size,t)
        prod=dict(nxt)
    for d,x in prod.items(): c[d]+=x
    return dict(c)

def min_formula(sizes,k):
    m=sum(sizes); T=sum(min(k-1,s-1) for s in sizes)
    a=m+1-k; b=m-T
    c1=comb(m,k); c2=1
    for s in sizes:c2*=comb(s,min(k-1,s-1))
    return min(a,b),(c1 if a<=b else 0)+(c2 if b<=a else 0)

# All heterogeneous 2--4-blade profiles of orders <=12, all nontrivial capacities.
checked=0
for r in range(2,5):
    for sizes in product(range(1,5),repeat=r):
        m=sum(sizes)
        if m>11:continue
        adj=graph_from_profile(sizes)
        for k in range(1,m):
            brute=brute_poly(adj,k)
            f=formula(sizes,k)
            assert brute==f,(sizes,k,brute,f)
            degree=min(brute)
            count=brute[degree]
            assert (degree,count)==min_formula(sizes,k),(sizes,k,degree,count)
            checked+=1
print('MIXED_BLADE_EXHAUSTIVE_OK',checked)

# Independently test the universal-vertex recurrence on every labelled graph
# of at most five vertices (including isolated vertices).
joinchecked=0
for n in range(1,6):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    for edge_mask in range(1<<len(pairs)):
        H=[0]*n
        for e,(a,b) in enumerate(pairs):
            if (edge_mask>>e)&1:
                H[a]|=1<<b;H[b]|=1<<a
        cone=[bits | (1<<n) for bits in H]+[(1<<n)-1]
        for k in range(1,n+1):
            actual=brute_poly(cone,k)
            if k>1:
                prior=brute_poly(H,k-1)
            else:
                prior={n:1}
            rhs=Counter(prior)
            for t in range(min(k,n)+1):rhs[n+1-t]+=comb(n,t)
            assert actual==dict(rhs),(n,edge_mask,k,actual,rhs)
            joinchecked+=1
print('UNIVERSAL_APEX_RECURRENCE_OK',joinchecked)

# Six parameter classes including the last tie and hub-dominating regime.
uniform_cases=0
for r in range(2,8):
    for b in range(2,8):
        m=r*b
        for k in range(1,m):
            alpha,c=min_formula((b,)*r,k)
            A=m+1-k
            B=r*max(1,b-k+1)
            assert alpha==min(A,B)
            if k==1: assert c==m+1
            if 2<=k<=b: assert alpha==r*(b-k+1) and c==comb(b,k-1)**r
            if b<k<r*(b-1)+1: assert alpha==r and c==b**r
            if k==r*(b-1)+1: assert alpha==r and c==b**r+comb(m,k)
            if k>r*(b-1)+1: assert alpha==m+1-k and c==comb(m,k)
            uniform_cases+=1
print('UNIFORM_PHASE_AND_MINIMUM_CENSUS_OK',uniform_cases)

def threshold_graph(bits):
    # Start from one vertex, then append 0-isolates and 1-universal vertices.
    adj=[0]
    for b in bits:
        q=len(adj)
        if b:
            adj=[x|(1<<q) for x in adj]+[(1<<q)-1]
        else:adj.append(0)
    return adj

def threshold_recursion(bits,k):
    # All polynomials indexed by load; no use of graph adjacency.
    polys=[{1:1} for _ in range(k+1)]
    for b in bits:
        q=next(iter(polys[0]))
        nxt=[]
        for h in range(k+1):
            if not b:
                nxt.append({j+1:c for j,c in polys[h].items()})
            elif h==0:
                nxt.append({q+1:1})
            else:
                c=Counter(polys[h-1])
                for t in range(min(h,q)+1):c[q+1-t]+=comb(q,t)
                nxt.append(dict(c))
        polys=nxt
    return polys[k]

threshold_tested=0
for n in range(1,10):
    for bits in product((0,1),repeat=n-1):
        adj=threshold_graph(bits)
        for k in range(n+1):
            b=brute_poly(adj,k)
            f=threshold_recursion(bits,k)
            assert b==f, (n,bits,k,b,f)
            threshold_tested+=1
print('ALL_THRESHOLD_CREATION_WORDS_OK',threshold_tested)
print('VERIFY_OK')
