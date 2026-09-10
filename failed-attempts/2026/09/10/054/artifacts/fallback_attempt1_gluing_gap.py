"""Fallback Attempt 1: quantitative gap for crude explicit routes to I(f128)>=8.

Models what FKG-gluing and generic Boolean bounds can honestly yield, vs 8.
- Gluing model: square-crossing floor c0; 2:1 RSW rectangle floor ~ c0^m;
  per-block pivotal floor ~ c0^K (K = number of glued arm events; a genuine
  pivotal needs >=4 arms + connections, so honest K>=6); total >= N*c0^K.
- KKL generic floor: Var*log(n)/(C*n) with n = #edges.
Stdlib only.
"""
import math

E = 257 * 128 + 256 * 129  # edges of 256x128 box
print(f"edges n = {E}, log n = {math.log(E):.3f}")

print("\n== FKG-gluing table: total >= N_blocks * c0^K ==")
for c0 in (0.5, 0.6, 0.75):
    for K in (4, 6, 8, 10, 15, 20):
        for N in (8, 32):
            tot = N * (c0 ** K)
            flag = "PASS8" if tot >= 8 else "fail"
            print(f"c0={c0} K={K:2d} N={N:2d} -> {tot:.2e}  {flag}")

print("\n== KKL generic floor ==")
n = E
for C in (1, 9):
    print(f"C={C}: Var*log(n)/(C*n) = {0.25 * math.log(n) / (C * n):.2e}  (fail vs 8)")

print("\nCONCLUSION: honest gluing (K>=6, c0<=0.75, N<=32) yields <= "
      f"{32 * 0.75**6:.2e} << 8; reaching 8 needs K<=3 with large c0, "
      "incompatible with a 4-arm pivotal event. Generic KKL ~1e-6. "
      "Crude-explicit route CANNOT reach 8; sharp arm/RSW constants needed.")
