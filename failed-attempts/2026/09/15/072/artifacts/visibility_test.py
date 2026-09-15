"""Billiard E-E visibility test for the disc model (bounded recovery test).

Model: Omega0 = unit disc, E = boundary arc |theta| < E_half (nonempty small open set).
A point x with direction v is 'E-E visible' if the forward billiard orbit from (x,v)
and the backward orbit from (x,-v) each hit E within N reflections. For the centre,
diameter orbits alternate {phi, phi+pi} so visibility = phi in E union (E+pi):
a proper cone; most directions are invisible. This script quantifies the missing cone
and shows reflections do not close it at the centre, while off-centre points gain
visibility only via long orbits (length L growing with N), so the attenuation weight
exp(-2*lambda*t) has max/min ratio exp(2|lambda|L) blowing up uniformly in lambda.
"""
import numpy as np


def trace_hits_E(x, v, E_half, N):
    p = np.array(x, float)
    d = np.array(v, float)
    for _ in range(N + 1):
        b = float(np.dot(p, d))
        c = float(np.dot(p, p)) - 1.0
        disc = b * b - c
        if disc < 0:
            return False
        t = -b + np.sqrt(disc)
        if t < 1e-12:
            t = -b - np.sqrt(disc)
            if t < 1e-12:
                return False
        p = p + t * d
        th = np.arctan2(p[1], p[0])
        wrapped = abs(((th + np.pi) % (2 * np.pi)) - np.pi)
        if wrapped < E_half:
            return True
        n = p / np.linalg.norm(p)
        d = d - 2 * np.dot(d, n) * n
    return False


def visible_frac(x, E_half, N, M=720):
    phis = np.linspace(0, 2 * np.pi, M, endpoint=False)
    cnt = 0
    for ph in phis:
        v = np.array([np.cos(ph), np.sin(ph)])
        if trace_hits_E(x, v, E_half, N) and trace_hits_E(x, -v, E_half, N):
            cnt += 1
    return cnt / M


if __name__ == "__main__":
    for E_half in [0.3, 0.6]:
        for N in [1, 2, 4, 8, 16]:
            for x in [(0.0, 0.0), (-0.5, 0.0), (0.5, 0.3)]:
                print(f"E_half={E_half} N={N} x={x} vis={visible_frac(x, E_half, N):.3f}")
    # attenuation weight blow-up illustration
    for lam, L in [(1.0, 4.0), (3.0, 12.0), (5.0, 12.0)]:
        print(f"lambda={lam} L={L} weight_ratio={np.exp(2 * abs(lam) * L):.3e}")
