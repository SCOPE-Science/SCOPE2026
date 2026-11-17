---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Direct local Rule184 and reflected Rule226 truth tables imply no cyclic output contains 1100 and F(G(y))=y exactly when y avoids cyclic 1100, including n<4 via repeated modular indices. Unbordered block 1100 allows cyclic inclusion-exclusion: a_nk=Σ_s(−1)^s n/(n−3s) binom(n−3s,s) binom(n−4s,k−2s). The transfer determinant is 1−(1+u)z+u^2 z^4 and hence weighted trace GF is [(1+u)z−4u^2 z^4]/[1−(1+u)z+u^2 z^4]. Setting u=1 yields tribonacci growth. Independently enumerated direct image, explicit Rule226 section and every fixed-density count for n=1..12. Infinite result comes from local finite truth tables and symbolic combinatorics, not sampled rings.

## originality

FAIL

FAIL: The Nov2, 2026 published complete primary text establishes the exact same necessary and sufficient cyclic 1100 avoidance, Rule226 explicit inverse including converse, same fixed-weight inclusion–exclusion coefficient, identical bivariate rational generating function, identical first values and tribonacci entropy. No part remains original under relabelling the count a_nk versus R_nk.

## value

FAIL

FAIL as separate mathematical contribution: original package is identical to the prior stronger self-contained theorem for the same natural object. The exact finite image invariant is useful in isolation, but is known already; reproducing the same 8-state versus 4-state determinant gives no motivated new theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
