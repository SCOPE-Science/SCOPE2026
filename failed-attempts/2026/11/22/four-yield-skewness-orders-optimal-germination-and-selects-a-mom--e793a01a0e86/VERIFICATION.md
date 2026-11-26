---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

FAIL

The opening Finding says that fixing the moments leaves an exact one-dimensional ambiguity in the optimal policy. This is false as a general assertion on the stated domain: the feasible probability set can be a singleton, and it can be a nonsingleton segment with the same optimizer g=1 throughout. For example take r=(1/2,1,3/2,2), the nonsingleton moment slice in the record's witness, and change s to 1/4. Each yield exceeds s, so all feasible growth derivatives are strictly positive and every law gives the same optimal policy. The precise numbered theorem (unlike the opening sentence) allows these cases and is correct. The rank-three moment constraints identify a one-dimensional signed difference proportional to the barycentric weights, normalized by the third moment; the reciprocal divided difference gives the exact derivative factor. Strict concavity follows from mu>s and yields the optimizer comparison with saturation, and the quartic identity at each positive yield gives the harmonic-mean threshold and equality case. The feasible-law endpoint really minimizes growth simultaneously for all g>0; at g=0 the laws tie. Exact rational recomputation of the witness confirms the matched moments, the +/-1/50 boundary derivatives, the quadratic for the robust optimizer, and the root 0.89243699474278668… . Frozen support was inspected, not executed; see /tmp/opencode/frozen-review-replay.py (germination) for the independent arithmetic. The theory applies to fixed positive yields, iid environments and the stated constant fraction, not to field performance or larger alphabets.

## originality

FAIL

The controlling exact sensitivity, not merely its sign, is a direct substitution into the published arbitrary-node reciprocal divided-difference formula. The third-moment coefficient for any test function is its third divided difference, because the equal lower moments kill the lower coefficients of the interpolating cubic. This specializes immediately to the displayed growth-derivative formula, leaving the usual concavity and harmonic criterion to give the policy classification. Thus the general formulas actually inspected, together with the classical seed-bank objective, cover the mathematical core mechanically. This verdict does not assert an earlier publication of the same biological wording, and does not depend on inaccessible sources.

## value

FAIL

The ecological question is motivated, and the example distinguishes partial and complete germination at equal mean and variance. But the exact coefficient is the standard reciprocal divided difference; the threshold, common adverse endpoint and support size follow by textbook interpolation and one-variable concavity, and the rational witness is an instance of choosing survival between unequal harmonic means. The review did not identify a useful, distinct nonmechanical claim that a repair could preserve.

The dated certificate retains the supplied scientific assessment, sources and limitations.
