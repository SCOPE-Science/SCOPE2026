---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Directly verify H(tp)=t^2(A(p)F(p)) with A=Z/2, positive fixed q_i=2-c/theta_i with c=(2d-1)/sum theta_i^-1. Relative projective ratios p_i/q_i are drawn toward unity under x(2-x) monotonicity, contracting their max/min spread; compactness in the open simplex and strictness imply p_n->q. The series defining log T* has bounded summands with geometric weights and a 2^-N B uniform truncation certificate; the identity T*(Fp)=A(p)T*(p)^2 conjugates radial mass to squaring, yielding the trichotomy and middle fixed limit (2/c)q. Equal theta bounds follow from 1/d<=sum p_i^2<=1; tangent linearization at uniform e has lambda=2(d-1)/(2d-1), and summing weighted quadratic terms gives coefficient 1/[B(2-lambda^2)]. Independently checked symmetric d=4 perturbation at epsilon=.001: inferred coefficient 0.45161404 vs exact 0.45161290; symbolic derivation is required for the universal theorem. No extrapolation from finite tests.

## originality

FAIL

Earlier fully read published Resultary finding dated 2026-11-02 treats the identical quadratic map with the identical normalized dynamics a(p)=A(p), G(p)=F(p), the exact same infinite-product critical radius and certified error, all-dimensional convergence, the three-case global extinction/nonzero-fixed/escape trichotomy on the entire nonnegative cone with arbitrary positive parameters. It strictly contains the principal submitted claim for its chamber, and more. The symmetric sharp bounds/curvature are additional easy consequences of that already available explicit formula and fixed-point linearization, not an original new global separatrix theorem.

## value

PASS

A uniform computable global basin boundary for a nonlinear positive high-dimensional dynamical map and its shape are mathematically motivated. Strict convergence, threshold certification and curvature are substantive objects independent of the priority failure; value is PASS for intrinsic importance, not for new authorship.

The dated certificate retains the supplied scientific assessment, sources and limitations.
