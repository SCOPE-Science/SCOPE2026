"""Standalone exact checks for the strong-resolving polynomial of line Grassmann graphs.

Run with Python 3.10+; standard library only. Finite test fields are GF(2), GF(3).
"""
from itertools import product
from math import comb
from collections import Counter


def point_rep(v, q):
    for x in v:
        if x:
            inv = pow(x, -1, q)
            return tuple((t * inv) % q for t in v)
    raise ValueError('zero vector')


def projective_points(q, d):
    return sorted({point_rep(v, q) for v in product(range(q), repeat=d) if any(v)})


def projective_lines(q, d):
    pts = projective_points(q, d)
    idx = {p: i for i, p in enumerate(pts)}
    lines = set()
    for i, a in enumerate(pts):
        for b in pts[i + 1:]:
            line = {idx[b]}
            for t in range(q):
                line.add(idx[point_rep(tuple((x + t*y) % q for x, y in zip(a, b)), q)])
            assert len(line) == q + 1
            lines.add(frozenset(line))
    return pts, sorted(lines, key=lambda f: tuple(sorted(f)))


def gaussian(n, k, q):
    num = den = 1
    for i in range(k):
        num *= q**(n-i)-1
        den *= q**(k-i)-1
    assert num % den == 0
    return num // den


def predicted(q, d):
    N=gaussian(d,2,q)
    p=gaussian(d,1,q)
    t=gaussian(d,3,q)
    r=gaussian(d-1,1,q)
    s=q*q+q+1
    coefficients=[1,N]
    for k in range(2,max(r,s)+1):
        c=lambda a,k: comb(a,k) if 0<=k<=a else 0
        coefficients.append(p*c(r,k)+t*(c(s,k)-s*c(q+1,k)))
    return coefficients


def maximal_cliques(neigh):
    """Exact Bron-Kerbosch enumeration on integer-mask adjacency."""
    n=len(neigh)
    def bit_iter(x):
        while x:
            b=x&-x
            yield b.bit_length()-1
            x-=b
    def explore(R,P,X):
        if not (P or X):
            yield R
            return
        pivot=max(bit_iter(P|X),key=lambda u:(P & neigh[u]).bit_count())
        candidates=P & ~neigh[pivot]
        for v in tuple(bit_iter(candidates)):
            bit=1<<v
            yield from explore(R|bit,P & neigh[v],X & neigh[v])
            P &= ~bit
            X |= bit
    return list(explore(0,(1<<n)-1,0))


def rank_mod(vectors,p):
    a=[list(v) for v in vectors]
    if not a: return 0
    nr=len(a); nc=len(a[0]); rank=0
    for col in range(nc):
        piv=next((i for i in range(rank,nr) if a[i][col]%p),None)
        if piv is None: continue
        a[rank],a[piv]=a[piv],a[rank]
        inv=pow(a[rank][col],-1,p)
        a[rank]=[(x*inv)%p for x in a[rank]]
        for row in range(nr):
            if row!=rank and a[row][col]:
                coef=a[row][col]
                a[row]=[(x-coef*y)%p for x,y in zip(a[row],a[rank])]
        rank+=1
        if rank==min(nr,nc): break
    return rank


def check(q,d):
    pts,lines=projective_lines(q,d)
    n=len(lines); assert n==gaussian(d,2,q)
    adj=[]
    for i,line in enumerate(lines):
        mask=0
        for j,other in enumerate(lines):
            if i!=j and not line.isdisjoint(other): mask|=1<<j
        adj.append(mask)
    # MMD pairs are exactly nonadjacent pairs, checked from all neighbors.
    for i in range(n):
        for j in range(i+1,n):
            dij=1 if adj[i]>>j&1 else 2
            i_md=all((1 if adj[k]>>j&1 else 2 if k!=j else 0)<=dij
                     for k in range(n) if adj[i]>>k&1)
            j_md=all((1 if adj[k]>>i&1 else 2 if k!=i else 0)<=dij
                     for k in range(n) if adj[j]>>k&1)
            assert (i_md and j_md)==(dij==2)
    maxima=maximal_cliques(adj)
    assert len(maxima)==gaussian(d,1,q)+gaussian(d,3,q)
    star=top=0
    for m in maxima:
        ids=[i for i in range(n) if m>>i&1]
        core=set(lines[ids[0]])
        for i in ids[1:]: core &= lines[i]
        if core:
            assert len(core)==1 and len(ids)==gaussian(d-1,1,q)
            star+=1
        else:
            spanned={p for i in ids for p in lines[i]}
            assert rank_mod([pts[p] for p in spanned],q)==3
            assert len(ids)==q*q+q+1
            top+=1
    assert star==gaussian(d,1,q) and top==gaussian(d,3,q)
    # Independent computation of each coefficient: union of the Boolean subcubes
    # supported on independently enumerated maximal cliques.
    all_sets=set()
    for m in maxima:
        bits=[]
        x=m
        while x:
            b=x&-x; bits.append(b); x-=b
        cur=[0]
        for b in bits:
            cur.extend(v|b for v in tuple(cur))
        all_sets.update(cur)
    actual=Counter(x.bit_count() for x in all_sets)
    expected=predicted(q,d)
    assert [actual[k] for k in range(len(expected))]==expected
    assert sum(actual.values())==len(all_sets)
    print('VERIFY_OK q=%d d=%d points=%d lines=%d stars=%d tops=%d cliques=%d' %
          (q,d,len(pts),n,star,top,len(all_sets)))
    print('VERIFY_POLYNOMIAL_OK q=%d d=%d coefficients=%s' % (q,d,','.join(map(str,expected))))

if __name__=='__main__':
    for parameters in [(2,4),(3,4),(2,5)]:
        check(*parameters)
    print('VERIFY_FINISHED all finite checks passed')
