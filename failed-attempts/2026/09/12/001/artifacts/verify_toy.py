"""Replayable exact-rational ledger for the toy comparison cap block (s=1/2, q=2).
Compares gradient vs mass integrals on basis {1, u-s} over u in [-1, 1/2],
with rho=1 weight (1-u^2). Proves the toy block is indefinite in full space
but positive on volume-preserving and Killing-orthogonal rays.
DOES NOT prove the true bubble gap: junction terms, true CMC potential,
and interface coupling are absent. Used as recovery-test evidence for CLEAN_EXIT.
Stdlib only (fractions)."""
from fractions import Fraction as F

G00 = F(9,8); M00 = F(9,8)
G11 = F(189,80); M11 = F(243,160)
G01 = F(-45,32); M01 = F(-81,64)
Q00 = G00 - 2*M00; Q11 = G11 - 2*M11; Q01 = G01 - 2*M01
print("Q block:", Q00, Q11, Q01)
print("det(Q) =", Q00*Q11 - Q01*Q01, "(expect -81/160 < 0: indefinite)")
assert Q00*Q11 - Q01*Q01 == F(-81,160)
# volume ray (3/4,1): V0=3/2, V1=-9/8
b0, b1 = F(3,4), F(1,1)
Qv = Q00*b0*b0 + 2*Q01*b0*b1 + Q11*b1*b1
Mv = M00*b0*b0 + 2*M01*b0*b1 + M11*b1*b1
print("vol-ray Q,M,Q/M =", Qv, Mv, float(Qv/Mv), "(expect 1.5)")
assert Qv/Mv == F(3,2)
# killing ray (5/4,1): P0=9/16, P1=-45/64
a0, a1 = F(5,4), F(1,1)
Qk = Q00*a0*a0 + 2*Q01*a0*a1 + Q11*a1*a1
Mk = M00*a0*a0 + 2*M01*a0*a1 + M11*a1*a1
print("killing-ray Q,M,Q/M =", Qk, Mk, float(Qk/Mk), "(expect 3.375=27/8)")
assert Qk/Mk == F(27,8)
# constraint independence
print("constraint det =", F(3,2)*F(-45,64) - F(-9,8)*F(9,16), "(expect -27/64)")
assert F(3,2)*F(-45,64) - F(-9,8)*F(9,16) == F(-27,64)
print("TOY LEDGER REPLAY OK")
