#!/usr/bin/env python3
from itertools import product
from collections import Counter, deque
from fractions import Fraction
from math import factorial


def leq(x,y,p,q):
    if x==y: return True
    return x < p and y >= p


def monotone(f,p,q):
    # every lower a is <= every upper b
    return all(leq(f[a], f[p+b], p,q) for a in range(p) for b in range(q))


def all_maps(p,q):
    n=p+q
    return [f for f in product(range(n), repeat=n) if monotone(f,p,q)]


def comparable(f,g,p,q):
    return all(leq(f[i],g[i],p,q) for i in range(p+q)) or all(leq(g[i],f[i],p,q) for i in range(p+q))


def rank_q(cols):
    if not cols: return 0
    m=len(cols[0]); n=len(cols)
    A=[[Fraction(cols[j][i]) for j in range(n)] for i in range(m)]
    r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]), None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        z=A[r][c]
        A[r]=[v/z for v in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r


def h1_rank_direct(f,p,q):
    # C1 target edge basis indexed by (a,b), a lower and b upper.
    def edge_image(x,y):
        u,v=f[x],f[y]
        vec=[0]*(p*q)
        if u==v: return vec
        assert u < p and v >= p
        vec[u*q+(v-p)]=1
        return vec
    cols=[]
    # z_ij = e_{i,j} - e_{i,q-1} - e_{p-1,j} + e_{p-1,q-1}
    for i in range(p-1):
        for j in range(q-1):
            terms=[(i,p+j,1),(i,p+q-1,-1),(p-1,p+j,-1),(p-1,p+q-1,1)]
            v=[0]*(p*q)
            for x,y,s in terms:
                w=edge_image(x,y)
                for k in range(p*q): v[k]+=s*w[k]
            cols.append(v)
    return rank_q(cols)


def falling(n,r):
    z=1
    for k in range(r): z*=n-k
    return z


def stirling2(n,r):
    dp=[[0]*(r+1) for _ in range(n+1)]
    dp[0][0]=1
    for i in range(1,n+1):
        for j in range(1,min(i,r)+1):
            dp[i][j]=dp[i-1][j-1]+j*dp[i-1][j]
    return dp[n][r]


def predicted_profile(p,q):
    out=Counter()
    null=q*(p+1)**p + p*(q+1)**q - p*q
    out[0]=null
    for r in range(2,p+1):
        fp=falling(p,r)*stirling2(p,r)
        for s in range(2,q+1):
            fq=falling(q,s)*stirling2(q,s)
            out[(r-1)*(s-1)]+=fp*fq
    return out


def predicted_total(p,q):
    return p**p*q**q + q*((p+1)**p-p**p) + p*((q+1)**q-q**q)


def check_case(p,q,components=False):
    maps=all_maps(p,q)
    assert len(maps)==predicted_total(p,q)
    prof=Counter(h1_rank_direct(f,p,q) for f in maps)
    assert prof==predicted_profile(p,q), (p,q,prof,predicted_profile(p,q))
    nonzero=sum(v for k,v in prof.items() if k>0)
    assert nonzero==(p**p-p)*(q**q-q)
    iso=sum(1 for f in maps if h1_rank_direct(f,p,q)==(p-1)*(q-1))
    assert iso==factorial(p)*factorial(q)
    comp_sizes=None
    if components:
        N=len(maps)
        adj=[[] for _ in range(N)]
        for i in range(N):
            for j in range(i+1,N):
                if comparable(maps[i],maps[j],p,q):
                    adj[i].append(j); adj[j].append(i)
        seen=[False]*N; comp_sizes=[]
        for s in range(N):
            if seen[s]: continue
            seen[s]=True; dq=deque([s]); c=0
            while dq:
                u=dq.popleft(); c+=1
                for v in adj[u]:
                    if not seen[v]: seen[v]=True; dq.append(v)
            comp_sizes.append(c)
        comp_sizes.sort(reverse=True)
        predicted_classes=1+(p**p-p)*(q**q-q)
        assert len(comp_sizes)==predicted_classes
        assert comp_sizes[0]==prof[0]
        assert all(x==1 for x in comp_sizes[1:])
    print(f"CASE p={p} q={q} maps={len(maps)} profile={dict(sorted(prof.items()))} classes={1+(p**p-p)*(q**q-q)}" + (f" component_sizes_head={comp_sizes[:5]}" if components else ""))

check_case(3,3,components=True)
check_case(3,4,components=False)
print("VERIFY_OK")
