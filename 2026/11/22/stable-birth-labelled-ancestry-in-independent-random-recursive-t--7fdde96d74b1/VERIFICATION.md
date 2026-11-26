---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and reproducibility

Run `python check.py` in a folder containing this verification file and `check.py`; no third-party dependencies are needed. The checker constructs the finite-state recurrence over exact rational numbers, then independently enumerates all possible tuples of parent choices for two independent recursive trees up to size seven and three trees up to size five. It compares the complete distributions, all finite means, and the probability of remaining at size two.

The checked census comprises 547,466 tuples of parent-choice vectors; there are 375 exact-rational assertions and 80 approximate checks of the Gamma and Euler product identities, 455 total. Numerical checks use specified finite product truncations and tolerances. These finite computations do not establish the almost-sure limit, tail domination or sharp late-arrival asymptotic; these require the proofs in `RESULT.md`.

The boundary \(n=1\) is excluded from the Gamma expression because birth two is a forced common ancestor. The conditional Gamma expression is used only for integers \(n\ge2\) and \(2\le s\le n\); the excluded state \(s=1\) has probability zero at these times.
