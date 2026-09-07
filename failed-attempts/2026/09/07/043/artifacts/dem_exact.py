"""Exact L_inf star discrepancy by critical-box (DEM) enumeration, O(N^2).

D_N^* = max over the 4 open/closed variants at grid corners
(a,b) in ({x_i} U {1}) x ({y_j} U {1}) of |C(a,b)/N - a*b|.
Exactness argument (critical-box lemma) is proved in DRAFT.md; the four
variants capture all one-sided limits of the cadlag counting function.

Includes: float64 vs mpmath-80-digit cross-check (delta-closeness + min-gap),
independent searchsorted implementation cross-check, ETK instance checks.
"""
import numpy as np
import mpmath as mp
import json, time

mp.mp.dps = 80
_theta = mp.power(mp.mpf(2), mp.mpf(1) / 3)
_th2 = _theta * _theta
A1H, A2H = _theta - 1, _th2 - 1
A1F = float(np.cbrt(2.0) - 1.0)
A2F = float(np.cbrt(4.0) - 1.0)
print("alpha float:", repr(A1F), repr(A2F))
print("alpha hp   :", A1H, A2H)

C0 = 0.026  # safe rounded-down certified constant (true c0 = 0.0260596...)


def points_float(N):
    n = np.arange(1, N + 1, dtype=np.float64)
    return np.mod(n * A1F, 1.0), np.mod(n * A2F, 1.0)


def points_hp(N):
    xs = np.empty(N)
    ys = np.empty(N)
    for i in range(1, N + 1):
        xs[i - 1] = float(mp.frac(i * A1H))
        ys[i - 1] = float(mp.frac(i * A2H))
    return xs, ys


def star_disc_exact(xs, ys):
    N = len(xs)
    assert len(np.unique(xs)) == N and len(np.unique(ys)) == N
    assert xs.min() > 0 and ys.min() > 0
    ox = np.argsort(xs)
    X = xs[ox]
    Y = ys[ox]
    oy = np.argsort(Y, kind="stable")
    Ys = Y[oy]
    rank = np.empty(N, dtype=np.int64)
    rank[oy] = np.arange(N)
    cnt = np.zeros(N, dtype=np.float64)
    P = np.empty(N, dtype=np.float64)
    best = 0.0
    invN = 1.0 / N
    def scan(P, copen):
        v = np.abs(copen * invN - a * Ys).max()
        w = np.abs(P * invN - a * Ys).max()            # y-closed counts
        n_in = cnt.sum()
        u = abs(n_in * invN - a)                        # b = 1 column
        m = v if v > w else w
        return u if u > m else m
    for i in range(N):
        a = X[i]
        np.cumsum(cnt, out=P)
        copen = np.concatenate((np.zeros(1), P[:-1]))  # y-strict counts
        m = scan(P, copen)  # x-strict state (point i not yet inserted)
        if m > best:
            best = m
        cnt[rank[i]] += 1  # insert point i exactly once
        np.cumsum(cnt, out=P)
        copen = np.concatenate((np.zeros(1), P[:-1]))
        m = scan(P, copen)  # x-closed state (point i included)
        if m > best:
            best = m
    np.cumsum(cnt, out=P)  # a = 1 column (all points)
    copen = np.concatenate((np.zeros(1), P[:-1]))
    best = max(best, float(np.abs(copen * invN - Ys).max()),
               float(np.abs(P * invN - Ys).max()))
    return best


def star_disc_v2(xs, ys):
    """Independent code path (mask + searchsorted) for cross-check, N<=512."""
    N = len(xs)
    X = np.sort(xs)
    Y = np.sort(ys)
    best = 0.0
    invN = 1.0 / N
    for a in list(X) + [1.0]:
        for sx in ("left", "right"):
            m = xs < a if sx == "left" else xs <= a
            sub = np.sort(ys[m])
            for sy in ("left", "right"):
                c = np.searchsorted(sub, Y, side=sy)
                best = max(best, float(np.abs(c * invN - a * Y).max()))
            best = max(best, abs(m.sum() * invN - a))
    return best


def etk_instance(N, D_exact):
    """Verify ETK RHS (outer const 9/4) with exact exponential sums >= D_exact,
    and the majorant chain using C0."""
    H = int(round(N ** (1 / 3)))
    while (H + 1) ** 3 <= N:
        H += 1
    while H ** 3 > N:
        H -= 1
    n = np.arange(1, N + 1, dtype=np.float64)
    tot = 0.0
    worst_margin = 1.0
    for h1 in range(-H, H + 1):
        for h2 in range(-H, H + 1):
            if h1 == 0 and h2 == 0:
                continue
            k = max(abs(h1), abs(h2))
            beta = h1 * A1F + h2 * A2F
            d = abs(beta - round(beta))
            assert d >= C0 / k / k * 0.999, (N, h1, h2, d)  # c0 usage check
            s = abs(np.sin(np.pi * N * beta)) / (N * abs(np.sin(np.pi * beta)))
            maj = min(1.0, 1.0 / (2 * N * d))
            assert s <= maj * (1 + 1e-9) + 1e-15, (N, h1, h2)
            r = max(1, abs(h1)) * max(1, abs(h2))
            tot += s / r
            cand = (k * k / (2 * N * C0))
            worst_margin = min(worst_margin, 1.0 / (2 * N * d) / max(s, 1e-300))
    rhs = 2.25 * (2.0 / (H + 1) + tot)
    return H, rhs, rhs / D_exact


if __name__ == "__main__":
    out = {}
    # cross-checks first (small N)
    for Nc in (64, 256):
        xs, ys = points_float(Nc)
        d1 = star_disc_exact(xs, ys)
        d2 = star_disc_v2(xs, ys)
        print(f"N={Nc}: exact={d1:.12f} v2={d2:.12f} agree={d1 == d2}")
        assert d1 == d2
    # float vs high-precision closeness + min gap (largest N)
    for Nc in (2048, 20000):
        xf, yf = points_float(Nc)
        xh, yh = points_hp(Nc)
        dx = float(np.abs(xf - xh).max())
        dy = float(np.abs(yf - yh).max())
        gx = float(np.diff(np.sort(xf)).min())
        gy = float(np.diff(np.sort(yf)).min())
        print(f"N={Nc}: max|float-hp|=({dx:.2e},{dy:.2e}) min-gaps=({gx:.2e},{gy:.2e})")
        assert max(dx, dy) < 1e-11 and min(gx, gy) > 1e-9
    # main exact table
    for Nc in (128, 256, 512, 1024, 2048, 4096, 8192, 16384, 20000):
        xs, ys = points_float(Nc)
        t0 = time.time()
        d = star_disc_exact(xs, ys)
        dt = time.time() - t0
        row = {"D": d, "sec": dt}
        if Nc <= 2048:
            H, rhs, ratio = etk_instance(Nc, d)
            row.update({"H": H, "ETK_RHS": rhs, "ETK_ratio": ratio})
            print(f"N={Nc}: D={d:.9f} H={H} ETK_RHS={rhs:.6f} ratio={ratio:.1f} ({dt:.2f}s)")
            assert rhs >= d
        else:
            print(f"N={Nc}: D={d:.9f} ({dt:.2f}s)")
        out[str(Nc)] = row
    json.dump(out, open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-78/output/artifacts/dem_table.json", "w"), indent=1)
    print("wrote dem_table.json")
