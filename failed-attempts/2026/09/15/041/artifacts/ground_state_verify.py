"""Symbolic verification of the closed-form INLS ground state.

Ansatz W(r) = (1 + r^s)^{-beta}, s = 2-b, beta = (d-2)/s.
Claim: ΔW + (d-b)(d-2) r^{-b} W^{alpha+1} = 0, alpha = (4-2b)/(d-2).
Hence with amplitude C^alpha = (d-b)(d-2) one gets ΔW + r^{-b}W^{alpha+1} = 0.
"""
import sympy as sp

# 1) General-parameter check: ratio ΔW / (r^{-b} W^{alpha+1}) should be constant.
r, d, b = sp.symbols('r d b', positive=True)
s = 2 - b
beta = (d - 2) / s
alpha = (4 - 2 * b) / (d - 2)
W = (1 + r**s)**(-beta)
Wp = sp.diff(W, r)
Wpp = sp.diff(Wp, r)
DeltaW = Wpp + (d - 1) / r * Wp
ratio = sp.simplify(DeltaW / (r**(-b) * W**(alpha + 1)))
print("general ratio ΔW / (r^-b W^{α+1}) =", ratio)
print("expected constant -(d-b)(d-2) =", sp.expand(-(d - b) * (d - 2)))
print("difference:", sp.simplify(ratio + (d - b) * (d - 2)))

# 2) Concrete instance d=6, b=1: W = 400 (1+r)^{-4}, check ΔW + r^{-1} W^{3/2} = 0.
r1 = sp.symbols('r1', positive=True)
W61 = 400 * (1 + r1)**(-4)
res = sp.simplify(sp.diff(W61, r1, 2) + 5 / r1 * sp.diff(W61, r1)
                  + r1**(-1) * W61**sp.Rational(3, 2))
print("d=6,b=1 residual ΔW + r^-1 W^{3/2} =", res)

# 3) Pohozaev identity K = P constants: E(W) = ((2-b)/(2(d-b))) K.
print("E(W)/K =", sp.Rational(1, 2) - (d - 2) / (2 * (d - b)),
      " simplified:", sp.simplify(sp.Rational(1, 2) - (d - 2) / (2 * (d - b))))
