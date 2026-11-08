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

# Reproducibility and scope

The main analytic verification expands \(\int_{\mathbb T}|P|^4\) into pair-sum convolution squares. All exceptional pair sums and their coefficients are enumerated in the proof, and the compression/perturbation argument handles every positive integer length, not only finite tests. The base sharp value \(15/7\) is an exact quadratic maximum.

Run `python3 check_dyadic_fourth.py` with the Python standard library. The observed result is `EXACT_MOMENT_CHECKS_PASS 1297`, testing collision structure and direct convolution moments for dyadic lengths up to ten, bases three through seven, and reproducible complex-integer coefficient samples. The exact result and full-support argument do not depend on the numeric length cutoff. The checker is not an independent mathematical audit.

Historical-priority comparison includes accessible paper sections and index summaries, not an exhaustive universe of unpublished manuscripts. The all-length dyadic magnitude optimizer is intentionally not given in closed form.
