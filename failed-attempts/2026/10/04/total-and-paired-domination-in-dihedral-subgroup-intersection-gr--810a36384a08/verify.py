#!/usr/bin/env python3
from itertools import combinations
from math import isqrt


def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def subgroup_vertices(n):
    # Elements are (a,e), representing r^a s^e with a mod n and e in {0,1}.
    V=[]
    names=[]
    # Rotation subgroups <r^d>, d|n, d<n. Exclude identity d=n.
    for d in divisors(n):
        if d==n: continue
        H=frozenset((k,0) for k in range(0,n,d))
        V.append(H); names.append(f"A_{d}")
    # Proper dihedral subgroups <r^d,r^j s>, d|n, d>1, j mod d.
    for d in divisors(n):
        if d==1: continue
        for j in range(d):
            H=set((k,0) for k in range(0,n,d))
            H.update(((j+k)%n,1) for k in range(0,n,d))
            V.append(frozenset(H)); names.append(f"H_{d},{j}")
    assert len(V)==len(set(V)), (n,len(V),len(set(V)))
    # every vertex is proper and nontrivial
    assert all(1 < len(H) < 2*n for H in V)
    return V,names

def graph(n):
    V,names=subgroup_vertices(n)
    N=[set() for _ in V]
    e=(0,0)
    for i,j in combinations(range(len(V)),2):
        if (V[i] & V[j]) != {e}:
            N[i].add(j); N[j].add(i)
    return V,names,N

def dominates(D,N):
    D=set(D)
    return all(v in D or bool(N[v]&D) for v in range(len(N)))

def total_dominates(D,N):
    D=set(D)
    return all(bool(N[v]&D) for v in range(len(N)))

def perfect_matching(D,N):
    S=frozenset(D)
    memo={}
    def rec(T):
        if not T: return True
        if len(T)%2: return False
        if T in memo: return memo[T]
        v=next(iter(T))
        R=T-{v}
        for u in R:
            if u in N[v] and rec(R-{u}):
                memo[T]=True
                return True
        memo[T]=False
        return False
    return rec(S)

def paired(D,N):
    return dominates(D,N) and perfect_matching(D,N)

def smallest_prime(n):
    for p in range(2,isqrt(n)+1):
        if n%p==0:
            return p
    return n

def is_prime(n):
    return smallest_prime(n)==n

def predicted(n):
    p=smallest_prime(n)
    if is_prime(n):
        return None,None,p
    gt=p if n%(p*p)==0 else p+1
    gp=gt if gt%2==0 else gt+1
    return gt,gp,p

def minimum(N,pred,maxk):
    for k in range(1,maxk+1):
        for C in combinations(range(len(N)),k):
            if pred(C,N): return k,C
    return None,None

for n in range(3,21):
    V,names,N=graph(n)
    gt,gp,p=predicted(n)
    if gt is None:
        # For prime n all proper nontrivial subgroups are the rotation subgroup of order n
        # and n reflection subgroups, all isolated.
        assert all(len(N[i])==0 for i in range(len(N))), (n,[len(x) for x in N])
        kt,Ct=minimum(N,total_dominates,4)
        kp,Cp=minimum(N,paired,4)
        assert kt is None and kp is None
        print(f"n={n} prime p={p} vertices={len(V)} total=none paired=none")
        continue
    # Verify the explicit Kayacan-style clique construction.
    P=[]
    for r in range(p):
        nm=f"H_{p},{r}"
        P.append(names.index(nm))
    if n%(p*p)==0:
        D=P
    else:
        D=P+[names.index("A_1")]
    assert len(D)==gt
    assert total_dominates(D,N)
    assert all(j in N[i] for i,j in combinations(D,2)), (n,[names[i] for i in D])
    if gt%2==0:
        DP=D
    else:
        # Add a vertex adjacent to the whole clique: <r^p> when p^2|n,
        # and <r^2> in the p=2, p^2 not dividing n case.
        if n%(p*p)==0:
            extra=names.index(f"A_{p}")
        else:
            assert p==2
            extra=names.index("A_2")
        DP=D+[extra]
    assert len(DP)==gp and paired(DP,N)
    # Exhaustively establish the lower values for this finite calibration range.
    kt,Ct=minimum(N,total_dominates,gt)
    kp,Cp=minimum(N,paired,gp)
    assert kt==gt, (n,kt,gt)
    assert kp==gp, (n,kp,gp)
    print(f"n={n} composite p={p} vertices={len(V)} gamma_t={gt} gamma_pr={gp} total_witness={[names[i] for i in D]} paired_witness={[names[i] for i in DP]}")
print("VERIFY_OK")
