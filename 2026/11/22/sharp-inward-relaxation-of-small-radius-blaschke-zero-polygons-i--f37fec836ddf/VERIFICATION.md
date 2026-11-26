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

Summing the boundary Poisson kernels and applying Parseval gives half the variance as E=Σ r^{2m}|p_m|² for normalized roots. Fix one maximal root at 1. Compactness gives attainment, and the regular-polygon energy d²r^{2d}/(1−r^{2d}) forces p_m→0 for m<d at every global minimizer; Newton's identities and the root at 1 then force z^d−1. The first d−1 power sums q are local analytic coordinates there. On a fixed small convex coordinate ball, the Hessian of the tail is O_d(r^{2d}) by geometric growth bounds on differentiated power sums, whereas the positive quadratic terms have Hessian ≥2r^{2d−2}I. The unconstrained minimum is interior by the boundary energy bound and unique by strict convexity. With P=z^d−1+Σ b_j(z^j−1), the first variations are δp_m=−m b_{d−m} for m<d and δp_d=dΣ b_j, by summing the simple-root perturbations. Thus ∂p_d/∂q_m=−d/m. Writing t=r², the stationary equations after dividing by t^m have analytic form q_m+Σ_{ℓ≥d} t^{ℓ−m}p_ℓ·overline(∂p_ℓ/∂q_m)=0 and identity Jacobian at (q,t)=(0,0). They give q_m=O(t^{d−m}) and q_{d−1}=d²t/(d−1)+O(t²). The resulting b_1=−d²t/(d−1)²+O(t²) gives the stated root jet, with strictly negative radial derivative for every root except 1. This makes the unconstrained optimizer feasible and proves global uniqueness, up to rotation, and conjugation symmetry. At order r^{2d+2}, the contributions to half-variance from p_{d−1} and p_d are respectively +d⁴/(d−1)² and −2d⁴/(d−1)²; the other terms are O_d(r^{2d+4}). This verifies the coefficient and suboptimality of the regular polygon. Scope is fixed d≥3 and sufficiently small r only. CHECK.py was inspected, not executed; its rational jet checks and trial-polynomial energies are supplementary, not evidence of global uniqueness by themselves.

## originality

PASS

The distinct contribution is unrestricted radial relaxation under a fixed outermost-zero radius for every fixed d≥3, with global uniqueness and sharp first shape and energy corrections. The Poisson representation and degree-two phenomenon are credited. Checked statements do not imply the higher-degree theorem; historical priority remains qualified.

## value

PASS

Fixing the largest zero modulus gives a natural aperture for the boundary-covering map. The variance measures nonuniformity of its angular speed. It is not routine to decide whether equal-radius symmetry persists when radial freedom is allowed; here the global minimizer breaks that constraint in every covered degree, with one active radius, an explicit jet for all zeros and a strict sharp energy gain. The result is useful within the fixed-degree small-radius regime without assuming an effective radius threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
