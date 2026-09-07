"""Johnson + canonical-orbit recomputation (stdlib only).
- Universe C(16,7)=11440.
- Conflict degree 819 (+1 self =820): C(7,5)C(9,2)+C(7,6)C(9,1)+C(7,7)C(9,0).
- Canonical c1 fix: orbit sizes C(7,t)C(9,7-t) for t=0..7; compatible t=0..4 sum 10620.
- Johnson upper 122 = floor(16/9 * 69) conditional on A(15,6,7)=69 (Ostergard, cited, not reproved).
Usage: python3 verify_johnson.py
"""
from math import comb

assert comb(16, 7) == 11440
print("C(16,7)=11440 OK")
deg = comb(7, 5)*comb(9, 2)+comb(7, 6)*comb(9, 1)+comb(7, 7)*comb(9, 0)
assert deg == 820, deg
print(f"closed neighbourhood size 820 (degree 819) OK: 21*36+7*9+1={deg}")
orbits = {t: comb(7, t)*comb(9, 7-t) for t in range(8)}
print("c2 orbits vs fixed c1:", orbits)
assert sum(orbits[t] for t in range(5)) == 10620
assert sum(orbits.values()) == 11440
print("compatible (t<=4) 10620 + conflicting 820 = 11440 OK")
A15 = 69
J = (16*A15)//9
assert J == 122
print(f"Johnson floor(16/9*{A15})={J} OK (conditional on A(15,6,7)=69)")
print(f"avg point-degree for M=122: {122*7/16}; M=121: {121*7/16}; M=109: {109*7/16}")
print("JOHNSON+CANONICAL COUNTS VERIFIED")
