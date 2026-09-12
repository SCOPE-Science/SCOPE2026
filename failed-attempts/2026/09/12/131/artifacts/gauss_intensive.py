"""Exact diagonal-Gaussian intensive uniformity scan (bounded recovery test).

Uses closed-form 1D entropic cost with eps*KL(pi|mu x nu):
  s=sqrt(a b), D=sqrt(eps^2+4ab), t=(D-eps)/(2s),
  C(a,b)=(a+b-(D-eps))/2 - (eps/2)*log(1-t^2).
Tensor sums over dims; checks (1/n)|S-OT|/eps over admissible profiles.
Class proxy: kappa=1.0 => var<=1; F=2.0 => avg inv-var<=2; M=1.0 => avg var<=1.
"""
import numpy as np

def C1(a, b, eps):
    s = np.sqrt(a * b)
    D = np.sqrt(eps * eps + 4 * a * b)
    t = (D - eps) / (2 * s)
    return (a + b - (D - eps)) / 2 - (eps / 2) * np.log1p(-t * t)

def OT1(a, b):
    return (np.sqrt(a) - np.sqrt(b)) ** 2 / 2

def scan(n, A, B, eps):
    C = sum(C1(a, b, eps) for a, b in zip(A, B))
    Cs = sum(C1(a, a, eps) for a in A) + sum(C1(b, b, eps) for b in B)
    S = C - Cs / 2
    OT = sum(OT1(a, b) for a, b in zip(A, B))
    return abs(S - OT) / n / eps, abs(S - OT) / n / eps**2

rng = np.random.default_rng(0)
print("eps-scan, random heterogeneous profiles in [0.5,1.0]:")
for n in [1, 2, 4, 8, 16, 32, 64]:
    A = rng.uniform(0.5, 1.0, n); B = rng.uniform(0.5, 1.0, n)
    row = []
    for eps in [0.2, 0.1, 0.05, 0.02, 0.01, 0.005]:
        r1, r2 = scan(n, A, B, eps)
        row.append(f"eps={eps}: R1={r1:.5f} R2={r2:.5f}")
    print(f"n={n}: " + " | ".join(row))

print("adversarial alternating endpoints {0.5,1.0}:")
for n in [1, 4, 16, 64]:
    A = np.array([0.5, 1.0] * ((n + 1) // 2))[:n]
    B = 1.5 - A  # swapped endpoints
    row = []
    for eps in [0.1, 0.05, 0.02, 0.01, 0.005]:
        r1, r2 = scan(n, A, B, eps)
        row.append(f"eps={eps}: R1={r1:.5f} R2={r2:.5f}")
    print(f"n={n}: " + " | ".join(row))

print("identical marginals (S must be 0):")
for n in [4, 64]:
    A = rng.uniform(0.5, 1.0, n)
    for eps in [0.1, 0.01]:
        r1, _ = scan(n, A, A, eps)
        print(f"n={n} eps={eps}: R1={r1:.3e}")
