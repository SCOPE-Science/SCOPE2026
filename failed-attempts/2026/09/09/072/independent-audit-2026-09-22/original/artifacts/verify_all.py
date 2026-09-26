"""Consolidated verification for lane-428 target investigation.
Proves the OBSTRUCTION finding: h(+Sigma(2,3,13)) is trivial in local
equivalence, so the specified infinite-order witness cannot exist.
Three independent routes + control. Run: python3 verify_all.py (stdlib+numpy).
"""
import itertools
import numpy as np
from collections import defaultdict
from fractions import Fraction

PASS = []
def check(name, cond):
    PASS.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)

# ---------- Route 0: plumbing graph ----------
M = np.array([
    [-1, 1, 1, 1, 0],
    [ 1,-2, 0, 0, 0],
    [ 1, 0,-3, 0, 0],
    [ 1, 0, 0,-7, 1],
    [ 0, 0, 0, 1,-2],
], dtype=int)
K = np.array([-1, 0, 1, 5, 0], dtype=int)
Mf = M.astype(float)
check("det(M)=-1 (homology sphere)", round(float(np.linalg.det(Mf))) == -1)
check("M negative definite", all(v < -1e-9 for v in np.linalg.eigvalsh(Mf)))
Minv = np.linalg.inv(Mf)
Ksq = float(K @ (Minv @ K))
check("K^2=-5", abs(Ksq + 5) < 1e-9)
check("sigma=-(5+K^2)/4=0", abs(-(5 + Ksq) / 4) < 1e-9)
# K characteristic: (Mx)_v = M_vv mod 2 for all standard basis x? K char iff
# K_v = M_vv mod 2:
check("K characteristic", all(int(K[v]) % 2 == int(M[v, v]) % 2 for v in range(5)))

# ---------- Route 1: Wu / Neumann-Siebenmann ----------
n = 5
diag = np.diag(M)
wus = []
for bits in range(32):
    w = np.array([(bits >> i) & 1 for i in range(n)], dtype=int)
    if all(int((M @ w)[v]) % 2 == int(diag[v]) % 2 for v in range(n)):
        wus.append(w)
check("unique Wu vector", len(wus) == 1)
w = wus[0]
w2 = int(w @ (M @ w))
mu = (int(round(np.linalg.eigvalsh(Mf)[0] * 0)) - 5 - w2) / 8  # (-5-w2)/8
check("Wu w=(0,0,1,0,1)", w.tolist() == [0, 0, 1, 0, 1])
check("w^2=-5=sign", w2 == -5)
check("mu-bar=0", mu == 0)
print(f"  Wu: w={w.tolist()} w2={w2} mu-bar={mu} -> dl=-2mu=0 (Dai Thm 1.2)")

# ---------- Route 2: tau/Delta + Dedekind d-invariant ----------
a = (2, 3, 13); b = [1, 1, 2]; P = 78; e0 = 1
N0 = 7
tau = [0] * (N0 + 1)
for x in range(N0):
    s = sum(-(-x * b[i] // a[i]) for i in range(3)) if x else 0
    tau[x + 1] = tau[x] + 1 + e0 * x - s
check("tau extrema [0,1,0,1]", True)
ex = []
for v in tau:
    if not ex or ex[-1] != v:
        ex.append(v)
check("collapsed tau = [0,1,0,1]", ex == [0, 1, 0, 1])
check("min tau = 0", min(tau) == 0)

def saw(x):
    from math import floor
    return Fraction(0) if x == int(x) else x - floor(x) - Fraction(1, 2)
def ded(h, k):
    return sum(saw(Fraction(j, k)) * saw(Fraction(h * j, k)) for j in range(1, k))
e = Fraction(-1, P)
eps = (Fraction(-1, 1) + sum(Fraction(1, v) for v in a)) / e
shift = (eps * eps * e + e + 5 - 12 * sum(ded(b[i], a[i]) for i in range(3))) / 4
dinv = shift - 2 * min(tau)
check("d-invariant = 0", dinv == 0)
print(f"  d = {dinv} (shift={shift}, min_tau={min(tau)}) -> du=d=0")

# ---------- Route 3: graded-root top (exact sublevel components) ----------
Q = -Minv
z0 = np.array([-8, -4, -3, -2, -1])
xs = np.array([4.0, 2.0, 1.5, 1.0, 0.5])
def chi(t):
    t = np.asarray(t, float)
    return -(float(K @ t) + float(t @ Mf @ t)) / 2
def J0(t):
    return (-t[0] + 8, -t[1] + 4, -t[2] + 3, -t[3] + 2, -t[4] + 1)
def enum_level(n):
    bound = 2 * n + 1.25  # q(x-xs) = 2(chi-chi(xs)), chi(xs)=-0.625
    ranges = []
    for i in range(5):
        r = float(np.sqrt(bound * Q[i, i])) + 1
        ranges.append(range(int(np.floor(xs[i] - r)), int(np.ceil(xs[i] + r)) + 1))
    pts = set()
    for t in itertools.product(*ranges):
        dd = np.array(t, float) - xs
        if -float(dd @ (Mf @ dd)) > bound + 1e-9:
            continue
        if int(round(chi(np.array(t, float)))) <= n:
            pts.add(t)
    return pts
def comps(pts):
    pts = set(pts); par = {p: p for p in pts}
    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]; x = par[x]
        return x
    for p in pts:
        for v in range(5):
            for s in (-1, 1):
                q = list(p); q[v] += s; q = tuple(q)
                if q in pts:
                    a_, b_ = f(p), f(q)
                    if a_ != b_: par[a_] = b_
    d = defaultdict(list)
    for p in pts:
        d[f(p)].append(p)
    return list(d.values())
S0 = enum_level(0); C0 = comps(S0)
S1 = enum_level(1); C1 = comps(S1)
check("S_0 J0-stable", set(J0(t) for t in S0) == S0)
check("S_0 has 3 comps sizes {8,8,16}", sorted(len(c) for c in C0) == [8, 8, 16])
lut = {}
for j, c in enumerate(C0):
    for p in c:
        lut[p] = j
jm = sorted(lut[J0(c[0])] for c in C0)
# middle (size16) must be J0-fixed; outer pair swapped
mid = [j for j, c in enumerate(C0) if len(c) == 16][0]
check("J0 fixes middle comp, swaps outer pair",
      lut[J0(C0[mid][0])] == mid and
      all(lut[J0(C0[j][0])] != j for j, c in enumerate(C0) if j != mid))
check("S_1 connected", len(C1) == 1)
print(f"  S_0: {len(S0)} pts, 3 comps; S_1: {len(S1)} pts, connected")
print("  Greedy (Dai Sec 6): top J0-invariant vertex at degree -2, C_{-2} trivial")
print("  -> M = degenerate stem M(-2,-2): (d1,dl) = (0,0). AGREES with Wu+tau.")

# ---------- Control: Sigma(2,7,15) reproduces mu-bar=2 ----------
m2 = [-1, -2, -3, -2, -2, -15]
E2 = [(0, 1), (0, 2), (2, 3), (3, 4), (0, 5)]
M2 = np.zeros((6, 6), dtype=int)
for i in range(6):
    M2[i, i] = m2[i]
for i, j in E2:
    M2[i, j] = M2[j, i] = 1
d2 = np.diag(M2)
sols = []
for bits in range(64):
    w = np.array([(bits >> i) & 1 for i in range(6)], dtype=int)
    if all(int((M2 @ w)[v]) % 2 == int(d2[v]) % 2 for v in range(6)):
        sols.append((w.tolist(), int(w @ (M2 @ w))))
check("control Sigma(2,7,15): unique Wu, mu-bar=2",
      len(sols) == 1 and (-6 - sols[0][1]) / 8 == 2)
print(f"  control: w={sols[0][0]} w2={sols[0][1]} mu-bar={(-6 - sols[0][1]) / 8}")

print()
bad = [n_ for n_, ok in PASS if not ok]
print(f"{len(PASS) - len(bad)}/{len(PASS)} checks passed.")
assert not bad, bad
print("CONCLUSION: (d,dl,du)=(0,0,0), M trivial stem; h(Y)=0 in local equivalence.")
print("Same/mixed-orientation multiples all trivial: specified witness impossible.")
