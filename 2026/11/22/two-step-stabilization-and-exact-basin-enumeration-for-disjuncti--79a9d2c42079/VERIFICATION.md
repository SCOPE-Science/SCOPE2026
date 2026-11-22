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

# Verification of the finite-grid dynamical and fiber formulas

Execute `python3 verify.py` with Python 3 standard library. The checker independently enumerates atomic valuations and evaluates disjunctive knowing-whether using row and column masks. It tests stabilization, terminal cross classification, every terminal-state inverse fiber, and finite Boolean-matrix inclusion–exclusion on the explicitly indicated grid sizes. It also computes all relevant pair-event joint probabilities for small squares and compares them to the elementary formulas used in the asymptotic proof. The checker returns `VERIFY_OK` on success.

The enumerations are finite consistency tests, not infinite proofs. The all-size geometry, inverse-fiber bijection, and Bonferroni asymptotic are established in `RESULT.md`. No external independent mathematical audit or historical-priority certification has been performed.
