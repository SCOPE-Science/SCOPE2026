#!/usr/bin/env python3
"""Cold verifier: checks stored tables + independently recomputes headline
class sums with the walk-based (Method B) rim-hook code.
Usage: python3 output/artifacts/verify.py
"""
import json, math, sys
from collections import Counter

sys.path.insert(0, "output")
from methodB_replay import chiB, classesB, partitions as partitionsB

A = json.load(open("output/artifacts/kronecker_A.json"))
ok = []
def check(name, cond):
    ok.append(cond)
    print(("PASS " if cond else "FAIL ") + name)

for n, P, fact in ((6, 11, 720), (7, 15, 5040), (8, 22, 40320)):
    e = A[str(n)]
    parts = [tuple(p) for p in e["parts"]]
    flat = e["flat"]
    check(f"n={n} table size {P}^3", len(flat) == P**3)
    check(f"n={n} class sizes sum to {fact}",
          sum(sz for _, sz in e["classes"]) == fact)
    # S3 symmetry of stored table
    s3 = all(flat[a*P*P+b*P+c] == flat[x*P*P+y*P+z]
             for a in range(P) for b in range(P) for c in range(P)
             for (x, y, z) in [sorted((a, b, c))[::-1]][:1])  # spot: sorted perm
    # full S3
    import itertools
    s3full = True
    for a in range(P):
        for b in range(P):
            for c in range(P):
                g = flat[a*P*P+b*P+c]
                for x, y, z in itertools.permutations((a, b, c)):
                    if flat[x*P*P+y*P+z] != g:
                        s3full = False
                        break
    check(f"n={n} full S3 symmetry (stored)", s3full)
    check(f"n={n} nonnegativity (stored)", all(g >= 0 for g in flat))

check("S6 nonzero 511/1331", sum(1 for g in A["6"]["flat"] if g > 0) == 511)
check("S7 nonzero 1599/3375", sum(1 for g in A["7"]["flat"] if g > 0) == 1599)
check("S8 nonzero 5048/10648", sum(1 for g in A["8"]["flat"] if g > 0) == 5048)
check("S6 max 5 unique ordered", A["6"]["max"] == 5 and len(A["6"]["argmax"]) == 1)
check("S7 max 9, 4 ordered argmax", A["7"]["max"] == 9 and len(A["7"]["argmax"]) == 4)
check("S8 max 17, unique ordered", A["8"]["max"] == 17 and len(A["8"]["argmax"]) == 1)
check("S6 argmax is (3,2,1)^3",
      [tuple(p) for p in [[3,2,1]]*3] == [tuple(A["6"]["parts"][i]) for i in A["6"]["argmax"][0]])
check("S8 argmax is (4,2,1,1)^3",
      all(tuple(A["8"]["parts"][i]) == (4,2,1,1) for i in A["8"]["argmax"][0]))

# Independent recomputation of the 22 slice class sums via Method B characters
n = 8; fact = 40320
parts = list(partitionsB(n))
idx = {p: i for i, p in enumerate(parts)}
cl = classesB(n)
C = {p: [chiB(p, m) for (m, s) in cl] for p in parts}
def g3(a, b, c):
    s = sum(sz*C[a][k]*C[b][k]*C[c][k] for k, (_, sz) in enumerate(cl))
    assert s % fact == 0
    return s // fact
lam = (4, 2, 1, 1)
order = [(8,), (1,)*8, (7,1), (2,)+(1,)*6, (6,1,1), (4,4), (3,)+(1,)*5,
         (2,2,2,2), (6,2), (2,2)+(1,)*4, (5,3), (5,1,1,1), (4,1,1,1,1),
         (2,2,2,1,1), (3,3,2), (4,2,2), (3,3,1,1), (5,2,1), (3,2,1,1,1),
         (4,3,1), (3,2,2,1), (4,2,1,1)]
claimed = [1,1,2,2,4,4,4,4,5,5,6,6,6,6,8,12,12,13,13,14,14,17]
recomputed = [g3(lam, lam, p) for p in order]
check("B-recomputed slice == claimed list", recomputed == claimed)
P = 22; f8 = A["8"]["flat"]
stored = [f8[idx[lam]*P*P+idx[lam]*P+idx[p]] for p in order]
check("B-recomputed slice == stored table", recomputed == stored)
check("maximizer class sum == 17*40320",
      sum(sz*C[lam][k]**3 for k, (_, sz) in enumerate(cl)) == 17*fact)

# Orthogonality spot check via Method B (full table would be slow; check diagonal+row 0)
import random
random.seed(8)
for i in sorted(random.sample(range(22), 6)):
    for j in sorted(random.sample(range(22), 6)):
        s = sum(sz*C[parts[i]][k]*C[parts[j]][k] for k, (_, sz) in enumerate(cl))
        if s != (fact if i == j else 0):
            check(f"B-orthogonality {parts[i]},{parts[j]}", False)
            break
    else:
        continue
    break
else:
    check("B-orthogonality 6x6 sample", True)

print("ALL PASS" if all(ok) else "SOME FAILURES")
sys.exit(0 if all(ok) else 1)
