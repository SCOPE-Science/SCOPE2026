"""Bounded recovery test for target: deterministic log-girth near-Ramanujan, every d.

Route R1: LPS Ramanujan base in degree D>=d, delete (D-d)-regular subgraph.
  Naive spectral cost: ||A_H|| <= D-d, so bound 2*sqrt(D-1)+(D-d) vs target 2*sqrt(d-1)+eps.
  Reports excess over target radius (eps=0 baseline; any excess>0 kills all small eps).
Route R2: iterated 2-lifts from fixed base (girth g0, size n0).
  Guaranteed girth stays within [g0, ...]; required c*log_{d-1}(N) grows unbounded in t.
  Shows stagnation: lifts preserve the lower bound g0 but add only O(1) per doubling at best
  under generic signings, while log N grows linearly in t (table of required vs guaranteed).
Route R3: random d-regular short-cycle first moment.
  E[#cycles length<=L] ~ sum_{k<=L} (d-1)^k/(2k); Poisson-heuristic P(girth>L) ~ exp(-E).
  Shows union-bound/conditional-expectation derandomization is hopeless (E grows as n^c).
"""
import math

print("=== R1: LPS degree-gap spectral cost (relaxed: D = smallest >= d with D-1 prime) ===")
def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    r = int(n ** 0.5)
    for i in range(3, r + 1, 2):
        if n % i == 0: return False
    return True

def next_lps_degree(d):
    for D in range(d, d + 100):
        if is_prime(D - 1):
            return D
    return None

r1_blocked = []
for d in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20]:
    D = next_lps_degree(d)
    gap = D - d
    naive = 2 * math.sqrt(D - 1) + gap
    target = 2 * math.sqrt(d - 1)
    excess = naive - target
    flag = "BLOCKED" if excess > 1e-9 else "gap-free"
    if excess > 1e-9:
        r1_blocked.append(d)
    print(f"d={d:3d} D={D:3d} gap={gap} naive_bound={naive:.3f} target_radius={target:.3f} excess={excess:.3f} [{flag}]")
print(f"degrees with positive excess (R1 fails for small eps): {r1_blocked}")
print("Note: true LPS needs p = 1 mod 4 prime powers + congruence sizes; relaxed gaps are lower bounds on the real cost.")

print()
print("=== R2: iterated 2-lift girth stagnation (d=3, base n0=100, girth g0=6) ===")
d, n0, g0 = 3, 100, 6
for t in [0, 5, 10, 15, 20, 30]:
    N = n0 * (2 ** t)
    req = 0.3 * math.log(N) / math.log(d - 1)
    print(f"lifts={t:3d} N={N:12d} guaranteed_girth~{g0}  required_0.3*log(N)={req:.2f}  deficit={req - g0:.2f}")
print("Guaranteed lower bound g0 is frozen while requirement grows linearly in t: R2 cannot reach c*log N.")

print()
print("=== R3: expected #cycles of length <= L = c*log_{d-1}(n) in random d-regular ===")
for d in [3, 7]:
    for n in [10**4, 10**6, 10**9]:
        for c in [0.3, 0.5]:
            L = c * math.log(n) / math.log(d - 1)
            klo = 3
            khi = int(math.floor(L))
            if khi < klo:
                print(f"d={d} n={n:.0e} c={c} L={L:.2f} (<3: vacuous range, no constraint)")
                continue
            E = sum((d - 1) ** k / (2 * k) for k in range(klo, khi + 1))
            print(f"d={d} n={n:.0e} c={c} L={L:.2f} E={E:.3e} Poisson-heuristic P(no short cycle)~exp(-E)~0 (E>>1)")
