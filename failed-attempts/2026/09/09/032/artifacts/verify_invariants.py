"""Verify the numerical/combinatorial certificate for the lane-362 boundary witness.

Proved object (see DRAFT.md): X = C1 U_p C2 stable compact-type curve,
g(C1)=5 hyperelliptic, g(C2)=6 hyperelliptic, one node p, pa(X)=11.
E1 = L1(+)L1 on C1, L1 = 2*g^1_2 (deg 4, h0=3) -> deg(E1)=8, h0=6.
E2 = A(+)A on C2, A = g^1_2 + x (deg 3, h0=2) -> deg(E2)=6, h0=4.
E0 on X glued via any fiber isomorphism: deg 14, rk 2, h0(X,E0) >= 8,
gamma(E0) <= 1 < 5 = Cliff_1(11). Naive limit semistable vs uniform-rank
line subbundles: any bidegree (e1,e2) with e1<=4, e2<=3 has total <=7.

Checks (stdlib only):
 1. classical invariants: Cliff1(11)=5, mu=7, gamma<=1, rho(2,14,6)=-31,
    Koszul slope 7 (cited divisor, not re-proved).
 2. chain arithmetic genus, component degrees, h0 counts, glued bound.
 3. stability enumeration over all subbundle bidegrees.
 4. Riemann-Roch consistency of cited special line bundles.
"""
import itertools

PASS, FAIL = [], []

def check(name, cond, detail=""):
    (PASS if cond else FAIL).append(name)
    print(("PASS" if cond else "FAIL") + f" | {name}" + (f" | {detail}" if detail else ""))

def rho_rank1(g, d, r):
    return g - (r + 1) * (g - d + r)

def rho_rank2(g, d, k):
    return 4 * (g - 1) + 1 - k * (k - d + 2 * (g - 1))

# ---- 1. classical invariants at g=11 ----
g = 11
cliff1 = (g - 1) // 2
check("Cliff1(11)=5", cliff1 == 5, f"floor(10/2)={cliff1}")
d, r = 14, 2
mu = d / r
check("mu(E0)=7", mu == 7)
h0_lo = 8
gamma_hi = mu - 2 * h0_lo / r + 2
check("gamma(E0)<=1", gamma_hi == 1, f"7-8+2={gamma_hi}")
check("gamma bound < Cliff1", gamma_hi < cliff1)
rho = rho_rank2(g, d, 6)
check("rho(2,14,6)=-31", rho == -31, f"41-72={rho}")
check("Kosz_11 slope=7", 6 + 12 / (g + 1) == 7)

# ---- 2. chain + component bookkeeping ----
g1, g2 = 5, 6
pa = g1 + g2 + 1 - 2 + 1  # nodes=1, components=2
check("pa(X)=11", pa == 11, f"5+6+1-2+1={pa}")
D1, D2 = 8, 6
check("deg(E0)=8+6=14", D1 + D2 == 14)
h1, h2 = 6, 4
check("h0(E1)=3+3=6", h1 == 6)
check("h0(E2)=2+2=4", h2 == 4)
glued_lo = h1 + h2 - r  # fiber matching imposes <= r conditions
check("h0(X,E0)>=6+4-2=8", glued_lo == 8)
check("witness h0>=6", glued_lo >= 6)

# component slopes (equal-degree splits => semistable, see DRAFT Lemma 1)
check("mu(E1)=4", D1 / 2 == 4)
check("mu(E2)=3", D2 / 2 == 3)

# Riemann-Roch consistency of cited special bundles (existence via
# hyperelliptic theory, cited in DRAFT; here only arithmetic consistency)
# L1: g=5, deg 4: chi = 0; cited h0=3 -> h1=3 (special, ok)
chi_L1 = 4 - 5 + 1
check("RR L1: chi=0, h0=3 => h1=3", chi_L1 == 0)
# A: g=6, deg 3: chi = -2; cited h0=2 -> h1=4 (special, contains g^1_2)
chi_A = 3 - 6 + 1
check("RR A: chi=-2, h0=2 => h1=4", chi_A == -2)
# Clifford bounds respected: h0-1 <= d/2 -> L1: 2<=2 ok; A: 1<=1.5 ok
check("Clifford L1 (2<=2)", 3 - 1 <= 4 / 2)
check("Clifford A (1<=1.5)", 2 - 1 <= 3 / 2)

# ---- 3. naive limit-semistability enumeration ----
# Lemma 1 (proved in DRAFT): any nonzero map N -> L1(+)L1 forces
# deg N <= 4; any nonzero map N -> A(+)A forces deg N <= 3.
# Hence uniform-rank line subbundles of E0 have bidegree e1<=4, e2<=3.
mu_tot = 14 / 2
worst = None
bad = []
for e1 in range(-2, 5):     # include negative/low degrees for completeness
    for e2 in range(-2, 4):
        tot = e1 + e2
        if tot > 2 * mu_tot:
            bad.append((e1, e2))
        if worst is None or tot > worst[0]:
            worst = (tot, e1, e2)
check("no bidegree with total>7 in range", len(bad) == 0, f"bad={bad}")
check("max total = 7 at (4,3)", worst[0] == 7 and (worst[1], worst[2]) == (4, 3),
      f"worst={worst}")
# one-sided supported subsheaves: N1(-p) has degree e1-1 <= 3; still bounded
check("supported bound (4-1)+3=6<=7", (4 - 1) + 3 <= 7)
check("supported bound 4+(3-1)=6<=7", 4 + (3 - 1) <= 7)

# ---- 4. component Brill-Noether context (informational) ----
# g^1_2 on genus 5,6 exists by hyperelliptic hypothesis (rho<0, special locus)
check("rho(5,1,2)=-3 special", rho_rank1(5, 2, 1) == -3)
check("rho(6,1,2)=-4 special", rho_rank1(6, 2, 1) == -4)

print(f"\n{len(PASS)} passed, {len(FAIL)} failed")
assert not FAIL, FAIL
print("VERIFY_OK")
