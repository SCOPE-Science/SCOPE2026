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

The full eight-cell likelihood for a two-plus-one assay protocol was reconstructed independently by enumeration over site and primary-sample latent states. Exact-rational parameter sweeps and a rational worked example in `verify_nested.py` check the four-moment identities, inversion and cell law. The analytical argument establishes uniqueness for all \(0<\psi,\theta<1\) and \(0<f<p<1\), which cannot be certified by finitely many diagnostics. The determinant identity was also obtained by direct symbolic differentiation during development; the standalone checker does not depend on a symbolic algebra package.

The input to inversion must be a true probability law satisfying the stated exchangeability and equal-marginal identities. A nonpositive covariance, an invalid square-root discriminant, or recovered parameters outside the strict domain means that the hypotheses of the theorem do not hold; it does not automatically identify which physical assumption failed. In particular no claim is made about calibration when contamination of an absent primary sample can occur before the assays.
