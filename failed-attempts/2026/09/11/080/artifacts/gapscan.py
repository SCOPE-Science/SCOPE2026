import math, sys
import numpy as np

lam = 3.0
alpha = (math.sqrt(5) - 1) / 2
LOG3 = math.log(3.0)

def LE_long(E, eps=0.0, n=300000, ntheta=4, renorm=10):
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

def ids_fib(E, q=144, ntheta=40):
    # IDS via rotation number of periodic approximant: count of eigenvalues <= E / q
    # Use exact tridiagonal eigvalsh on period-q approximant with phase average
    p = int(round(q * alpha))
    thetas = np.linspace(0, 1, ntheta, endpoint=False)
    tot = 0
    for th in thetas:
        d = np.array([2 * lam * math.cos(2 * math.pi * (th + k * p / q)) for k in range(q)])
        off = np.ones(q - 1)
        M = np.diag(d) + np.diag(off, 1) + np.diag(off, -1)
        # periodic BC: corner entries
        M[0, q - 1] = 1.0
        M[q - 1, 0] = 1.0
        w = np.linalg.eigvalsh(M)
        tot += int(np.sum(w <= E))
    return tot / (ntheta * q)

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "fine"
    if mode == "fine":
        Es = np.linspace(0.1, 0.6, 501)
        for E in Es:
            E = float(E)
            l0 = LE_long(E, 0.0, n=120000, ntheta=2)
            print(f"E={E:.4f} L0={l0:.6f} d={l0-LOG3:+.6f}", flush=True)
    elif mode == "ids":
        Es = np.linspace(0.1, 0.6, 251)
        prev = None
        for E in Es:
            E = float(E)
            v = ids_fib(E)
            flag = ""
            if prev is not None and abs(v - prev) < 1e-12:
                flag = "  <plateau?"
            prev = v
            print(f"E={E:.4f} IDS~{v:.5f}{flag}", flush=True)
