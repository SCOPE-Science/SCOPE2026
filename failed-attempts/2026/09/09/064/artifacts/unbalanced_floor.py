"""Unbalanced floor at chi=1, g<=2 (§L): extends §C beyond balanced types.

HYPOTHESIZED Euler form (flagged): chi = g-(k1+k2+k3)+3p+2b-1, with per-sector
Ai = g+p+b-1-ki satisfying 0<=Ai<=g-p (Takahashi Remark 4.3 direction).
Under this form, enumeration at g=0,1,2 gives:
  g=0: unique (p,b,k)=(0,1,(0,0,0)) -> disk page -> S^3, excluded (§B).
  g=1: p=0; b=1: perms of (1,0,0) [3]; b=2: (1,1,1) [1] -> disk/lens pages
       -> S^3 (H1, h1_check.py), all excluded.
  g=2: p=0; b=1: 6 types (disk -> S^3, excluded); b=2: 3 types (lens -> S^3,
       excluded); b=3: unique (2,2,2) (pair-of-pants -> Seifert or L#L';
       L#L' homology sphere -> S^3, excluded) -> survives iff Seifert.
Hence UNCONDITIONAL g>=2 and g=2-iff-Seifert hold for unbalanced types too,
CONDITIONAL on the hypothesized Euler form. The balanced case (§C/floor_g2.py)
needs no hypothesis; Theorem D needs neither.
"""
import json
from itertools import product

def enum_unbalanced(g, chi=1, Plo=0, Phi=4, Blo=1, Bhi=8, Klo=0, Khi=8):
    sols = []
    for p in range(Plo, Phi):
        for b in range(Blo, Bhi):
            for ks in product(range(Klo, Khi), repeat=3):
                if chi != g - sum(ks) + 3 * p + 2 * b - 1:
                    continue
                As = [g + p + b - 1 - k for k in ks]
                if not all(0 <= A <= g - p for A in As):
                    continue
                if not (0 <= p <= g):
                    continue
                sols.append({"p": p, "b": b, "k": list(ks)})
    return sols

res = {}
for g in [0, 1, 2]:
    res[g] = enum_unbalanced(g)
# widen box and confirm stability (no stragglers)
res_wide = {}
for g in [0, 1, 2]:
    res_wide[g] = enum_unbalanced(g, Phi=6, Bhi=12, Khi=12)
stable = all(sorted(map(str, res[g])) == sorted(map(str, res_wide[g])) for g in res)

# classify by page
def page(b, p):
    return {(1, 0): "disk->S^3", (2, 0): "annulus->lens"}.get((b, p), "pants-or-higher")

summary = {}
for g in [0, 1, 2]:
    by_b = {}
    for s in res[g]:
        by_b.setdefault(s["b"], []).append(tuple(s["k"]))
    summary[g] = {b: sorted(set(v)) for b, v in by_b.items()}

expected = {
    0: {1: [(0, 0, 0)]},
    1: {1: [(0, 0, 1), (0, 1, 0), (1, 0, 0)], 2: [(1, 1, 1)]},
    2: {1: [(0, 0, 2), (0, 1, 1), (0, 2, 0), (1, 0, 1), (1, 1, 0), (2, 0, 0)],
        2: [(1, 1, 2), (1, 2, 1), (2, 1, 1)], 3: [(2, 2, 2)]},
}
match = all(summary[g] == expected[g] for g in expected)
out = {"unbalanced_g012": summary, "box_stable": stable, "matches_hand_derivation": match,
       "conclusion": "g>=2 unconditional; g=2 possible iff Seifert (b=3 type (2,2,2)); "
                     "CONDITIONAL on hypothesized unbalanced Euler form",
       "UNBALANCED_FLOOR_OK": stable and match}
print(json.dumps(out, indent=2))
assert stable and match
