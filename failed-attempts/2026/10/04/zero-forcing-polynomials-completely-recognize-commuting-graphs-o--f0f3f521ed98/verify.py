#!/usr/bin/env python3
from itertools import permutations, combinations
from fractions import Fraction

def compose(p,q):
    return tuple(p[q[i]] for i in range(len(p)))

def s3_group():
    G=list(permutations(range(3)))
    return G, compose

def dihedral_group(n):
    G=[(i,e) for i in range(n) for e in (0,1)]
    def mul(x,y):
        i,e=x; j,f=y
        return ((i + (j if e==0 else -j)) % n, (e+f)%2)
    return G,mul

def quaternion_group():
    # Elements are (sign,basis) with basis 0=1,1=i,2=j,3=k.
    G=[(s,b) for s in (1,-1) for b in range(4)]
    table={
        (0,0):(1,0),(0,1):(1,1),(0,2):(1,2),(0,3):(1,3),
        (1,0):(1,1),(2,0):(1,2),(3,0):(1,3),
        (1,1):(-1,0),(2,2):(-1,0),(3,3):(-1,0),
        (1,2):(1,3),(2,3):(1,1),(3,1):(1,2),
        (2,1):(-1,3),(3,2):(-1,1),(1,3):(-1,2),
    }
    def mul(x,y):
        sx,bx=x; sy,by=y
        s,b=table[(bx,by)]
        return (sx*sy*s,b)
    return G,mul

def commute(x,y,mul):
    return mul(x,y)==mul(y,x)

def center(G,mul):
    return {x for x in G if all(commute(x,y,mul) for y in G)}

def commuting_graph(G,mul):
    Z=center(G,mul)
    V=[x for x in G if x not in Z]
    N=[set() for _ in V]
    for i,x in enumerate(V):
        for j in range(i+1,len(V)):
            if commute(x,V[j],mul):
                N[i].add(j); N[j].add(i)
    return Z,V,N

def centralizer_profile(G,mul):
    Z,V,N=commuting_graph(G,mul)
    seen=[]
    for u in V:
        C={x for x in G if commute(u,x,mul)}
        # AC condition for each noncentral element.
        assert all(commute(x,y,mul) for x in C for y in C)
        X=frozenset(C-Z)
        if X not in seen: seen.append(X)
    # Distinct noncentral centralizer parts must partition V.
    union=set()
    for X in seen:
        assert not (union & set(X))
        union |= set(X)
    assert union==set(V)
    return sorted(len(X) for X in seen), Z, V, N

def zero_forces(C,N):
    blue=set(C)
    while True:
        move=None
        for v in sorted(blue):
            W=N[v]-blue
            if len(W)==1:
                move=next(iter(W))
                break
        if move is None:
            return len(blue)==len(N)
        blue.add(move)

def zero_forcing_polynomial(N):
    n=len(N)
    d={}
    for k in range(n+1):
        c=0
        for C in combinations(range(n),k):
            if zero_forces(C,N): c+=1
        if c: d[k]=c
    return d

def predicted(profile):
    # Polynomial represented by coefficient dictionary.
    poly={0:1}
    z=0
    nontriv=0
    min_count=1
    for m in profile:
        if m==1:
            factor={1:1}
            z+=1
        else:
            factor={m-1:m,m:1}
            z+=m-1
            nontriv+=1
            min_count*=m
        new={}
        for a,ca in poly.items():
            for b,cb in factor.items():
                new[a+b]=new.get(a+b,0)+ca*cb
        poly=new
    return poly,z,nontriv,min_count

def rank_fraction(M):
    A=[[Fraction(x) for x in row] for row in M]
    m=len(A); n=len(A[0]) if A else 0
    r=0; c=0
    while r<m and c<n:
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None:
            c+=1; continue
        A[r],A[p]=A[p],A[r]
        q=A[r][c]
        A[r]=[x/q for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                q=A[i][c]
                A[i]=[A[i][j]-q*A[r][j] for j in range(n)]
        r+=1; c+=1
    return r

def witness_from_components(N):
    # Determine connected components; commuting graph of an AC-group has clique components.
    n=len(N); seen=set(); comps=[]
    for v in range(n):
        if v in seen: continue
        stack=[v]; seen.add(v); C=[]
        while stack:
            x=stack.pop(); C.append(x)
            for y in N[x]:
                if y not in seen:
                    seen.add(y); stack.append(y)
        comps.append(C)
    A=[[0]*n for _ in range(n)]
    nontriv=0
    for C in comps:
        # Component must be a clique.
        for x in C:
            assert set(C)-{x} == N[x]
        if len(C)>=2:
            nontriv+=1
            for i in C:
                for j in C:
                    A[i][j]=1
    # Off-diagonal pattern exact.
    for i in range(n):
        for j in range(i+1,n):
            assert ((A[i][j]!=0)==(j in N[i]))
    assert rank_fraction(A)==nontriv
    return nontriv

cases=[
    ("S3",)+s3_group(),
    ("D8",)+dihedral_group(4),
    ("D10",)+dihedral_group(5),
    ("D12",)+dihedral_group(6),
    ("Q8",)+quaternion_group(),
]
expected={
    "S3":[1,1,1,2],
    "D8":[2,2,2],
    "D10":[1,1,1,1,1,4],
    "D12":[2,2,2,4],
    "Q8":[2,2,2],
}
for name,G,mul in cases:
    profile,Zc,V,N=centralizer_profile(G,mul)
    assert profile==expected[name], (name,profile)
    brute=zero_forcing_polynomial(N)
    pred,z,nontriv,min_count=predicted(profile)
    assert brute==pred, (name,brute,pred)
    assert min(brute)==z
    assert brute[z]==min_count
    mr=witness_from_components(N)
    assert mr==nontriv
    max_nullity=len(V)-mr
    assert max_nullity==z
    print(f"{name}: profile={profile}, |V|={len(V)}, Z=M={z}, mr={mr}, min_sets={min_count}, polynomial={brute}")

print("VERIFY_OK")
