"""Fallback check (numpy only): zero-extension norm on (S3,M3).

Claim under test: every linear E:Lip0(S3)->Lip0(M3) with RE=Id has ||E||>=2.
Counterexample: (E0 f)(x) = f(x) on S3, 0 on the 6 interior nodes.
Proves ||E0|| = sqrt(3) < 2, i.e. E_3 <= sqrt(3), refuting the threshold-2 claim.

Repro: python3 output/artifacts/fallback_check.py  (numpy only)
"""
import numpy as np
from itertools import combinations

def lca_len(a, b):
    k = 0
    for x, y in zip(a, b):
        if x == y:
            k += 1
        else:
            break
    return k

def gdist(a, b):
    return len(a) + len(b) - 2 * lca_len(a, b)

def nodes(h):
    out = [()]
    for d in range(1, h + 1):
        out += [tuple(int(x) for x in format(i, f"0{d}b")) for i in range(2 ** d)]
    return out

def leaves(h):
    return [n for n in nodes(h) if len(n) == h]

h = 3
M = nodes(h)
S = set([()] + leaves(h))
assert len(M) == 15 and len(S) == 9, (len(M), len(S))
d = {(u, v): gdist(u, v) ** 0.5 for u in M for v in M}

# Minimum distance between distinct vertices of M3 (=1, attained on edges)
mind = min(d[u, v] for u in M for v in M if u != v)
print("min distinct-vertex distance in M3:", mind)
assert mind == 1.0

# Root-leaf distance
rl = d[(), (0, 0, 0)]
print("root-leaf distance:", round(rl, 10), "= sqrt(3) =", round(3 ** 0.5, 10))
assert abs(rl - 3 ** 0.5) < 1e-12

# Extremal radial function: f(r)=0, f(leaf)=sqrt(3). Must be 1-Lipschitz on S3.
f = {s: (0.0 if s == () else 3 ** 0.5) for s in S}
lipS = max(abs(f[u] - f[v]) / d[u, v] for u in S for v in S if u != v)
print("Lip(f_radial on S3) =", round(lipS, 10))
assert abs(lipS - 1.0) < 1e-9

# Zero extension E0 f: same on S3, 0 elsewhere. Exact Lipschitz constant on M3.
g = {x: f[x] if x in S else 0.0 for x in M}
pairs = [(u, v) for u in M for v in M if u != v]
lipM = max(abs(g[u] - g[v]) / d[u, v] for u, v in pairs)
print("Lip(E0 f_radial on M3) =", round(lipM, 10), " vs sqrt(3) =", round(3 ** 0.5, 10))
assert abs(lipM - 3 ** 0.5) < 1e-9

# Universal upper bound (analytic, checked constants above):
# any f with Lip(f)<=1 has |f(leaf)| <= d(r,leaf)*1 = sqrt(3);
# E0f off S3 is 0, so every mixed pair has ratio <= sqrt(3)/1 = sqrt(3);
# pure pairs have ratio <= 1 or 0. Hence ||E0|| <= sqrt(3) < 2.
print("||E0|| = sqrt(3) =", round(3 ** 0.5, 10), "< 2 by margin", round(2 - 3 ** 0.5, 10))
assert 3 ** 0.5 < 2.0
print("FALLBACK REFUTED: exhibited linear extender E0 with RE=Id and norm sqrt(3) < 2")
