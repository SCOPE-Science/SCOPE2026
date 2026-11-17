---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For a nondegenerate noncircular ellipse a>b>0 and d>=1, the Joukowski parametrization z=Au+B/u and conjugate w=Bu+A/u gives ideal generator Q with bidegree (2,2). Hermitian bidegree-(d,d) restriction has kernel Q times Hermitian bidegree-(d-2,d-2), dimension (d-1)^2; hence the full intensity-profile real span has dimension (d+1)^2-(d-1)^2=4d. Its highest Fourier coefficient is necessarily real because only |z|^(2d) contributes, eliminating sin(2d theta). Discrete orthogonality at 4d equally spaced points determines all lower modes and recovers the top cosine iff cos(2d theta0) != 0, otherwise rank 4d-1. The two involutions of Joukowski coordinates generate a nonunit dilation, forcing any rational quotient p/q of equal-ellipse intensities to be constant unimodular. Independent exact symbolic Hermitian profile ranks at degrees 1,2,3 were 4,8,12 with kernel dimensions 0,1,4. The circle boundary d>=1 behaves differently (dimension 2d+1, phase nonuniqueness). The claim's linear full-profile minimum is not a nonlinear phase-retrieval lower bound.

## originality

FAIL

Complete stronger published same-day theorem covers every mathematical conclusion; no distinct original remainder.

## value

PASS

Exact dimension and optimal deterministic full-intensity sampling on a noncircular ellipse form a natural, substantive inverse problem. The mathematical result has intrinsic value even though this particular presentation is already covered by a separate complete public theorem; correctness and value do not rescue originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
