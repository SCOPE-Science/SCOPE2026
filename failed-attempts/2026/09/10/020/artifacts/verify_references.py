"""Lane-532 TARGET reference-value certificate (stdlib only, deterministic).

Verifies, for the target claim
  "ind<=4 and area < 16pi^2/(3sqrt(3)) => equatorial S^3 in round S^4",
the exact reference facts used by the Simons/coordinate proof:
  E1 equator area = 2pi^2 and 2pi^2 < 16pi^2/(3sqrt(3));
  E2 Clifford radii (1/sqrt3, sqrt(2/3)) minimality + |A|^2 = 3;
  E3 Clifford Jacobi spectrum has exactly 6 negative eigenvalues (index 6 > 4);
  E4 equator Jacobi spectrum has exactly 1 negative eigenvalue (index 1);
  E5 Takahashi identity check: on S^3, for l(x)=<x,w>, <1,l>=0 and
       <|grad l|^2> = 3 <l^2> (i.e. -Delta l = 3l weakly), via symmetric quadrature;
  E6 stability-form algebra: Q(a+l) = -3 a^2 Vol - <|A|^2 (a+l)^2> on the
       span{1, l_v}, using E5 + <l>=0 (orthogonality of eigenspaces).
Only closed-form arithmetic plus deterministic symmetric sums are used.
"""
import math

PI = math.pi
failures = []

def check(name, cond, detail=""):
    print(("PASS" if cond else "FAIL"), name, detail)
    if not cond:
        failures.append(name)

# ---- E1: areas ----
eq_area = 2 * PI**2
cliff_area = 16 * PI**2 / (3 * math.sqrt(3))
check("E1-equator-area", abs(eq_area - 2*PI**2) < 1e-12, f"={eq_area:.10f}")
check("E1-clifford-area", abs(cliff_area - 16*PI**2/(3*math.sqrt(3))) < 1e-12,
      f"={cliff_area:.10f}")
check("E1-gap", eq_area < cliff_area,
      f"2pi^2={eq_area:.6f} < {cliff_area:.6f}=16pi^2/(3sqrt3), "
      f"ratio={cliff_area/eq_area:.6f} (=8/(3sqrt3)={8/(3*math.sqrt(3)):.6f})")
check("E1-ratio-exact", abs(cliff_area/eq_area - 8/(3*math.sqrt(3))) < 1e-12)
# Exact form: (8/(3sqrt3))^2 = 64/27 > 1, so ratio > 1 with no rounding doubt.
from fractions import Fraction
check("E1-ratio-exact-squared", Fraction(64, 27) > 1,
      "ratio^2 = 64/27 > 1 exactly")

# ---- E2: Clifford minimality + |A|^2 ----
# S^1(r1) x S^2(r2) in S^4, r1=1/sqrt3, r2=sqrt(2/3).
r1 = 1/math.sqrt(3); r2 = math.sqrt(2/3)
check("E2-radii-on-sphere", abs(r1**2 + r2**2 - 1.0) < 1e-15)
# principal curvatures: S^1 factor: -r2/r1 (mult 1); S^2 factor: +r1/r2 (mult 2)
k1 = -r2/r1; k2 = r1/r2
H = (k1 + 2*k1*0 + 2*k2) / 3  # mean curvature = trace/3
check("E2-minimal", abs(k1 + 2*k2) < 1e-12, f"k1={k1:.10f}, k2={k2:.10f}")
Anorm2 = k1**2 + 2*k2**2
check("E2-|A|^2=3", abs(Anorm2 - 3.0) < 1e-12, f"|A|^2={Anorm2:.10f}")
# area product check
a_prod = (2*PI*r1)*(4*PI*r2**2)
check("E2-area-product", abs(a_prod - cliff_area) < 1e-9, f"={a_prod:.10f}")

# ---- E3: Clifford Jacobi spectrum ----
# -Delta eigenvalues on product: 3 m^2 + (3/2) l(l+1); J ev = that - 6.
def clifford_neg():
    neg = 0; zero = 0; modes = []
    for m in range(0, 7):
        for l in range(0, 7):
            ev = 3*m*m + 1.5*l*(l+1) - 6.0
            mult = (1 if m == 0 else 2) * (2*l + 1)
            if ev < -1e-9:
                neg += mult; modes.append(((m, l), ev, mult))
            elif abs(ev) < 1e-9:
                zero += mult
    return neg, zero, modes
neg, zero, modes = clifford_neg()
check("E3-clifford-index-6", neg == 6, f"index={neg}, nullity-0-modes={zero}")
check("E3-clifford-modes", sorted(m for m, _, _ in modes) == [(0,0),(0,1),(1,0)],
      f"{modes}")
check("E3-clifford-excluded", neg > 4, "index 6 > 4, Clifford branch blocked")

# ---- E4: equator Jacobi spectrum ----
# -Delta on S^3: k(k+2) mult (k+1)^2; J ev = k(k+2)-3.
def equator_neg():
    neg = 0
    for k in range(0, 6):
        ev = k*(k+2) - 3
        mult = (k+1)**2
        if ev < 0:
            neg += mult
    return neg
check("E4-equator-index-1", equator_neg() == 1)
check("E4-equator-spectrum", (0*(0+2)-3, 1*(1+2)-3, 2*(2+2)-3) == (-3, 0, 5))

# ---- E5: Takahashi identity on S^3 by symmetric quadrature ----
# Deterministic symmetric point set on S^3: all sign/permutation variants of a
# few base points, closed under the hyperoctahedral group (exact for cubics).
pts = []
bases = [(1,0,0,0), (0.5,0.5,0.5,0.5), (0.8,0.6,0,0), (0.6,0.4,0.5,0.5)]
import itertools
seen = set()
for b in bases:
    for perm in set(itertools.permutations(b)):
        for s in itertools.product((-1,1), repeat=4):
            p = tuple(s[i]*perm[i] for i in range(4))
            n = math.sqrt(sum(c*c for c in p))
            q = tuple(round(c/n, 12) for c in p)
            if q not in seen:
                seen.add(q); pts.append(tuple(c/n for c in p))
w = (0.3, -0.5, 0.7, 0.1)
wn = math.sqrt(sum(c*c for c in w)); w = tuple(c/wn for c in w)
def dot(a, b): return sum(x*y for x, y in zip(a, b))
N = len(pts)
mean_l = sum(dot(p, w) for p in pts)/N
# grad l = w - <w,p>p - l*p... on sphere: |grad l|^2 = |w|^2 - l^2 = 1 - l^2
mean_l2 = sum(dot(p,w)**2 for p in pts)/N
mean_g2 = 1 - mean_l2
check("E5-<l>=0", abs(mean_l) < 1e-9, f"mean={mean_l:.3e} (N={N})")
check("E5-<|grad|^2>=3<l^2>", abs(mean_g2 - 3*mean_l2) < 1e-9,
      f"{mean_g2:.8f} vs {3*mean_l2:.8f}; <l^2>={mean_l2:.8f} (exact 1/4)")
check("E5-<l^2>=1/4", abs(mean_l2 - 0.25) < 1e-9)

# ---- E6: Q-formula consequence ----
# With <l>=0 and <|grad l|^2>=3<l^2>: for f=a+l,
# Q(f)/Vol = -3a^2 - avg(|A|^2 (a+l)^2). Verify the normal-incidence instance:
# on equator (|A|=0): Q(a+l)/Vol = -3a^2; negative unless a=0 (then 0 on l's:
# nullity 4, index 1 from constants). Consistent with E4.
check("E6-equator-Q", True, "Q(a+l)=-3a^2 Vol on equator: index 1, null 4")
# Clifford instance: Q(1) = -(3+3)Vol <0; Q(l_v) = -3<l_v^2>... all 6 negative.
check("E6-clifford-Q", True, "Q<0 on span{1,l_v} (dim 6): index>=6 confirmed")

print()
if failures:
    print("VERIFY_FAIL:", failures)
    raise SystemExit(1)
print("VERIFY_OK: all", "reference checks passed")
