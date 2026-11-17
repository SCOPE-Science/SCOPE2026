#!/usr/bin/env python3
"""Finite signed-Lefschetz and homology checks for the perfect-matching ladder complex.

Run: python3 verify_ladder.py
Only the Python standard library is used.
"""
from collections import defaultdict
from math import comb


def dataset(n):
    """All perfect-matchings and their faces, represented by edge bitmasks."""
    a = list(range(n))
    b = list(range(n, 2*n-1))
    c = list(range(2*n-1, 3*n-2))
    def rec(i):
        if i == n:
            yield 0
            return
        for s in rec(i+1):
            yield s | (1 << a[i])
        if i+1 < n:
            for s in rec(i+2):
                yield s | (1 << b[i]) | (1 << c[i])
    perfect = list(rec(0))
    faces = set()
    for s in perfect:
        t = s
        while True:
            faces.add(t)
            if t == 0:
                break
            t = (t - 1) & s
    return a, b, c, perfect, faces


def maps(n, a, b, c, row=False, end=False):
    perm = {}
    for i in range(n):
        perm[a[i]] = a[n-1-i] if end else a[i]
    for i in range(n-1):
        j = n-2-i if end else i
        perm[b[i]] = c[j] if row else b[j]
        perm[c[i]] = b[j] if row else c[j]
    return perm


def sign_trace(faces, perm):
    """Direct reduced alternating trace on augmented simplicial chains."""
    total = 0
    invariant = 0
    for f in faces:
        ids = [i for i in range(len(perm)) if f & (1 << i)]
        mapped = 0
        for i in ids:
            mapped |= 1 << perm[i]
        if mapped != f:
            continue
        invariant += 1
        inversions = sum(perm[x] > perm[y] for k,x in enumerate(ids)
                         for y in ids[k+1:])
        total += (-1) ** (len(ids) + inversions)
    return -total, invariant


def gf2_betti(faces):
    """Independent boundary-matrix ranks using exact binary column elimination."""
    by_card = defaultdict(list)
    for f in faces:
        if f: by_card[f.bit_count()].append(f)
    dims = {i:len(v) for i,v in by_card.items()}
    rank = {}
    for j in range(2, max(dims)+1):
        lower = {f:i for i,f in enumerate(by_card[j-1])}
        pivots = {}
        for f in by_card[j]:
            mask = 0
            t = f
            while t:
                bit = t & -t
                mask ^= 1 << lower[f ^ bit]
                t -= bit
            while mask:
                h = mask.bit_length()-1
                if h not in pivots:
                    pivots[h] = mask
                    break
                mask ^= pivots[h]
        rank[j] = len(pivots)
    betti={}
    for j,v in dims.items():
        z=v-rank.get(j,0)-rank.get(j+1,0)
        if j == 1: z -= 1  # reduced homology of connected complexes
        if z: betti[j-1] = z
    return betti


def check():
    sample = {}
    total_faces = 0
    total_group_actions = 0
    for n in range(2, 13):
        a,b,c,perfect,faces=dataset(n)
        assert len(perfect)>0
        total_faces += len(faces)
        obs=[]
        for g in range(4):
            p=maps(n,a,b,c, row=bool(g&1), end=bool(g&2))
            assert sorted(p.values()) == list(range(3*n-2))
            L,num=sign_trace(faces,p)
            if n%2 == 0:
                m=n//2; d=m-1
                expected=(-1)**d * (1 if not(g&2) else (-1)**comb(m,2))
            else:
                expected=0
            assert L==expected, (n,g,L,expected)
            obs.append((L,num))
            total_group_actions += 1
        if n<=8:
            betti=gf2_betti(faces)
            expected_betti={} if n%2 else {(n-2)//2:1}
            assert betti==expected_betti, (n,betti,expected_betti)
        sample[n]={'perfect_matchings':len(perfect),'faces':len(faces),
                   'reduced_lefschetz':[x[0] for x in obs]}
    assert sample[12]['reduced_lefschetz'] == [-1,-1,1,1]
    print('PARAMETERS 2..12 inclusive; checked '+str(total_faces)+' distinct faces across cases')
    print('CHECKED '+str(total_group_actions)+' direct signed simplicial traces')
    print('CHECKED mod-two reduced boundary ranks for 2..8 inclusive')
    for n in [2,4,6,8,10,12]:
        print('n=%d: %s' % (n,sample[n]))
    print('VERIFY_OK')


if __name__=='__main__':
    check()
