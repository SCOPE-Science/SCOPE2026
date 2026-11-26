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

PASS

Put s=σ², m=E X and d=SD(X)=m√(e^s−1). The common positive-z support is 0<z<m/d, and the common Jacobian cancels at x±=m±dz. Completing the square gives log f(x)=constant−(log x−(μ−s))²/(2s). Subtracting its two evaluations yields artanh(dz/m)[−3−log(1−(dz/m)²)/s], as in the record. The bracket increases strictly from −3 to +∞, so the unique interior positive crossing has (dz/m)²=1−e^(−3s), strictly between 0 and 1. Division by e^s−1 gives κ²=e^(−s)+e^(−2s)+e^(−3s), proving strict decrease, the √3 limit, and the large-σ equivalent. The cubic in q=e^(−s) is strictly increasing in q between its values 0 and 3, yielding the unique quoted one-SD transition. This is a positive-radius crossing; equality at z=0 is excluded. The supplied script was inspected, not executed; its finite checks do not establish the theorem for all σ.

## originality

PASS

Limited to the explicit finite-shape arithmetic-mean-reflected density formula and its threshold: these are distinct from the earlier integrated-tail results and the Gamma analogue in the inspected material. No checked statement explicitly covers the mean-reflected lognormal crossing or the more general equal-density-pair rule. This finding does not establish priority or a nonroutine contribution; the direct reduction to the standard density is decisive against scientific value.

## value

FAIL

The statistic is naturally normalized but its precise value is a routine deduction from the textbook density and moments. The log density is quadratic in log x around the log-mode, so equal-density points have product equal to the squared mode. At x±=m±dz their product is m²−d²z²; the entire formula follows by solving that single equation, with the signs from the same quadratic difference and the threshold by setting z=1. The record identifies no substantive use requiring this precise crossing or cubic cutoff and establishes no further property beyond this direct calculation. The value decision does not depend on inaccessible papers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
