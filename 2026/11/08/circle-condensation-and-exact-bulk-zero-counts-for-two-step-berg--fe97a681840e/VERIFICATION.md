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

# Verification and limits

Run the complete standalone check with `python verify_step_weight.py`. The checker uses Python standard-library complex arithmetic to reconstruct the monomial coefficients of the exact series, evaluates contour winding numbers for six tuples of jump radius, exponent, and contour radius, and compares the bilateral series with the infinite product at three nonreal annulus points. The observed result was:

`STEP_BERGMAN_CHECK_PASS argument_windings=6 product_identities=3`

The six finite contours are numerical spot checks only; a winding calculation with discretized samples is not an exact computer-assisted argument-principle certificate. The proof of the eventual contour winding for every real \(0<a<r<1\) follows instead from the normally convergent bilateral product and locally uniform limit in RESULT.md. The empirical distribution is established by subharmonic compactness, \(L^1_{\mathrm{loc}}\)-convergence of normalized logarithmic potentials, and distributional Laplacians, not by finite numerical enumeration. The exact counts do not classify possible extra zeros near \(|s|=1\). No independent audit or expert certification has been performed.
