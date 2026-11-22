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

Run `python3 verify.py` with a standard Python 3 interpreter. The script uses integer Bell recurrences, exact fractions, exhaustive set partitions of orders three through six, complete pairs of graph-edge requirements through four labeled vertices, and exact rational grids of admissible exchangeable three-label measures. It verifies that \(q(1+p)-2p^2\) controls every increasing-event covariance, and that all three uniform-Bell non-nested covariance classes have the asserted signs. It also checks Pitman–Yor and independent-color parameter identities with rational inputs.

Observed run: `PASS: exact checks = 18650`. The proof of the infinite parameter and order ranges is analytic and contained in RESULT.md. Exhaustive finite checks cannot independently establish those quantifiers.
