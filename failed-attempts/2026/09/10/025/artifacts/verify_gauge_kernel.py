"""Monte Carlo replay of gauge-kernel inclusion int_O L_V[p,q] = 0 (stdlib only).

V(x) = (1-r^2) x3 (1-x3) e1 vanishes on all of dOmega (lateral + caps).
h = L_V = dV + dV^T - (div V) I.
Pairs: (u1,u2) = (x1, x1^2-x2^2) and (x1x3, x2x3), all harmonic on Omega.
Exact claim: integral is 0 by div-W identity (W|dO = 0 since V|dO = 0).
Pass: |estimate| <= 5e-3 with N=400000 (MC error scale).
"""
import math
import random

random.seed(3)
VOL = math.pi


def dV(x1, x2, x3):
    g = x3 * (1 - x3)
    h = (1 - x1**2 - x2**2) * (1 - 2 * x3)
    return [[-2*x1*g, -2*x2*g, h], [0, 0, 0], [0, 0, 0]]


def L_of(A):
    tr = A[0][0]
    return [[A[i][j]+A[j][i]-(tr if i == j else 0) for j in range(3)] for i in range(3)]


def mc(pairs, N=400000):
    outs = []
    for (pf, qf) in pairs:
        acc = 0.0
        for _ in range(N):
            u = random.random(); r = math.sqrt(u)
            th = random.random() * 2 * math.pi; x3 = random.random()
            x1 = r * math.cos(th); x2 = r * math.sin(th)
            L = L_of(dV(x1, x2, x3))
            p = pf(x1, x2, x3); q = qf(x1, x2, x3)
            acc += sum(L[i][j]*p[i]*q[j] for i in range(3) for j in range(3))
        outs.append(acc / N * VOL)
    return outs


pairs = [
    (lambda x1, x2, x3: [1, 0, 0], lambda x1, x2, x3: [2*x1, -2*x2, 0]),
    (lambda x1, x2, x3: [x3, 0, x1], lambda x1, x2, x3: [0, x3, x2]),
]
vals = mc(pairs)
for k, v in enumerate(vals):
    print(f"pair{k+1}: integral = {v:.6f} (expect 0)")
    assert abs(v) <= 5e-3, v
print("GAUGE-KERNEL-MC_OK")
