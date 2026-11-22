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

`check.py` uses Python 3 standard library only. Run `python3 check.py` from this file's directory. Actual execution ended with `ALL_NEUMANN_BV_L1_CHECKS_PASS` after checks of seven time scales, Markov kernel normalization, independently quadrature-evaluated crossing integrals, 450 signed multijump tests, and spectral time derivatives/asymptotic ratios.

These computations are finite numerical sanity checks, not interval certificates or proofs of global monotonicity. The universal inequality is proved in RESULT.md by distributional signed-jump reduction, the positivity and symmetry of the heat kernel, and the strict monotonicity of its wrapped Gaussian derived from Jacobi's product. The equality cases follow from strict uniqueness of the maximizing jump. The arithmetic is floating point, with explicit tolerances in the standalone checker.

No independent mathematical audit has been performed. Reproducibility extends to the embedded checker and the explicit analytical formulas, not to an external certificate.
