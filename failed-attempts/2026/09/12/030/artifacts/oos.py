"""Out-of-sample check: D(N) envelope at fresh N with FIXED fit constants.

Fixed calibration-window {24,32,48,64} coefficients (hardcoded, no refit):
D(N) = [S(N)-(ah*srN+bh*lnN+ch)] - [U(N)-(a0*srN+b0*lnN+c0)].
Claim envelope: |D(N)| <= 1/sqrt(N). PASS if holds at every fresh N tested.
"""
import math
import numpy as np
from sunset import sums

A0, B0, C0 = (-18.812360300686, -0.324277370273, 25.704864263727)
AH, BH, CH = (-14.440972350558, 1.053826312080, 22.385826578869)
K, BETA = 1.0, 0.5

if __name__ == "__main__":
    import sys
    Ns = [int(a) for a in sys.argv[1:]] or [3, 5, 96]
    ok = True
    for N in Ns:
        U = sums(N, heat=False)
        S = sums(N, heat=True)
        V = U - (A0 * math.sqrt(N) + B0 * math.log(N) + C0)
        P = S - (AH * math.sqrt(N) + BH * math.log(N) + CH)
        D = P - V
        bound = K * N ** (-BETA)
        passed = abs(D) <= bound
        ok &= passed
        print(f"N={N:3d} U={U:+.5f} S={S:+.5f} V={V:+.5f} P={P:+.5f} "
              f"D={D:+.5f} bound={bound:.5f} {'PASS' if passed else 'FAIL'}", flush=True)
    print("OOS_RESULT:", "ALL_PASS" if ok else "FAIL")
