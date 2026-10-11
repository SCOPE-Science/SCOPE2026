#!/usr/bin/env python3
from itertools import product, combinations
from math import gcd

# A factor (p,e) denotes Z/(p^e).  All examples have at least one e>=2,
# hence the product ring is nonreduced.
def elements(factors):
    mods=[p**e for p,e in factors]
    return list(product(*[range(m) for m in mods])), mods

def mul(x,y,mods):
    return tuple((a*b)%m for a,b,m in zip(x,y,mods))

def is_unit(x,factors):
    return all(gcd(a,p)==1 for a,(p,e) in zip(x,factors))

def zero_div_graph(factors):
    E,mods=elements(factors)
    zero=tuple(0 for _ in mods)
    V=[x for x in E if x!=zero and not is_unit(x,factors)]
    adj=[set() for _ in V]
    for i,x in enumerate(V):
        for j in range(i+1,len(V)):
            if mul(x,V[j],mods)==zero:
                adj[i].add(j); adj[j].add(i)
    return V,adj,mods

def total_dom(S,adj):
    S=set(S)
    return all(bool(adj[v] & S) for v in range(len(adj)))

def perfect_matching(S,adj):
    S=set(S)
    if not S:
        return True
    if len(S)%2:
        return False
    v=next(iter(S))
    for u in sorted(adj[v] & S):
        if perfect_matching(S-{v,u},adj):
            return True
    return False

def paired_dom(S,adj):
    return total_dom(S,adj) and perfect_matching(S,adj)

def minima(adj, cap):
    gt=gp=None
    n=len(adj)
    for k in range(2,min(cap,n)+1):
        if gt is None:
            for S in combinations(range(n),k):
                if total_dom(S,adj):
                    gt=k; break
        if gp is None and k%2==0:
            for S in combinations(range(n),k):
                if paired_dom(S,adj):
                    gp=k; break
        if gt is not None and gp is not None:
            break
    return gt,gp

def socle_vector(factors,i):
    out=[]
    for j,(p,e) in enumerate(factors):
        if j!=i:
            out.append(0)
        elif e==1:
            out.append(1)
        else:
            out.append(p**(e-1))
    return tuple(out)

def check_witness(factors,V,adj):
    k=len(factors)
    idx={x:i for i,x in enumerate(V)}
    X=[socle_vector(factors,i) for i in range(k)]
    assert all(x in idx for x in X)
    D=[idx[x] for x in X]
    assert total_dom(D,adj)
    assert all(j in adj[i] for i,j in combinations(D,2))
    if k%2==0:
        assert paired_dom(D,adj)
        return len(D)
    y=tuple((X[1][t]+X[2][t]) for t in range(k))
    # coordinates lie in distinct factors, so no modular wrap occurs here
    assert y in idx and y not in X
    W=D+[idx[y]]
    assert paired_dom(W,adj)
    return len(W)

cases=[
    ((2,2),(2,1)),             # Z4 x Z2
    ((2,2),(3,1)),             # Z4 x Z3
    ((2,3),(3,1)),             # Z8 x Z3
    ((2,2),(2,1),(2,1)),       # Z4 x Z2 x Z2
    ((2,2),(3,1),(2,1)),       # Z4 x Z3 x Z2
    ((2,3),(2,1),(3,1)),       # Z8 x Z2 x Z3
    ((2,2),(2,1),(2,1),(2,1)),# Z4 x Z2^3
]

print('VERIFY_OK')
for factors in cases:
    V,adj,mods=zero_div_graph(factors)
    k=len(factors)
    expected_pr=2*((k+1)//2)
    witness=check_witness(factors,V,adj)
    gt,gp=minima(adj, expected_pr)
    assert gt==k, (factors,gt,k)
    assert gp==expected_pr, (factors,gp,expected_pr)
    assert witness==expected_pr
    print(f'factors={factors} vertices={len(V)} gamma_t={gt} gamma_pr={gp} witness={witness}')
