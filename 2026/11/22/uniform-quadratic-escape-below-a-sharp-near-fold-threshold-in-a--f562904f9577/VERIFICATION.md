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

Rechecked the complete corrected RESULT.md. In the frozen endpoint proof, exclusion of a two-cycle in the zero set did not exclude a single directed transition between its two points. The repair rules out each arrow independently: x'=x+y rules out either self-arrow, and W is unchanged at a zero of the drift whereas W(P+)-W(P-)=2z>0. Then Q+Q∘F has no zeros, is continuous and coercive, and attains a positive minimum. Direct expansion of the coboundary and completion of the square prove strict-chamber drift; comparison with R+(1+b)R²/2 yields both claimed uniform liminf bounds (not a common transient). Pointwise escape gives no invariant probability by dominated convergence. Subtracting the signed two-cycle residuals gives X=2/(1+b), and their remaining common part gives kz²-az+K=0; both the positive double root and the absence of any earlier positive root are checked. On the cited slice the rational difference is 1/5210. The corrected theorem retains the closed chamber without claiming that escape ceases immediately beyond it.

## originality

PASS

Best-of-knowledge pass on the closed global escape chamber and quantitative rate only. The same-map numerical literature and the strongest exact overlap establish different statements; the known slice fold is credited as a comparator, not counted as original. The endpoint correction changes the proof, not the originality scope.

## value

PASS

For a model introduced to exhibit recurrence without fixed points, a certified all-orbit nonrecurrence chamber answers a different dynamical question from cycle searches. Inclusion of the degenerate drift endpoint and the exclusion of even unbounded-support invariant probabilities are substantive. The fold comparator gives a parameter-exact measure of the remaining gap without claiming its classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
