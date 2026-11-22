#!/usr/bin/env python3
"""Independent finite checks of the dihedral character formulas for cycle-power cut complexes.

Requires only Python 3; test evidence is finite and does not replace the general proof.
"""
from itertools import combinations
from math import comb


def character(n, p, kind, a):
    assert p >= 2 and n >= 6*p-3
    if kind == 'r':
        if a % n == 0:
            return comb(n-2*p, 2) - (2*p*p+p-1)
        if n % 2 == 0 and a % n == n//2:
            return (-1)**(n//2)*(1-n//2)
        return (-1)**(a*(n-1))
    assert kind == 's'
    a %= n
    if n % 2:
        return (-1)**((n-1)//2) * ((4*p-n-1)//2)
    if a % 2 == 0:
        return (-1)**((n-2)//2) * (2*p+1-n//2)
    return (-1)**(n//2) * (2*p-1-n//2)


def is_gamma_face(indices, n, p):
    # All triples must induce a connected graph. Equivalent to nonedge
    # graph maximum degree at most one; check pairwise nonadjacencies.
    for x in indices:
        count = 0
        for y in indices:
            if x == y:
                continue
            d = abs(x-y)
            if min(d, n-d) > p:
                count += 1
                if count >= 2:
                    return False
    return True


def fixed_gamma_lefschetz(n, p, kind, a):
    # Signed augmented face trace on the Alexander dual. Enumerate only
    # unions of permutation orbits, with independent degree constraints.
    if kind == 'r':
        g = [(i+a) % n for i in range(n)]
    else:
        g = [(a-i) % n for i in range(n)]
    seen, orbits = set(), []
    for i in range(n):
        if i in seen:
            continue
        orbit, j = [], i
        while j not in seen:
            seen.add(j)
            orbit.append(j)
            j = g[j]
        orbits.append(orbit)
    if len(orbits) == n:
        raise ValueError('Identity action: use the published sphere rank')
    total = 0
    def recurse(k, selected, degrees, orientation):
        nonlocal total
        if k == len(orbits):
            total += (-1)**len(selected) * orientation
            return
        recurse(k+1, selected, degrees, orientation)
        orbit = orbits[k]
        new_degrees = [0]*len(orbit)
        changed = degrees[:]
        for i, x in enumerate(orbit):
            for j, y in enumerate(selected):
                d = abs(x-y)
                if min(d, n-d) > p:
                    changed[j] += 1
                    new_degrees[i] += 1
            for j in range(i):
                d = abs(x-orbit[j])
                if min(d, n-d) > p:
                    new_degrees[i] += 1
                    new_degrees[j] += 1
        if max(changed+new_degrees, default=0) <= 1:
            recurse(k+1, selected+orbit, changed+new_degrees,
                    orientation * (-1)**(len(orbit)-1))
    recurse(0, [], [], 1)
    # Sign of permutation on full vertex set = product of cycle signs.
    ambient = (-1)**(n-len(orbits))
    return ambient * total


def direct_cut_face_trace(n, p, kind, a):
    # Completely separate check of the cut complex using complements of
    # disconnected triples and all their faces, without Alexander duality.
    limit = 1 << n
    face = bytearray(limit)
    full = limit-1
    for x,y,z in combinations(range(n),3):
        edges = sum(min(abs(u-v),n-abs(u-v))<=p
                    for u,v in ((x,y),(x,z),(y,z)))
        if edges <= 1:
            face[full ^ ((1<<x)|(1<<y)|(1<<z))] = 1
    # Downward closure of facets.
    for i in range(n):
        bit = 1 << i
        for mask in range(limit):
            if not (mask & bit) and face[mask|bit]:
                face[mask] = 1
    if kind == 'r':
        g = [(i+a)%n for i in range(n)]
    else:
        g = [(a-i)%n for i in range(n)]
    lefschetz = -1  # Reduced augmentation term.
    for mask in range(1, limit):
        if not face[mask]:
            continue
        S = [i for i in range(n) if mask & (1<<i)]
        images = [g[i] for i in S]
        if sum(1<<j for j in images) != mask:
            continue
        parity = sum(images[i]>images[j] for i in range(len(S))
                     for j in range(i+1,len(S))) % 2
        lefschetz += (-1)**(len(S)-1+parity)
    return (-1)**(n-4)*lefschetz


def invariant_rank(n,p):
    if n%2:
        if n%4==1:
            return 0
        return (n-4*p+1)//2
    return (n-4*p-1-3*((-1)**(n//2)))//4


def run():
    count_orbit = 0
    count_direct = 0
    checked_params = 0
    for p in range(2,7):
        for n in range(6*p-3, 6*p+3):
            checked_params += 1
            group_total = sum(character(n,p,'r',a) for a in range(n))
            group_total += sum(character(n,p,'s',a) for a in range(n))
            assert group_total % (2*n) == 0
            assert group_total//(2*n) == invariant_rank(n,p)
            for a in range(1,n):
                if a in (1,2,n//2,n-1):
                    got = fixed_gamma_lefschetz(n,p,'r',a)
                    assert got == character(n,p,'r',a),(n,p,'r',a,got)
                    count_orbit += 1
            for a in ([0] if n%2 else [0,1]):
                got = fixed_gamma_lefschetz(n,p,'s',a)
                assert got == character(n,p,'s',a),(n,p,'s',a,got)
                count_orbit += 1
    # Direct cut-complex checks from distinct definitions, not from the dual.
    for p,n in [(2,9),(2,10),(2,11),(3,15),(3,16)]:
        for kind in ('r','s'):
            for a in range(n):
                got = direct_cut_face_trace(n,p,kind,a)
                expected = character(n,p,kind,a)
                assert got == expected,(n,p,kind,a,got,expected)
                count_direct += 1
    print('PARAMETER_CASES',checked_params)
    print('DUAL_ORBIT_CHARACTER_CHECKS',count_orbit)
    print('DIRECT_CUT_CHARACTER_CHECKS',count_direct)
    print('BURNSIDE_INVARIANT_CHECKS',checked_params)
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
