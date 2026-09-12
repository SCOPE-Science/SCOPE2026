"""Kasteleyn determinant for the two-periodic Aztec diamond (Chhita-Johansson convention).

Graph (CJ rotated coords): W={(i,j): i odd in [1,2n-1], j even in [0,2n]},
B={(i,j): i even in [0,2n], j odd in [1,2n-1]}. Edges: diagonal neighbours.
Kasteleyn matrix K(b,w) per Chhita-Johansson (2.3) with parameters (a,b=1).
Z_n(a) = |det K|.
"""
import numpy as np

def build_K(n, a, b=1.0):
    W = [(i, j) for i in range(1, 2*n, 2) for j in range(0, 2*n+1, 2)]
    B = [(i, j) for i in range(0, 2*n+1, 2) for j in range(1, 2*n, 2)]
    wi = {w: k for k, w in enumerate(W)}
    N = len(W)
    assert len(B) == N, (len(B), N)
    K = np.zeros((N, N), dtype=np.complex128)
    e1 = (1, 1); e2 = (-1, 1)
    for r, (x1, x2) in enumerate(B):
        s = (x1 + x2) % 4
        assert s in (1, 3)
        j = 0 if s == 1 else 1  # B_j class
        nbrs = {
            (x1+1, x2+1): (a*(1-j) + b*j),            # y = x+e1
            (x1-1, x2+1): (a*j + b*(1-j))*1j,          # y = x+e2
            (x1-1, x2-1): (a*j + b*(1-j)),             # y = x-e1
            (x1+1, x2-1): (a*(1-j) + b*j)*1j,          # y = x-e2
        }
        for w, val in nbrs.items():
            c = wi.get(w)
            if c is not None:
                K[r, c] = val
    return K

def logZ(n, a):
    K = build_K(n, a)
    sign, logabs = np.linalg.slogdet(K)
    return logabs  # log|det K| = log Z

if __name__ == "__main__":
    import math
    for n in [1, 2, 3, 4, 5, 6]:
        lz = logZ(n, 1.0)
        exact = n*(n+1)/2*math.log(2)
        print(f"n={n} logZ(a=1)={lz:.10f} exact={exact:.10f} match={abs(lz-exact)<1e-8}")
