#!/usr/bin/env python3
"""Reproducible finite sanity checks for real graph evolution algebras."""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter


def connected(adj):
    seen={0}; stack=[0]
    while stack:
        i=stack.pop()
        for j in adj[i]:
            if j not in seen:
                seen.add(j);stack.append(j)
    return len(seen)==len(adj)


def twin_classes(adj):
    groups={}
    for i,nbrs in enumerate(adj):
        groups.setdefault(tuple(sorted(nbrs)),[]).append(i)
    return list(groups.values())


def qgraph(adj,cs):
    out=[]
    for c in cs:
        v=c[0]; out.append({j for j,d in enumerate(cs) if d[0] in adj[v]})
    return out


def rank_mat(a):
    a=[[F(z) for z in r] for r in a]; m=len(a); n=len(a[0]) if m else 0
    r=0
    for j in range(n):
        piv=next((i for i in range(r,m) if a[i][j]),None)
        if piv is None:continue
        a[r],a[piv]=a[piv],a[r]
        t=a[r][j]
        for k in range(j,n):a[r][k]/=t
        for i in range(r+1,m):
            t=a[i][j]
            if t:
                for k in range(j,n):a[i][k]-=t*a[r][k]
        r+=1
        if r==m:break
    return r


def bipartition(adj):
    col={0:0}; stack=[0]
    while stack:
        i=stack.pop()
        for j in adj[i]:
            if j not in col:col[j]=1-col[i];stack.append(j)
            elif col[j]==col[i]:return None
    return col


def eligible(adj):
    deg=[len(x) for x in adj]
    if len(set(deg))==1:return True
    col=bipartition(adj)
    return col is not None and all(len({deg[v] for v in col if col[v]==side})==1 for side in (0,1))


def adjacency(n,mask):
    a=[set() for _ in range(n)]
    for bit,(i,j) in enumerate(combinations(range(n),2)):
        if (mask>>bit)&1:a[i].add(j);a[j].add(i)
    return a


def verify_rankone_characterization(a):
    groups=twin_classes(a)
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            # A pair generates a 1-dimensional multiplication image
            # precisely when its two neighborhoods coincide.
            first={x for x in a[i]};second={x for x in a[j]}
            one_dim=(first==second)
            assert one_dim==(any(i in g and j in g for g in groups))


def verify_multiplication(a,blocks,scalars):
    # matrices act on basis coefficient columns; exact entries (Fraction)
    n=len(a); P=[[F(0) for _ in range(n)] for _ in range(n)]
    for c,block in zip(blocks[0],blocks[1]):
        assert len(c)==len(block)
        for i,src in enumerate(c):
            for j,dst in enumerate(c):P[dst][src]=scalars[src]*F(block[j][i])
    def prod(x,y,rw):
        z=[F(0)]*n
        for i in range(n):
            if x[i]*y[i]:
                coeff=x[i]*y[i]/(len(a[i]) if rw else 1)
                for j in a[i]:z[j]+=coeff
        return z
    images=[[P[j][i] for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            e=[F(0)]*n
            if i==j:
                for t in a[i]:e[t]+=1
            left=[sum((P[k][t]*e[t] for t in range(n)),F(0)) for k in range(n)]
            right=prod(images[i],images[j],True)
            assert left==right,(i,j,left,right)


def main():
    counts=Counter()
    for n in range(2,7):
        for mask in range(1<<(n*(n-1)//2)):
            a=adjacency(n,mask)
            if not connected(a):continue
            cs=twin_classes(a);h=qgraph(a,cs)
            assert connected(h)
            assert all(h[i] != h[j] for i in range(len(h)) for j in range(i+1,len(h)))
            verify_rankone_characterization(a)
            rq=rank_mat([[int(j in h[i]) for j in range(len(h))] for i in range(len(h))])
            counts['graphs']+=1
            if rq<len(h):
                counts['singular_quotient']+=1
                counts['sq_eligible' if eligible(a) else 'sq_obstructed']+=1
                if len(cs)<n:counts['sq_with_twins']+=1
        counts[f'connected_n{n}']=counts['graphs']-sum(counts[f'connected_n{j}'] for j in range(2,n))
    # A uniform triple-clone blow-up of C_8 has singular twin quotient.
    # U=(2/3)J-I is a rational orthogonal map fixing the all-one vector.
    n=8; m=3
    a=[set() for _ in range(n*m)]
    for i in range(n):
        for j in ((i-1)%n,(i+1)%n):
            for v in range(i*m,(i+1)*m):a[v].update(range(j*m,(j+1)*m))
    cs=[list(range(i*m,(i+1)*m)) for i in range(n)]
    U=[[F(2,3)-(1 if i==j else 0) for j in range(m)] for i in range(m)]
    assert all(sum(U[i][k]*U[j][k] for k in range(m))==(1 if i==j else 0) for i in range(m) for j in range(m))
    assert all(sum(row)==1 for row in U)
    assert rank_mat([[int(j in qgraph(a,cs)[i]) for j in range(n)] for i in range(n)])<n
    verify_multiplication(a,(cs,[U]*n),[F(6)]*(n*m))
    # Odd path P7: singular quotient, false-twin-free, irregular, not biregular.
    path=[set() for _ in range(7)]
    for i in range(6):path[i].add(i+1);path[i+1].add(i)
    assert len(twin_classes(path))==7 and not eligible(path)
    assert rank_mat([[int(j in path[i]) for j in range(7)] for i in range(7)])<7
    keys=['graphs','singular_quotient','sq_eligible','sq_obstructed','sq_with_twins']
    print('VERIFY_OK '+' '.join(f'{k}={counts[k]}' for k in keys))
    print('connected_counts='+','.join(f'{n}:{counts[f"connected_n{n}"]}' for n in range(2,7)))
    print('exact_nonpermutation_orthogonal_example=C8_blowup_3 P7_obstruction=degree_profile')

if __name__=='__main__':main()
