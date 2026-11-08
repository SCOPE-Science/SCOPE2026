"""Finite exact checks of 3-round profiles for Grassmann adjacency graphs.
Only standard Python; graphs are genuine subspaces of F_2 or F_3.
This checker supplements, rather than replaces, the uniform-field proof.
"""
from itertools import combinations, product
from collections import defaultdict
from math import prod

def subspaces(n,k,q):
    assert q in (2,3) and 1<=k<=n
    out=[]
    for piv in combinations(range(n),k):
        # reduced row-echelon basis; free entries only right of pivot
        free=[(i,j) for i,p in enumerate(piv) for j in range(p+1,n) if j not in piv]
        for vals in product(range(q),repeat=len(free)):
            rows=[[0]*n for _ in range(k)]
            for i,p in enumerate(piv):rows[i][p]=1
            for (i,j),v in zip(free,vals):rows[i][j]=v
            s=frozenset(tuple(sum(c*rows[i][j] for i,c in enumerate(t))%q
                        for j in range(n)) for t in product(range(q),repeat=k))
            out.append(s)
    assert len(out)==len(set(out))
    return out

def gaussian(n,k,q):
    numerator=prod(q**(n-i)-1 for i in range(k))
    denominator=prod(q**(k-i)-1 for i in range(k))
    assert numerator%denominator==0
    return numerator//denominator

def profiles(n,k,q):
    V=subspaces(n,k,q); N=len(V)
    assert N==gaussian(n,k,q)
    zero=(0,)*n
    # intersection size equals q^intersection_dimension
    inter=[None]*N
    for i in range(N):
        inter[i]=[len(V[i]&V[j]) for j in range(i)]
    adj=[0]*N
    for i in range(N):
        for j in range(i):
            if inter[i][j]==q**(k-1):
                adj[i] |=1<<j; adj[j] |=1<<i
    full=(1<<N)-1
    if min(k,n-k)==1:
        assert N>=3 and all(x.bit_count()==N-1 for x in adj)
        return N,{"complete": True}
    patterns=defaultdict(set)
    for i in range(N):
        for j in range(i):
            d=k
            sz=inter[i][j]
            while sz>1:
                assert sz%q==0
                sz//=q; d-=1
            forbid=(1<<i)|(1<<j)
            bits=full^forbid
            for a,b in product((0,1),repeat=2):
                mask=((adj[i] if a else full^adj[i]) &
                      (adj[j] if b else full^adj[j]) &bits)
                if mask:patterns[d].add((a,b))
                if d<=2:assert mask,(n,k,q,i,j,a,b)
            if d>=3:assert (1,1) not in patterns[d]
    assert set(patterns)==set(range(1,min(k,n-k)+1))
    full_patterns=set(product((0,1),repeat=2))
    for d,patterns_d in patterns.items():
        expected=full_patterns if d<=2 else full_patterns-{(1,1)}
        assert patterns_d==expected,(n,k,q,d,patterns_d)
    return N,{d:sorted(patterns[d]) for d in sorted(patterns)}

if __name__=='__main__':
    checks=((2,1,2),(3,2,2),(4,2,2),(5,2,2),(4,2,3),(6,3,2))
    for n,k,q in checks:
        N,P=profiles(n,k,q)
        print(f'GF({q}) n={n} k={k}: N={N}, distinct_distance_profiles={len(P)}')
    print('GRASSMANN_RANK_THREE_CHECKS_OK')
