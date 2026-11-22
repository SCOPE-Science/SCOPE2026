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

# Verification record

The proof is analytic. Its critical steps are: (i) solving the killed-diffusion backward boundary-value equation; (ii) deriving the stationary cluster covariance by conditional counting of distinct offspring pairs; (iii) establishing the exact Fourier orientation; (iv) rewriting the two hitting transforms with exponential corrections; (v) controlling those corrections, together with one derivative, uniformly at high frequency; and (vi) obtaining eventual simple roots and their two-term asymptotics by the inverse-function principle and a square-root expansion.

A reproducible numerical consistency program is provided as `checks/spectral_two_wall.py` (NumPy and SciPy). Running it returned `PASS: 106 spectral, zero-ladder and independent heat-flux checks`. It tests a separate absorbing-heat-kernel eigenfunction representation at moderate frequencies, several noncentral positions, the zero-degradation boundary, root location, exact midpoint positivity, and complex-conjugation symmetry. These are finite diagnostic checks only, not certificates of global spectral signs.

Scientific limitations: observations of high-frequency roots would be exponentially noise-sensitive; the exact physical model excludes source motion, offspring dependence and partially absorbing walls. Classical point-process spectral theory is prior knowledge. Prior literature was searched, but an implicit general result may remain unrecognized. An independent audit was not performed.
