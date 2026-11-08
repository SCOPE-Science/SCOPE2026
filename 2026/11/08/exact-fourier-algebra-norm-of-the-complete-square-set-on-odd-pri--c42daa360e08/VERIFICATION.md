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
Run `python3 artifacts/verify.py` using the Python standard library. It produces twelve lines starting `CASE_OK`, four lines starting `SLOPE_OK`, and the terminal marker `SQUARE_RESIDUE_WIENER_NORM_PASS` when all tests succeed.

The checker obtains the complete square set by direct modular squaring, evaluates all Fourier coefficients by sums of complex roots of unity, and independently generates the theoretical coefficients from the valuation/Legendre formulas. It checks exact set cardinalities, all coefficients, direct versus stratified normalized absolute Fourier mass, Fourier orthogonality and Parseval for the twelve listed prime-power pairs. It also compares depth-30 and depth-60 norms with the explicit linear coefficient for four odd primes.

The direct complex-trigonometric comparisons use floating-point tolerance and therefore are **not exact symbolic certificates**. The arbitrary-depth theorem is justified by the explicit Gauss-sum and valuation proof in `RESULT.md`; the checker is finite corroboration. No external or independent mathematical audit was performed.
