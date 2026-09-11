import math, sys
import numpy as np

# Worst-case search: slope at eps=0.02 on dense grid over [0.1,0.6],
# extra refinement inside (0.415,0.44). n=240k, ntheta=8.
lam = 3.0
alpha = (math.sqrt(5) - 1) / 2

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
    n = 240000
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("all", "coarse"):
        print("== coarse [0.1,0.6] step 0.01 ==", flush=True)
        for E in np.linspace(0.1, 0.6, 51):
            E = float(E)
            l0 = LE(E, 0.0, n)
            l2 = LE(E, 0.02, n)
            print(f"E={E:.3f} slope02={(l2-l0)/(2*math.pi*0.02):.4f}", flush=True)
    if which in ("all", "fine"):
        print("== fine (0.40,0.45) step 0.002 ==", flush=True)
        for E in np.linspace(0.40, 0.45, 26):
            E = float(E)
            l0 = LE(E, 0.0, n)
            l2 = LE(E, 0.02, n)
            print(f"E={E:.4f} slope02={(l2-l0)/(2*math.pi*0.02):.4f}", flush=True)
