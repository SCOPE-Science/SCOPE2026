---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The self-contained file `artifacts/verify.py` uses direct neighbourhood bit masks and brute-force examination of every vertex subset. It does not use the closed-form feasibility inequalities in the actual graph predicate. For each integer \(3\le n\le8\), every integer \(1\le k\le n-2\), it computes the bivariate count of feasible sets and checks every coefficient against the formula. It also compares exact minimum sizes and counts, then checks the coefficient-derived extremal identities and the difference from complete-bipartite domination for all \(3\le n\le60\).

Executed command: `python3 artifacts/verify.py`.

Observed output ended in `ALL_COEFFICIENT_MINIMA_AND_MATCHING_DELETION_GAP_OK n=3..60` and `VERIFY_OK`. The calculations inspect only finite test ranges; arbitrary size and capacity are handled by the combinatorial proof. No independent external validation has been performed.
