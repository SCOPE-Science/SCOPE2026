# Bounded recovery test: volumes for candidate v0=0 families.
# Family A (product): X = P1xP1, D = two fibres of pr1 (bidegree (2,0)).
# -K = O(2,2). -K-cD = O(2-2c,2). Ample iff c<1. vol = 2*(2-2c)*2 = 8(1-c) -> 0.
# Family B (proportional): X = P2, D = smooth cubic. -K-cD = O(3-3c). vol = (3-3c)^2 = 9(1-c)^2 -> 0.
import numpy as np
for c in [0.0, 0.25, 0.5, 0.75, 0.9, 0.99]:
    vA = 8*(1-c)
    vB = 9*(1-c)**2
    print(f"c={c:.2f}  vA={vA:.4f}  vB={vB:.6f}")
print("v0(A)=0, v0(B)=0; no uniform eps>0 on full [0,1]; uniform eps exists on [0,c0] for any c0<1.")
