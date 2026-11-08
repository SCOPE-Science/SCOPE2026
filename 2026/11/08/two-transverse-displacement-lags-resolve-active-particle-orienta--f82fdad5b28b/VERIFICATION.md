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

# Verification scope

The self-contained `CHECK.py` uses Python 3 standard library, computes the two finite-lag second-moment functions, performs one-dimensional inverse bisections, tests 200 seeded physical triples, and checks exact rational algebra for the one-lag ambiguity. It completed with `PASS: 1063 exact/numerical assertions`.

Analytical proof checks: (i) the angular generator gives all needed stationary harmonics; (ii) both centered angular first harmonics decay at rate \(r+d\); (iii) direct integration yields both positional covariances including the known thermal term; (iv) strict stochastic ordering of the normalized kernels \((t-s)e^{-\lambda s}\) proves monotonicity of the lag ratio; (v) the second scalar inversion is strictly monotone; (vi) two exact rational reset-to-diffusion ratios give the same one-lag anisotropy and have valid positive relaxation roots. The boundary intervals are open because every three-parameter rate is strictly positive and finite.

The universal conclusions rely on the complete analytical argument in `RESULT.md`, not finite grids or floating point output. The tests are diagnostic rather than independent certification. No experimental data, finite-sample error bounds, measurement-noise stability theorem, or independent scientific audit is supplied.
