---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The per-period log growth difference is the difference of the two equally weighted Monod averages; common mortality cancels, and the last incomplete period contributes a bounded error to the log ratio. All four factors in the logarithmic derivative are positive even when the low level is zero. The ratio H of the two quadratic factors is strictly increasing, so R' has at most one zero. Its sign at v=0 is the sign of m^2-K1*K2 and its sign at v=m^2 is strictly negative. Equality in the first test gives strict decrease in the open interval, not a second crossing. The endpoint heights satisfy R(m^2)<R(0); hence in the single-maximum case the two interior sign changes occur exactly for R(0)<a2/a1<R(v*). The lower endpoint does not count as an interior switch, and the maximum gives a tangency. Independent substitution and root calculation reproduce 0.1851993002684 and 0.7405149854459 and the stated sign order; at maximal variance the witness net exponents are 39/110 and 7/15, the minima on the interval. The proof is uniform over the stated domain, with no feedback assumption hidden in the averaging. The supplied check.py was inspected, not executed; the independent algebra and numerical evaluation are distinct from its reported rational tests.

## originality

PASS

Best-of-knowledge pass for the sharp variance criterion in the prescribed two-level nutrient model, not for Monod concavity, averaging itself, or fluctuation-driven changes of competitive outcomes in general.

## value

PASS

Concavity makes each mean growth response decline as variance grows, but does not order the declines. The theorem gives a sharp, interpretable boundary for reentrant relative growth, including an exact witness where both species still have positive net exponents. This is a useful benchmark for fluctuation models; it neither predicts coexistence or exclusion in a coupled system nor provides empirical validation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
