#!/usr/bin/env python3
import itertools, json
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

def downclosure(facets):
    D={0}
    for F in facets:
        sub=F
        while True:
            D.add(sub)
            if sub==0:
                break
            sub=(sub-1)&F
    return D

def is_downset(D,k):
    if 0 not in D:
        return False
    for x in D:
        y=x
        while True:
            if y not in D:
                return False
            if y==0:
                break
            y=(y-1)&x
    return True

def full_vertex(D,k):
    return all((1<<i) in D for i in range(k))

def induced_size(D,T):
    return sum((face & ~T)==0 for face in D)

def formula_ghw(D,k):
    out=[]
    for r in range(1,k+1):
        s=k-r
        best=0
        for comb in itertools.combinations(range(k),s):
            T=sum(1<<i for i in comb)
            best=max(best,induced_size(D,T))
        out.append(len(D)-best)
    return out

def inv_mod(a,q):
    return pow(a,-1,q)

def rank_mod(rows,q,ncols):
    A=[list(r) for r in rows if any(x%q for x in r)]
    rr=0
    for c in range(ncols):
        p=next((i for i in range(rr,len(A)) if A[i][c]%q),None)
        if p is None:
            continue
        A[rr],A[p]=A[p],A[rr]
        iv=inv_mod(A[rr][c]%q,q)
        A[rr]=[(iv*x)%q for x in A[rr]]
        for i in range(len(A)):
            if i!=rr and A[i][c]%q:
                f=A[i][c]%q
                A[i]=[(A[i][j]-f*A[rr][j])%q for j in range(ncols)]
        rr+=1
        if rr==len(A):
            break
    return rr

def subspaces_rref(k,r,q):
    for piv in itertools.combinations(range(k),r):
        P=set(piv)
        free=[(i,c) for i,p in enumerate(piv)
              for c in range(p+1,k) if c not in P]
        for vals in itertools.product(range(q),repeat=len(free)):
            B=[[0]*k for _ in range(r)]
            for i,p in enumerate(piv):
                B[i][p]=1
            for (i,c),v in zip(free,vals):
                B[i][c]=v
            yield B

def direct_ghw(D,k,q):
    faces=[f for f in sorted(D) if f]
    columns=[[1 if (f>>i)&1 else 0 for i in range(k)] for f in faces]
    best=[10**9]*(k+1)
    for r in range(1,k+1):
        for B in subspaces_rref(k,r,q):
            supp=0
            for col in columns:
                hit=False
                for row in B:
                    if sum(a*b for a,b in zip(row,col))%q:
                        hit=True
                        break
                supp+=hit
            if supp<best[r]:
                best[r]=supp
    return best[1:]

# Exhaust all downsets on k<=4 whose declared vertex set is all k vertices.
checked=0
for k in range(1,5):
    all_faces=list(range(1<<k))
    for mask in range(1<<(1<<k)):
        if not (mask&1):
            continue
        D={f for j,f in enumerate(all_faces) if (mask>>j)&1}
        if not is_downset(D,k) or not full_vertex(D,k):
            continue
        fgh=formula_ghw(D,k)
        for q in (2,3):
            assert direct_ghw(D,k,q)==fgh
        checked+=1
assert checked>0

# Source Example 4.2.
facets=[]
for F in ([0,1],[0,2,3],[4,5,6,7]):
    m=0
    for i in F:
        m|=1<<i
    facets.append(m)
D=downclosure(facets)
assert len(D)-1==24
assert formula_ghw(D,8)==CERT["example_4_2"]["generalized_hamming_weights"]
assert direct_ghw(D,8,2)==CERT["example_4_2"]["generalized_hamming_weights"]

# Source Theorem 5.2 family: all subsets except full base and full vertex set.
for N in range(1,7):
    k=N+2
    base=(1<<(N+1))-1
    full=(1<<k)-1
    D={x for x in range(1<<k) if x not in (base,full)}
    assert is_downset(D,k)
    got=formula_ghw(D,k)
    expected=[2**(N+2)-2-2**(N+2-r) for r in range(1,N+3)]
    assert got==expected
    assert len(D)-1==2**(N+2)-3

print("VERIFY_OK")
