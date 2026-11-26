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

For real circular BV with unnormalized L1, a displacement z of shortest length h satisfies the translation bound by integrating |Df| over oriented arcs of length h. A semicircle has variation 2, translated symmetric-difference length 2h, and pointwise differences of one sign at each x across all shifts, proving the probability-convolution norm without symmetry. Positive shift density forces equality in the translation bound for almost every h; opposite Jordan supports at distance < π would put positive masses of both on an open family of subsemicircular arcs, forcing strict cancellation. Cross-support distances must all be π, hence both Jordan parts are opposite atoms. The wrapped variance-2t Gaussian gives the triangular-distance Fourier series with the stated normalization; its derivative in phase is the positive Dirichlet heat evolution of 1 on (0,π). After multiplication by π exp(t)/4 the time derivative for β=|b|>0 is cos(βt)+βsin(βt) plus an O_β(exp(-8t)) C¹ remainder. Fixed disjoint neighborhoods of the leading zeros have derivative of fixed sign bounded away from zero, and the leading value is bounded away from zero outside them. This gives exactly one late zero per neighborhood, no other late zeros, the stated time error, and the signed value error after using cos(π/2+arctan β+nπ)=(-1)^(n+1)β/sqrt(1+β²). For b=0 every term of the derivative is positive. Replay: RESULT.md lines 33–58. VERIFICATION.md and check.py were inspected, not executed: the 160 recorded grid and truncated-series comparisons are supplementary, not used as proof or as a certificate.

## originality

PASS

The symmetric-kernel identity and semicircle rigidity have substantial distinct catalogue coverage; the abstract nonsymmetric extension uses the same short translation argument. The supported distinction is the drifted continuous heat theorem, with strict phase ordering and the complete late critical-time law for every fixed nonzero drift. No inspected distinct statement gives those refinements, and they do not follow from the symmetric or discrete results alone. This is a bounded best-knowledge comparison, not a priority determination.

## value

PASS

The exact worst-case L1 defect gives a quantitative distinction between zero drift and arbitrarily small fixed nonzero drift: monotonicity versus an infinite alternating sequence, with complete late-time localization and signed height. The extremizers and phase ordering give the operational meaning of the coefficient rather than only bounds. This is a useful sharp semigroup result beyond the known even-kernel case; value does not rest on recomputing the Fourier multiplier.

The dated certificate retains the supplied scientific assessment, sources and limitations.
