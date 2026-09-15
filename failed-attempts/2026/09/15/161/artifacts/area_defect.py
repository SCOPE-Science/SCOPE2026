"""Area/defect scan for Tonkonog-Vianna Chekanov-type tori Ta in CP^2.

Least Maslov-2 disk area a; next area A=(1-a)/2 (a+2A=1, line area normalised to 1).
Monotonicity defect class D2-D1: mu=0, area d(a)=A-a=(1-3a)/2.
Monotone iff d(a)=0 iff a=1/3.
Recovery test: d(a)>0 for every a in (1/9,1/3), so monotone exclusion of
Maslov-0 bubbling fails on the whole open interval; only the endpoint a=1/3
is monotone.
"""
import json
import os

def defect(a):
    A = (1 - a) / 2
    return A - a  # (1-3a)/2

grid = [1/9 + k*(1/3 - 1/9)/12 for k in range(13)]
rows = [{"a": a, "A": (1-a)/2, "d": defect(a)} for a in grid]
ok_uniform_obstruction = all(r["d"] > 0 for r in rows if r["a"] < 1/3 - 1e-12)
endpoint = defect(1/3)

out = {
    "grid": rows,
    "d_at_1_9": defect(1/9),
    "d_at_1_3": endpoint,
    "uniform_positive_defect_on_open_interval": ok_uniform_obstruction,
    "conclusion": ("Maslov-0 class of positive area exists for every a in "
                   "(1/9,1/3); monotone compactness holds only at a=1/3."),
}
os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
print(json.dumps(out, indent=2))
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "area_defect_result.json"), "w") as f:
    json.dump(out, f, indent=2)
