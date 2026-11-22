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

This package supplies an analytic proof and a standalone finite checker. It does not claim externally performed mathematical validation.

## Analytic checks

The normalization uses \((2\pi)^{-1}\int\), and the Fourier coefficient is obtained by adding the two elementary arc integrals. The denominator values at the two poles are stated separately. For every integer frequency, cancellation near the moving pole is given by the exact identity \(\sin(\pi\alpha t)=\pm\sin(\pi(1-\alpha)(t-L))\). Four logarithmic shoulders and bounded exterior tails yield the limit. The irrational Cesàro limit is uniform over starting shifts, which is indispensable because the second pole moves with the exponent. The rational case uses periodic bounded discrepancy rather than irrational equidistribution.

## Reproducibility

From the root of this package run `python3 checks/verify_tent_phase.py`. The checker uses only the Python standard library, compares Fourier coefficients against direct quadrature of the original phase in several cases, tests exceptional frequencies, checks the symmetric-tent harmonic formula against a controlled finite-frequency sum, and verifies the finite root-of-unity means. Finite calculations are supplementary and do not certify the infinite statement.

## Boundaries

No uniform-in-parameter limit or irrational bounded remainder is asserted. Earlier equivalent formulations could remain unindexed. Independent audit has not been performed.
