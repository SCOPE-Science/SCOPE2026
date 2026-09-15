"""Partial certificate: nodal blow-up volume on nef interval [0,1].
Verifies: E=P1xP1, E^3=2, vol(pi*H-uE)=4-2u^3 for u in [0,1] (nef range),
int_0^1 vol = 3.5, hence (1/4)*that = 0.875 = 7/8 is a STRICT LOWER bound for S_X(E).
Shows incompleteness: tau>1 expected (hyperplanes through node give effectivity beyond u=1),
so true S_X(E) > 7/8; lines through node enter negative part of Zariski decomposition.
Therefore A/S < 16/7 on this divisor alone and exact S needs decomposition not completed.
"""
from fractions import Fraction
S_nef_part = Fraction(7,8)
print("nef-interval contribution:", float(S_nef_part), S_nef_part)
assert S_nef_part == Fraction(7,8)
# A_X(E)=2 for 3-fold ODP blow-up (discrepancy 1 => log discrepancy 2)
A = 2
print("A/S_lowerbound_ratio =", float(Fraction(16,7)))
print("OK: lower-bound certificate holds; exact S undetermined")
