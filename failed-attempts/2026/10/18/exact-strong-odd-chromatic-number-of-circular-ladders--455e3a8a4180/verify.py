#!/usr/bin/env python3
"""Independent, standard-library checks for strong odd prism colourings."""
from collections import defaultdict

U=((0,1),(2,3),(1,0),(3,2))
V5=((0,1),(2,3),(1,4),(3,0),(4,2))
V7=((0,1),(2,3),(1,0),(3,2),(0,4),(1,3),(4,2))

def construct(n):
    if n<5 or not n%2: raise ValueError('odd n >=5 required')
    base=V5 if n%4==1 else V7
    return U*((n-len(base))//4)+base

def neighbors(n, v):
    i,row=divmod(v,2)
    return (2*((i-1)%n)+row,2*((i+1)%n)+row,2*i+1-row)

def check_coloring(columns):
    n=len(columns)
    assert n>=3
    f=[c for pair in columns for c in pair]
    for v in range(2*n):
        near=neighbors(n,v)
        assert all(f[v]!=f[w] for w in near), ('improper',n,v)
        tally=defaultdict(int)
        for w in near: tally[f[w]]+=1
        assert all(k%2 for k in tally.values()), ('parity',n,v)
    return True

def odd_independent_max(n):
    ns=[neighbors(n,i) for i in range(2*n)]
    best=0
    for s in range(1<<(2*n)):
        b=s.bit_count()
        if b<=best:continue
        good=True
        for i in range(2*n):
            k=sum((s>>j)&1 for j in ns[i])
            if ((s>>i)&1 and k!=0) or (not ((s>>i)&1) and k==2):
                good=False;break
        if good:best=b
    return best

def transition_possible(q,n):
    # Whole finite-state search rather than consulting any construction.
    states=[(a,b) for a in range(q) for b in range(q) if a!=b]
    N=len(states)
    def valid(p,x,z):
        if p[0]==x[0] or p[1]==x[1] or x[0]==z[0] or x[1]==z[1]:return False
        a=[p[0],z[0],x[1]];b=[p[1],z[1],x[0]]
        return len(set(a)) in (1,3) and len(set(b)) in (1,3)
    out=[[] for _ in range(N*N)]
    for i,p in enumerate(states):
        for j,x in enumerate(states):
            for k,z in enumerate(states):
                if valid(p,x,z):out[i*N+j].append(j*N+k)
    # Check existence of a closed walk of exact length n.
    for root in range(N*N):
        reach={root}
        for _ in range(n):
            reach={v for u in reach for v in out[u]}
            if not reach:break
        if root in reach:return True
    return False

def cyclic_triples(c):
    return {(c[(i-1)%len(c)],c[i],c[(i+1)%len(c)]) for i in range(len(c))}

if __name__=='__main__':
    for length in (5,7):
        check_coloring(V5 if length==5 else V7)
    # Local triples stabilize after two U blocks, providing a finite check
    # for the whole construction by a mathematical locality argument.
    for base in (V5,V7):
        allowed=set().union(*(cyclic_triples(U*k+base) for k in range(3)))
        assert all(check_coloring(U*k+base) for k in range(3))
        for k in range(3,65):
            assert cyclic_triples(U*k+base)<=allowed
        print('base',len(base),'local triple types',len(allowed),'stabilization checked through',64)
    for n in range(5,500,2):check_coloring(construct(n))
    print('constructed odd orders 5..499:',248)
    for n in range(3,10):
        ans=odd_independent_max(n)
        expected=n if n%2==0 else (n-1)//2
        assert ans==expected,(n,ans,expected)
        print('odd-independent optimum',n,ans)
    for q in range(2,6):
        for n in range(3,13):
            found=transition_possible(q,n)
            expected=(q>=2 if n%2==0 else q>= (6 if n==3 else 5))
            assert found==expected,(q,n,found,expected)
        print('finite-state q',q,'orders 3..12 matched theorem')
    print('VERIFICATION_OK')
