"""Recovery test: EMM v2 (2,-(2n+1)) formulas at n=1 vs target cell (tb=-4,rot=1).

Encodes Etnyre-Min-Mukherjee 2206.14848v2 Theorems 1.15 (Legendrian) and 1.17
(transverse) as stated in the HTML rendering, plus Geiges-Onaran Fig5
Lemma 5.5 values. Checks attainability of target invariants.

Run: python3 output/artifacts/recovery_test.py
"""
import json

n = 1
ls = [0]  # {-n+1,...,n-1} step 2 for n=1
target_tb, target_rot = -4, 1
target_sl = target_tb - target_rot  # transverse push-off

results = {"n": n, "target": {"tb": target_tb, "rot": target_rot, "sl": target_sl}}

# Thm 1.15(1): xi_{2n}, rot = -(i-2n+1) / +(i-2n+1)
xi2_rots = set()
for i in [target_tb]:
    xi2_rots.add(-(i - 2*n + 1))
    xi2_rots.add(+(i - 2*n + 1))
# Thm 1.15(3): xi_{n-l}, rot = -(i+2l+1) / +(i+2l+1)
xi1_rots = set()
for l in ls:
    for i in [target_tb]:
        xi1_rots.add(-(i + 2*l + 1))
        xi1_rots.add(+(i + 2*l + 1))

results["emm_xi2_tb-4_rots"] = sorted(xi2_rots)
results["emm_xi1_tb-4_rots"] = sorted(xi1_rots)
results["rot1_in_xi2"] = target_rot in xi2_rots
results["rot1_in_xi1"] = target_rot in xi1_rots

# Thm 1.17: allowed non-loose transverse sl for n=1,l=0
allowed_sl = set()
for l in ls:
    allowed_sl.add(2*l + 1)
    allowed_sl.add(-2*l - 1)
results["emm_allowed_nonloose_sl"] = sorted(allowed_sl)
results["target_sl_nonloose"] = target_sl in allowed_sl

# GO Fig5 m=1: tb=m-5, rot=+/-(m-6)
m = 1
results["go_fig5_m1"] = {"tb": m - 5, "rots": [m - 6, -(m - 6)], "host": "xi_{3/2} GO = xi_2 EMM"}

attainable = results["rot1_in_xi2"] or results["rot1_in_xi1"]
if not attainable and not results["target_sl_nonloose"]:
    results["verdict"] = "TARGET_CELL_ABSENT"
else:
    results["verdict"] = "TARGET_CELL_MAYBE_PRESENT"

print(json.dumps(results, indent=2))
# Assertions encoding the block:
assert not results["rot1_in_xi2"], "unexpected rot=1 in xi_2"
assert not results["rot1_in_xi1"], "unexpected rot=1 in xi_1"
assert not results["target_sl_nonloose"], "unexpected non-loose sl=-5"
assert results["verdict"] == "TARGET_CELL_ABSENT"
print("RECOVERY_TEST_PASS: (tb=-4,rot=1) absent as non-loose; sl=-5 loose-only.")
