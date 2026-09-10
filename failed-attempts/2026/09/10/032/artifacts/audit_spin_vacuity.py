"""Lane-584 step 3: non-spin certificate => Pin(2)-BF vacuity; S1-BF dimension;
wall-crossing integer template. Exact arithmetic + statement-level theorems.
"""
import json

# Q1 = diag(1,-1) (+) H is ODD (Q(e1,e1)=1) => w2(Z1) != 0 (Wu: w2 pairs as
# diagonal mod 2) => Z1 non-spin. Exact: characteristic vector (1,1,0,0) is not
# divisible by 2; equivalently no spin structure since form odd.
Q1=[[1,0,0,0],[0,-1,0,0],[0,0,0,1],[0,0,1,0]]
assert Q1[0][0]%2==1
print("NON-SPIN: Q1 odd (e1^2=+1) => w2(Z1)!=0 => Z1 admits NO spin structure.")

# Consequence: Pin(2)-equivariant family Bauer-Furuta (which requires a fiberwise
# spin structure, Lin-Mukherjee setting: S2xS2 spin) is UNDEFINED on E_F.
# The target's 'S1/Pin(2) ... where defined' therefore collapses: only the
# S1-equivariant (spin-c) family BF can be defined. The Pin(2) prong is vacuous.
print("PIN2-VACUITY LEMMA: Pin(2)-family BF undefined on non-spin Z1; target's "
      "BF prong reduces to S1-equivariant (spin-c) BF only. (Statement level: "
      "Pin(2) BF needs spin per LM; Wu formula gives w2!=0.)")

# S1-BF dimension ledger (flux sector): ordinary d=-1, families exp-dim d+1=0 =>
# S1-BF is a stable class in stem 0 (degree 0), whose Hurewicz image is the
# integer FSW count; S1-BF nontrivial => FSW!=0 mod 2 (contrapositive: FSW=0 in
# PSC chamber does NOT imply S1-BF trivial globally -- chamber dependence).
print("S1-BF DIMENSION: flux sector families exp-dim 0 => stem-0 stable class; "
      "S1-BF nontriviality implies FSW!=0 in that chamber (statement level).")

# Wall-crossing integer template (exact pairing inputs):
# c_flux=(1,1,2,2): decompose c = c0 + c_H with c0=(1,1) on Q0 (c0^2=0),
# c_H=(2,2) on H (c_H^2=2*2*2=8). Any wall-crossing jump J for a single
# transverse crossing is +/-1 (signed reducible count); FSW(C_far)=J.
# The sign depends on crossing orientation; magnitude 1 IFF the metric path
# meets the c1^+-wall transversely exactly once. No such path exhibited in-lane.
c0_sq = 1*1 - 1*1
cH_sq = 2*2*2
print(f"c0^2={c0_sq}, cH^2={cH_sq}, total={c0_sq+cH_sq} (need 8).")
assert c0_sq+cH_sq==8
print("WC-INTEGER: single transverse crossing contributes +/-1; "
      "multi-crossing or non-transverse path gives arbitrary integer; "
      "J=+-1 unproved without explicit path.")

# Honest binary status:
print("BINARY STATUS: survival (FSW=1) NOT proved; killing isotopy NOT found; "
      "PSC chamber gives FSW=0 locally; far-chamber value = J (uncomputed).")

out={"non_spin":True,"Pin2_BF_defined":False,"S1_BF_stem":0,
 "c0_sq":c0_sq,"cH_sq":cH_sq,"J_status":"uncomputed"}
with open("output/artifacts/spin_vacuity_ledger.json","w") as f:
    json.dump(out,f,indent=2)
print("wrote output/artifacts/spin_vacuity_ledger.json")
print("ALL VERIFY_OK")
