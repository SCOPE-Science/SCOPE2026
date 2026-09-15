"""Recovery test for Hicks Conjecture 3.2.2 literal statement.

Schematic model of Example 3.2.3: the quoted Kasteleyn determinant
Z = 3 - (z1 + z2 + z1*z2) vanishes at (1,1); flipping all matching
signs (as the unsigned Definition 3.2.1 would suggest) gives
Z2 = 3 + (z1 + z2 + z1*z2) = 6 at (1,1). Hence the predicted Floer
support {Z = 0} depends entirely on sign data omitted from Def 3.2.1,
so mu^1 = d_nabla is ill-posed as literally stated.
Run: python3 output/artifacts/sign_check.py
"""
import sympy as sp

z1, z2 = sp.symbols('z1 z2')
Z = 3 - (z1 + z2 + z1 * z2)   # as quoted in Hicks Example 3.2.3
Z2 = 3 + (z1 + z2 + z1 * z2)  # unsigned/sign-flipped variant

for label, Zfun in (("Z", Z), ("Z2", Zfun if False else Z2)):
    print(label, "= ", Zfun)
print("Z(1,1)  =", Z.subs({z1: 1, z2: 1}))
print("Z(-1,-1)=", Z.subs({z1: -1, z2: -1}))
print("Z2(1,1) =", Z2.subs({z1: 1, z2: 1}))
assert Z.subs({z1: 1, z2: 1}) == 0
assert Z2.subs({z1: 1, z2: 1}) == 6
print("OK: sign data moves the predicted support; literal unsigned claim ill-posed.")
