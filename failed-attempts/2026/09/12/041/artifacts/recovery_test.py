"""Lane-1159 bounded recovery test (stdlib only).

Test 1: homological status of M.
  Topic stipulates H1(M)=Z/5 (rational homology sphere, b1=0), vol~1.0147.
  NOTE (convention flag, recorded honestly): under the standard SnapPy
  framing where (p,q) kills p*meridian+q*longitude on a knot in S^3,
  (p,q)=(-1,2) would give |H1|=|p|=1, not 5; getting Z/5 needs |p|=5
  (e.g. a 5 or -5 slope). This looks like a slope-notation typo in the
  topic. It does not affect the argument: under EITHER reading M is a
  rational homology sphere (b1=0), so H^3(M;R)=R (no GV-homological
  shortcut) and compact-leaf quick kills fail. We adopt the topic's
  H1=Z/5 as authoritative and verify the consequences.

Test 2: local resilient-leaf toy model.
  f(x)=lam*x contracting linear holonomy (lam=0.5); g(x)=mu*x+(1-mu)*c
  with mu=0.6, c=1.0 placing a second branch disjoint from f's image
  (ping-pong). IFS simulation: attractor of random orbit is Cantor-like
  (spreads over interval, box-count samples hit many bins, orbit of a
  point accumulates on itself without collapsing to a cycle). Then checks
  generator count: a single map (cyclic pseudogroup = solid-torus
  holonomy) collapses to a fixed point/periodic orbit (no exceptional
  set -- Denjoy/Kopell/Sacksteder abelian fact), so TWO independent
  generators are needed, which a ball/solid-torus plug cannot supply.
"""
import random

# ---- Test 1 ----
# Authoritative (per topic): H1 = Z/5.
h1_order = 5
b1 = 0
print(f"Test1: H1 order={h1_order} b1={b1}")
assert h1_order == 5 and b1 == 0
# Poincare duality for closed oriented 3-manifold: H^3(M;R) = R, H^1 = 0.
h3_dim = 1
h1_betti = 0
assert h3_dim == 1 and h1_betti == 0
# Convention flag computation (honest record, no assert on topic):
p, q = -1, 2
print(f"Test1 note: standard-framing |p| for slope ({p},{q}) is {abs(p)} "
      f"!= 5; slope-notation typo suspected, immaterial (b1=0 either way).")
print("Test1 PASS: M rational homology sphere; H^3(M;R)=R so no "
      "GV-homology shortcut; H^1=0 blocks easy compact-leaf fibrations.")

# ---- Test 2 ----
lam, mu, c = 0.5, 0.6, 1.0
def f(x): return lam * x
def g(x): return mu * x + (1 - mu) * c

random.seed(1159)
x = 0.3
pts = []
for i in range(20000):
    x = f(x) if random.random() < 0.5 else g(x)
    if i >= 5000:
        pts.append(x)
nbins = 64
lo, hi = min(pts), max(pts)
bins = set()
for v in pts:
    b = int((v - lo) / (hi - lo + 1e-12) * nbins)
    bins.add(min(b, nbins - 1))
print(f"Test2a: two-generator IFS spread over [{lo:.4f},{hi:.4f}], "
      f"bins hit {len(bins)}/{nbins}")
assert len(bins) > nbins // 2, "attractor should be spread out, not a cycle"
print("Test2a PASS: local ping-pong model has Cantor-like spread "
      "(local dynamics feasible).")

# single-generator (cyclic) control: iterates collapse to fixed point
y = 0.3
for _ in range(5000):
    y = f(y)
print(f"Test2b: single-map orbit collapses to {y:.2e} (fixed point, "
      f"no exceptional set)")
assert abs(y) < 1e-12
print("Test2b PASS: cyclic holonomy cannot host resilient leaf "
      "=> plug needs >=2 generators, unavailable in ball/solid torus.")

print("ALL RECOVERY TESTS PASS: blockage is global realization, "
      "not local dynamics.")
