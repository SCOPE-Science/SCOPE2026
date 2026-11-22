"""Reproducible checks for a multiscale Landweber confidence-interval construction.

Requires Python 3 with numpy. The infinite-dimensional-index and large-scale
limit claims are proved separately by explicit inequalities, not by this script.
"""
import math
import numpy as np


def construction(q, r):
    assert q >= 2 and r >= 2
    ii = np.arange(1, r + 1, dtype=float)
    c = np.power(float(q), -ii)
    c /= np.linalg.norm(c)
    e1 = np.eye(r)[0]
    v = e1 - c
    v /= np.linalg.norm(v)
    V = np.eye(r) - 2.0 * np.outer(v, v)
    singular = np.power(float(q), -2.0 * ii)
    A = (V * singular) @ V.T
    omega = q**4 / 2.0
    return V, A, omega, c, singular


def modal_rows(q, r):
    V, A, omega, c, singular = construction(q, r)
    rows = []
    sds = []
    paddings = []
    for j in range(1, r + 1):
        k = 2 * (q ** (4 * (j - 1)))
        t = 0.5 * np.power(float(q), -4.0 * np.arange(r, dtype=float))
        u = -np.expm1(float(k) * np.log1p(-t))
        a = c * u / singular
        sd = np.linalg.norm(a)
        # nu=M=sigma=1; the actual global bias bound from source Lemma 3.4.
        # Stable form avoids subtracting two large near-equal logarithms.
        log_b = math.log(2.0) - 4 * math.log(q) + k * math.log1p(-1 / (k + 1)) - math.log(k + 1)
        b = math.exp(log_b)
        rows.append(a / sd)
        sds.append(sd)
        paddings.append(b / sd)
    return np.array(rows), np.array(sds), np.array(paddings)


def run():
    count = 0
    for q in (2, 3, 5, 8, 16):
        for r in (2, 3, 4):
            V, A, omega, c, singular = construction(q, r)
            assert np.allclose(V.T @ V, np.eye(r), atol=1e-12)
            assert np.allclose(V[0], c, atol=1e-12)
            assert np.allclose(np.linalg.eigvalsh(A), np.sort(singular), atol=1e-12)
            count += 3
            T, sds, pads = modal_rows(q, r)
            assert np.allclose(np.linalg.norm(T, axis=1), np.ones(r), atol=1e-12)
            assert np.all(pads >= 0) and np.all(pads < 1)
            count += 2
            # Verify the exact modal scalar formula against actual Landweber recurrence.
            k = 2 * q**4 if q <= 5 else 2
            y = np.linspace(-0.73, 0.91, r)
            B = A.T @ A
            x = np.zeros(r)
            for _ in range(k):
                x = x + omega * A.T @ (y - A @ x)
            ey = V.T @ y
            t = 0.5 * np.power(float(q), -4.0 * np.arange(r, dtype=float))
            u = -np.expm1(float(k) * np.log1p(-t))
            modal_x = V @ (u * ey / singular)
            assert np.allclose(x, modal_x, rtol=1e-7, atol=1e-7)
            count += 1
    for r in (2, 3, 4, 5):
        prev = None
        for q in (4, 8, 16, 32):
            T, sds, pads = modal_rows(q, r)
            off = float(np.max(np.abs(T @ T.T - np.eye(r))))
            assert np.max(np.abs(T - np.eye(r))) < 5.0 / q
            assert np.max(pads) < 4.0 * q**-5
            if prev is not None:
                assert off <= prev + 1e-8
            prev = off
            count += 3
        assert off < 0.05
        count += 1
    # Stochastic consistency check only; convergence is supplied by the proof.
    q, r, alpha = 32, 3, 0.05
    T, _, pads = modal_rows(q, r)
    z = 1.959963984540054
    rng = np.random.default_rng(261000882)
    vals = rng.standard_normal((200000, r)) @ T.T
    empirical = np.mean(np.all(np.abs(vals) <= z + pads, axis=1))
    limiting = (1-alpha)**r
    assert abs(empirical-limiting) < 0.007
    count += 1
    print(f'VERIFY_OK {count} assertions; r={r}, q={q}, empirical={empirical:.5f}, limit={limiting:.5f}')


if __name__ == '__main__':
    run()
