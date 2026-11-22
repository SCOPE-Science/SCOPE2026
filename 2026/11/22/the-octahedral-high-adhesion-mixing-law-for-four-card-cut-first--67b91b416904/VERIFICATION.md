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

# Reproducibility and verification

Run `python3 verification/check_four_card.py` using Python 3 and its standard library. The package contains this complete standalone checker, which enumerates all \(24\) permutations and six cyclic-rotation classes, including all five possible cuts, all internal contact bond masks, and all three block-release rules. It verifies the complete exact rational six-by-six first-order quotient generators, full double-stochastic kernels at \(q=0,1/10,1/3\), and support confinement at \(q=0\). The check recorded 7,471 exact-rational assertions; 18 supplementary total-variation computations at \(q=1/50\) and \(q=1/100\) agreed with the analytic profile within \(0.045\) in absolute error. These are finite checks and must not be mistaken for an infinite-limit proof. The latter is given in RESULT.md by finite-dimensional fast/slow stochastic averaging and an exact six-state spectral decomposition.

The output theorem excludes the correlated-label shuffle, a growing deck, rescaled time zero, and error thresholds greater than or equal to \(5/6\). No independently assessed certificate is claimed.
