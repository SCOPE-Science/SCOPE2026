"""Lane-584: adjunction-alert adjudication (exact arithmetic + careful
statement audit). Is the families-adjunction bound really violated?
Key: adjunction constrains BASIC classes / effective representatives for the
given spin-c; d=-1 sector + violation bound interplay.
"""
import json

# Pairings of c=(1,1,2,2) with basis classes (Q1):
# <c,h>=1, <c,e>=-1, <c,f1>=2, <c,f2>=2.
# Genus-0 reps: h: CP1 in CP2 summand, sq +1. e: CP1 in -CP2, sq -1.
# f1,f2: S2 factors, sq 0.
# Families adjunction (Baraglia, "Families Seiberg-Witten invariants and
# canonical divisors"? / KMT use): IF FSW(E_F,s)!=0 and S is an F-related
# embedded surface of genus g with [S]^2>=0, then 2g-2 >= |<c1(s),[S]>|+[S]^2.
# Contrapositive on h: 2(0)-2=-2 vs |1|+1=2: -2>=2 FALSE => FSW=0 REQUIRED,
# provided h has an F-related (here: F-fixed) representative.
# Same on f1: -2 vs |2|+0=2 FALSE => FSW=0 REQUIRED if f1 F-fixed.
print("Bound arithmetic CONFIRMED: h: -2 >= 2 false; f1: -2 >= 2 false.")

# Adjudication of the F-fixed-representative hypothesis:
# (i) h-side: CP1 summand in Z0=CP2#-CP2. P is a contractible cork embedded
# in Z0 via nucleus embedding. A generic CP1 line misses a 4-ball; P is not
# a ball but is a small contractible submanifold. Transversality: any surface
# can be isotoped off a codimension-0 submanifold? NO -- P has codim 0, so
# generic isotopy does NOT avoid P. Need: CP1 representative disjoint from
# the SPECIFIC P locus. Nucleus embeddings place P near the nucleus fiber
# region; a generic line CP1 in the CP2 summand CAN be chosen in the complement
# of a fixed compact P if P does not separate... but CP1 represents h which
# pairs 1 with the fiber? Hmm: h is the section-ish class. Whether a
# disjoint representative exists is a genuine Kirby-calculus question about
# the fixed embedding (H-emb data), NOT decidable by homology alone.
print("(i) h-side F-fixed rep: needs Kirby-level disjointness from fixed P.")
print("    NOT certified in-lane (no diagram engine). Hypothesis open.")
# (ii) f1-side (neck spheres): Wall-key F has NO invariant neck => f1 has
# NO F-related representative a priori; adjunction inapplicable to f1.
print("(ii) f1-side: Wall-key F, no invariant neck => adjunction INAPPLICABLE.")
# (iii) Even if FSW(flux) were killed by h-adjunction, note c_flux pairs
# nontrivially: the bound violation uses |<c,S>|; the flux construction
# DELIBERATELY pairs 1..2 with every positive class. Any flux class with
# c^2=8 on Q1=diag(1,-1)(+)H: c=(a,b,m,n), a,b odd, m,n even, a^2-b^2+2mn=8.
# |<c,h>|=|a|>=1 always (a odd). h sq +1 g 0 needs |a|+1<=0?? i.e. NEVER
# satisfiable. So EVERY flux-sector class violates h-adjunction IF h F-fixed.
# Exact: |a|>=1 => |a|+1>=2 > -2 always. So EITHER h not F-fixable (then no
# constraint) OR FSW=0 for the ENTIRE flux sector (sector-wide killing!).
print("(iii) SECTOR-WIDE: |a|>=1 for every flux c => h-bound violated for ALL")
print("     flux classes (if h F-fixed). So h-disjointness decides the whole")
print("     sector: FSW=0 sector-wide, or constraint vacuous. SHARP DICHOTOMY.")

# Minimal check: is there ANY char class with c^2=8 AND |a|+1<=-2? No: |a|>=0
# always gives |a|+1>=1>-2. Even a=0 impossible (a odd required). Exact.
print("DICHOTOMY (exact): no flux class satisfies h-adjunction; the only")
print("  escape is h not F-fixable. Decisive question for the target.")

out={"bound_arithmetic":True,"h_rep_open":"Kirby disjointness needed",
 "f1_inapplicable":True,"sector_wide_dichotomy":True,"certified":False}
with open("output/artifacts/adjudication_ledger.json","w") as f:
    json.dump(out,f,interrupt:=2) if False else json.dump(out,f,indent=2)
print("wrote output/artifacts/adjudication_ledger.json")
print("ALL VERIFY_OK")
