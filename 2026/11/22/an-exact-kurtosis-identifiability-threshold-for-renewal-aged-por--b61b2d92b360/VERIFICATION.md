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

Substitution y² gives the beta seed moments and independence multiplies each by the corresponding exponential-age gamma moment. In particular let b=3/2+1/σ: the compact seed's fourth and sixth normalized moments are 3b/(b+1) and 15b²/((b+1)(b+2)); b strictly decreases and both expressions strictly increase in b. For m=2,3 the log derivative of Γ(1+mu)/Γ(1+u)^m is m[ψ(1+mu)−ψ(1+u)]>0, and u=2/(σ+2) strictly decreases. This proves strict monotonicity for both ratios; K has endpoint limits 6 and 9/5 and crosses 3 exactly once. The symmetry cumulant identity then reduces its sixth cumulant at the crossing to S−15. For independent strict sign verification, Euler's gamma product gives the factor ∏_{n≥1}(1+u/n)^m/(1+mu/n). The tail log is in [0,m(m−1)u²/(2N)] by differentiating each log factor and comparing ∑_{n>N}1/n² with the integral. Exact fixed-point floor/ceiling arithmetic at N=2500 gave K(1.14) in (3.00639481,3.00688277), K(1.15) in (2.99833820,2.99882177), and S(1.14) in (14.59190752,14.59901485). The same integer recurrences are replayable in /workspace/branches/audit_gamma.py. This verifies the sign without depending on the frozen checker’s float conversions of interval endpoints. The audit is for the independent renewal mixture, not a solution of a nonlinear PDE with an imposed source or finite-sample identifiability.

## originality

PASS

Pass is for the global standardized-moment identifiability law and its unique Gaussian-fourth-moment crossing with strictly negative sixth cumulant. The free shape, renewal law, stationary integral, and mixed even-moment recipe are covered or immediate from known formulas; they are not the originality basis. The source integral yields the ratios but does not supply the joint range, invertibility, and signed standardized sixth-cumulant classification as a stronger result.

## value

PASS

The normalized statistic is informative for a natural physical family even when length and reset rate are unknown: one exact fourth moment uniquely identifies the nonlinear exponent over its whole finite range. The unique exponent matching a Gaussian at fourth order has a proved nonzero sixth-order diagnostic, so the result distinguishes parameter identification within the model from Gaussian identification across models. This is not a claim about estimator performance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
