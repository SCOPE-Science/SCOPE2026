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
# Reproducibility

Run the dependency-free `CHECK.py` with Python 3.8 or later. It constructs the integer adjacency matrix on every even cycle of orders \(4,6,\ldots,18\), obtains the raw two-sensor consecutive-time observation rows and uses a fraction-free Bareiss determinant. It checks for every offset that the determinant vanishes if and only if the offset is noncoprime, and that the absolute value is \(1\) in the coprime case.

It independently tests three affine spectral evolutions of the form \(B=lpha A+eta I\), with nonzero integer \(lpha\), for all even cycle orders \(4,6,\ldots,12\). The exact predicted determinant magnitude is \(|lpha|^{M(M-1)}\) at the coprime offsets. Actual result: `CHECK_OK exact_determinants=185 even_cycles=4..18`.

The checker verifies a finite collection of exact integer instances, not a proof for all \(M\). The all-parameter proof is the Fourier/Vandermonde/sine-product argument in RESULT.md, together with the explicit triangular walk-count argument for adjacency evolution. The complete recent motivating manuscript remains an originality-review access limitation. No independent audit has occurred.
