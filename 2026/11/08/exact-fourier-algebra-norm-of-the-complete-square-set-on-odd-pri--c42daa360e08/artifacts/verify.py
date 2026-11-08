"""Exact-structure checks for Fourier norms of all square residues modulo odd prime powers.

Standard library only. Direct root-of-unity sums are numerical diagnostics,
not substitutes for the all-depth symbolic proof.
"""
from __future__ import annotations
import cmath
import math

CASES = [(3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
         (5, 1), (5, 2), (5, 3), (5, 4), (7, 2), (7, 3), (11, 2)]


def formula(p: int, k: int):
    assert p % 2 == 1 and k >= 1
    N = p ** k
    E = tuple(m for m in range(1, k + 1) if (k - m) % 2 == 0)
    Q_size = 1 + sum((p - 1) * p ** (m - 1) // 2 for m in E)
    tau = math.sqrt(p) * (1 if p % 4 == 1 else 1j)
    vals = []
    for t in range(N):
        if t == 0:
            vals.append(Q_size)
            continue
        v = 0
        w = t
        while w % p == 0:
            v += 1
            w //= p
        B = 1 + sum((p - 1) * p ** (m - 1) // 2 for m in E if m <= v)
        if (v + 1) in E:
            sign = 1 if pow(w % p, (p - 1) // 2, p) == 1 else -1
            vals.append(B + p ** v * (-1 + sign * tau) / 2)
        else:
            vals.append(B)
    return Q_size, vals


def slope(p: int):
    g = math.sqrt(p) if p % 4 == 1 else math.sqrt(p + (p / (p + 1)) ** 2)
    return (p - 1) / (4 * (p + 1)) + (p - 1) * g / (4 * p)


def norm_by_strata(p: int, k: int):
    E = tuple(m for m in range(1, k + 1) if (k - m) % 2 == 0)
    N = p ** k
    total = (1 + sum((p - 1) * p ** (m - 1) // 2 for m in E)) / N
    tau = math.sqrt(p) * (1 if p % 4 == 1 else 1j)
    for v in range(k):
        B = 1 + sum((p - 1) * p ** (m - 1) // 2 for m in E if m <= v)
        if v + 1 in E:
            aa = B - p ** v / 2
            bb = p ** v * tau / 2
            total += (p - 1) * (abs(aa + bb) + abs(aa - bb)) / (2 * p ** (v + 1))
        else:
            total += (p - 1) * B / p ** (v + 1)
    return total


def check():
    for p, k in CASES:
        N = p ** k
        squares = {a * a % N for a in range(N)}
        size, vals = formula(p, k)
        assert len(squares) == size, (p, k, size, len(squares))
        brute = [sum(cmath.exp(2j * math.pi * t * a / N) for a in squares)
                 for t in range(N)]
        worst = max(abs(x - y) for x, y in zip(brute, vals))
        assert worst < 1e-7 * max(1, size), (p, k, worst)
        norm_direct = sum(abs(x) for x in brute) / N
        norm_values = sum(abs(x) for x in vals) / N
        norm_fast = norm_by_strata(p, k)
        assert abs(norm_direct - norm_values) < 1e-7
        assert abs(norm_direct - norm_fast) < 1e-7
        assert abs(sum(brute).real - N) < 1e-7 * N
        assert abs(sum(abs(z) ** 2 for z in brute) - N * size) < 1e-7 * N * size
        print(f"CASE_OK p={p} k={k} size={size} norm={norm_fast:.12f} max_coefficient_err={worst:.3g}")
    for p in (3, 5, 7, 11):
        s = slope(p)
        v30, v60 = norm_by_strata(p, 30), norm_by_strata(p, 60)
        # Convergence of bounded intercept, not a proof of its existence.
        assert abs((v60 - v30) - 30 * s) < .02, (p, s, v30, v60)
        print(f"SLOPE_OK p={p} slope={s:.12f} residual30={v30 - 30*s:.9f} residual60={v60 - 60*s:.9f}")
    print("SQUARE_RESIDUE_WIENER_NORM_PASS")


if __name__ == '__main__':
    check()
