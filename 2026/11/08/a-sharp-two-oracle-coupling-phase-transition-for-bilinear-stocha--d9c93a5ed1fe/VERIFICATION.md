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

# Reproducibility and logical limits

Run `python3 verify.py` with an ordinary Python 3 standard-library interpreter. `verification_output.txt` records the actual output of the packaged program. The checks use exact rational arithmetic to compare deterministic stage updates, the four-coupling average, stability and optimization identities, and a rational witness. The continuous-parameter results—including uniqueness and the golden-radical threshold—follow from the displayed proof rather than the finite sample of test inputs.

The procedure does not run an independent audit, use external correctness certificates, or assert formal proof verification. The literature comparisons are specialist research judgments and retain historical-overlap risk.
