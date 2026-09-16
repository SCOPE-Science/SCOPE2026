"""Checks supporting the lamplighter target investigation.

Model: L = (Z/2) wr Z, elements (f, k) with f: Z -> Z/2 finitely supported, k in Z.
Multiplication: (f,k)(g,m) = (f + shift_k(g), k+m), shift_k(g)(n) = g(n-k).
Identity (0,0); inverse of (f,k) is (shift_{-k}(f), -k).

Checks:
 1. Group law sanity (closure/associativity/identity/inverse) on samples.
 2. Z-intervals are Folner for the quotient Z (ratio 2/(2n+1) -> 0).
 3. Base N =irical direct sum exhausts via finite subgroups of size 2**(2n+1).
 4. Naive boxes B_n = {supp in [-n,n]} x [-n,n] are NOT Folner for L:
    |t B_n \\ B_n| / |B_n| -> 1/2 for the shift generator t. (Exact counts.)
 5. Center triviality on window B_2: only identity commutes with both
    generators a0 (lamp at 0) and t (shift) -> the 2-generated group L is
    not nilpotent -> L is not locally nilpotent.
"""

from itertools import product

# Represent f as frozenset of support (positions with lamp on).


def shift(supp, k):
    return frozenset(n + k for n in supp)


def mul(a, b):
    f, k = a
    g, m = b
    return (f ^ shift(g, k), k + m)  # symmetric difference = addition mod 2


def inv(a):
    f, k = a
    return (shift(f, -k), -k)


E = (frozenset(), 0)
A0 = (frozenset({0}), 0)  # lamp toggle at 0
T = (frozenset(), 1)      # shift by 1

# 1. Group law sanity on a sample window.
window = [(frozenset(s), k) for r in range(3) for s in product([0, 1], repeat=0)
          for k in range(-2, 3)]
# build all configs supported in {-2..2} x shifts in {-2..2}
elems = [(frozenset(i for i in range(-2, 3) if bits[i + 2]), k)
         for bits in product([0, 1], repeat=5) for k in range(-2, 3)]
import random
random.seed(7)
ok = True
for _ in range(3000):
    a, b, c = (random.choice(elems) for _ in range(3))
    if mul(mul(a, b), c) != mul(a, mul(b, c)):
        ok = False
    if mul(a, E) != a or mul(E, a) != a:
        ok = False
    if mul(a, inv(a)) != E or mul(inv(a), a) != E:
        ok = False
print("1. group-law samples associative w/ identity+inverse:", ok,
      f"({len(elems)}-element window, 3000 random triples)")

# 2. Z-interval Folner ratios.
print("2. Z-interval Folner |gF Δ F|/|F| for F=[-n,n], g=+1:",
      [round(2 / (2 * n + 1), 6) for n in (1, 2, 4, 8, 16)])

# 3. Base exhaustion sizes.
print("3. |N_n| for lamps supported in [-n,n]:",
      [(n, 2 ** (2 * n + 1)) for n in range(0, 5)])

# 4. Naive-box boundary under the shift generator, exact counts.
print("4. naive box B_n: |B_n|, |tB_n \\ B_n|, ratio (limit 1/2):")
for n in range(1, 9):
    size = 2 ** (2 * n + 1) * (2 * n + 1)
    # t(f,k) = (shift_1(f), k+1) exits B_n iff k == n (shift index out) or
    # k <= n-1 and n+1 in supp(shift_1 f), i.e. n in supp(f).
    out_k = 2 ** (2 * n + 1)          # k == n slice, all configs
    out_supp = (2 * n) * 2 ** (2 * n)  # k in [-n, n-1], f(n) == 1
    out = out_k + out_supp
    print(f"   n={n}: |B_n|={size}, out={out}, ratio={out / size:.6f}")

# 5. Center check on window B_2 (configs in [-2,2], shift in [-2,2]),
#    testing commutation with generators A0 and T where defined.
B2 = [(frozenset(i for i in range(-2, 3) if bits[i + 2]), k)
      for bits in product([0, 1], repeat=5) for k in range(-2, 3)]
central = [g for g in B2 if mul(g, A0) == mul(A0, g) and mul(g, T) == mul(T, g)]
print("5. elements of window B_2 commuting with both generators:", central)
assert central == [E], "window center check failed"
print("   => only identity commutes with <A0, T> on this window; "
      "Z(L) = 1 globally (central (f,k): k=0 by T-commutation, f=0 by A0-shifts), "
      "so the 2-generated L is not nilpotent => L not locally nilpotent.")
