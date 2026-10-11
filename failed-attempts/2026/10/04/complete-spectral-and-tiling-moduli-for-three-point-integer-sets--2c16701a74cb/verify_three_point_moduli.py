#!/usr/bin/env python3
import itertools, math, cmath

def mask_zero(u, v, g, j):
    N = 3*g
    z = cmath.exp(2j*math.pi*j/N)
    val = 1 + z**(g*u) + z**(g*v)
    return abs(val) < 1e-8

def predicted_spectra(g):
    return {tuple(sorted((0, 3*r+1, 3*s+2))) for r in range(g) for s in range(g)}

def actual_spectra(u, v, g):
    N = 3*g
    zeros = [j for j in range(1,N) if mask_zero(u,v,g,j)]
    out = set()
    for a,b in itertools.combinations(zeros,2):
        if mask_zero(u,v,g,(a-b)%N):
            out.add(tuple(sorted((0,a,b))))
    return out

def tiling_complements(g):
    N=3*g
    A={0,g,2*g}
    out=set()
    for T in itertools.combinations(range(N),g):
        sums=[(a+t)%N for a in A for t in T]
        if len(set(sums))==N:
            out.add(tuple(T))
    return out

def predicted_complements(g):
    out=set()
    for phases in itertools.product(range(3), repeat=g):
        out.add(tuple(sorted(r+g*phases[r] for r in range(g))))
    return out

checked_pairs=0
for g in range(1,7):
    pred=predicted_spectra(g)
    assert len(pred)==g*g
    for u in range(-8,9):
        for v in range(-8,9):
            if len({0,u,v})<3 or math.gcd(abs(u),abs(v))!=1:
                continue
            if {u%3,v%3}!={1,2}:
                continue
            got=actual_spectra(u,v,g)
            assert got==pred, (g,u,v,len(got),len(pred))
            checked_pairs += 1
    gotT=tiling_complements(g)
    predT=predicted_complements(g)
    assert gotT==predT, (g,len(gotT),len(predT))
    assert len(gotT)==3**g
print(f"VERIFY_OK spectral_instances={checked_pairs} tiling_g_values=6")
