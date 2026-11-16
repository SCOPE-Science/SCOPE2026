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

# Reproducible checks

Run `python3 CHECK.py` from the directory containing the standalone script. It uses Python standard-library `math`, `cmath` and `random`, with a fixed reproducible seed. The expected report is:

`CHECK_OK spherical_moment_quadrature=12 first_band_inequalities=500 inverse_distance=250 gram_identity=100 global_shell_alias=48 pure_degree_one=4 total=914`

The checker evaluates scalar and first spherical moments by 4096-step trapezoidal angular quadrature at six radii, verifies 500 scalar monotonicity lower inequalities, compares 250 inverse distances, compares 100 exact symbolic-form Gram determinant identities against complex four-coordinate inner products, verifies 48 higher-band alias root relations and checks four exceptional Bessel radii. It does not certify uncountably many locations, all radii, or all source mixtures. Those conclusions instead use the complete analytic argument in `RESULT.md`, specifically the sine-product expansion and the finite-dimensional algebraic rank identity. No outside certification has been performed.

# Boundaries and units

Area measure on \(S^2\) is normalized to one. The projective quotient is taken over complex nonzero scalars, not only positive real scalars. The sharp \(3/\kappa\) bound applies to ratios \(Y\), not unnormalized measurement coefficients. The closed-ball boundary \(\kappa R=\pi\) fails because antipodes have equal projective lines. Generic rank does not imply unique inverse recovery of arbitrary multiatom mixtures.
