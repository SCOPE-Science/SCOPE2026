#!/usr/bin/env python3
"""Exact finite checks for geodesic general-position complexes of uniform spiders.
No third-party dependencies. The unrestricted mathematical statement uses a chain proof.
"""
from itertools import combinations, permutations, product
from math import comb, factorial
from collections import defaultdict, deque


def spider(r, ell):
    vertices = list(range(1, 1 + r * ell))
    groups = [list(range(1 + a * ell, 1 + (a + 1) * ell)) for a in range(r)]
    adj = {v: set() for v in range(1 + r * ell)}
    for group in groups:
        last = 0
        for v in group:
            adj[last].add(v)
            adj[v].add(last)
            last = v
    return adj, groups


def distances(adj):
    ds = {}
    for x in adj:
        d = {x: 0}
        q = deque([x])
        while q:
            v = q.popleft()
            for w in adj[v]:
                if w not in d:
                    d[w] = d[v] + 1
                    q.append(w)
        assert len(d) == len(adj)
        ds[x] = d
    return ds


def direct_faces(ds):
    vs = sorted(ds)
    forbidden = set()
    for x, y, z in combinations(vs, 3):
        if any(ds[a][c] == ds[a][b] + ds[b][c]
               for a,b,c in ((x,y,z), (x,z,y), (y,x,z))):
            forbidden.add(frozenset((x,y,z)))
    faces = [()]
    for k in range(1, len(vs)+1):
        for s in combinations(vs, k):
            fs = set(s)
            if not any(t <= fs for t in forbidden):
                faces.append(s)
    return faces


def model_faces(groups):
    arms = [set(g) for g in groups]
    vs = sorted(set.union(*arms))
    faces = [()]
    for k in range(1, len(groups)+1):
        for arm_indices in combinations(range(len(groups)),k):
            for chosen in product(*(groups[i] for i in arm_indices)):
                faces.append(tuple(sorted(chosen)))
    for g in groups:
        faces.extend(combinations(g,2))
    faces.append((0,))
    faces.extend((0,v) for v in vs)
    assert len(faces) == len(set(faces))
    return faces


def rank_binary(cols):
    pivot = {}
    for x in cols:
        while x:
            p = x.bit_length()-1
            if p in pivot:
                x ^= pivot[p]
            else:
                pivot[p] = x
                break
    return len(pivot)


def betti_mod2(faces):
    bydim = defaultdict(list)
    for f in faces:
        if f:
            bydim[len(f)-1].append(f)
    ranks = {}
    for d in range(1,max(bydim)+1):
        rows={f:i for i,f in enumerate(bydim[d-1])}
        cols=[sum(1 << rows[f[:j]+f[j+1:]] for j in range(len(f))) for f in bydim[d]]
        ranks[d] = rank_binary(cols)
    return {d:len(faces_d)-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0)
            for d,faces_d in bydim.items()}


def par_sign(mapping):
    inversions = sum(a>b for i,a in enumerate(mapping) for b in mapping[i+1:])
    return -1 if inversions%2 else 1


def cycle_count(perm):
    n=len(perm)
    seen=set()
    count=0
    for a in range(n):
        if a not in seen:
            count+=1
            j=a
            while j not in seen:
                seen.add(j)
                j=perm[j]
    return count


def check(r,ell):
    adj,groups=spider(r,ell)
    faces=direct_faces(distances(adj))
    predicted=model_faces(groups)
    assert set(faces)==set(predicted), (r,ell,'facets mismatch')
    ranks=betti_mod2(faces)
    h1=r*(comb(ell,2)+ell)-1
    htop=(ell-1)**r
    expected={1:h1,r-1:htop}
    if r == 2:
        expected[1]=h1+htop
    for d in range(1,max(ranks)+1):
        assert ranks.get(d,0)==expected.get(d,0), (r,ell,d,ranks,expected)
    # Signed chain traces, independent of the proposed character formulas.
    all_dim=defaultdict(list)
    for f in faces:
        if f:all_dim[len(f)-1].append(f)
    perm_tests=list(permutations(range(r)))
    for arm_perm in perm_tests:
        vperm={0:0}
        for a in range(r):
            for depth in range(ell):
                vperm[groups[a][depth]]=groups[arm_perm[a]][depth]
        chain_lefschetz=0
        for d,fs in all_dim.items():
            signed_trace=0
            for f in fs:
                ordered=tuple(vperm[v] for v in f)
                if set(ordered)==set(f):
                    signed_trace+=par_sign(ordered)
            chain_lefschetz+=(-1)**d*signed_trace
        fixed=sum(arm_perm[a]==a for a in range(r))
        h1_trace=(comb(ell,2)+ell)*fixed-1
        inv=sum(arm_perm[i]>arm_perm[j] for i in range(r) for j in range(i+1,r))
        top_trace=(-1)**inv*(ell-1)**cycle_count(arm_perm)
        target=1-h1_trace+(-1)**(r-1)*top_trace
        assert chain_lefschetz==target,(r,ell,arm_perm,chain_lefschetz,target)
    quotient_h1=comb(ell,2)+ell-1
    quotient_htop=comb(ell-1,r) if ell-1>=r else 0
    h1_avg=sum((comb(ell,2)+ell)*sum(p[a]==a for a in range(r))-1 for p in perm_tests)
    ht_avg=sum((-1)**sum(p[i]>p[j] for i in range(r) for j in range(i+1,r))*(ell-1)**cycle_count(p)
               for p in perm_tests)
    assert h1_avg==factorial(r)*quotient_h1
    assert ht_avg==factorial(r)*quotient_htop
    return len(faces), len(perm_tests), ranks, quotient_h1, quotient_htop


def main():
    profiles=[(3,1),(3,2),(3,3),(3,4),(4,1),(4,2),(4,3),(5,1),(5,2)]
    total_faces=0; total_perms=0
    for r,ell in profiles:
        result=check(r,ell)
        total_faces+=result[0];total_perms+=result[1]
        print(f'r={r},ell={ell}: faces={result[0]}, permutations={result[1]}, reduced_mod2_betti={result[2]}, quotient_H1={result[3]}, quotient_Htop={result[4]}')
    print(f'PASS: {len(profiles)} profiles, {total_faces} faces, {total_perms} signed symmetry tests')

if __name__=='__main__': main()
