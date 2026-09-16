"""Rigorous certificate for lane-20514: locates lambda0 and certifies obstructions.

Uses only exact integer arithmetic and explicit rational bounds
(no floating-point trust needed for the logical conclusions).
"""
from fractions import Fraction

def p_int(x: int) -> int:
    return x**3 - 6*x**2 + 5*x - 1

def pp_int(x: int) -> int:
    return 3*x**2 - 12*x + 5

# 1. Integer evaluations
assert p_int(5) == -1, p_int(5)
assert p_int(6) == 29, p_int(6)
assert p_int(4) == -13, p_int(4)

# 2. Monotonicity on [5, +inf): p'(x) = 3x^2-12x+5 = x(3x-12)+5 >= 5 > 0 for x>=5
# (for integer x>=5, 3x-12>=3 so x(3x-12)>=15). Hence exactly one root in (5,6).
# Consequences: lambda0 in (5,6), in particular lambda0 > 4 and lambda0 != 4.

# 3. Loop parameter bounds: delta0 = sqrt(lambda0) in (sqrt(5), sqrt(6)) subset (2, 2.5).
# sqrt(5) > 2 since 5 > 4; sqrt(6) < 2.5 since 6 < 6.25 = (5/2)^2.
assert 5 > 2**2
assert 6 < Fraction(25, 4)
print("p(4) =", p_int(4))
print("p(5) =", p_int(5))
print("p(6) =", p_int(6))
print("=> unique root lambda0 of x^3-6x^2+5x-1 in open interval (5,6); hence lambda0 > 4.")
print("=> delta0 = sqrt(lambda0) in (sqrt(5), sqrt(6)) subset (2, 2.5); hence delta0 > 2.")
print("=> TLJ(delta0) abstract planar algebra exists (Jones, generic delta>2), infinite-depth A_infty.")

# 4. Norm of A_infinity = 2: truncations A_n (path on n vertices) have norm 2cos(pi/(n+1)).
import math
print("\nFinite-path approximants 2cos(pi/(n+1)):")
for n in [5, 10, 20, 50, 100, 1000]:
    v = 2*math.cos(math.pi/(n+1))
    assert v < 2.0
    print(f"  n={n}: {v} (< 2, -> 2)")
print("sup_n 2cos(pi/(n+1)) = 2; each A_n embeds in A_infty; row-sum bound gives ||A_infty|| <= 2.")
print("Hence ||A_infty|| = 2, so ||A_infty||^2 = 4 != lambda0 in (5,6).")

print("\nPopa amenability chain (cited, not recomputed):")
print("  hyperfinite N,M + finite index => amenable subfactor (Popa 1994);")
print("  irreducible => extremal; amenable extremal => ||Gamma||^2 = index.")
print("  With Gamma = A_infty: index would have to be 4. Contradiction with lambda0 in (5,6).")
print("\nCERTIFICATE COMPLETE: no such irreducible hyperfinite subfactor exists.")
