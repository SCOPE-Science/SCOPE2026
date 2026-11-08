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

# Reproducibility and scientific checks

Run `python3 verify.py` with the Python standard library. This program derives the recurrence and separately enumerates all structure matrices for seven small field-size and dimension pairs, computing ranks and support components independently. It solves the centroid defining linear identities on selected independently enumerated matrices, and verifies the lower/upper probability inequalities for multiple parameters. The observed success marker is `VERIFY_OK_CENTROID`.

These are exhaustive only for the specified small samples. The complete arbitrary-prime-power, all-dimension theorem and its fixed-field asymptotic are justified by the mathematical proof in `RESULT.md`, not by finite computation. The mathematical claim has undergone self-review; no independent audit, external certification, or exhaustive publication-priority determination has occurred.
