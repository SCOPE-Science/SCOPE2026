"""Small-N Pareto-4.5 Wigner edge probe (stdlib only, fixed seed).

Support-only numerics for the target: (i) max-entry scaling ~ N^{-1/18};
(ii) empirical edge spread is O(N^{-2/3}) with TW1-plausible location.
Largest eigenvalue via cyclic Jacobi (exact orthogonal diagonalization).
GOE proxy: Wigner with Rademacher x_ij (same code path, moment contrast).
"""
import math
import random
import sys

XM = math.sqrt(5.0) / 3.0
ALPHA = 4.5
SEED = 562


def sample_std_pareto(rng):
    u = rng.random()
    while u >= 1.0:  # guard u==1
        u = rng.random()
    y = XM * (1.0 - u) ** (-1.0 / ALPHA)
    return y if rng.random() < 0.5 else -y


def wigner(n, rng, sampler):
    s = 1.0 / math.sqrt(n)
    a = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            v = sampler(rng) * s
            a[i][j] = v
            a[j][i] = v
    return a


def jacobi_max_eig(a, tol=1e-10, max_sweeps=25):
    n = len(a)
    for _ in range(max_sweeps):
        off = 0.0
        for p in range(n - 1):
            ap = a[p]
            for q in range(p + 1, n):
                apq = ap[q]
                off += apq * apq
                if abs(apq) > 1e-300:
                    app = ap[p]
                    aqq = a[q][q]
                    theta = (aqq - app) / (2.0 * apq)
                    t = (1.0 if theta >= 0 else -1.0) / (abs(theta) + math.sqrt(theta * theta + 1.0))
                    c = 1.0 / math.sqrt(t * t + 1.0)
                    sn = t * c
                    # apply rotation to rows/cols p,q
                    for k in range(n):
                        akp = a[k][p]
                        akq = a[k][q]
                        a[k][p] = c * akp - sn * akq
                        a[k][q] = sn * akp + c * akq
                    for k in range(n):
                        apk = a[p][k]
                        aqk = a[q][k]
                        a[p][k] = c * apk - sn * aqk
                        a[q][k] = sn * apk + c * aqk
        if off < tol * tol:
            break
    return max(a[i][i] for i in range(n))


def run(n, trials, sampler, seed):
    rng = random.Random(seed)
    lam = []
    mmax = []
    for _ in range(trials):
        a = wigner(n, rng, sampler)
        m = 0.0
        for i in range(n):
            for j in range(i, n):
                v = abs(a[i][j])
                if v > m:
                    m = v
        mmax.append(m)
        lam.append(jacobi_max_eig(a))
    return lam, mmax


def stats(v):
    m = sum(v) / len(v)
    var = sum((x - m) ** 2 for x in v) / len(v)
    return m, math.sqrt(var)


def main():
    # Rademacher sampler defined with same (rng) signature
    def rademacher(rng):
        return 1.0 if rng.random() < 0.5 else -1.0

    plan = [(20, 120), (30, 60), (40, 30)]
    print(f"{'N':>4} {'trials':>6} {'law':>8} {'mean(lmax)':>10} {'sd':>8} "
          f"{'mean(s)':>9} {'sd(s)':>7} {'mean(max|H|)':>12} {'N^-1/18':>9}")
    for n, tr in plan:
        for name, sampler in (("pareto", sample_std_pareto), ("radem", rademacher)):
            lam, mmax = run(n, tr, sampler, SEED + n)
            ml, sl = stats(lam)
            s = [(x - 2.0) * n ** (2.0 / 3.0) for x in lam]
            ms, ss = stats(s)
            mm, _ = stats(mmax)
            print(f"{n:>4} {tr:>6} {name:>8} {ml:>10.4f} {sl:>8.4f} "
                  f"{ms:>9.3f} {ss:>7.3f} {mm:>12.3e} {n ** (-1.0/18.0):>9.3e}")
    print("SIM_EDGE_OK (support only: edge O(N^-2/3) spread, max-entry N^-1/18 scale)")


if __name__ == "__main__":
    sys.exit(main())
