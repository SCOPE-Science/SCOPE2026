"""Trace scaling barrier certificate."""
import math
for g in [100, 1000, 10000]:
    R = 0.5*math.log(g)
    mult = g*math.exp(R/2)/R  # multiplicative counting g*e^R
    add = (g+math.exp(R))/R  # additive counting g+e^R
    ident = g/R
    print(f"g={g} R={R:.2f} ident={ident:.1f} add={add:.1f} mult={mult:.1f} mult/ident={mult/ident:.1f}")
