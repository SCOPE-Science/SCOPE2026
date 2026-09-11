import math
import numpy as np

# Analyticity test: in a gap, L(E,eps) is analytic in (E,eps) near (E*,0),
# hence even in eps: L(eps)-L(0) = c2 eps^2 + O(eps^4) -> slope = c2*eps/(2pi) -> 0.
# On spectrum: L(eps)-L(0) = 2pi*eps exactly.
# Distinguish via CONVERGENCE: eps -> 0 with n -> infinity (error << eps^2 ~ 1e-6).
# At E*=0.4274: L0-log3 ~ +0.0013 with n=120k -- but is that a gap signature
# (positive gap lift) or finite-n error? Check convergence of d(n)=L_n(E*,0)-log3
# vs d(n) at spectrum point: gap lift should persist, error should decay.
lam = 3.0
alpha = (math.sqrt(5) - 1) / 2
LOG3 = math.log(3.0)

def LE(E, eps, n, ntheta=4, renorm=10, seed=0):
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
    for E in [0.4274, 0.30]:
        row = []
        for n in [60000, 120000, 240000, 480000]:
            l0 = LE(E, 0.0, n)
            row.append(f"n={n}: L0-log3={l0-LOG3:+.6f}")
        print(f"E={E}: " + "  ".join(row), flush=True)
