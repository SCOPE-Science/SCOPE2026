"""Exact Griesmer audit for the [36,10,14] problem. stdlib only."""
from math import ceil
import json
import os
HERE = os.path.dirname(os.path.abspath(__file__))

def griesmer(k, d):
    return sum(ceil(d / (1 << i)) for i in range(k))

rows = []
for (k, d) in [(10, 13), (10, 14), (10, 15), (9, 7), (9, 8), (9, 14),
               (7, 14), (7, 15), (8, 14), (9, 13), (10, 12), (26, 3),
               (26, 4), (12, 14), (12, 13)]:
    rows.append({"k": k, "d": d, "G": griesmer(k, d)})

for r in rows:
    print(f"G(k={r['k']:2d}, d={r['d']:2d}) = {r['G']:3d}")
print()
# Key admissibility checks for n=36 and residual length 22
print("G(10,13)=%d <=36 ? %s  -> [36,10,13] Griesmer-admissible" % (griesmer(10,13), griesmer(10,13)<=36))
print("G(10,14)=%d <=36 ? %s  -> [36,10,14] Griesmer-admissible (gap open at Griesmer level)" % (griesmer(10,14), griesmer(10,14)<=36))
print("G(10,15)=%d <=36 ? %s  -> Griesmer does not even rule out d=15" % (griesmer(10,15), griesmer(10,15)<=36))
print("Residual: G(9,7)=%d <=22 ? %s" % (griesmer(9,7), griesmer(9,7)<=22))
print("Residual: G(9,8)=%d <=22 ? %s" % (griesmer(9,8), griesmer(9,8)<=22))
# ceil(d/2) values
print("ceil(14/2)=%d, ceil(15/2)=%d" % (ceil(14/2), ceil(15/2)))
with open(os.path.join(HERE, "griesmer_table.json"), "w") as f:
    json.dump(rows, f, indent=1)
print("wrote griesmer_table.json")
