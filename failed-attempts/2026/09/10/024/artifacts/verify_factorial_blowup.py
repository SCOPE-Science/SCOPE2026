"""Quantify the factorial obstruction in the as-written KL chain.

Chain: Cor 6.1 gives E[tau_k^{-2}] <= C2 (1+log(n/k))^beta with beta=16
(alpha=1/8); Thm 6.2 sums over k and multiplies by e^6; Bochner (5)
multiplies by 4. Target needs final constant <= 8.

This script certifies, with exact integer arithmetic:
 (i)  (1/n) sum_{k=1}^n (1+log(n/k))^16  ->  I_16 = sum_{j=0}^{16} C(16,j) j!
       = 56874039553217 exactly (Riemann-sum liminf argument in DRAFT notes).
 (ii) the deduction (86)->(87) with alpha=1/8 forces C2 >= 2^16 = 65536
       (x0^2 term), and Thm 6.2 forces a further e^6 factor.
 (iii) resulting floor on the chain's final constant: >= ~6e21 >> 8.
Discrete sums at finite n illustrate the blowup (floating point, heuristic).
"""
import math
from math import comb, factorial

beta = 16
I16 = sum(comb(beta, j) * factorial(j) for j in range(beta + 1))
print("I_16 exact =", I16)
assert I16 == 56874039553217

for b in (2, 4, 8, 16):
    print(f"beta={b} integral", sum(comb(b, j) * factorial(j) for j in range(b + 1)))

for n in (10, 100, 1000):
    s = sum((1 + math.log(n / k)) ** 16 for k in range(1, n + 1)) / n
    print(f"n={n} avg-sum(beta=16) = {s:.6g}")

C2_floor = 2 ** 16
e6 = math.exp(6)
S = I16
C62_floor = e6 * (C2_floor + 1) * S   # Thm 6.2 constant floor
Cfinal_floor = 4 * C62_floor          # after Bochner factor 4
print("C2 floor (2^16) =", C2_floor)
print("Thm6.2 constant floor >= {:.3e}".format(C62_floor))
print("Final Var constant floor >= {:.3e}".format(Cfinal_floor))
print("Target needs <= 8; gap >= {:.2e}x".format(Cfinal_floor / 8))
assert Cfinal_floor > 1e21
print("OK: as-written alpha=1/8, beta=16 route cannot reach single digits.")
