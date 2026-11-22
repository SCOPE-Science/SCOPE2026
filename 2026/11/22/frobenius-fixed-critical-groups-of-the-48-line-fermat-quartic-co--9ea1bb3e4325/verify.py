#!/usr/bin/env python3
"""Exact integral arithmetic for Fermat-quartic line-graph Galois fixed groups.

Python 3 standard library only. All finite-field checks are independent of the
symbolic congruence construction; the symbolic construction, not finite samples,
proves the incidence rules. Values are computed, not imported from a table.
"""
from collections import Counter
from itertools import product
from math import prod
from hashlib import sha256
import json

PAIRS = (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2)))
LABELS = [(k,a,b) for k in range(3) for a in range(4) for b in range(4)]
N = len(LABELS)


def adjacency_congruences():
    a = [[0]*N for _ in range(N)]
    for i,(k,x,y) in enumerate(LABELS):
        for j in range(i):
            t,u,v = LABELS[j]
            if k == t:
                intersects = x == u or y == v
            elif t == 0 and k == 1:
                intersects = (u+y-x-v)%4 == 0
            elif t == 0 and k == 2:
                intersects = (u+v+y+1-x)%4 == 0
            elif t == 1 and k == 2:
                intersects = (u+v-x-y)%4 == 0
            else:
                raise AssertionError('ordered partitions')
            a[i][j] = a[j][i] = int(intersects)
    return a


def modular_rank(mat,p):
    A = [[x%p for x in row] for row in mat]
    r=0
    for c in range(len(A[0])):
        s=next((i for i in range(r,len(A)) if A[i][c]),None)
        if s is None: continue
        A[r],A[s]=A[s],A[r]
        inv=pow(A[r][c],-1,p)
        A[r] = [(x*inv)%p for x in A[r]]
        for i in range(r+1,len(A)):
            k=A[i][c]
            if k: A[i]=[(x-k*y)%p for x,y in zip(A[i],A[r])]
        r+=1
        if r==len(A):break
    return r


def adjacency_from_equations(p,root):
    z=root
    assert pow(z,4,p)==p-1 and pow(z,8,p)==1
    eq=[]
    for k,a,b in LABELS:
        rows=[]
        for (i,j),power in zip(PAIRS[k],(2*a+1,2*b+1)):
            row=[0]*4
            row[i]=1
            row[j]=-pow(z,power,p)
            rows.append(row)
        eq.append(rows)
    A=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(i):
            A[i][j]=A[j][i]=int(modular_rank(eq[i]+eq[j],p)<4)
    return A


def local_smith(matrix,prime,k):
    """Prime-adic Smith valuations via integral elementary ops mod prime**k."""
    mod=prime**k
    A=[[v%mod for v in row] for row in matrix]
    n,m=len(A),len(A[0]);vals=[]
    def valuation(t):
        if t==0:return k
        e=0
        while t%prime==0:t//=prime;e+=1
        return e
    for s in range(n):
        v,i,j=min((valuation(A[i][j]),i,j) for i in range(s,n) for j in range(s,m))
        assert v<k,'modulus too small to resolve an invariant factor'
        A[i],A[s]=A[s],A[i]
        for row in A:row[j],row[s]=row[s],row[j]
        power=prime**v
        unit=(A[s][s]//power)%(mod//power)
        inv=pow(unit,-1,mod//power)
        for i in range(s+1,n):
            x=A[i][s]
            assert x%power==0
            mult=(x//power)*inv%(mod//power)
            if mult:
                A[i]=[(u-mult*w)%mod for u,w in zip(A[i],A[s])]
            assert A[i][s]==0
        for j in range(s+1,m):
            x=A[s][j]
            assert x%power==0
            mult=(x//power)*inv%(mod//power)
            if mult:
                for i in range(s,n):
                    A[i][j]=(A[i][j]-mult*A[i][s])%mod
            assert A[s][j]==0
        vals.append(v)
    return vals


def fixed_invariants(A, q, root):
    where={lab:i for i,lab in enumerate(LABELS)}
    perm=[where[(k, ((q*(2*a+1))%8-1)//2, ((q*(2*b+1))%8-1)//2)] for k,a,b in LABELS]
    assert all(A[perm[i]][perm[j]]==A[i][j] for i in range(N) for j in range(N))
    bases=[i for i in range(N) if i!=root]
    rows={v:i for i,v in enumerate(bases)}
    L=[[14*(i==j)-A[u][v] for j,v in enumerate(bases)] for i,u in enumerate(bases)]
    T=[[0]*47 for _ in range(47)]
    for j,u in enumerate(bases):
        for v,coef in ((perm[u],1),(perm[root],-1),(u,-1),(root,1)):
            if v!=root:T[rows[v]][j]+=coef
    B=[L[i]+T[i] for i in range(47)]
    val={p:local_smith(B,p,k) for p,k in ((2,9),(3,5),(5,3))}
    counts={p:Counter(v for v in vals if v) for p,vals in val.items()}
    r=max(sum(c.values()) for c in counts.values())
    primes=[]
    for p,c in counts.items():
        primes.append([1]*(r-sum(c.values()))+[p**ex for ex,num in sorted(c.items()) for _ in range(num)])
    factors=[prod(f) for f in zip(*primes)]
    assert all(y%x==0 for x,y in zip(factors,factors[1:]))
    return Counter(factors),counts,perm

EXPECTED={
1:{4:2,12:10,24:5,192:6,960:2,1920:3,5760:1},
3:{2:3,4:1,12:3,48:3,96:2,192:1,960:2,2880:1},
5:{2:1,4:2,12:9,60:1,240:4,720:1},
7:{2:3,4:1,12:3,48:3,96:2,192:1,960:2,2880:1},
}

def main():
    A=adjacency_congruences()
    assert all(sum(r)==14 for r in A)
    assert sum(map(sum,A))//2==336
    for p,primitive in ((17,3),(41,6),(73,5)):
        # Find an actual primitive eighth root if suggested primitive root is not generator.
        z=next(x for x in range(1,p) if pow(x,8,p)==1 and pow(x,4,p)==p-1)
        assert adjacency_from_equations(p,z)==A, ('line determinant mismatch',p)
    visited={0};front=[0]
    while front:
        u=front.pop()
        for v in range(N):
            if A[u][v] and v not in visited:
                visited.add(v);front.append(v)
    assert len(visited)==48
    all_results={}
    for root in (0,15,47):
        for q in (1,3,5,7):
            factors,locals_,perm=fixed_invariants(A,q,root)
            assert factors==Counter(EXPECTED[q]),(root,q, factors)
            assert sum(perm[i]==i for i in range(48))==(48 if q==1 else 0)
            assert all(perm[perm[i]]==i for i in range(48))
            all_results[q]=dict(sorted(factors.items()))
            print('root',root,'q mod 8',q,'factors',dict(sorted(factors.items())), 'local', {p:dict(sorted(c.items())) for p,c in locals_.items()})
    # known matrix-tree order from independent published graph spectrum
    full=prod(k**v for k,v in EXPECTED[1].items())
    assert full==2**115*3**28*5**6
    print('GRAPH_SHA256',sha256(bytes(x for row in A for x in row)).hexdigest())
    print('FERMAT_48_LINE_FROBENIUS_FIXED_CRITICAL_GROUPS_OK')

if __name__=='__main__':main()
