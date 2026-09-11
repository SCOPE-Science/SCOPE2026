import math
import numpy as np

lam = 3.0
alpha = (math.sqrt(5) - 1) / 2

def approx_gaps(q, th=0.0, lo=0.05, hi=0.65):
    p = int(round(q * alpha))
    d = np.array([2 * lam * math.cos(2 * math.pi * (th + k * p / q)) for k in range(q)])
    off = np.ones(q - 1)
    M = np.diag(d) + np.diag(off, 1) + np.diag(off, -1)
    M[0, q - 1] = 1.0
    M[q - 1, 0] = 1.0
    w = np.sort(np.linalg.eigvalsh(M))
    gaps = []
    for i in range(len(w) - 1):
        a, b = w[i], w[i + 1]
        if b > lo and a < hi and b - a > 1e-9:
            gaps.append((a, b, b - a))
    return w, gaps

if __name__ == "__main__":
    import sys
    q = int(sys.argv[1]) if len(sys.argv) > 1 else 377
    for th in [0.0, 0.25, 0.5]:
        w, gaps = approx_gaps(q, th)
        gaps.sort(key=lambda g: -g[2])
        print(f"q={q} th={th}: neig_in_range={sum(1 for x in w if 0.05 < x < 0.65)}")
        for a, b, wd in gaps[:12]:
            print(f"   gap ({a:.5f},{b:.5f}) width={wd:.5f} center={(a+b)/2:.5f}")
