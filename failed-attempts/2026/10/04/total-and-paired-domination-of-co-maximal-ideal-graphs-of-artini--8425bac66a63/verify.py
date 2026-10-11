#!/usr/bin/env python3
from itertools import product, combinations

def graph(ks):
    tops=tuple(k-1 for k in ks)
    V=[]
    for a in product(*[range(k) for k in ks]):
        # vertex iff ideal is proper and not contained in J:
        # at least one coordinate is whole, and not all are whole.
        if a != tops and any(a[i]==tops[i] for i in range(len(ks))):
            V.append(a)
    adj=[set() for _ in V]
    for i,a in enumerate(V):
        for j in range(i+1,len(V)):
            b=V[j]
            # in a local factor, sum is whole iff one summand is whole
            if all(a[t]==tops[t] or b[t]==tops[t] for t in range(len(ks))):
                adj[i].add(j); adj[j].add(i)
    return V,adj

def total_dominates(S,adj):
    S=set(S)
    return all(adj[v] & S for v in range(len(adj)))

def has_perfect_matching(S,adj):
    S=set(S)
    if len(S)%2: return False
    if not S: return True
    v=next(iter(S))
    for u in adj[v] & S:
        if has_perfect_matching(S-{v,u},adj):
            return True
    return False

def paired_dominates(S,adj):
    return total_dominates(S,adj) and has_perfect_matching(S,adj)

def minima(ks):
    V,adj=graph(ks)
    r=len(ks)
    gt=gp=None
    for k in range(1, r+2):
        if gt is None:
            for S in combinations(range(len(V)),k):
                if total_dominates(S,adj):
                    gt=k; break
        if gp is None and k%2==0:
            for S in combinations(range(len(V)),k):
                if paired_dominates(S,adj):
                    gp=k; break
        if gt is not None and gp is not None:
            break
    return len(V),gt,gp

cases=[
    (2,2),(2,3),(3,3),
    (2,2,2),(2,2,3),(2,3,3),
    (2,2,2,2),(2,2,2,3),
    (2,2,2,2,2)
]
rows=[]
for ks in cases:
    N,gt,gp=minima(ks)
    r=len(ks)
    assert gt==r, (ks,N,gt)
    assert gp==(r if r%2==0 else r+1), (ks,N,gp)
    rows.append((ks,N,gt,gp))

# Support-level universal witness checks through r=9.
for r in range(2,10):
    # maximal ideals have support [r]\{i}
    M=[frozenset(j for j in range(r) if j!=i) for i in range(r)]
    supports=[frozenset(S) for k in range(1,r) for S in combinations(range(r),k)]
    # D=M is total dominating.
    for S in supports:
        assert any(S|T==frozenset(range(r)) for T in M)
    for T in M:
        assert any(T!=U and T|U==frozenset(range(r)) for U in M)
    if r%2:
        X=frozenset({0})
        assert X|M[0]==frozenset(range(r))

print("VERIFY_OK")
for ks,N,gt,gp in rows:
    print(f"ideal_counts={ks}: vertices={N} gamma_t={gt} gamma_pr={gp}")
print("support_witness_checks_r=2..9_passed")
