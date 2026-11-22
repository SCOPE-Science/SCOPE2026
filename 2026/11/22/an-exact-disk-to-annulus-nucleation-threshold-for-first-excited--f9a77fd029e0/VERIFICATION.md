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

# Verification of the first-excited wavelet mask theorem

The wavelet-kernel formula is imported explicitly from Abreu--Speckbacher (arXiv:2210.13056, Proposition 1, equation (20)); the scalar Jacobi specialization is checked symbolically in the proof. The radial hyperbolic measure, exact integrated energy, strict lobe monotonicity, uniqueness of all threshold levels and the bathtub inequality are reconstructed in `RESULT.md`. The local Taylor derivation establishes the linear-width and quadratic-disk shifts. The parameter limit requires a rescaled unique-root argument; a finite asymptotic sample is not substituted for this argument.

Run `python check.py` after installing SciPy and mpmath. The embedded checker was executed successfully, with **104 finite assertions**. These cover four positive parameters, six finite budgets per parameter, analytic versus quadrature mass formulas, high-precision right-sided birth expansions, and exact weight-one radicals. A finite test cannot prove the global theorem or historical originality.

This verification is a self-review of the claim. Independent audit has not been performed.
