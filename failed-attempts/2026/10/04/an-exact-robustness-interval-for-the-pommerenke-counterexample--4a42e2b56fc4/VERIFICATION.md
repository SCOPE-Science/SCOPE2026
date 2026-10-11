---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Keeping the Guo-Hu pair and fixed point \(z_0=400/399\), the curvature numerator and denominator are quadratic functions of the mixing weight. Independent exact arithmetic reproduced the discriminant \(36000^2\cdot103288299735\) and the roots \(0.201486508538007\ldots\) and \(0.953210606835668\ldots\); the denominator has positive coefficients on \([0,1]\). Thus the same fixed point violates the strict exterior-convexity condition exactly on the displayed interval. The source's weighted Laurent-tail argument extends to every convex mixture and keeps the family in \(\Sigma\).

## originality

FAIL

The source already supplies the same two functions, the same fixed test point, the exact derivative values there, the strict-convexity criterion and the Laurent-tail univalence argument; it evaluates the resulting expression at \(\lambda=3/5\). Replacing that fixed scalar by a variable \(\lambda\), taking the real part of the ratio of affine complex functions, and solving the resulting quadratic inequality is a routine symbolic corollary of those published inputs. Exact endpoint numbers need not have appeared previously for the scientific statement to be implication-covered.

## value

FAIL

The robustness interval is a useful quantitative annotation of the counterexample, but it is obtained by a routine one-parameter substitution and quadratic-root calculation using the same pair and same test point, and it does not classify convexity outside that test-point obstruction. Under the shared value bar, that does not constitute an independent mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
