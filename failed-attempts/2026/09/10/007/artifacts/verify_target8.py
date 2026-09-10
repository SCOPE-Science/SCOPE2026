"""Target lemma audit 8 (TARGET phase): ground E(1)/E(1)_{2,3} numerics from scratch.

Proves (exact integer arithmetic, no quotes except log-transform invariance):
 E1. e(CP2)=3, sig(CP2)=+1; e(CPbar)=3, sig=-1 (standard cell data, quoted
     as input cells only).
 E2. Connected-sum rules e(X#Y)=e(X)+e(Y)-2, sig additive (quoted rules) =>
     E(1)=CP2#9CPbar: e=3+9*1=12, sig=1-9=-8 (exact loop below).
 E3. Log transform preserves e,sig (quoted Kodaira/Dolgachev fact) =>
     E(1)_{2,3}: e=12, sig=-8, b2=10, (b2+,b2-)=(1,9), chi_h=1, c1^2=0.
     Simply-connected + odd (homeo CP2#9CPbar by Donaldson/Morgan-Mrowka +
     Freedman, quoted) => Q odd rank-10 det -1 sig -8 (audit1 gram certified).
"""
import json

out = {"tables": {}, "checks": {}}
e_cp2, s_cp2 = 3, 1
e_cpb, s_cpb = 3, -1
e, s = e_cp2, s_cp2
for i in range(9):
    e = e + e_cpb - 2
    s = s + s_cpb
out["tables"]["E1_connected_sum"] = {"e": e, "sig": s}
out["checks"]["E2_E1_12_minus8"] = (e == 12 and s == -8)
b2 = e - 2
bp, bm = (b2 + s)//2, (b2 - s)//2
ch = (s + e)//4
c1 = 3*s + 2*e
out["tables"]["E3_Dolgachev"] = {"e": e, "sig": s, "b2": b2, "b2+": bp,
    "b2-": bm, "chi_h": ch, "c1^2": c1,
    "rule": "log transform preserves e,sig (quoted)"}
out["checks"]["E3"] = (b2 == 10 and bp == 1 and bm == 9 and ch == 1 and c1 == 0)
out["checks"]["target_closed"] = False

with open("output/artifacts/target_audit8.json", "w") as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))
print("ARTIFACT_WROTE output/artifacts/target_audit8.json")
