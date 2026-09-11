import math
import numpy as np

# Refine: (a) L0(E) profile across the gap at high n; (b) small-eps increment
# scaling at center: Delta(eps)=L(eps)-L(0) vs eps: linear 2pi*eps (spectrum,
# slope 1) vs quadratic c2*eps^2 (gap, slope->0). Push n=480k, ntheta=8.
lam = 3.0
alpha = (math.sqrt(5) - 1) / 2
LOG3 = math.log(3.0)

def LE(E, eps, n, ntheta=8, renorm=10, seed=1):
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
    import sys
    mode = sys.argv[1] if len(sys.argv) > 1 else "profile"
    if mode == "profile":
        for E in [0.415, 0.418, 0.421, 0.424, 0.4274, 0.431, 0.434, 0.437, 0.440]:
            l0 = LE(E, 0.0, 240000)
            print(f"E={E}: L0-log3={l0-LOG3:+.6f}", flush=True)
    else:
        E = 0.4274
        l0 = LE(E, 0.0, 480000)
        print(f"E={E}: L0={l0:.7f} lift={l0-LOG3:+.7f}", flush=True)
        for eps in [0.005, 0.01, 0.02, 0.04]:
            le = LE(E, eps, 480000)
            d = le - l0
            print(f"  eps={eps}: Delta={d:.7f} 2pi*eps={2*math.pi*eps:.7f} "
                  f"slope={d/(2*math.pi*eps):.4f} Delta/eps^2={d/eps**2:.3f}", flush=True)
