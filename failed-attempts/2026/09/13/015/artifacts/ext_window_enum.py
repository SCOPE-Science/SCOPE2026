"""Bounded scope-enumeration for V(0) ANSS window 55<=stem<=70, 0<=s<=6 at p=3.

Not a full Ext computation; enumerates BP monomial degrees and ANSS bidegree
collisions to test whether named generators u(s=2), w(s=5) in stem 62 can be
isolated by degree bookkeeping alone, and how far v1-tower / differential data
escapes the window.
"""
import json, itertools

p = 3
# |vi| = 2(p^i - 1)
vdeg = {i: 2*(3**i - 1) for i in range(1, 6)}
print("BP degrees:", vdeg)

# Bidegrees of interest: stem n = t-s = 62, s=2 -> t=64; s=5 -> t=67
targets = [(2, 64), (5, 67)]
print("targets (s,t):", targets)

# Enumerate monomials v1^a v2^b v3^c v4^d with internal degree near window stems.
# Internal degree |m| contributes to t-s modulo Ext cohomological degree shifts;
# here we just list raw |m| in [50, 80] to show crowding near stem 62.
sols = []
for a in range(0, 21):
    for b in range(0, 6):
        for c in range(0, 3):
            for d in range(0, 2):
                deg = a*vdeg[1] + b*vdeg[2] + c*vdeg[3] + d*vdeg[4]
                if 50 <= deg <= 80:
                    sols.append((deg, a, b, c, d))
sols.sort()
print(f"monomial raws in [50,80]: {len(sols)}")
for s in sols:
    print(s)

# v1-tower escape: stem-62 class times v1^k lands at stem 62+4k
print("\nv1-tower escape from stem 62:")
for k in range(0, 6):
    print(f"  k={k}: stem {62+4*k} {'INSIDE 55-70' if 55 <= 62+4*k <= 70 else 'OUTSIDE window'}")

# Toda candidate x stems per topic formula n-9-k*8 with n=62
print("\nToda x candidate stems (53-8k):")
for k in [1, 2, 3, 4]:
    print(f"  k={k}: stem {53-8*k} OUTSIDE window" if not (55 <= 53-8*k <= 70) else f"  k={k}: stem {53-8*k}")

# Differential crossing: d_r from (s,t) lands at (s+r, t+r-1), stem drops by 1.
# Sources in window can hit s+r>6 (outside ledger); targets in window can come from s-r<0.
print("\nd_r crossing for r in {3,5,7,9} from stem-62 bidegrees:")
for (s, t) in targets:
    for r in [3, 5, 7, 9]:
        print(f"  d_{r}({s},{t}) -> ({s+r},{t+r-1}) stem {t+r-1-(s+r)} s'={s+r} {'OUTSIDE s<=6' if s+r>6 else 'inside'}")

# Collision count: raw monomial degrees hitting exactly 62 +/- small Ext shifts
hits62 = [s for s in sols if s[0] in (62-8, 62-4, 62, 62+4)]
print(f"\nraw monomials within Ext-shift distance of 62: {len(hits62)} (ambiguity, need full Ext ring)")

result = {
    "bp_degrees": vdeg,
    "n_monomials_50_80": len(sols),
    "n_near_62": len(hits62),
    "v1_escape_outside": [62+4*k for k in range(6) if not (55 <= 62+4*k <= 70)],
    "x_stems": [53-8*k for k in [1,2,3,4]],
}
with open("result_enum.json", "w") as f:
    json.dump(result, f, indent=2)
print("\nwrote result_enum.json")
