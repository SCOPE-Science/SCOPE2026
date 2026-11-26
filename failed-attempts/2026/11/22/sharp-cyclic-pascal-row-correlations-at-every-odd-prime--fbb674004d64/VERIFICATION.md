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

Lucas's theorem gives the digit weight x+1. Splitting by the low-digit carry gives the two cyclic cross-sum coefficients as sums of products; summing the arithmetic polynomials gives the stated A and B. At lag one, B=p and the high-block zero-lag sum is S_p^(r-1), so the affine recurrence gives alpha_p S_p^r + (1-alpha_p)p^r from H_0=1. Both arrays have the same moments. After dividing by S_p^r the centering correction is theta_p^r with theta_p=3(p+1)/(2(2p+1))<1, and the variance is positive. For fixed h>1 the recursion reduces to smaller lags; the two displayed polynomial differences give strictness for nonzero digits at q>=1 and for one-digit lags d>1. The d=0 identity then gives precisely powers of p as maximizers; positivity and rationality follow by induction. Independent replay: `python3 /workspace/reproduce_frozen.py 4` checked 806 depth/lag pairs by counting original binomial entries and directly summing cyclic products, at p=3,5,7,11. The frozen `artifacts/verify.py` is present despite not being listed by the shallow excerpt; it was inspected, not executed. The finite tests corroborate the proof only.

## originality

FAIL

A distinct same-day published record explicitly states the same central all-odd-prime fixed-lag cyclic Pearson theorem, recursion, sharp constant and complete maximizing set, and additionally states a second tier and the infimum. This is demonstrable coverage, not a priority determination. Its exact finite carry recurrence also mechanically gives the assigned record's explicit lag-one formula, so that display does not support a separate repair.

## value

PASS

As mathematics, the all-prime sharp extremum and its complete equality set answer a natural question about dependence between separated Pascal rows; one-row digit counts alone do not identify which shifts preserve the most correlation. This assessment of the theorem's significance gives no separate contribution credit to a record with the documented material overlap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
