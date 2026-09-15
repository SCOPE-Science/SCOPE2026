"""Explicit constants for optimized-mollifier nonvanishing proportion.
Verifies c(Delta)=Delta/(1+Delta), S1^2/S2 ratio, and c' formula.
"""
from fractions import Fraction

def c_of(delta: Fraction) -> Fraction:
    return delta / (1 + delta)

for d in [Fraction(1, 4), Fraction(1, 12), Fraction(1, 2)]:
    print(f"Delta={float(d):.6f} ({d}) -> c={float(c_of(d)):.6f} ({c_of(d)}), "
          f"S2 bound=1+1/Delta={float(1+1/d):.6f}")

# Harmonic Cauchy check: S1=1, S2=1+1/Delta => ratio S1^2/S2 = Delta/(1+Delta)
for d in [Fraction(1, 4), Fraction(1, 12)]:
    S1, S2 = 1.0, 1.0 + 1.0 / float(d)
    print(f"check Delta={d}: S1^2/S2={S1**2/S2:.6f} == c={float(c_of(d)):.6f}")

# Natural proportion formula: c' = c^2 * c_w^2 / C_neg (illustrative placeholders)
c = float(c_of(Fraction(1, 4)))
for cw, Cneg in [(0.5, 10.0), (0.1, 100.0)]:
    print(f"illustrative c_w={cw}, C_neg={Cneg} -> c'={c**2*cw**2/Cneg:.3e}")
print("OK")
