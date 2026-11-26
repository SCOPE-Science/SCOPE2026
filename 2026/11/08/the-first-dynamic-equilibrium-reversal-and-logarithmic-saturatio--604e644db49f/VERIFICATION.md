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

The two ensembles have the same graph-distance compatibility and normalization 2b, but different measures on terminal configurations. From the cited exact formulas, put A(t)=sum_{k=b}^{2b−1} t^k(1+t); it increases strictly from 0 to 2b and the equilibrium root solves A(t)=1. Logarithmic differentiation at that root gives S=b/[t A'(t)], reproducing the stated reciprocal and giving monotone algebraic bounds. My independent /workspace/branches/audit_ladder.py used dyadic root brackets, those polynomial derivative bounds, and the composite midpoint rule rather than the frozen trapezoid code. For the dynamic term it enclosures e^v for v=−P_b or v=2H_b−1/b by the positive Taylor series with directed integer rounding, bounds the remainder by 7/6 times term 41 for 0<=v<=6, and reciprocates. From |P'|<=2b, |P''|<=2b² and e^P<=1, the scaled midpoint error is at most b³/(4N²). For N=4096 every exact comparison was strict: S−J<0 at b=1,...,9, with S_9−J_9 in [−0.0001030740,−0.0000813480], and S_10−J_10 in [0.0026574377,0.0026872401]. Separately q=t^b satisfies −log q=2b artanh(q(1−q)); q(1+q)<=1 bounds q uniformly away from 1. For x=2bq, this yields x=O(log b), then x+log x=log(2b)+O(log² b/b), and monotone inversion gives x=W(2b)+O(log² b/b). Substitution in 1/S gives 1+1/x+O(q). The derivative of x/(1+x) is O(1/log² b) near W(2b), giving the asserted O(log b/b) error. Expanding 1/(1+W) with W(z)=log z−log log z+O(log log z/log z) gives the stated second coefficient. This verifies the first crossing, not that all b>=10 have the same strict ordering. The cited dynamic limit is background, not a new deduction from the ten comparisons.

## originality

PASS

The distinct contributions supported by the available comparison are the certified first crossing at b=10 and the quantitative two-row equilibrium expansion. Do not credit as new the exact ladder formulas, the already tabulated reversal signs at separated ranges, limiting coverage or the general Lambert-W mechanism. The strongest indexed match is the identical record; the nearby variance result and one-dimensional asymptotic literature do not directly supply the two-row claims. Primary body/table retrieval was limited, leaving explicit priority risk.

## value

PASS

For this shared admissibility rule, dynamic sampling and uniform sampling of maximal configurations are different scientific ensembles. Locating their first strict inversion resolves what the older widely spaced samples could not, including the close sign at nine. The asymptotic also quantifies the slow static approach to its limit, which matters for finite blockade ranges where a qualitative limit alone is not predictive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
