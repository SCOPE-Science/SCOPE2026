---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

PASS. At h=(1-2m)/m and r=(1+delta)/m the full population recurrence exactly reduces to x_(k+1)=(1+delta)x_k(1-x_k^2). With a=(1+delta)^(-2), y=x^(-2), direct expansion gives y_(k+1)=a(y_k+2+(3y_k-2)/(y_k-1)^2). Positive initial state is fixed, |delta| small, and all y_k>1. Uniform affine comparison for k<=S/|delta| gives y_k~k and y_k=2k+O(1+|delta|k^2+log(k+1)). Thus R(y_k)=3/(2k)+O(|delta|+(1+log k)/k^2); a^(-k)=1+O_S(|delta|k) and the weighted sum is (3/2)log n+O(1). Exact variation of constants yields the signed epsilon a^n log(1/epsilon) correction and O(epsilon) residual uniformly for s0<=n epsilon<=S. At delta=0 the absolutely summable remainder produces a finite constant. Independent recurrence iteration for n≈1.2/epsilon, epsilon=.01,.005,.002 reproduced bounded residual/epsilon for both signs; it is not an infinite proof.

## originality

PASS

PASS (best of knowledge). Leading pitchfork finite-time profiles and fixed-critical algebraic behavior are prior, but the inspected primary leading-scaling analysis and related indexed results do not state a uniform signed second-order inverse-square epsilon log(1/epsilon) coefficient with O(epsilon) remainder. More general parabolic iteration normal forms may dominate and remain a priority risk.

## value

PASS

PASS. A two-sided, jointly time/parameter-uniform second-order term with exact 3/2 coefficient and controlled O(epsilon) remainder is a motivated quantitative refinement of a tricritical finite-time scaling law, not the already-known pitchfork leading profile. The observed logarithmic correction matters precisely in the natural n|delta|=O(1) window and is not a routine renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
