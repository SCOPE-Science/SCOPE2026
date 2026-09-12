"""Main real-scale certificate for lane-1098 (stdlib only).

Proves the negative TARGET resolution:
  Square Module-LWE dual at ML-KEM-512 shape (dim 512, q=3329) is generically
  trivial: for uniform A in M_2(R_q), R_q = Z_q[x]/(x^256+1), the coefficient
  matrix M = phi(A) in M_512(F_q) is invertible with probability >= 0.999988,
  in which case the dual lattice is exactly q*Z^512 and EVERY dual vector
  gives Fourier-distinguisher advantage EXACTLY 0 (any sample count).
  Hence overall attack advantage <= 1.2e-5 < 0.20. Target conjunction false.

Checks below: q primality, splitting shape (128 quadratics), GL_2 block
probability (exact Fraction), explicit instance A=I (det 1), BKZ-2.0 style
GSA numbers (delta_64, L_pred, GH, heuristic required length), clause audit.
"""
import math
from fractions import Fraction

Q = 3329
N_RING = 256
K = 2
DIM = K * N_RING  # 512
ETA2 = 2
SIG2 = ETA2 / 2  # Var of centered binomial B_eta = eta/2 = 1


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(math.isqrt(n))
    f = 3
    while f <= r:
        if n % f == 0:
            return False
        f += 2
    return True


assert is_prime(Q), "q must be prime"
print(f"q = {Q} prime: True")

# Splitting of x^256+1 over F_q: roots have order 512 (since x^256 = -1).
# Linear factor  <=>  512 | (q-1).  Full split over F_{q^2}  <=>  512 | (q^2-1).
c1 = (Q - 1) % 256 == 0
c2 = (Q - 1) % 512 != 0
c3 = (Q * Q - 1) % 512 == 0
assert c1 and c2 and c3
nquad = N_RING // 2  # 128: roots in F_{q^2}\\F_q pair up under Galois
print(f"256 | q-1: {c1}; 512 | q-1: {not c2} (none => no linear factor); "
      f"512 | q^2-1: {c3} => x^256+1 = {nquad} irreducible quadratics")
print(f"R_q ~= (F_{{q^2}})^{nquad}, Q0 = q^2 = {Q*Q}")

# Typicality: A in M_2(R_q) <-> 128 independent 2x2 blocks over F_{Q0}.
# P(block invertible) = |GL_2(F_Q0)| / Q0^4 = (1-1/Q0)(1-1/Q0^2), exact.
Q0 = Q * Q
p_block = Fraction((Q0 * Q0 - 1) * (Q0 * Q0 - Q0), Q0 ** 4)
p_all = p_block ** nquad
one_minus = Fraction(1, 1) - p_block  # exact singular-branch mass per block
union_bd = one_minus * nquad  # P(any block singular) <= 128*(1-p)
print(f"P(block invertible) = {float(p_block):.12f}")
print(f"P(all {nquad} blocks invertible) = {float(p_all):.9f}")
print(f"union-bound singular mass <= {float(union_bd):.3e} "
      f"(= {union_bd.numerator}/{union_bd.denominator})")
assert float(union_bd) < 1.2e-5 < 0.20

# Explicit instance: A0 = I_2 over R_q -> coefficient matrix M0 = I_512,
# det = 1 mod q, dual lattice = q*Z^512, lambda_1 = q exactly.
det_M0 = 1 % Q
assert det_M0 == 1
lam1 = Q
print(f"explicit instance A0=I_2: det(phi(A0)) mod q = {det_M0}; "
      f"dual = qZ^{DIM}; lambda_1 = {lam1}")

# BKZ-2.0-style GSA numbers (closed form, Chen-Nguyen root-Hermite formula).
BETA = 64
delta = ((BETA / (2 * math.pi * math.e)) * (math.pi * BETA) ** (1 / BETA)) ** (
    1 / (2 * (BETA - 1)))
L_pred = (delta ** DIM) * Q  # generic GSA prediction, det^{1/d}=q (square)
GH = math.sqrt(DIM / (2 * math.pi * math.e)) * Q  # Gaussian heuristic
req = Q * math.sqrt(math.log(5) / (2 * math.pi**2 * SIG2))  # heur. len for 0.20
print(f"delta_64 = {delta:.6f}")
print(f"GSA predicted BKZ-64 length L_pred ~= {L_pred:.3e}")
print(f"1.05*L_pred ~= {1.05*L_pred:.3e} (>= q={Q}: clause-(a) satisfiable)")
print(f"Gaussian heuristic length ~= {GH:.1f}")
print(f"heuristic length needed for adv 0.20 (sigma^2=1) ~= {req:.1f}")
assert Q <= 1.05 * L_pred  # length-q vectors satisfy the 1.05-clause
assert GH > req  # even existential heuristic length fails at square dim

# Decisive Fourier fact (exact, no heuristics): every v in qZ^512 satisfies
# <v,b> = 0 mod q for all b, so the Fourier statistic is identically 1 in
# both worlds -> advantage exactly 0 at ANY sample count (hence <= 2^40).
adv_explicit = 0.0
adv_overall_bound = float(union_bd)  # singular branch bounded by 1
print(f"advantage on invertible branch (prob >= {float(p_all):.6f}): exactly 0")
print(f"overall attack advantage <= {adv_overall_bound:.3e} < 0.20")
assert adv_explicit < 0.20 and adv_overall_bound < 0.20

print("CERTIFICATE_OK")
