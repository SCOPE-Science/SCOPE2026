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

# Verification

The proof's probability claims are established analytically: the exact normalized binomial coefficient vector, independent uniform-circle event measure, Lagrange inverse, conditional chord CDF, stochastic comparison with exponentials, gamma tail and positive-Gram matrix inequality give the two inverse moment regimes. Only fixed \(N,m,k\) are covered. No unproved endpoint at \(p=k/2\) is asserted.

To reproduce supplementary finite checks, install NumPy and run `python CHECK.py` in the extracted directory. The checker has been executed successfully (`CHECK_OK assertions= 5715 dimensions=3..8`). It tests exact binomial and chord inequalities, Vandermonde interpolation, spectral superadditivity, and the gamma survival expression; it does not verify continuum probabilities or prove any infinite assertion.

No independent mathematical audit has been performed. Earlier equivalent literature and the exact transition within \(2N\le m<3N\) remain unverified or unresolved.
