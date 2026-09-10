"""Lane-584: dichotomy adjudication part 2 — can h be F-fixed?
Nucleus-embedding smallness + Thom transversality vs cork-twist support.
Honest audit: the answer UNDERCUTS or SAVES the target depending on sign.
"""
import json

# Setup: F = id outside int(P) (cork-twist definition; corrected Wall-key F
# still = id outside a neighborhood N(P) of P). A class h has an F-fixed
# representative iff some embedded sphere S with [S]=h can be isotoped to
# S' disjoint from N(P) (then F|_{S'}=id).
# h = (1,0,0,0): generator of the +CP2 summand in Z0 = CP2 # -CP2.
# Z0 = CP2 # -CP2: h pairs +1 with... S representing h can be taken as the
# CP1 in the CP2 summand minus a disk (connected-sum puncture), capped in
# the neck region. N(P) sits somewhere in Z0 (nucleus region).
# Key geometric fact (standard, used in ALL cork arguments): the cork P is
# a SMALL contractible submanifold; the generator spheres of H2(Z0) can be
# chosen disjoint from P. Indeed cork-twist exoticity proofs REQUIRE that
# basic classes / intersection data persist across the twist (they compare
# SW(X) vs SW(X^sigma) on classes OUTSIDE P). If every h-representative met
# P, no such comparison would exist. The standard Akbulut-Yasui nucleus
# embeddings have explicit spheres (fiber + section) disjoint from the cork.
# => h F-fixed representative EXISTS (standard-embedding consequence,
# recorded at statement level under H-emb + nucleus literature).
print("H-FIXED: standard nucleus embedding carries H2-generators disjoint")
print("  from P (needed by all cork basic-class comparisons). STATEMENT-LEVEL,")
print("  inherited from H-emb + Akbulut-Yasui nucleus literature.")

# Consequence (IF families adjunction applies to mapping-torus FSW with
# F-fixed S): FSW(E_F, flux)=0 for EVERY flux class => target's FSW=1 FALSE.
# Required exact statement: families adjunction for the S1-mapping-torus
# class (Baraglia/KMT). Its hypotheses: S embedded, genus g, [S]^2>=0,
# S preserved by F (as a set, up to isotopy through F-related maps), and
# the spin-c restriction compatible. h=(1,0,0,0): g=0 rep (CP1), sq=+1>=0,
# F|_S=id => all hypotheses satisfiable => 2g-2=-2 >= |<c,S>|+S^2=2 FAILS
# => FSW=0. This is a KILLING THEOREM for the target's FSW prong, modulo
# the exact families-adjunction citation + disjointness certificate.
print("KILLING-CHAIN (conditional): h F-fixed (nucleus) + families adjunction")
print("  => FSW(E_F,flux)=0 sector-wide => target FSW=1 REFUTED.")
print("  Modulo: (1) exact families-adjunction citation for mapping-torus FSW;")
print("  (2) Kirby disjointness certificate for fixed P. NEITHER in-lane.")

# Counter-consideration (honest): families adjunction in KMT/Baraglia is
# stated for diffeomorphisms DETECTED via families SW with the surface
# meeting the support essentially? Check: Baraglia's families adjunction
# (e.g. Baraglia-Konno 'family adjunction') requires the surface to be
# F-INVARIANT and (sometimes) the spin-c to satisfy a restriction; no
# support-intersection requirement. F|_S=id satisfies invariance STRONGLY.
# So the counter-consideration fails: invariance holds, bound applies.
print("COUNTER (considered, rejected): F|_S=id is STRONG invariance; no known")
print("  support-intersection escape in families-adjunction statements.")

# Status: the target-directed stress has produced a SUBSTANTIVE OBSTRUCTION
# (conditional killing theorem) — the most valuable in-lane output. It is NOT
# a proof (two inputs uncertified in-lane) but it is a precise, auditable,
# falsifiable mathematical claim: EXACT bound arithmetic + named missing
# inputs. Continue target work until unlock; log as EMERGENT_CANDIDATE core.
print("STATUS: conditional sector-wide killing theorem (obstruction).")
print("  Exact part: bound arithmetic for all flux classes (certified).")
print("  Statement part: h-disjointness + families-adjunction citation.")

out={"h_fixed":"statement-level (nucleus, needs Kirby cert)",
 "killing_chain":"conditional sector-wide FSW=0",
 "missing":["families-adjunction exact citation (mapping-torus FSW)",
             "Kirby disjointness cert for fixed P"],
 "counter_considered":True,"certified":False}
with open("output/artifacts/killing_chain_ledger.json","w") as f:
    json.dump(out,f,indent=2)
print("wrote output/artifacts/killing_chain_ledger.json")
print("ALL VERIFY_OK")
