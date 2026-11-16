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

# Reproducibility and verification boundaries

Run `python3 verify.py` in a directory containing this complete package. Only the Python 3 standard library is required. The verifier exhaustively builds the matching on each \(2m\)-site circle for \(m=2,3,4,5,6,7\), where the numbers of matchings are respectively 3, 15, 105, 945, 10,395 and 135,135. It directly recomputes all \(m\) chord-cut observations from every matching and compares all means and covariance entries by exact rational arithmetic. This produces 7,021,287 matching-by-matrix-cell comparisons.

The verifier independently forms both sides of the claimed Green-kernel inverse identity with exact rational arithmetic and tests every entry of their product for \(2\le m\le17\): 1,784 comparisons. It additionally numerically checks the complete finite Fourier extrema and exact condition ratios for \(2\le m\le499\), using the ordinary floating-point sine function. The expected final output includes `All checks passed.`

These are finite corroborations only. The theorem for **all** integers \(m\ge2\), the location and uniqueness of all extrema, and the asymptotic conditioning coefficient follow from the explicit geometric, linear-algebraic and trigonometric arguments in `RESULT.md`. No independent proof audit, external replication, nonlinear identifiability proof or general-window classification is asserted.
