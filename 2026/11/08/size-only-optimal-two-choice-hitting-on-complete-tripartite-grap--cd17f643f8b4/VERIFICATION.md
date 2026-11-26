---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Under the proposed priority, a B or C vertex hits the target whenever it is offered, with positive probability 1-(1-1/d)^2; from A one step first reaches B or C. Thus the proposed chain is transient off the target and the three-state system gives its unique finite positive hitting values. Its coefficients follow by enumerating two ordered independent offers, with repetition. I independently expanded both Cramer identities symbolically and checked strict positivity of the expanded P on a-2,c-1,b-c >= 0, including the constant term. The numerator of H_C-H_B vanishes precisely at b=c; the determinant is positive because the transient matrix has spectral radius less than one. The resulting order makes the rule attain the one-step Bellman minimum. For any competing strategy, iteration of the Bellman inequality up to the target or step N gives a lower bound by the candidate value on the expected elapsed time plus the bounded terminal residual. For any competitor of finite mean the residual tends to zero, and infinite mean cannot improve the candidate. This handles adaptive strategies and the tie case without a stronger stochastic-dominance assertion.

## originality

PASS

The supported distinct claim is the parameter-uniform size order, including the exact equality boundary and its evaluated three-state system. The minimum-value control rule, existence of an optimal stationary rule and a general strategy algorithm were known. The inspected sources did not supply the size ranking, nor a stronger ordering theorem covering this family.

## value

PASS

This is an explicit structural decision rule for a natural graph family. It resolves every ordering, including ties, across an unbounded range of part sizes; the nontarget classes on opposite parts are all one edge from the target, so distances alone do not decide their ranking. It avoids numerical or graph-specific strategy optimization. The quotient system alone, with the ranking assumed, would not supply this contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
