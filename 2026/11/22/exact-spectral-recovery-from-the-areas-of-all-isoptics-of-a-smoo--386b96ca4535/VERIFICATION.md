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

The first and second tangent-line intersection equations were solved explicitly. Green's formula was reduced to the established area identity (Michalska, 2003, Eq. 1.1). Fourier coefficients were extracted and both parity recurrences telescoped with convergence justified by the support function's two continuous derivatives.

The included standalone checker `check_isoptic_area_inverse.py` executed successfully, printing `ISOPTIC_AREA_SPECTRAL_INVERSE_CHECKS_OK`. It tested seven direct areas of isoptic curves from their tangent-intersection geometry against the analytic area formula, checked reconstructed coefficients for a five-harmonic support function, integrated the area profile for independent cosine coefficients, and checked positive curvature for the two-oval ambiguity example.

Limits: finite computation only checks selected instances, not all smooth ovals. No certified numerical-error bounds or noise stability are asserted. The proof is analytic; the 2003 forward formula is prior art. Historical priority and external independent validation are not established.
