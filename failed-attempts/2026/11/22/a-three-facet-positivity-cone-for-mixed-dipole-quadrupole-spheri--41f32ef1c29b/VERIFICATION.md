---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Legendre recurrence gives multipliers H_n=1+bA_n+cB_n; degree zero, degree one, and the limit are necessary. Exact independent symbolic expansion confirms all three barycentric identities and the positive determinant. An alternative check uses u=r^2 and m=2n+1: A_infinity-A_n=(1-u)/(2rm); the slope (B_infinity-B_n)/(A_infinity-A_n) is (3/(4r))[2(1+u)+((1-u)m+2(1+u))/(m^2-4)]. For m>=5 the slope is strictly between those of m=1 and m=3 (the residual fraction decreases for m>2). Horizontal distances to the limiting point are in ratio 1:1/3:1/m, so the two finite-point weights are positive and sum to at most 3/m<1. The two admissible pairwise intersections and the b=0 limiting-face witness expose each facet. Noncollinearity precludes simultaneous equality; the positive weights give H_n>0 for all n>=2, hence both parities yield strict finite-site definiteness by the spherical criterion. On L_infinity=0, expanding the displayed weights gives the stated positive 1/n term; with normalized measure the eigenvalues are r^n H_n. RESULT.md lines 25–89 and independent algebra support these facts; the supplied script was inspected, not executed.

## originality

FAIL

Direct exact coverage is established by the distinct Nov. 16 Resultary record 14d28644b2c5. Relabel its modulation parameters (a,b) as (b,c) and use P_1(t)=t: the domain, coefficients, three necessary and sufficient inequalities, facets, determinant, barycentric weights and strictness coincide. The comparator also proves universality. The boundary 1/n formula is a direct leading-degree expansion of its already exact weights, not an independent surviving result.

## value

FAIL

A finite irredundant covariance decision rule is intrinsically useful, but this record repeats the identical rule and proof already available for this family. The only extra displayed boundary asymptotic is mechanically read from the prior exact rational weights and does not add an independent mathematical use or a new classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
