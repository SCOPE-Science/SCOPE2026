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

# Verification information

The theorem is proved symbolically in RESULT.md. To independently replay finite checks, run `python3 checker.py` with Python 3 standard library only. The verifier tests the original Gram linear system using exact rational arithmetic, not just a substituted one-dimensional recurrence. It checks several mass/target/predictor combinations, both nonsingular implicit branches, rank collapse at a uniform predictor, an exact fractional-linear trajectory, the parity-dependent stopping thresholds, and the explicit oscillator predictor.

The saved output `CHECKS.txt` records 1,044 exact-rational assertions/check steps, 12 asymptotic stopping checks, and 16 oscillator tests. The finite checks do not establish the infinite-time limit or its sharp constant; those follow from the Cayley identity and the logarithmic expansion in the written proof.

All computations are exact rational or standard floating-point tests. No formal proof assistant, external validation, or independent mathematical audit is claimed. The numerical demonstration near a singular predictor is not a claim of reliable floating-point performance at exact singularity.
