"""Exact integer arithmetic for the slot-count transfer matrix M3.

States = slot counts {1,2,3}. M3[i][j] = # insertion letters taking i -> j
(l/r stay, m +1, f -1; m from 3 exits the slice and is dropped for the
superset walk count).
"""
from fractions import Fraction

M = [[2, 1, 0],
     [2, 4, 2],
     [0, 3, 6]]

# Row sums
rowsums = [sum(r) for r in M]
print("M3 =", M)
print("row sums =", rowsums, "max =", max(rowsums))

# Characteristic polynomial of M3: det(M - xI) computed symbolically.
# |2-x, 1, 0; 2, 4-x, 2; 0, 3, 6-x|
# = (2-x)*((4-x)(6-x)-6) - 1*(2*(6-x)-0) + 0
# (4-x)(6-x) = x^2 -10x +24; minus 6 -> x^2-10x+18.
# So p(x) = -x^3 +12x^2 -36x +24, i.e. monic q(x)=x^3-12x^2+36x-24.
def q(x):
    return x**3 - 12*x**2 + 36*x - 24

for x in [0, 1, 2, 3, 6, 7, 8, 9, 12]:
    print(f"q({x}) = {q(x)}")

assert q(7) == -17, q(7)
assert q(8) == 8, q(8)
assert q(9) == 57, q(9)
assert q(12) == 12**3 - 12*144 + 36*12 - 24
print("q(12) =", q(12))
assert q(7) < 0 < q(8)  # IVT root in (7,8)

# q'(x) = 3x^2-24x+36 = 3(x-2)(x-6); increasing on [6,inf)
def qp(x):
    return 3*x**2 - 24*x + 36
assert qp(8) > 0
# q(8)=8>0 and increasing afterwards -> no root >= 8 (checked symbolically:
# qp>0 on [8,inf) since both factors positive).
print("IVT enclosure of simple root in (7,8): OK")
print("Row-sum Perron cap: rho(M3) <= 9 <= 12: OK")

# Walk-count growth bound replay: v0=e1, v_{k+1}=v_k M; ||v||_1 growth <=9.
def matvec(v, A):
    n = len(v)
    return [sum(v[i]*A[i][j] for i in range(n)) for j in range(n)]

v = [1, 0, 0]
for k in range(6):
    print(k, v, sum(v))
    v = matvec(v, M)
print("dominant ratio v5/v4 sums:", sum(v)/sum(matvec([1,0,0],M)) if False else "")

# Submatrix {1,2} spectral radius = 3+sqrt(3) < 4.74 < 6 <= rho driver at state 3.
import math
print("3+sqrt(3) =", 3 + math.sqrt(3))
print("ALL CHECKS PASSED")
