"""Reproducible virtual-dimension check for lane-840 target.

Pair (dP4, smooth E), beta=-K, w=E.beta=4. Log CY (c1_log=0), g=0:
  vdim M_{0,N}(X/D,beta) = (dimX-3)(1-g) + c1_log.beta + N = N-1.
Compares insertion codim vs vdim for minimal readings and the balanced N=4 case.
Stdlib only. Prints ZERO / BALANCED verdicts; asserts expected outcomes.
"""
K2 = 9 - 5  # dP4 = P2 blown up at 5 points
w = K2      # E = -K, E.beta = (-K)^2 = K^2
print(f"dP4 K^2={K2}, w=E.beta={w}")
assert K2 == 4 and w == 4

def vdim(N):
    return N - 1  # g=0 log CY surface

cases = [
    ("reading A: N=1 (psi^1 + pt_X)", 1, 1 + 2),
    ("reading B: N=2 (psi^1 interior + pt_E on E)", 2, 1 + 1),
    ("balanced: N=4 (psi^1 + pt + pt)", 4, 1 + 1 + 1),
]
for label, N, codim in cases:
    v = vdim(N)
    verdict = "ZERO (overconstrained)" if codim > v else ("BALANCED" if codim == v else "POSITIVE-VDIM")
    print(f"{label}: vdim={v} codim={codim} excess={v - codim} => {verdict}")

assert vdim(1) - 3 == -3  # reading A excess
assert vdim(2) - 2 == -1  # reading B excess
assert vdim(4) - 3 == 0   # balanced case
print("VDIM_CHECK_OK")
