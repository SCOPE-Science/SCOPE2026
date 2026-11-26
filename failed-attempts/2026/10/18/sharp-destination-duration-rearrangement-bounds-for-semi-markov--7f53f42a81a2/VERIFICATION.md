---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

At visit n the expected holding-time contribution is P^n μ, so Tonelli gives the coupling-independent finite mean Nμ. The second moments of passage sums truncated at n visits satisfy the displayed renewal recurrence with the truncated first moment on the right. They are bounded by N(ν+2||m||∞ μ); monotone convergence permits passing to the second-moment equation and solving it. At each row, write X=H_i, Y=m_{J_i}; integrating the joint survival function computes E[XY]. At fixed thresholds s,t with marginal tail probabilities p,q, the Fréchet bounds max(0,p+q−1) and min(p,q) hold, and quantile reversal or alignment attains them at every threshold simultaneously, also for atoms. If both laws are nonconstant, there are positive-length threshold intervals for each on which p,q are in (0,1), so the integrated gap is strictly positive. N_{ik}>0 exactly when k is reachable from i among transient states (including the start). Thus the condition at line 23 means the interval has positive width, not that no kernel attains the endpoints. Pooling equal destination means or splitting their quantile intervals gives the same extrema. Fresh rowwise kernel mixtures interpolate the variance because μ and ν are fixed. Independently recomputed the continuous example by conditioning on the two branches: sorted branches have variance 1/12, with conditional mean separation 0 or 2, giving 1/12 and 13/12; the independent kernel has within-branch variance 1/3 and separation 1, giving 7/12. The uploaded exact feedback script was inspected, not executed; its enumeration is not a continuum proof.

## originality

FAIL

The claimed envelope, simultaneity, attainable interval, and width are direct consequences of the known semi-Markov reward moment formula and classical fixed-marginal rearrangement; no distinct remainder requiring an additional network theorem was established. This is evidence of prior implication, not a claim that an examined source prints the identical network formulation. Inaccessible papers do not drive the finding.

## value

FAIL

The fixed-marginal sensitivity question is useful and the example illustrates a real effect. As a standalone scientific finding, however, the envelope reduces directly to classical two-variable coupling applied to the existing linear moment formula. The extra exact statements use only positivity and mixture linearity, and the example is a two-branch substitution rather than an independent unresolved invariant. The package is useful exposition, but does not establish a separate valuable result beyond the direct deduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
