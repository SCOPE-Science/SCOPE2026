---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

Direct congruence gives 2x2 SPD block with diagonal theta,b and offdiagonal sqrt(theta*v), and m copies of c. Since lambda_+>b>c, kappa=lambda_+/min(lambda_-,c); lambda_-=c iff theta(d-v)=cd, possible uniquely for v<d. Before collision block condition number decreases up to theta=b by maximizing theta(b-v)/(theta+b)^2, after collision lambda_+/c strictly increases. This establishes unique theta*=min(b,theta_coll), transition v1=d²/b and both closed minimum formulas. Three eigenvalues imply generic exact CG minimal-polynomial degree 3; two eigenvalues yield universal <=2 CG steps. Independent rational samples validate numeric examples but not the entire real parameter domain.

## originality

PASS

The finite perturbation exact two-threshold classification of optimal reference-vector scaling versus universal PCG termination is not implied by inspected perturbative bounds, general diagonal scaling algorithms, or other separately published preconditioner risk theorems.

## value

PASS

Motivated distinction between condition-number minimization and finite-step Krylov termination for recycled spectral preconditioners; exact transition and divergence of a forced two-step scale exhibit a quantitative cost of imperfect reference eigenvectors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
