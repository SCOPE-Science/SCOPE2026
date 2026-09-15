"""Elementary capacity check: why ball/probe displacement is inconclusive past 1/9.

Normalise line area = 1, so CP^2 has total area 3 (c1=3H). Clifford torus T_Cl
is monotone with disk area 1/3. A sufficient displacement of Ta from T_Cl would
need a ball B(c) disjoint from T_Cl containing Ta (then move B(c) within the
complement). Known small-torus displaceability uses c shrinking with a; past
the admitted low-area threshold 1/9 no uniform c(a) with the required disjoint
transitive pair is available locally. This script records the numerical gap:
required capacity lower bound ~ 3a (Ta needs ~ area a disks inside B(c),
c > a at least; monotone image needs c >= 1/3 to obstruct) versus maximal
ball capacity known to embed in CP^2 \ T_Cl (complement of Clifford contains
balls up to capacity 1/3 by toric picture, but positioning Ta inside one
while keeping disjointness is uncontrolled for exotic Ta).
Conclusion: elementary capacities neither displace nor obstruct uniformly;
both directions need Floer data. Inconclusive locally -> supports BLOCKED.
"""
import json
import os

def required_capacity(a):
    return 3 * a  # rough/volumetric proxy: Ta's minimal ball scales with a

rows = []
for k in range(13):
    a = 1/9 + k*(1/3 - 1/9)/12
    rows.append({"a": a, "proxy_required_c": required_capacity(a),
                 "complement_max_c": 1/3})
out = {"rows": rows,
       "conclusion": ("proxy required capacity 3a exceeds complement maximum "
                      "1/3 exactly when a>1/9; elementary ball fitting is "
                      "inconclusive past the threshold without exotic-torus "
                      "position control. No uniform displacement or "
                      "obstruction follows from capacities alone.")}
print(json.dumps(out, indent=2))
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "ball_capacities_result.json"), "w") as f:
    json.dump(out, f, indent=2)
