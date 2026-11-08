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

The analytic proof is provided in `RESULT.md`; it establishes stationary symmetry, a uniform position-chain coupling, two-step hitting probabilities, and concentration of empty bins. Reproduce finite checks with `python3 checks.py`. The checker enumerates unicycle states for part sizes (2,2), (2,3), (3,2), and (3,3), checks invariant column sums and two-step hitting inequalities exactly, and verifies coupon empty-bin variance formulas. Expected output ends with `total exact assertions=12430; PASS`.

Finite verification does not establish asymptotic mixing, uniqueness of a mathematical discovery, or independent certification. The proof's limiting steps require the bounded-aspect-ratio assumption. Independent audit has not been performed.
