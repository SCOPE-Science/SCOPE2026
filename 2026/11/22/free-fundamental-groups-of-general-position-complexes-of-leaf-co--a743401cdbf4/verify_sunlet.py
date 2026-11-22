#!/usr/bin/env python3
"""Independent finite checks for the sunlet general-position fundamental group theorem."""
from collections import deque
from itertools import combinations
from math import comb


def graph(n):
    N=2*n
    a=[set() for _ in range(N)]
    for i in range(n):
        for j in ((i+1)%n,n+i):
            a[i].add(j); a[j].add(i)
    return a


def distances(a):
    out=[]
    for start in range(len(a)):
        d=[-1]*len(a);d[start]=0
        queue=deque([start])
        while queue:
            u=queue.popleft()
            for v in a[u]:
                if d[v]<0:
                    d[v]=d[u]+1; queue.append(v)
        assert min(d)>=0
        out.append(d)
    return out


def good(d,a,b,c):
    x,y,z=d[a][b],d[a][c],d[b][c]
    return x+y>z and x+z>y and y+z>x


def rank_mod_prime(rows,p):
    pivots={}
    for row in rows:
        v={k:t%p for k,t in row.items() if t%p}
        while v:
            k=max(v)
            if k not in pivots:
                z=v[k]; inv=pow(z,-1,p)
                pivots[k]={j:(x*inv)%p for j,x in v.items()}
                break
            q=pivots[k]; c=v[k]
            for j,x in q.items():
                y=(v.get(j,0)-c*x)%p
                if y: v[j]=y
                elif j in v: del v[j]
    return len(pivots)


def check(n,primes):
    adj=graph(n);d=distances(adj)
    N=2*n; base=n
    pairs=[(i,j) for i in range(N) for j in range(i+1,N) if i!=base and j!=base]
    index={e:i for i,e in enumerate(pairs)}
    faces3=[(i,j,k) for i,j,k in combinations(range(N),3) if good(d,i,j,k)]
    rows=[]
    for i,j,k in faces3:
        r={}
        for e,c in [((j,k),1),((i,k),-1),((i,j),1)]:
            if base not in e: r[index[e]]=c
        rows.append(r)
    expected=n if n%2 else 2*n
    betti={}
    for p in primes:
        rank=rank_mod_prime(rows,p)
        betti[p]=len(pairs)-rank
        assert betti[p]==expected,(n,p,betti[p],expected)

    # Independently test the proof's exceptional-pair and one-root link statements.
    empty=[]; unmatched=[]
    for i,j in combinations(range(n),2):
        permissible=[k for k in range(n) if good(d,i,j,n+k)]
        if not permissible: empty.append((i,j))
        if n%2==0 and ((j-i)%n==1 or (j-i)%n==n-1):
            assert not permissible
            assert all(not good(d,i,j,k) for k in range(n) if k!=i and k!=j)
        elif not permissible: unmatched.append((i,j))
    assert not unmatched
    assert len(empty)==(0 if n%2 else n)

    for i in range(n):
        leaves=range(n,2*n)
        good_edges={(a,b) for a,b in combinations(leaves,2) if good(d,i,a,b)}
        assert all((min(n+i,a),max(n+i,a)) not in good_edges for a in leaves if a!=n+i)
        reachable={n+(i+1)%n}
        while True:
            new=reachable|{v for a,b in good_edges for v in (a,b) if a in reachable or b in reachable}
            if new==reachable: break
            reachable=new
        assert reachable==set(leaves)-{n+i}
    return f'n={n:2d} allowable_triangles={len(faces3):5d} exceptional_root_edges={len(empty):2d} H1_dimensions={betti}'


def main():
    print('Sunlet geodesic general-position complex: direct all-pairs BFS verification')
    for n in range(3,15):
        print(check(n,(2,3,5)))
    for n in (15,16,18,20):
        print(check(n,(2,)))
    print('ALL CHECKS PASSED')


if __name__=='__main__':
    main()
