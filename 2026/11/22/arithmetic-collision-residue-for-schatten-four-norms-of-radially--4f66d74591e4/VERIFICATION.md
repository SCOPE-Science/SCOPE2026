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

# Mathematical verification and reproducibility

The proof in `RESULT.md` uses the exact monomial basis and Gram-square trace, the bijective collision parametrization \(pn=qm\), and the fixed-degree Gamma-ratio remainder. These analytic steps cover all allowed positive real damping speeds and all \(\alpha>-1\); finite tests do not prove the infinite result.

Run `python verify.py` after installing `numpy` and `scipy` (requirements listed in `requirements.txt`). At packaging, the program printed `RADIAL_MONOMIAL_S4_MOMENT_DIAGNOSTIC_OK 403`. It performs 384 finite matrix-versus-series tests, 9 phase-singular-value comparisons, and 10 near-boundary samples. The finite samples verify implementation consistency only; floating-point error and cutoff errors are not used to assert sharpness or uniqueness.

The precise scope and scientific limits are in the proof and limitations sections. Publication-priority assessment is qualified by lack of access to the complete text of the closest publisher article. Independent audit has not been performed.
