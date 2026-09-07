"""Independent verifier: exact-rational 69-pair census of N22=8 witness. No floating point.
Reruns in milliseconds; asserts N22==8 with strict positivity and strict best-response slacks.
Usage: python3 verify_champion.py
"""
from fractions import Fraction
import json, time, sys
sys.path.insert(0, ".")
# inline import to avoid path issues when run from artifacts dir
import importlib.util, pathlib
spec = importlib.util.spec_from_file_location("census", str(pathlib.Path(__file__).parent/"census.py"))
census_mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(census_mod)
census = census_mod.census; count_N22_fast = census_mod.count_N22_fast
A=[[3, 3, 0, 0], [1, 2, 2, 2], [2, 0, 2, 2], [1, 0, 3, 3]]
B=[[2, 2, 1, 3], [0, 2, 3, 0], [2, 0, 3, 0], [1, 1, 0, 2]]
t0=time.time()
eqs=census(A,B)
dt=time.time()-t0
n22=sum(1 for e in eqs if e['k']==2)
print(f"census: {len(eqs)} isolated square-support eqs in {dt*1000:.1f} ms; N22={n22}")
assert n22==8, f"expected 8, got {n22}"
assert len(eqs)==9, len(eqs)
# strict checks re-verified
for e in eqs:
    assert all(v>0 for v in e['x']) and all(v>0 for v in e['y'])
    assert e['detM']!=0 and e['detN']!=0
    assert all(s>0 for s in e['srow'].values()) and all(s>0 for s in e['scol'].values())
    assert isinstance(e['v'], Fraction)
# fast counter agreement
assert count_N22_fast(A,B)==8
# no floats anywhere
import numbers
for e in eqs:
    for v in list(e['x'])+list(e['y'])+[e['v'],e['w'],e['detM'],e['detN']]:
        assert isinstance(v, Fraction), type(v)
print("VERIFY OK: N22=8 certified, all slacks>0, dets!=0, Fraction-only, no float")
