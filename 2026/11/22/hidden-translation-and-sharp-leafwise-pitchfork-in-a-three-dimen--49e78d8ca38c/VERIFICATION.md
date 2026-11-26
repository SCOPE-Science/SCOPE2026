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

# Reproducibility and limits

Run `python3 check_resonance.py` from this directory. The checker uses the Python standard library. It checks sampled drift identities, sampled fiber bounds, six nearby supercritical cases, and an irrational-rotation mean diagnostic. In the branch tests only the sine row of the Jacobian acquires the cosine factor, and finite differences check both Jacobian columns. The tests compare the multiplier near one to its first-order expansion and check the absolute values of both multipliers.

The finite checks are supplementary. The exact translation, invariant-probability assertions, all-time contraction, stationary law, mean-error estimate and local stability classification follow from the analytic argument in `RESULT.md`.
