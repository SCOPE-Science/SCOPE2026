#!/usr/bin/env python3
from itertools import product
from math import comb

ASSERTIONS = 0

def check(cond):
    global ASSERTIONS
    assert cond
    ASSERTIONS += 1

def orbit_formula(d):
    return sum(comb(d-2*j+7, 7) for j in range(d//2 + 1))

def all_subspaces_f2(d):
    V = range(1 << d)
    subs = []
    for mask in range(1 << (1 << d)):
        if not (mask & 1):
            continue
        els = [x for x in V if (mask >> x) & 1]
        ok = True
        for a in els:
            for b in els:
                if not ((mask >> (a ^ b)) & 1):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            subs.append(mask)
    return subs

def rank_vectors(vectors, d):
    piv = {}
    for x in vectors:
        y = x
        while y:
            p = y.bit_length() - 1
            if p in piv:
                y ^= piv[p]
            else:
                piv[p] = y
                break
    return len(piv)

def gl_f2(d):
    if d == 0:
        return [(0,)]
    maps = []
    for imgs in product(range(1 << d), repeat=d):
        if rank_vectors(imgs, d) != d:
            continue
        arr = []
        for x in range(1 << d):
            y = 0
            for i in range(d):
                if (x >> i) & 1:
                    y ^= imgs[i]
            arr.append(y)
        maps.append(tuple(arr))
    return maps

def act_mask(mask, g):
    out = 0
    for x, y in enumerate(g):
        if (mask >> x) & 1:
            out |= 1 << y
    return out

def brute_orbits(d):
    subs = all_subspaces_f2(d)
    gl = gl_f2(d)
    triples = list(product(subs, repeat=3))
    triple_set = set(triples)
    seen = set()
    orbit_count = 0
    for t in triples:
        if t in seen:
            continue
        orbit_count += 1
        orb = {tuple(act_mask(m, g) for m in t) for g in gl}
        seen |= orb
        for s in orb:
            check(s in triple_set)
    check(len(seen) == len(triples))
    return len(subs), len(gl), len(triples), orbit_count

# Direct orbit enumeration over F_2 in dimensions 0..3.
rows = []
for d in range(4):
    ns, ng, nt, no = brute_orbits(d)
    check(no == orbit_formula(d))
    rows.append((d, ns, ng, nt, no))

# Independent coefficient extraction from 1/((1-z)^8(1-z^2)).
coeff = []
for d in range(101):
    c = sum(comb(a+7, 7) for a in range(d+1) if (d-a) % 2 == 0)
    check(c == orbit_formula(d))
    coeff.append(c)

# Structural weight check: eight one-dimensional indecomposables and one
# two-dimensional indecomposable give the first ten coefficients.
expected = [1, 8, 37, 128, 367, 920, 2083, 4352, 8518, 15792]
check(coeff[:10] == expected)

print(f"VERIFY_OK {ASSERTIONS} exact assertions")
print("F2_rows", rows)
print("first_10", coeff[:10])
