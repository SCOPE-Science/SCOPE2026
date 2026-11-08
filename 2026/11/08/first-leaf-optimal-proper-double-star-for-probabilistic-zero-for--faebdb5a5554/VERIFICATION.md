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

# Exact computation verification

To reproduce, run `python3 verify.py` with no additional files or dependencies. The script computes exact binomial-transition fractions and solves the finite triangular Markov first-step recurrences for **all six** proper double-star graph types with at most nine vertices. All hub-versus-leaf and asymmetric source-orbit comparisons are asserted on exact fractions. It also verifies the exact positive rational difference between the larger hub and a neighboring leaf in \(D_{2,5}\), and independently implements the original PZF process on individually labeled vertex subsets for five graph types, checking complete equality of all four source-orbit expectation fractions. Decimal printouts are illustrative only.

The exhaustive theorem applies only to the six enumerated graph types; no unexamined graph types of that bounded proper class remain. The checker does not establish a symbolic infinite-parameter result, nor does it provide an independent mathematical audit.
