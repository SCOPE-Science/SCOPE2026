---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Fix the support P of positive base labels. On P the valid root/leaf pairs are (1,1),(1,2),(2,0),(2,1),(2,2). Outside P the leaf cannot be zero, and it may be 1 exactly when a positive base neighbor is present; label 2 is always sufficient. This establishes independence of the local choices, all three weight factors, and unique decomposition by P. No connectivity assumption was used. Adjoining to P all vertices outside P and its boundary gives a dominating set of size n−b(P); any minimum dominating set attains the bound, so the least exponent is n+γ(G). Exactly the maximizing supports contribute there, with local constant term 2 per positive root. Evaluation at one is direct. Independent exhaustive base-3 enumeration for all 75 labeled bases of orders 1–4 compared 1,215 coefficient positions with the product; it reproduced the stated two-vertex-edge polynomial and the K3 leading coefficient 6. This was separate from the inspected, unexecuted supplied checkers; their larger counts are package-reported, and neither computation substitutes for the general proof.

## originality

PASS

Pass for the all-base all-weight Italian transform and general minimum multiplicity formula, not the scalar minimum or any priority claim on cycle bases. In addition to already known sunlet minima, an earlier record gives the entire polynomial for sunlets. No inspected broader statement effects this substitution for unrestricted Italian labelings of arbitrary one-leaf coronas.

## value

PASS

This identifies sufficient base-graph information for every coefficient of a natural enumerator, for arbitrary cyclic or disconnected bases as well as trees. It also gives an explicit census of all optimizers, not just the already known minimum. Replacing enumeration of labelings on 2n vertices by a structural subset sum is useful without implying polynomial-time complexity. The all-base reduction, not repetition of the known sunlet counts, is the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
