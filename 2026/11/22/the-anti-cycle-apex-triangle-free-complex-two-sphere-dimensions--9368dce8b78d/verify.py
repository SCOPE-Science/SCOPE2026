#!/usr/bin/env python3
"""Independent finite checks for triangle-free subset complexes of cones over cycle complements.
Only standard Python is needed. This is finite corroboration, not the proof of the all-n result.
"""
from collections import defaultdict, Counter, deque
from itertools import combinations
from math import comb


def triangles(n):
    """Forbidden triangles of K_1 * complement(C_n), with apex n."""
    edges = set()
    for i in range(n):
        for j in range(i+1, n):
            if ((j-i) % n not in (1, n-1)):
                edges.add((i, j))
        edges.add((i, n))
    return [sum(1 << x for x in t) for t in combinations(range(n+1), 3)
            if all(tuple(sorted(p)) in edges for p in combinations(t, 2))]


def simplices(n):
    forbidden = triangles(n)
    fs = [S for S in range(1 << (n+1)) if not any((S & t) == t for t in forbidden)]
    return fs


def cycle_edge_facets(n):
    edges = [(i, (i+1)%n) for i in range(n)]
    return {sum(1 << v for v in (a+b)) for a,b in combinations(edges, 2)
            if len(set(a+b)) == 4}


def orient_facets(n, facet_set):
    facets = sorted(facet_set)
    ridge_to_facets=defaultdict(list)
    for facet in facets:
        seq=[v for v in range(n) if facet & (1<<v)]
        for idx in range(4):
            ridge=facet^(1<<seq[idx])
            ridge_to_facets[ridge].append((facet,(-1)**idx))
    assert all(len(entries)==2 for entries in ridge_to_facets.values())
    signs={facets[0]:1}; todo=deque([facets[0]])
    while todo:
        a=todo.popleft(); seq=[v for v in range(n) if a&(1<<v)]
        for idx in range(4):
            ridge=a^(1<<seq[idx]); aa=(-1)**idx
            for b,bb in ridge_to_facets[ridge]:
                if a==b: continue
                want=-signs[a]*aa*bb
                if b in signs: assert signs[b]==want
                else: signs[b]=want; todo.append(b)
    assert len(signs)==len(facets)
    chain=Counter()
    for a,sgn in signs.items():
        seq=[v for v in range(n) if a&(1<<v)]
        for idx in range(4):chain[a^(1<<seq[idx])]+=sgn*((-1)**idx)
    assert all(val==0 for val in chain.values())
    return signs


def action_sign(n, signs, p):
    a=next(iter(signs)); base=[v for v in range(n) if a & (1<<v)]
    seq=[p(v) for v in base]
    b=sum(1<<v for v in seq)
    inversions=sum(seq[i]>seq[j] for i in range(4) for j in range(i+1,4))
    assert b in signs
    return signs[a]*signs[b]*(-1 if inversions%2 else 1)


def betti_mod2(n, fs):
    by=defaultdict(list)
    for s in fs:
        if s: by[s.bit_count()-1].append(s)
    ranks={}
    for d in sorted(by):
        if d==0: continue
        basis={}; idx={face:j for j,face in enumerate(by[d-1])}
        for face in by[d]:
            row=0; bits=face
            while bits:
                bit=bits&-bits; bits-=bit
                row ^= 1<<idx[face^bit]
            while row:
                head=row.bit_length()-1
                if head in basis:row^=basis[head]
                else:basis[head]=row;break
        ranks[d]=len(basis)
    return {d: len(by[d])-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0)
            for d in sorted(by) if len(by[d])-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0)}


def main():
    for n in range(3, 13):
        fs=simplices(n); fset=set(fs)
        assert len(fs)==len(fset)
        # A face containing the apex h is equivalent to an independent set of the base complement.
        apex_faces=[s for s in fs if s&(1<<n)]
        assert all(all(((i-j)%n in (1,n-1)) for i,j in combinations([v for v in range(n) if s&(1<<v)], 2)) for s in apex_faces)
        base={s for s in fset if not (s&(1<<n))}
        if n in (4,5):
            assert len(base)==(1<<n)
        if n>=6:
            expected=cycle_edge_facets(n)
            true_facets={s for s in base if not any(s!=t and s&t==s for t in base)}
            assert true_facets==expected, (n,true_facets^expected)
            assert all(any(s & facet==s for facet in expected) for s in base)
            assert len(expected)==n*(n-3)//2
            dim_count=Counter(s.bit_count()-1 for s in fs if s)
            assert [dim_count[d] for d in range(4)]==[n+1,comb(n+1,2),n*(n-2),n*(n-3)//2]
            orient=orient_facets(n,expected)
            assert action_sign(n,orient,lambda i:(i+1)%n)==1
            assert action_sign(n,orient,lambda i:(-i)%n)==1
        else:dim_count=Counter(s.bit_count()-1 for s in fs if s)
        if n<=10:
            b=betti_mod2(n,fs)
            want={} if n==3 else ({2:1} if n in (4,5) else {2:1,3:1})
            assert b==want, (n,b,want)
        else:b='not computed'
        print(f'n={n}: faces={len(fs)-1}; f={dict(sorted(dim_count.items()))}; reduced_F2_homology={b}; checks=PASS')
    print('ALL FINITE CHECKS PASSED; infinite conclusion requires the geometric proof.')

if __name__=='__main__':main()
