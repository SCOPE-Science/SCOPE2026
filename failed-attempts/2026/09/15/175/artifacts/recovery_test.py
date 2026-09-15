"""Bounded recovery test: original vs corrected wall-dynamics multiplicities.

Models the phenomenon in LW Remark 4.3 / Jensen Remark 3.2:
- Original billiards: two directed paths back to same point cause doubling
  each 4-iteration cycle -> multiplicity 2^i after 4i cycles (exponential).
- Jensen geometric merge rule: superposed seeds kept once with halved
  coefficient -> multiplicity stays 1.

Also records the concrete merge-corner labels from Jensen Sec 4.2 and the
verification bound 2p(p+1) from Conjecture 3.1 (the target claim).
"""
from collections import Counter

def original_multiplicity(cycles):
    # each 4-iteration block doubles (two paths mu -> mu), Fig.6 LW18
    return 2 ** cycles

def corrected_multiplicity(cycles):
    # merge rule: superposition reduced to multiplicity one each block
    return 1

print("cycles(4i iters) | original mult | corrected mult")
for c in range(0, 7):
    print(f"{c:>17} | {original_multiplicity(c):>13} | {corrected_multiplicity(c):>14}")

# Concrete merge data points cited in the target (Jensen Sec 4.2)
merges = {
    5: [("II", "88(v8)"), ("III", "87(v7)"), ("corner", "5w1+5w2")],
    7: [("II", "104(v6)"), ("III", "103(v5)"), ("corner", "5? -> lw1+lw2"),
        ("II", "118(v6)"), ("III", "117(v5)"), ("corner2", "2lw1+lw2")],
    11: [("II", "160(v6)"), ("III", "159(v5)"),
         ("II", "182(v6)"), ("III", "181(v5)")],
}
print("\nMerge-rule data points (Jensen 4.2, cf. target):")
for p, v in merges.items():
    print(f"  p={p}: {v}  bound 2p(p+1)={2*p*(p+1)}")

# Minimal multiset simulation of one merging corner:
# two giant leaps towards lambda each contribute label L with coeff c;
# original keeps sum with multiplicity 2, corrected keeps half-sum once.
def merge_corner(leaps):
    # leaps: list of (label, coeff) contributed by each giant leap
    total = Counter()
    for lab, c in leaps:
        total[lab] += c
    original = dict(total)  # superposition kept (mult 2 possible)
    corrected = {lab: c // 2 if c % 2 == 0 else c / 2 for lab, c in total.items()}
    # merge rule keeps only superposed seeds, multiplicity one:
    # here both leaps target same label -> single kept entry
    return original, corrected

orig, corr = merge_corner([("88(v8)", 1), ("88(v8)", 1)])
print("\nType-II toy merge (two leaps -> 88(v8)):")
print("  original (superposed, mult 2):", orig)
print("  corrected (kept once, halved):", corr)

orig3, corr3 = merge_corner([("87(v7)", 1), ("87(v7)", 1), ("87(v7)", 1)])
# type III: three leaps -> three points each with half the superposed coeff;
# toy shows the halving; full geometry gives 3 distinct wall points.
print("Type-III toy merge (three leaps -> 87(v7) family):")
print("  original:", orig3, " corrected halved coeff:", corr3)

print("\nConclusion: combinatorics of over-prediction vs merge cancellation is")
print("reproducible locally, but equality p-zeta_i = ^p n_{x_i} / ^p n^2_{x_i}")
print("requires Soergel intersection-form computation (MAGMA ASLoc, unavailable).")
