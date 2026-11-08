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

# Verification and reproducibility

The analytical proof in `RESULT.md` determines all dimensions \(d\ge3\). The file `orthant_spectral_check.py` verifies the formula independently in a finite range by constructing the unrestricted quadratic trace-free basis and integrating each monomial product via the positive-orthant Dirichlet moment formula. The routine does not form its matrix from the claimed vertex-edge incidence decomposition; it diagonalizes the full constructed matrix directly.

Run `python orthant_spectral_check.py` after installing the NumPy requirement specified in `requirements.txt`. The observed result was `ORTHANT_HARMONIC_SPECTRUM_CHECKS_PASS 399`. Tested dimensions were \(3\le d\le12\), with additional large-dimension analytic-formula comparisons. The 399 assertions are finite corroboration, not an infinite certificate.

The normalization in every test is \(d(d+2)\) times the conditional orthant quartic moment; the actual concentration eigenvalues are \(2^{-d}\) times this test matrix's eigenvalues. Strict spectral ordering for all dimensions is proved symbolically in `RESULT.md` using \(3<\pi<22/7\). The convergence constant is derived from the two exact spectral branches rather than inferred by regression.

Originality was compared to explicitly named foundational and geometrically related sources; an equivalent implicit classical formula cannot be excluded. Independent mathematical validation has not been carried out.
