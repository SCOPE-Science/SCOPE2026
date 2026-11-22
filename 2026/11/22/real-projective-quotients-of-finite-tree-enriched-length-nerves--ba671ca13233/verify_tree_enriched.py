#!/usr/bin/env python3
"""Finite arithmetic checks of ordered graph-distance length nerves and free quotients.

No external dependencies. Mod-p tests illustrate, but do not prove, infinite claims.
"""
from collections import defaultdict


def distmat(n, edges):
    d = [[0 if i == j else n + 2 for j in range(n)] for i in range(n)]
    for i,j in edges:
        d[i][j] = d[j][i] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


def cells(n, edges, L):
    d = distmat(n,edges)
    c = {0:[(i,) for i in range(n)]}
    for k in range(1,L+1):
        a=[]
        for t in c[k-1]:
            length=sum(d[t[i]][t[i+1]] for i in range(len(t)-1))
            for j in range(n):
                if j!=t[-1] and length+d[t[-1]][j]<=L:
                    a.append(t+(j,))
        c[k]=a
    return c


def rank_mod(columns,p):
    piv={}
    for co in columns:
        a={k:v%p for k,v in co.items() if v%p}
        while a:
            k=max(a)
            val=a[k]
            if k not in piv:
                piv[k]={j: v*pow(val,-1,p)%p for j,v in a.items()}
                break
            for j,v in piv[k].items():
                a[j]=(a.get(j,0)-val*v)%p
                if a[j]==0:a.pop(j,None)
    return len(piv)


def chain_betti(n,edges,L,p,swap=None):
    c=cells(n,edges,L)
    if swap is not None:
        assert sorted(swap)==list(range(n))
        assert all(swap[swap[i]]==i and swap[i]!=i for i in range(n))
        assert {tuple(sorted((swap[i],swap[j]))) for i,j in edges} == {tuple(sorted(e)) for e in edges}
        def canon(t):
            return min(t,tuple(swap[i] for i in t))
    else:
        def canon(t):return t
    c={k:sorted(set(canon(t) for t in ts)) for k,ts in c.items()}
    ranks={0:0}
    for k in range(1,L+1):
        idx={x:i for i,x in enumerate(c[k-1])}
        columns=[]
        for t in c[k]:
            co=defaultdict(int)
            for j in range(k+1):
                f=t[:j]+t[j+1:]
                if any(f[h]==f[h+1] for h in range(len(f)-1)):continue
                co[idx[canon(f)]]+=1 if j%2==0 else -1
            columns.append(co)
        ranks[k]=rank_mod(columns,p)
    return [len(c[k])-ranks.get(k,0)-ranks.get(k+1,0) for k in range(L+1)]


def main():
    trees=[('edge',2,[(0,1)],None),
           ('path3',3,[(0,1),(1,2)],None),
           ('path4',4,[(i,i+1) for i in range(3)],[3,2,1,0]),
           ('star4',4,[(0,1),(0,2),(0,3)],None),
           ('path5',5,[(i,i+1) for i in range(4)],None),
           ('path6',6,[(i,i+1) for i in range(5)],[5,4,3,2,1,0]),
           ('double-star6',6,[(0,1),(0,2),(0,3),(1,4),(1,5)],[1,0,4,5,2,3]),
           ('path8',8,[(i,i+1) for i in range(7)],[7,6,5,4,3,2,1,0])]
    total=0
    for name,n,edges,swap in trees:
        max_L=4 if n<=6 else 3
        for L in range(1,max_L+1):
            for p in (2,3,5):
                b=chain_betti(n,edges,L,p)
                assert b==[1]+[0]*(L-1)+[n-1], (name,L,p,'cover',b)
                total+=1
                if swap:
                    q=chain_betti(n,edges,L,p,swap)
                    s=(n-2)//2
                    # RP^L mod p has a top class for p odd iff L odd;
                    # at p=2 it has one class in each degree through L.
                    expected=[1]+([1]*(L-1) if p==2 else [0]*(L-1))
                    expected += [s+(1 if p==2 or L%2 else 0)]
                    assert q==expected, (name,L,p,'quotient',q,expected)
                    total+=1
    print('PASS: %d independent modular homology checks over p=2,3,5'%total)
    print('Cases: edge, paths, star, branched double-star; degrees through four.')
    print('NOTE: finite-field verification is not an integral proof or an exhaustive theorem test.')

if __name__=='__main__':main()
