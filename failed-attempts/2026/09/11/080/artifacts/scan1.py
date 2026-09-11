import math, sys
import numpy as np

lam = 3.0
alpha = (math.sqrt(5) - 1) / 2

def LE(E, eps, n=40000, ntheta=6, renorm=10):
    thetas = np.linspace(0, 1, ntheta, endpoint=False)
    tot = 0.0
    for th in thetas:
        M = np.eye(2, dtype=complex)
        s = 0.0
        ph = 2 * math.pi * th
        step = 2 * math.pi * alpha
        ce = math.cosh(2 * math.pi * eps)
        se = math.sinh(2 * math.pi * eps)
        for k in range(1, n + 1):
            a = ph + k * step
            V = 2 * lam * (math.cos(a) * ce - 1j * math.sin(a) * se)
            A11 = E - V
            m00, m01, m10, m11 = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
            M[0, 0] = A11 * m00 - m10
            M[0, 1] = A11 * m01 - m11
            M[1, 0] = m00
            M[1, 1] = m01
            if k % renorm == 0:
                nrm = float(np.linalg.norm(M))
                s += math.log(nrm)
                M /= nrm
        nrm = float(np.linalg.norm(M))
        s += math.log(nrm)
        tot += s / n
    return tot / ntheta

if __name__ == "__main__":
    Es = np.linspace(0.1, 0.6, 21)
    for E in Es:
        E = float(E)
        l0 = LE(E, 0.0)
        l2 = LE(E, 0.02)
        l5 = LE(E, 0.05)
        l10 = LE(E, 0.10)
        s2 = (l2 - l0) / (2 * math.pi * 0.02)
        s5 = (l5 - l0) / (2 * math.pi * 0.05)
        s10 = (l10 - l0) / (2 * math.pi * 0.10)
        print(f"E={E:.3f} L0={l0:.6f} s02={s2:.4f} s05={s5:.4f} s10={s10:.4f}", flush=True)
