#!/usr/bin/env python3
"""Independent finite checks of projective rook partial-conjugation enumeration."""
from itertools import combinations, permutations, product
from collections import Counter
from math import comb, factorial


def cyclic(m):
    return tuple(tuple((a+b)%m for b in range(m)) for a in range(m))

def klein():
    return tuple(tuple(a^b for b in range(4)) for a in range(4))

def symmetric3():
    pp=list(permutations(range(3)))
    index={p:i for i,p in enumerate(pp)}
    return tuple(tuple(index[tuple(a[b[j]] for j in range(3))] for b in pp) for a in pp)

def quaternion8():
    # ±1, ±i, ±j, ±k indexed 0..7 as sign*4 + basis.
    # i*j=k, j*k=i, k*i=j; reverse products have a minus sign.
    # Representation (sign, quaternion basis) with sign 0 positive and 1 negative.
    signs=((0,0,0,0),(0,1,0,1),(0,1,1,0),(0,0,1,1))
    axes=((0,1,2,3),(1,0,3,2),(2,3,0,1),(3,2,1,0))
    return tuple(tuple(4*((a//4)^(b//4)^signs[a%4][b%4])+axes[a%4][b%4] for b in range(8)) for a in range(8))


def group_info(tab):
    N=len(tab)
    ident=next(e for e in range(N) if all(tab[e][x]==x and tab[x][e]==x for x in range(N)))
    inv={a:next(b for b in range(N) if tab[a][b]==ident==tab[b][a]) for a in range(N)}
    Z=[a for a in range(N) if all(tab[a][b]==tab[b][a] for b in range(N))]
    assert all(tab[tab[a][b]][c]==tab[a][tab[b][c]] for a in range(N) for b in range(N) for c in range(N))
    return ident, inv, Z


def elems(n,tab):
    N=len(tab)
    yield ()
    for r in range(1,n+1):
        for a in combinations(range(n),r):
            for b in permutations(range(n),r):
                if len(set(b))!=r: continue
                for labels in product(range(N),repeat=r):
                    yield tuple(sorted(zip(a,b,labels)))


def project(g,tab,Z):
    if not g: return ()
    return min(tuple((a,b,tab[z][v]) for a,b,v in g) for z in Z)


def invmap(g,inv):
    return tuple(sorted((b,a,inv[v]) for a,b,v in g))


def multiply(g,h,tab):
    # arrows first g, then h: maps a->b->c, label multiplication accordingly
    hd={a:(b,v) for a,b,v in h}
    return tuple(sorted((a,hd[b][0],tab[v][hd[b][1]]) for a,b,v in g if b in hd))


def direct_signature(g,tab,inv):
    # conjugation on all single matrix units in the maximal local corner
    src=sorted(b for _,b,_ in g)
    lookup={b:(a,v) for a,b,v in g}
    return (tuple(src),tuple((b,c,x,lookup[b][0],lookup[c][0],tab[tab[inv[lookup[b][1]]][x]][lookup[c][1]])
        for b in src for c in src for x in range(len(tab))))


def formula(n,tab,Z):
    N=len(tab); z=len(Z)
    sq={u:sum(tab[a][a]==u for a in range(N)) for u in Z}
    ranks=[]; selfs=[]
    for r in range(n+1):
        ranks.append(1 if r==0 else comb(n,r)**2*factorial(r)*N**r//z)
        if r==0:
            selfs.append(1);continue
        s=0
        for t in range(r//2+1):
            f=r-2*t
            arrangements=factorial(r)//(factorial(f)*factorial(t)*2**t)
            sumroot=sum(k**f for k in sq.values())
            s+=arrangements*(N**t)*sumroot//z
        selfs.append(comb(n,r)*s)
    return ranks,selfs


def run(name,tab,n):
    ident,inv,Z=group_info(tab)
    reps={}
    sigs={}
    for g in elems(n,tab):
        k=project(g,tab,Z)
        reps[k]=g
        if n<=2 or (n==3 and name in ('C2','S3')):
            sig=direct_signature(g,tab,inv)
            assert (sig in sigs and sigs[sig]==k) or sig not in sigs
            sigs[sig]=k
    if n<=2 or (n==3 and name in ('C2','S3')):
        assert len(sigs)==len(reps)
    rank=Counter(); iself=Counter()
    for k in reps:
        r=len(k)
        rank[r]+=1
        kinv=project(invmap(k,inv),tab,Z)
        if k==kinv:
            assert project(multiply(k,k,tab),tab,Z)==project(tuple((a,a,ident) for a,_,_ in k),tab,Z)
            iself[r]+=1
    want_r,want_i=formula(n,tab,Z)
    got_r=[rank[r] for r in range(n+1)]; got_i=[iself[r] for r in range(n+1)]
    assert got_r==want_r,(name,n,got_r,want_r)
    assert got_i==want_i,(name,n,got_i,want_i)
    print(name,'n=',n,'|G|=',len(tab),'|Z|=',len(Z),'rank=',got_r,'self_inverse=',got_i,'PASS')

if __name__=='__main__':
    for name,group in [('C2',cyclic(2)),('C3',cyclic(3)),('C4',cyclic(4)),('V4',klein()),('S3',symmetric3()),('Q8',quaternion8())]:
        for n in (1,2,3): run(name,group,n)
    print('VERIFY_OK')
