"""Bounded recovery test: lowest-weight resonance for H_c(S_n), small n.

Convention (standard, e.g. Ginzburg-Guay-Opdam-Rouquier):
  h_c(lam) = (n-1)/2 - c * ct(lam),  ct = sum of contents (j-i) over boxes.
Only differences matter: h(lam)-h(mu) = -c*(ct(lam)-ct(mu)).
Resonance h(lam)-h(mu) in Z is necessary for lam,mu to lie in the same
block of O_c (hence for a possible nontrivial Ext^1).
Also prints K-class indistinguishability note: [E]=[M1]+[M2] for any
extension, so characters cannot separate extension classes.
"""
from itertools import permutations

def partitions(n, max_part=None):
    if n == 0:
        yield []
        return
    if max_part is None:
        max_part = n
    for first in range(min(max_part, n), 0, -1):
        for rest in partitions(n - first, first):
            yield [first] + rest

def content_sum(lam):
    s = 0
    for i, row in enumerate(lam):
        for j in range(row):
            s += (j - i)
    return s

def report(n, c_num, c_den, label):
    print(f"--- n={n}, c={label} ---")
    lams = list(partitions(n))
    cts = {tuple(l): content_sum(l) for l in lams}
    for l in lams:
        print(f"  lam={l} ct={cts[tuple(l)]}")
    print("  pairwise d = ct(lam)-ct(mu), h-diff = -c*d:")
    resonant = []
    for i, l in enumerate(lams):
        for m in lams[i+1:]:
            d = cts[tuple(l)] - cts[tuple(m)]
            # h-diff = -(c_num/c_den)*d ; resonant iff c*d in Z iff (c_num*d) % c_den == 0
            res = "resonant" if (c_num * d) % c_den == 0 else "non-resonant"
            if res == "resonant":
                resonant.append((l, m, d))
            print(f"    {l} vs {m}: d={d} -> {res}")
    print(f"  resonant pairs: {len(resonant)}")
    return resonant

r1 = report(2, 1, 2, "1/2")
r2 = report(3, 1, 3, "1/3")
r3 = report(3, 1, 2, "1/2 (generic-ish check)")

print()
print("Conclusion:")
print(f"  n=2,c=1/2 resonant pairs = {len(r1)} (non-semisimple block exists: easy route fails)")
print(f"  n=3,c=1/3 resonant pairs = {len(r2)} (overlapping eu-spectra: eu-ss is a real constraint)")
print("  Character/support invariants are constant across Ext^1 classes with fixed")
print("  composition factors, hence cannot decide lifting to HC bimodules.")
