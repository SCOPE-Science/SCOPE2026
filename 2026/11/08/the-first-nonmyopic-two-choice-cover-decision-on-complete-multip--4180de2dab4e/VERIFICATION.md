---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For a with-replacement two-offer walk on complete multipartite K_(n_1,...,n_k), part exchangeability reduces each state to (visited-count vector x,current part i). Exact Bellman V_x(i)=1+sum_{a,b} q_i(a)q_i(b) min(C(a),C(b)) follows by conditioning on both proposed neighbor types; all policies are proper since simultaneous identical offers can force any two-step destination path with positive uniform probability. Independently implemented rational policy iteration solving finite same-coverage-layer linear systems and checking every Bellman equality, enumerating ALL integer partitions with >=2 parts through N=9. Verified 58 graph types N<=8, zero seen-first strict advantage, and 29 N=9 types with ONLY K_(1,2,6) exceptional. Three inequivalent state profiles (0,1,1),(0,2,1),(0,2,2), walker in 6-part, unseen singleton offer and seen 2-part offer. For (0,2,2), independent fractions Qnew=863502507888814/58892405629491 and Qold=136185927932950168179443/9289655025356352195549, difference 3210462360632365129/1327093575050907456507 >0. Source code choice_multipartite_exact.py read and equivalent recursion inspected. Finite classification is exhaustive for <=9, no claim above.

## originality

PASS

The primary 2021 Georgakopoulos–Haslegrave–Sauerwald–Sylvester full text studies the same with-replacement two-choice walk and cover-time hardness for general graphs, not the precise smallest multipartite seen-first decision reversal. Published SCOPE path example exhibits earlier failure on 6 vertices among arbitrary connected graphs, but paths with >3 vertices are not complete multipartite; SCOPE complete-bipartite unseen-first dominance covers a strict subfamily only. No located broader theorem implies unique K_(1,2,6) nine-vertex state pattern.

## value

PASS

A natural local greedy covering decision is globally suboptimal at a sharp small structure despite immediately increasing visited count. Exhaustive complete-multipartite cutoff and exact rational state exhibit a meaningful finite nonmyopic control boundary, not a random unmotivated statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
