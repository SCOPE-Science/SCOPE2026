---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For SPD A and candidate direction d, η*=−(dᵀA²e)/(dᵀA²d), so the smoothed error is oblique projection P_d e=(I−d(dᵀA²)/(dᵀA²d))e. Its exact Euclidean norm is ||d|| ||A²d||/(dᵀA²d). Applying the sharp positive-definite antieigenvalue/Kantorovich extremal inequality to B=A² with eigenvalues m=λmin(A)² and M=λmax(A)² yields ||P_d|| <=(m+M)/(2√mM)=(κ²+1)/(2κ). Endpoint-eigenspace weights attain equality for A=diag(1,κ) and d=(κ,1). Independently recomputed exact rational P, singular norm and equality errors for five κ. Residual contraction is automatic in A² norm; κ>1 admits strictly increasing Euclidean error. All scope and one-dimensional exception checked.

## originality

FAIL

FAIL on prior implication, not mathematical correctness: the boxed extremal factor is exactly the classical sharp antieigenvalue operator-cosine law for an SPD B=A², combined with the standard norm of a codimension-one oblique projection. Preexisting operator-trigonometry literature explicitly addresses minimum-residual iterative schemes. The frozen proof itself explicitly performs this standard substitution and has no further distinct mathematical classification beyond its two-endpoint equality witness. The exact error statement is a direct corollary of this stronger prior framework without a separate nonstandard theorem.

## value

PASS

The solver interpretation is substantively motivated: residual improvement can conceal Euclidean error growth; a sharp κ-dependent bound and two-dimensional witness can be useful to practitioners. This mathematical usefulness does not remedy covered originality, so the decision is failed. Whether the synthesis is sufficiently routine for independent publication is a secondary risk, not relied upon for rejection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
