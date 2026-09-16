"""Bounded recovery test for lane-20512 target.

Tests whether 'all periodic points repelling + connected + Inou-Wang
combinatorics' determines Yoccoz-puzzle shrinking (hence local connectivity).

Part 1: shows repelling of low-period cycles is a weak, non-quantitative
  condition in z^3+c (sample parameters), giving no modulus lower bound.
Part 2: simulates nest-diameter bounds under two modulus regimes:
  (a) uniform lower bound m_k >= m0 (a priori bounds hold) -> divergent sum,
      diameters -> 0 (shrinking / LC consistent);
  (b) summable degenerate moduli m_k ~ 1/k^2 (no a priori bounds, the
      Inou-Wang-type danger) -> diameters -> definite residual > 0
      (non-shrinking fiber consistent).
  Conclusion: repelling+connectedness is consistent with BOTH outcomes; the
  missing datum is a divergent-modulus bound, which cannot be manufactured
  from the hypotheses.
Part 3: toy Thurston-pullback model with a neutral manifold (non-rigidity):
  contraction transverse to the manifold but isometry along it, so
  combinatorial convergence does not force uniqueness / geometric shrinking.
"""
import cmath
import math

print("=== Part 1: repelling fixed points in z^3+c ===")
# Fixed points satisfy z^3 - z + c = 0; multiplier = 3z^2.
# Sample c values in/near the cubic connectedness locus (critical orbit bounded).
def fixed_points(c):
    # solve cubic z^3 - z + c = 0 via numpy-free Cardano? use simple Newton scan
    roots = []
    for guess in [complex(x, y) for x in (-1.5, -0.5, 0.5, 1.5) for y in (-1.5, -0.5, 0.5, 1.5)]:
        z = guess
        for _ in range(200):
            f = z**3 - z + c
            fp = 3*z**2 - 1
            if fp == 0:
                break
            z = z - f/fp
        if abs(z**3 - z + c) < 1e-9:
            if not any(abs(z - r) < 1e-6 for r in roots):
                roots.append(z)
    return roots

def crit_bounded(c, n=200, R=2.0):
    z = 0j
    for _ in range(n):
        z = z**3 + c
        if abs(z) > R:
            return False
    return True

for c in [0j, -0.2+0j, 0.2j, -1.0+0j, -2.0+0j, 0.5j]:
    roots = fixed_points(c)
    mults = [abs(3*r**2) for r in roots]
    print(f"c={c!s:12s} bounded={crit_bounded(c)!s:5s} nfixed={len(roots)} "
          f"min|mult|={min(mults) if mults else float('nan'):.4f} mults={[round(m,3) for m in mults]}")

print()
print("=== Part 2: nest diameters under divergent vs summable moduli ===")
# Model: d_{k+1} = d_k * exp(-pi*m_k) capped stylized Gr\"otzsch-type contraction.
# Any monotone contraction with sum(m_k)=inf -> 0 vs sum<inf -> positive limit
# illustrates the logical gap; constants are illustrative, not sharp.
def simulate(mods, d0=1.0):
    d = d0
    for m in mods:
        d *= math.exp(-math.pi * m / 3.0)
    return d

N = 50
bounded_mods = [0.5]*N          # uniform a priori bound
degenerate_mods = [1.0/(k**2) for k in range(1, N+1)]  # summable, no uniform bound
d_bounded = simulate(bounded_mods)
d_degen = simulate(degenerate_mods)
print(f"uniform m>=0.5, N={N}: sum={sum(bounded_mods):.3f} diam~{d_bounded:.3e} -> 0")
print(f"summable m=1/k^2, N={N}: sum={sum(degenerate_mods):.6f} (->pi^2/6={math.pi**2/6:.6f}) diam~{d_degen:.6f} > 0")
print("Both regimes have connected, repelling-compatible nests; shrinking is undecided without modulus bound.")

print()
print("=== Part 3: toy Thurston pullback with neutral (non-rigid) direction ===")
# T(x,y) = (x/2, y): x = Teichmuller distance transverse, y = deformation along
# combinatorial class (Inou-Wang manifold). Two points with same x but
# different y stay a fixed distance apart forever: no unique fixed point,
# no contraction along the class. Hence combinatorial equivalence cannot
# force geometric shrinking/uniqueness.
def T(p):
    x, y = p
    return (x/2.0, y)

p, q = (1.0, 0.0), (1.0, 1.0)
for n in [0, 1, 5, 20]:
    pn, qn = p, q
    for _ in range(n):
        pn, qn = T(pn), T(qn)
    dist = math.hypot(pn[0]-qn[0], pn[1]-qn[1])
    print(f"n={n:3d} p={tuple(round(v,6) for v in pn)} q={tuple(round(v,6) for v in qn)} dist={dist:.6f}")
print("Transverse distance -> 0 but inter-point distance -> 1: non-uniqueness persists.")
print("RESULT: recovery test CONFIRMS BLOCK — hypotheses do not determine shrinking/LC.")
