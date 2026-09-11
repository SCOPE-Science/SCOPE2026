"""Scaling obstruction: fixed-cutoff frequency-localized interaction-Morawetz
absorption is incompatible with critical focusing cascade sequences.

Model: L^2-critical rescaling in 3D, phi_N(x) = N^{1/2} phi(N x),
keeps Hdot1 and L^6 invariant while ||.||_4^4 scales as N^{-1}.
Hence (focusing potential ~ L^6^6) / (Morawetz main term ~ L^4^4) ~ N -> inf.
Stdlib + mpmath only.
"""
import mpmath as mp

mp.mp.dps = 30

print("=== Part 1: exact model constants (Gaussian phi) ===")


def C(p, a=1.0):
    return 4 * mp.pi * mp.quad(lambda r: mp.e**(-a * p * r * r / 2) * r * r,
                               [0, mp.inf])


C4 = C(4)
C6 = C(6)
print("C4 = ||phi||_4^4 =", C4)
print("C6 = ||phi||_6^6 =", C6)
ratio = C6 / C4
print("C6/C4 =", ratio)
assert abs(ratio - mp.mpf("0.544331053951817355154952016601")) < mp.mpf("1e-20")
for N in [10, 100, 1000, 1000000]:
    R = N * ratio
    print("N = %8d  potential/main ratio = %.6g  (ledger needs <= 1/8)" % (N, float(R)))
    assert R > mp.mpf("1/8")

print("=== Part 2: general scaling exponents (critical, 3D) ===")
# ||phi_N||_p^p = N^{p/2-3} ||phi||_p^p ; Hdot1 exponent 0.
e4 = mp.mpf(4) / 2 - 3      # -1
e6 = mp.mpf(6) / 2 - 3      # 0
eH = 2 * (mp.mpf(1) / 2 + 1 - mp.mpf(3) / 2)  # gradient L^2 exponent 0
print("L4^4 exponent:", e4, " L6^6 exponent:", e6, " Hdot1 exponent:", eH)
assert e4 == -1 and e6 == 0 and eH == 0
print("=> error/main ~ N^{+1} -> infinity on ANY critical cascade sequence.")

print("=== Part 3: Bernstein direction ===")
# ||P_M f||_6 <= c M^{3(1/4-1/6)} ||f||_4 = c M^{+1/4} ||f||_4 : GROWING.
b = 3 * (mp.mpf(1) / 4 - mp.mpf(1) / 6)
print("Bernstein L4->L6 exponent:", b)
assert b == mp.mpf(1) / 4 and b > 0
print("=> bounding high-frequency L^6 by L^4 costs M^{+1/4},",
      "never gains a small factor; the Draft's N*^{-1} gain was sign-flipped.")

print("SCALING_OBSTRUCTION_CONFIRMED")
