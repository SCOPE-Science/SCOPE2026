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

For the two difference vectors X−Y and X−Z their single-coordinate covariance matrix is [[2,1],[1,2]], giving determinant 1+4(a+b)+12ab in the joint Gaussian integral; the same-pair integral gives offset 0, and the product of means offset 16ab. Centering gives coefficients (1,−2,1). Kernel degeneracy kills every different unordered pair, retaining 2/[n(n−1)] exactly. Convex decrease of z^(−d/2) with gap ratio 3 gives strict positivity, and four-point mixed increments rule out proportionality unless a=b. The factored geometric term is (1−16(a−b)²/[1+4(a+b)]²)^(d/4). The centered residual tends to 1 when dab→∞, to g(uv) in the critical scaling, and is asymptotic to 4dab/[1+4(a+b)] when dab→0 (with remainder O(d(d+1)(ab/[1+4(a+b)])²)). This yields all three limits, the sharp subcritical log rate and the fixed unequal-bandwidth limit. For strictness at criticality, the given projected Gaussian exponential has mixed moment exp(4(u+v)²)g(uv), and its random exp(2uV) dependence at fixed S,T rules out proportionality to the v projection. Thus the normalized critical expression, not merely g(uv), is strictly between zero and one for u≠v.

## originality

PASS

Passes to best current knowledge for the explicit Gaussian mixed determinants and the sharp normalized cross-scale law, not for U-statistic degeneracy, the general covariance polarization, or the existing one-bandwidth variance and adaptive kernel methodology. The closest same-statistic theorem gives the exact variance identity for one kernel, which yields a generic mixed inner product by polarization but not the evaluated mixed-bandwidth determinant or critical correlation. The similar two-sample papers inspected do not state that Gaussian cross-bandwidth law in their compared results.

## value

PASS

Multiple bandwidths are used for multiscale tests; this exact covariance determines the null redundancy of pairs of bandwidths and discloses a sharp scale separating near perfect correlation, finite correlation, and decorrelation. The nontrivial critical dependence and its small/large-scale limits go beyond a re-evaluation of the known one-bandwidth variance. In particular, decorrelation can occur despite very small raw variances and is not a power assertion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
