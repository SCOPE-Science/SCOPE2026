---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Two marks on one vertex cannot both be positive. Fix a hub-answer pattern and ask that all marked leaves be positive; this forces adjacent hub colours to be distinct and to avoid their respective leaf-target palettes. Such hub colours also suffice for every leaf pattern with those hub answers: a negative leaf can use the remaining colour distinct from its target and hub. With no marked hubs the only extra failure once each palette has size at most two is identical size-two palettes. With just a marked left hub, its feasible colour set is the complement of the left palette minus the right forced colour, if the right complement is a singleton. A mark can vary iff its target lies in a feasible set of size at least two. Writing H_t=X_t−1 and C_t=1+3H_t, the choices contribute 3C_b+6D_b+6H_a C_b+6H_a D_b, which expands to the frozen left-hub term before multiplying by z. With both hubs marked, two nonempty palettes allow at most three adjacent hub pairs and cannot hit four bit patterns. With exactly one nonempty palette that palette must be a singleton u, the opposite hub must target u and its own hub can target either other colour. With both palettes empty the hub targets must differ and all four answers then occur. These cases give the claimed polynomial, including the empty support. There is no support on all vertices, and all leaves targeted at 1 plus the left hub at 2 shatter. At the top degree the one-hub terms give 6(2^a+2^b+2), and the two-hub terms add 6 for each singleton bank. At fixed s=a+b and 1≤a≤b, consecutive coefficients divided by six decrease by 2^(s−a−1)−2^a+1_{a=1}>0 for a<floor(s/2). Independent replay: python3 /workspace/reviews/check_mathematics.py 2 checks every coefficient via trace splitting on eight parameter pairs up to eight vertices, returning top counts 78 vs 60 at order six. The proof, not the computation, covers unbounded a,b.

## originality

PASS

The supported distinct claim is the complete marked polynomial and its fixed-order reconstruction coefficient, not the scalar VC dimension or vertex projection. A distinct same-day projected double-star result is a substantial comparison but does not supply target multiplicities; day-level dates establish no ordering.

## value

PASS

Double stars retain the minimal nontrivial coupling between two leaf banks on a tree. Their degree alone discards the arm-size distribution, and projected supports discard mark multiplicities. The full rank counts and recovery of the unordered arm sizes from just the top marked coefficient and order give a concrete refinement of these established invariants, not a finite tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
