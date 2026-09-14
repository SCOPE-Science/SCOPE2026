"""Bounded recovery / scope-coverage test for the isolated-blocks unitriangularity target.

Question: does the target's universal quantifier ("for EVERY isolated B_s", EVERY ell != p)
force cases lying outside the hypotheses of every available engine
(Bonnafe-Rouquier / Bonnafe-Dat-Rouquier reduction, Brunat-Dudas-Taylor-type
unipotent unitriangularity, ordinary/Kawanaka GGGR projectivity)?

Method: encode (i) good/bad primes per exceptional type, (ii) a conservative set of
well-attested isolated centralizer types C^o(s) with the order of s (all from the
Bonnafe quasi-isolated classification tables / standard subsystem lists; each listed
C^o is NOT a Levi subgroup), (iii) a choice of good p and bad ell != p with s an
ell'-element. Check each candidate against engine hypotheses H1-H3:
  H1 (BR/BDR reduction to a unipotent block): needs C^o(s) contained in a proper Levi.
  H2 (BDT unipotent unitriangularity input): needs ell good for the group.
  H3 (ordinary Kawanaka/GGGR reduction to projectives): needs ell good / ell not
       dividing the relevant component-group orders (coded conservatively: ell good
       for G and ell not dividing |A(s)| when known).
A candidate that fails H1 by definition of isolated AND fails H2 is a concrete
quantifier-forced gap for any uniform "for all s, all ell by these methods" claim.

All inputs below are standard textbook data (root-system bad primes; Bonnafe Table
isolated types). This script only checks quantifier coverage, it proves no theorem.
"""

import json

# Bad primes of the root system (p good <=> p not in this set)
BAD = {"E6": {2, 3}, "E7": {2, 3}, "E8": {2, 3, 5}}

# Conservative, well-attested isolated cases: (ambient type, C^o(s) type, order(s)).
# - E8 / A8: centralizer of an element of order 3 (A8 subsystem, not a Levi of E8).
# - E8 / A2+E6: centralizer of an element of order 3 (not a Levi of E8).
# - E6 / A2+A2+A2 ("3A2"): centralizer of an element of order 3 (not a Levi of E6).
# Each is listed as isolated (C^o not contained in any proper Levi) in Bonnafe's
# quasi-isolated classification tables for the adjoint groups.
CANDIDATES = [
    {"G": "E8", "Co": "A8", "order_s": 3, "Co_non_Levi": True},
    {"G": "E8", "Co": "A2+E6", "order_s": 3, "Co_non_Levi": True},
    {"G": "E6", "Co": "A2+A2+A2", "order_s": 3, "Co_non_Levi": True},
]

# Trial parameters: p good for G, ell != p, s an ell'-element.
TRIALS = [
    {"G": "E8", "Co": "A8", "p": 7, "ell": 2},
    {"G": "E8", "Co": "A2+E6", "p": 7, "ell": 2},
    {"G": "E6", "Co": "A2+A2+A2", "p": 7, "ell": 2},
]

rows = []
for t in TRIALS:
    G, p, ell = t["G"], t["p"], t["ell"]
    cand = next(c for c in CANDIDATES if c["G"] == G and c["Co"] == t["Co"])
    s_ord = cand["order_s"]
    p_good = p not in BAD[G]
    ell_neq_p = ell != p
    s_ell_prime = (s_ord % ell != 0)
    in_scope = p_good and ell_neq_p and s_ell_prime  # target quantifier forces this case
    h1_br_reduction = (not cand["Co_non_Levi"])  # needs C^o inside a Levi
    h2_ell_good = ell not in BAD[G]  # BDT-type input needs ell good
    # H3 conservative: ell good for G (else modular GGGR/Kawanaka projectivity conditional)
    h3_kawanaka = ell not in BAD[G]
    gap = in_scope and (not h1_br_reduction) and (not h2_ell_good)
    rows.append({
        "G": G, "Co": cand["Co"], "order_s": s_ord, "p": p, "ell": ell,
        "in_target_scope": in_scope,
        "H1_BR_reduction_available": h1_br_reduction,
        "H2_ell_good_for_BDT_input": h2_ell_good,
        "H3_unconditional_Kawanaka_projective": h3_kawanaka,
        "quantifier_forced_gap": gap,
    })

verdict = (
    "BLOCKED_AS_UNIFORM_CLAIM"
    if all(r["quantifier_forced_gap"] for r in rows) and len(rows) > 0
    else "NO_FORCED_GAP"
)

print(json.dumps({"rows": rows, "verdict": verdict}, indent=2))
