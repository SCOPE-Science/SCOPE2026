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

Write G for the weighted sum of branch passabilities. On the positive-payoff region log F is strictly concave: log(1-exp(-x0)) is strict in x0 and log G is strict in the branch coordinates. At a common branch marginal tau the efforts are [log(w_i/tau)]_+, G=tau sum_i(w_i/tau-1)_+, and trunk marginal equality gives exp(x0)=1+G/tau. Thus total effort as a function of tau is continuous and strictly decreasing on (0,w_1), ranging from infinity to zero. Setting tau=w_j verifies the thresholds and that equality still gives zero effort to j. Exponentiating the budget yields the stated polynomial, and exp(x0)-exp(x1)=sum_{i>1}(w_i/tau-1)_+ verifies strict trunk dominance only after the second activation. For geometric weights the candidate has finite support. The concavity tangent inequality bounds the log-payoff difference of any positive-payoff competitor by the common budget multiplier times the total effort difference: all omitted-coordinate marginals are no larger, and the inequality extends by finite truncation and summability. Strict concavity gives uniqueness. The geometric-sum factor at j is q^(-(j-1))/(1-q) times [1-q^(j-1)(1+(j-2)(1-q))]; adding the log ratios gives the stated expansion and inversion. For m=1 the limiting trunk advantage is zero, consistent with the one-active-branch case; the positive large-budget advantage in Proof 4 is in its k>=2 case. RESULT.md Proofs 1–5 and checker.py were inspected; the finite random-allocation tests are not the global certificate.

## originality

PASS

The product of route passabilities and additive accessible habitat are established, as is marginal equalization. The supported distinct claim is the coupled continuous-budget staircase, its strict common-barrier advantage once branching is active, and the geometric-weight support asymptotic. None of the strongest inspected comparators supplies this combination or a theorem that gives the coupled thresholds directly.

## value

PASS

A common downstream bottleneck and ranked habitats are natural features of the ecological model. Full budget thresholds and the direction of the trunk-versus-branch effort inequality are usable structural benchmarks beyond numerical optimization at a few budgets. The geometric sequence isolates a precise law for diversification across many small tributaries. This is an idealized mathematical benchmark, not an empirical prescription.

The dated certificate retains the supplied scientific assessment, sources and limitations.
