---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The implication was reconstructed from the source propositions rather than accepted from the package verifier. For \(\gamma\le\alpha\), the exact rule is threshold monotonicity. For \(\gamma>\alpha\), choosing the test-score threshold and loss value one inside the universal exclusion condition forces the source's empirical-risk statistic to be at most \(\alpha\), exactly the \(\gamma=\alpha\) criterion. The same substitution applies to Proposition A.1's weighted statistic. The package's two strict finite-sample constructions also satisfy the bounded-loss constraints and make the inclusion strict on each side of \(\alpha\).

## originality

FAIL

The final theorem is implication-covered by the defining paper. Proposition 4.4 prints the exact two regimes. For \(\gamma>\alpha\), its universal exclusion condition may be evaluated at the allowed choice consisting of the test score and loss value one; this makes the excluded candidate equal to the first displayed empirical-risk quantity, so selection forces that quantity to be at most \(\alpha\). Proposition A.1 prints the same structure for known covariate-shift weights. Remark 4.5 already says Proposition 4.4 justifies choosing \(\gamma=\alpha\). The reward statement is then immediate from indicator dominance.

## value

FAIL

The conclusion is useful as exposition, but the scientific step is only a one-substitution corollary of the source's exact computational shortcut, and the source already states that this proposition justifies \(\gamma=\alpha\). Multiplying an already-covered pointwise indicator inequality by a nonnegative reward and taking expectations adds no independent mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
