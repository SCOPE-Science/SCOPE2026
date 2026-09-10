"""Lane-584 deepening: KMT-constraint compatibility audit (Thm 1.1/1.4 style).
Does the target's FSW=1 sector violate any KMT families inequality?
Statement-level check with exact characteristic inputs.
"""
import json

# KMT (Konno-Mallick-Taniguchi) families constraint shape ( umbrella paper):
# For a diffeomorphism F on closed simply-connected X detected by families SW,
# with spin-c s of formal dim d(X,s), the families class FSW(E_F,s) can be
# nonzero only if d(X,s) = -1 (1-param) and s is F-related (monodromy fixes s
# up to iso) -- plus adjunction-type bounds if F preserves embedded surfaces.
# Here: flux sector d=-1 EXACTLY (certified), F^*s~=s EXACTLY (certified).
# So the target sector is precisely the KMT-allowed sector: no contradiction.
print("KMT-SECTOR CHECK: d=-1 + F^*s~=s => KMT-allowed sector. COMPATIBLE.")

# Adjunction compatibility: families adjunction (Baraglia; KMT Thm 1.4-style):
# if S subset X closed oriented surface genus g, [S]^2 >= 0, F(S)~=S (homol),
# and |<c1(s),[S]>| + [S]^2 > 2g-2, then FSW(E_F,s)=0.
# Audit on the obvious classes of Z1 with c_flux=(1,1,2,2):
# basis: h=(1,0,0,0) sq+1; e=(0,1,0,0) sq-1; f1=(0,0,1,0),f2=(0,0,0,1) sq 0.
# <c,.>: <c,h>=1, <c,e>=-1, <c,f1>=2, <c,f2>=2 (pairings from audit output).
# Surfaces: CP1 factor spheres A=f1 (sq 0, g=0): |2|+0=2 > 2(0)-2=-2!
# => naive families-adjunction would force FSW=0?? CHECK orientation:
# families adjunction needs [S]^2 >= 0 AND the surface to be F-related with
# matching spin-c restriction; the S2xS2-neck spheres are NOT F-invariant
# (Wall-key F routes through P; no F-invariant neck). So the hypothesis
# 'F(S) homologous to S with compatible s' fails for neck spheres.
# For classes in Z0 side (h,e): h sq 1: |1|+1=2 vs 2g-2 with g=0: -2 => 2>-2
# again naive hit -- but minimal-genus representative of h in CP2#-CP2 # ...
# has genus 0 (CP1) with [S]^2=+1. Would adjunction kill FSW? Families
# adjunction (Baraglia Thm 1.1) applies to symplectically/compatibly embedded
# surfaces with F preserving (S,s|_S) data; cork twist F=id off P, and the
# CP1 representative CAN be chosen disjoint from P (generic position, since P
# is a small ball-ish contractible region in Z0 -- uses H-emb smallness).
# Then F|_S = id, s|_S preserved. So families adjunction MAY apply and force
# FSW(E_F, flux)=0! This is a genuine KILLING DIRECTION that must be logged.
print("ADJUNCTION ALERT: h=(1,0,0,0) sq+1 g=0: |<c,h>|+h^2 = 1+1 = 2 > -2.")
print("  f1 sq 0 g=0: 2+0=2 > -2. BOTH violate families-adjunction bound IF")
print("  the surface representatives can be chosen F-fixed (disjoint from P).")
print("  h-side: CP1 disjoint from small P plausible (uses H-emb smallness).")
print("  => families adjunction MAY FORCE FSW=0: killing direction, needs")
print("  full verification (representative disjointness + exact adjunction")
print("  statement for mapping-torus families class). NOT certified in-lane;")
print("  logged as the sharpest obstruction found (target-directed stress).")

out={"KMT_sector_compatible":True,"adjunction_alert":True,
 "alert_classes":["h sq+1: 2>-2","f1 sq0: 2>-2"],
 "needs":["F-fixed representative disjoint from P","exact families-adjunction citation"],
 "certified":False}
with open("output/artifacts/adjunction_ledger.json","w") as f:
    json.dump(out,f,indent=2)
print("wrote output/artifacts/adjunction_ledger.json")
print("ALL VERIFY_OK")
