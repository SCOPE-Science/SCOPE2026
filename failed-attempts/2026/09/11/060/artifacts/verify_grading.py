"""Replay: LOSS Alexander-grading collapse at (tb,rot)=(7,0) for T(2,3).

Checks:
  A = (tb - rot + 1)/2 = 4
  HFK support for genus-1 T(2,3): |A| <= 1, so group in grading 4 is 0.
  Hence LOSS (minus and hat) vanishes identically; no distinguished pair.
"""
from fractions import Fraction

tb, rot = 7, 0
A = Fraction(tb - rot + 1, 2)
print(f"tb={tb} rot={rot} -> A(LOSS) = (tb-rot+1)/2 = {A}")
assert A == 4, A

# Parity check: tb+rot odd for null-homologous Legendrian knots
assert (tb + rot) % 2 == 1, "parity violated"
print("parity tb+rot odd: OK")

# HFK support bound: genus g(T(2,3)) = 1; HFK(S^3,K,A)=0 for |A|>g.
g = 1
# Published hat-HFK table for right-handed trefoil (Ozsvath-Szabo):
# rank 1 in each of A in {-1,0,1}, 0 elsewhere.
hfk_hat_table = {-1: 1, 0: 1, 1: 1}
assert int(A) not in hfk_hat_table, "unexpected support"
print(f"genus g={g}; HFK-hat table {hfk_hat_table}; A={int(A)} outside support: OK")
print(f"HFK^(-)/(-S^3,T(2,3)) in Alexander grading {int(A)} is the zero group.")

# Conclusion
print("CONCLUSION: LOSS(L)=0 and hat-LOSS(L)=0 for every Legendrian T(2,3) with (7,0).")
print("No pair L1,L2 at (7,0) satisfies LOSS(L1)!=LOSS(L2). LOSS-gap half IMPOSSIBLE.")
print("VERIFY_OK")
