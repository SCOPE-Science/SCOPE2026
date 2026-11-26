#!/usr/bin/env python3
"""Independent finite verification of balanced-spider power zero forcing.

Uses only the Python standard library. Checks the exact graph support of a
symmetric matrix, explicit null vectors, rank modulo two primes, a concrete
forcing process, and exhaustive zero forcing for selected small parameters.
"""
from itertools import combinations


def modular_rank(a, p):
    a = [[x % p for x in row] for row in a]
    nr = len(a)
    nc = len(a[0]) if a else 0
    r = 0
    for c in range(nc):
        pivot = next((j for j in range(r,nr) if a[j][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        factor = pow(a[r][c], -1, p)
        for j in range(r+1,nr):
            if a[j][c]:
                z = a[j][c] * factor % p
                for h in range(c,nc):
                    a[j][h] = (a[j][h]-z*a[r][h]) % p
        r += 1
        if r==nr:
            break
    return r


def build(m, ell, k):
    labels = [(0,0)] + [(i,d) for i in range(1,m+1) for d in range(1,ell+1)]
    n = len(labels)
    adj = [set() for _ in labels]
    for a in range(n):
        for b in range(a+1,n):
            i,d=labels[a]; j,e=labels[b]
            if i==0: dist=e
            elif j==0: dist=d
            elif i==j: dist=abs(d-e)
            else: dist=d+e
            if dist<=k:
                adj[a].add(b);adj[b].add(a)

    # Columns of P are (k+1)-consecutive-vertex incidence vectors.
    p = [[int(t<=s<=t+k) for t in range(ell-k)] for s in range(ell)]
    c = [[sum(p[s][h]*p[t][h] for h in range(ell-k))
          for t in range(ell)] for s in range(ell)]
    b = [[int((s+1)+(t+1)<=k) for t in range(ell)] for s in range(ell)]
    mat = [[0]*n for _ in range(n)]
    for i in range(1,m+1):
        for s in range(ell):
            u=1+(i-1)*ell+s
            mat[0][u]=mat[u][0]=int(s+1<=k)
            for j in range(1,m+1):
                for t in range(ell):
                    v=1+(j-1)*ell+t
                    mat[u][v]=c[s][t]+b[s][t] if i==j else b[s][t]

    for u in range(n):
        for v in range(n):
            assert mat[u][v]==mat[v][u]
            if u!=v:
                assert (mat[u][v]!=0)==(v in adj[u]), (m,ell,k,u,v)
    # Build exactly k independent solutions to P^T v=0 from arbitrary first k entries.
    null_basis=[]
    for h in range(k):
        v=[int(j==h) for j in range(k)]
        for t in range(ell-k):
            v.append(-sum(v[t:t+k]))
        assert len(v)==ell
        assert all(sum(v[t:t+k+1])==0 for t in range(ell-k))
        null_basis.append(v)
    for i in range(1,m):
        for v in null_basis:
            x=[0]*n
            for s in range(ell):
                x[1+(i-1)*ell+s]=v[s]
                x[1+(m-1)*ell+s]=-v[s]
            assert all(sum(mat[u][v]*x[v] for v in range(n))==0 for u in range(n))
    expected=n-(m-1)*k
    for modulus in (1000000007,1000000009):
        assert modular_rank(mat,modulus)==expected, (m,ell,k,modulus)
    return adj


def forces(adj,selected):
    selected=set(selected)
    while len(selected)<len(adj):
        step=[]
        for v in selected:
            white=adj[v]-selected
            if len(white)==1:
                step.append(next(iter(white)))
        if not step:
            return False
        selected.update(step)
    return True


def brute_z(adj,bound):
    n=len(adj)
    for s in range(bound):
        for cand in combinations(range(n),s):
            if forces(adj,cand):
                return s
    return bound


if __name__=='__main__':
    exact=0
    exhaustive=0
    genuinely_new=0
    for m in range(2,6):
        for k in range(1,8):
            for ell in range(k+1,k+4):
                if 1+m*ell>46:
                    continue
                a=build(m,ell,k)
                target=(m-1)*k
                starters=[1+(i-1)*ell+s for i in range(1,m)
                          for s in range(ell-k,ell)]
                assert len(starters)==target
                assert forces(a,starters)
                exact+=1
                genuinely_new+=(k>=4)
                if len(a)<=16 and target<=8:
                    assert brute_z(a,target)==target
                    exhaustive+=1
    print('VERIFY_OK witness_support_rank_forcing=',exact,
          'higher_power_cases=',genuinely_new,
          'exhaustive_zero_forcing_cases=',exhaustive)
