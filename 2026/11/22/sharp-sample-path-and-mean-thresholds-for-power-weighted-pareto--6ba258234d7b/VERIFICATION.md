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

Independently integrating the survival-indicator covariance gives the mean without truncated-moment cancellation. Write min(1,tX)=t∫_0^{1/t}1_{X>x} dx. For 1≤x≤y its two indicators have covariance y^(-α)(1−x^(-α)); below x=1 the covariance vanishes. Tonelli gives divergence at β≥2 by the inner t integral for x,y>1. For β<2 it gives 2/((2−β)(α+1−β)) times ∫_1^∞ x^(β−α−1)(1−x^(−α)) dx whenever β<α, and divergence for β≥α by the large-y tail of the preceding y integral (whose integrand is y^(β−α−2)∫_1^y(1−x^(−α))dx). The last integral gives the boxed rational mean, including α=1 and 2, and the three mean pole constants follow. On each fixed sample, below 1/max X_i the empirical function is exactly t times the sample mean. The population corrections give leading squared orders t^(2α)/(1−α)^2, t^2 log²(1/t), or t² times the nonzero almost-sure squared centered sample mean. Integration yields the claimed path thresholds and constants, with factor 2 for the third-order pole at α=1. For β below the mean threshold, the centered functions are measurable as Hilbert-valued variables (the map from X is continuous there by the t-Lipschitz bound), with second moment equal to the trace just computed; the iid Hilbert CLT and continuous norm square give the stated limit. Reviewed the frozen verification notes and code; the recorded 83 checks are corroboration, not the basis for the real-parameter claims.

## originality

PASS

Best of current knowledge: the new part supported here is the exact joint phase diagram, trace and boundary laws for the specified unfitted Pareto null at a singular power weight, not the minCF, weighted-distance testing framework or the Hilbert CLT itself.

## value

PASS

Singular weighting is a natural endpoint stress test of an established goodness-of-fit discrepancy. Merely checking that each observed sample gives a finite number can conceal a non-integrable statistic under the null. The exact gap in thresholds, distinct blow-up laws and calibration trace supply information needed for choosing weights, without claiming fitted-null calibration or performance under alternatives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
