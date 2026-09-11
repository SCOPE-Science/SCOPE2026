import math, sys
import numpy as np

# High-precision slope INSIDE the candidate gap: E*=0.4274 (center),
# eps in {0.02,...,0.10}: slope=(L(eps)-L(0))/(2 pi eps).
# If E* is in a true gap: L is analytic+even in eps -> slope -> 0 as eps->0,
# and at eps=0.02 slope should already be small.
# Contrast with spectrum point E=0.3 (slope ~1).
lam = 3.0
alpha = (math.sqrt(5) - 1) / 2

def LE(E, eps, n=120000, ntheta=6, renorm=10, seed=0):
    rng = np.random.default_rng(seed)
    thetas = rng.random(ntheta)
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
    for E in [0.4274, 0.30, 0.45]:
        l0 = LE(E, 0.0)
        row = f"E={E}: L0={l0:.6f} "
        for eps in [0.02, 0.04, 0.06, 0.08, 0.10]:
            le = LE(E, eps)
            slope = (le - l0) / (2 * math.pi * eps)
            row += f"s({eps:.2f})={slope:.4f} "
        print(row, flush=True)
