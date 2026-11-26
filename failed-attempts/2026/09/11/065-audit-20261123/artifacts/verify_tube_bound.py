"""Verify the shrinking-tube bound for o(h^2) torus quasimodes.

Theorem under test: L2-normalized u_h on T^2=R^2/Z^2 with
||(-h^2 Delta - 1) u_h|| = o(h^2) satisfies tube mass -> 0, hence <= 7/8.

Checks:
1. Thin-window single-shell selection: window |N - R^2| <= W with W -> 0
   contains at most one integer shell for small h (W < 1/4).
2. Fiber lemma: for fixed k1, #{k2 : |k2^2 - A| <= W} <= 2 when W < 1/4,
   tested over spectral values A = R^2 - k1^2 for small h.
3. Analytic decay table: M(v) <= 2*sqrt(h)*J*||v||^2 with J <= 2 gives
   M(v) <= 4*sqrt(h) -> 0; tail ||w||^2 <= r^2/delta^2 -> 0.
4. Numerical tube mass of random exact single-shell eigenfunctions:
   small and consistent with M <= 4*sqrt(h).
"""
import cmath
import math
import random

print("=== 1. thin-window shell uniqueness ===")
ntest = 0
for h in [0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001, 1e-4]:
    R2 = 1.0 / (4 * math.pi**2 * h**2)
    # simulate residual r = h^3 (which is o(h^2)); delta = h*sqrt(r) = h^2.5
    r = h**3
    delta = h * math.sqrt(r)
    W = delta / (4 * math.pi**2 * h**2)
    Nstar = int(math.floor(R2 + 0.5))
    cnt = sum(1 for N in range(Nstar - 3, Nstar + 4) if abs(N - R2) <= W)
    assert W < 0.25, (h, W)
    assert cnt <= 1, (h, R2, W, cnt)
    ntest += 1
print(f"pass: {ntest} values of h give window W<1/4 with <=1 shell")

print("=== 2. fiber lemma (W < 1/4 -> <= 2 values of k2) ===")
def fiber_count(A, W):
    n = 0
    B = A + W
    if B < 0:
        return 0
    kmax = int(math.ceil(math.sqrt(B))) + 1
    for k in range(-kmax, kmax + 1):
        if abs(k * k - A) <= W:
            n += 1
    return n

random.seed(0)
worst = 0
tested = 0
cases = []
for h in [0.01, 0.002, 0.0005, 1e-4]:
    R2 = 1.0 / (4 * math.pi**2 * h**2)
    r = h**3
    W = h * math.sqrt(r) / (4 * math.pi**2 * h**2)
    R = math.sqrt(R2)
    for k1 in [0, 1, 5, 37, int(R / 2), int(R) - 1, int(R), int(R) + 1]:
        cases.append((R2 - k1 * k1, W))
for _ in range(200):
    A = random.uniform(-5, 1e8)
    W = random.uniform(0, 0.24)
    cases.append((A, W))
for (A, W) in cases:
    n = fiber_count(A, W)
    worst = max(worst, n)
    tested += 1
    assert n <= 2, (A, W, n)
print(f"pass: {tested} cases, worst fiber count = {worst} (bound 2)")

print("=== 3. analytic decay table (r = h^3 model residual) ===")
print(" h        r=o(h^2)   delta      M(v)<=4sqrt(h)  tail<=r^2/d^2")
for h in [0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001]:
    r = h**3
    delta = h * math.sqrt(r)
    Mv = 4 * math.sqrt(h)
    tail = r**2 / delta**2
    print(f" {h:<8} {r:.2e}   {delta:.2e}   {Mv:.4f}           {tail:.2e}")

print("=== 4. random single-shell eigenfunctions ===")
def lattice_pts(N):
    pts = []
    r = int(math.isqrt(N))
    for k1 in range(-r - 1, r + 2):
        d = N - k1 * k1
        if d < 0:
            continue
        k2 = int(math.isqrt(d))
        for s in ({k2, -k2} if k2 else {0}):
            if s * s == d:
                pts.append((k1, s))
    return pts

def tube_mass(pts, coeff, h, nq=2000):
    """M = sum_{k1} int_{tube} |g_{k1}(x2)|^2 dx2, tube = |x2|<sqrt(h) mod 1."""
    from collections import defaultdict
    fib = defaultdict(list)
    for (k1, k2), c in zip(pts, coeff):
        fib[k1].append((k2, c))
    d = math.sqrt(h)
    M = 0.0
    for a, b in ((0.0, d), (1.0 - d, 1.0)):
        for j in range(nq):
            x = a + (b - a) * (j + 0.5) / nq
            F = 0.0
            for k1, lst in fib.items():
                s = 0j
                for (k2, c) in lst:
                    s += c * cmath.exp(2j * math.pi * k2 * x)
                F += abs(s) ** 2
            M += F * (b - a) / nq
    return M

random.seed(1)
for N in [65, 325, 4225]:
    pts = lattice_pts(N)
    R = math.sqrt(N)
    h = 1.0 / (2 * math.pi * R)
    J = max(sum(1 for (a, b) in pts if a == k1) for k1, _ in pts)
    assert J <= 2, (N, J)
    for trial in range(3):
        coeff = [random.gauss(0, 1) + 1j * random.gauss(0, 1) for _ in pts]
        nrm = math.sqrt(sum(abs(c) ** 2 for c in coeff))
        coeff = [c / nrm for c in coeff]
        M = tube_mass(pts, coeff, h)
        print(f"N={N:5d} h={h:.5f} modes={len(pts):3d} Jmax={J} "
              f"tube_mass={M:.5f} analytic<= {4*math.sqrt(h):.5f}")
        assert M <= 4 * math.sqrt(h) + 0.02, (N, M)
print("\nALL CHECKS PASS")
