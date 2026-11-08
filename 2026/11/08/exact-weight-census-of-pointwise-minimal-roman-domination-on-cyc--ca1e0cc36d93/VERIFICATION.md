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

# Finite and symbolic checks

Standalone `verify.py` (Python 3 standard library only) independently reconstructs Roman feasibility and pointwise minimality, without using the gap theorem as an oracle for its exhaustive labelings. On all cycles of orders 3–11, it checks all 265707 ternary functions. A second exhaustive checker constructs defender sets independently through order 18 (524280 subsets) and compares canonical labels with the claimed unique private-neighbor family. Exact integer arithmetic independently compares explicit binomial coefficients against the rational bivariate recurrence for all orders 3–45 (1075 candidate coefficients), and checks the support and unweighted recurrence for orders up to 65.

Expected observed output:

`VERIFY_OK bruteforce_labelings_n=3..11 265707 independent_defender_subsets_n=3..18 524280 explicit_coefficients_n=3..45 1075 recurrence_and_support_n=3..65 PASS`

The unrestricted theorem is established by the combinatorial proof in RESULT.md. These finite tests are corroboration only, not an infinite formal certificate. A primary PDF page-image attempt yielded HTTP 403, but indexed text of its all-RDF theorem was read. No independent mathematical audit has been performed.
