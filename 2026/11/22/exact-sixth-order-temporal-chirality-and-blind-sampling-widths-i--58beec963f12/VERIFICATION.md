---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The asserted statistic is the difference of raw products of three squared increments, not a path-law criterion. Conditional on the independent environment, disjoint Brownian increments are independent with conditional variances equal to twice their integrated diffusivities. To check the three-time sign directly, center the diffusivity vector x and set D=diag(x), R=(P-P^T)/sqrt(3). Centering only removes terms symmetric in the two lags. On the mean-zero subspace the semigroup is exp(-ct)(cos(bt)I+sin(bt)R). The antisymmetric moment has coefficient 2 x^T R D x/3=2V/(3 sqrt(3)) multiplying exp(-c(s+t)) sin(b(s-t)); the cyclic cubic expansion fixes its sign. Reflecting all observation times in the three-window interval exchanges the two gaps and reverses the kernel. For I=(exp(lambda h)-1)/lambda the three window integrals in the complex form are exp(-lambda h)I, exp(ibh) sin(bh)/b, and conjugate(I), respectively, leaving the stated real exponential and the factor 8. The prose in Proof 4 writes the wrong middle exponent (-ibt); the displayed integrand has +2ibt and its evaluation is correct. The two-time centered semigroup calculation gives the even-in-b covariance and stationarity gives the Brownian MSD. Since c>0 the I factor cannot vanish, and for b != 0 there exist nonnegative gaps with sin(b(u-v)) != 0. Thus exactly h=n*pi/abs(b) are blind for all gaps when V != 0; coincident diffusivities and equal rates give vanishing contrast at every width. These are analytic checks; the frozen script was inspected, not executed.

## originality

PASS

The same blind lattice is already the sampled hidden-chain resonance. Distinct content is the exact integrated squared-increment contrast and the proof that this particular continuous-window statistic has precisely that lattice of universal zeros, not the lattice as a new property of the hidden chain or higher-order time-reversal diagnostics in general.

## value

PASS

The exact contrast gives an experimentally meaningful witness in a model whose mean-square displacement and two-time squared-increment covariance do not resolve direction. Its finite-window amplitude explains when even this higher-order observation loses direction information for all gap choices. The contribution is the joint contrast and sharp observational boundary, not a general claim that a higher-order statistic detects irreversibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
