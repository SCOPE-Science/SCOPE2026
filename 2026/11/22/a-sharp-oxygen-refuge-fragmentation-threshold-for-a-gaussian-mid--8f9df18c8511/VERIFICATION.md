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

# Verification summary

The theorem follows from the derivative factorization, a unique negative maximum of the auxiliary Gaussian-weighted linear function, a sharp surface-truncation inequality, and a Taylor expansion around the double stationary point. These steps are proved in `RESULT.md` and involve no computer-dependent or external mathematical lemma.

`CHECK.py` uses only the Python standard library. It verifies 25,814 supplementary assertion groups covering stationary roots, the exact threshold and its strict boundary, potential disconnected viable sets, the finite-column example, monotonicity in oxygen-centre depth, and near-fold square-root and three-halves asymptotics. It can be run using `python3 CHECK.py` from the extracted file directory.

The numerical evaluations check finite cases only; they are not an exhaustive proof. Model limitations, physiological approximations, and provisional historical priority are stated explicitly. This document reports no independent review or certification.
