import math
import numpy as np

# Refine gap edges at fixed phase, several large q: is (~0.422,~0.433) boundary
# converging to nonzero width? Track band edges near 0.427 for th=0 and th=0.25.
lam = 3.0
alpha = (math.sqrt(5) - 1) / 2

def edges_near(q, th, lo=0.40, hi=0.46):
    p = int(round(q * alpha))
    d = np.array([2 * lam * math.cos(2 * math.pi * (th + k * p / q)) for k in range(q)])
    off = np.ones(q - 1)
    M = np.diag(d) + np.diag(off, 1) + np.diag(off, -1)
    M[0, q - 1] = 1.0
    M[q - 1, 0] = 1.0
    w = np.sort(np.linalg.eigvalsh(M))
    w = w[(w > 0.30) & (w < 0.56)]
    return w

if __name__ == "__main__":
    for q in [144, 233, 377, 610, 987]:
        for th in [0.0, 0.1, 0.25, 0.4]:
            w = edges_near(q, th)
            gaps = [(w[i], w[i + 1], w[i + 1] - w[i]) for i in range(len(w) - 1)
                    if w[i + 1] - w[i] > 0.004]
            print(f"q={q} th={th}: " +
                  "; ".join(f"({a:.5f},{b:.5f},w={c:.5f})" for a, b, c in gaps[:6]))
