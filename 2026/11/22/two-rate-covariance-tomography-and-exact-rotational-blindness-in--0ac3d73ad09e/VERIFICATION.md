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

Renewal from zero gives the Gaussian age mixture and the reset covariance 2∫exp(−ru) exp(−Ku) D exp(−Kᵀu)du. The integrand is strictly positive definite at finite u, so C₁, C₂ and Δ=C₁−C₂ are strictly positive definite. The two stable Lyapunov equations subtract to KΔ+ΔKᵀ=Q; in dimension two every possible antisymmetric part of KΔ is ωJ, and the first equation then fixes D. With M=Δ⁻¹C₁ the off-diagonal slope of D is (JM−MᵀJ)₁₂/2=(M₂₂−M₁₁)/2. The single linear equality and the strict inequalities tr(K)>0, det(K)>0 and Dᵢᵢ>0 yield the complete fiber, including infeasible h=0,d₀≠0; uniqueness of each stable Lyapunov solution proves sufficiency. As a check of this infeasible branch, take r₁=1,r₂=2, Δ=I and C₁ with diagonal 2 and off-diagonal 1/2, C₂=C₁−I. All covariance order checks pass, but h=0 and d₀=3/4. Unequal diagonal damping gives nonzero h, and the covariance as a function of parameters is rational, so the exceptional algebraic condition is nontrivial. In the blind family, whitening by D⁻¹/² gives damping κI plus a skew matrix, so the age-specific covariance is (1−exp(−2κt))D/κ, independent of rotation. The resulting exponential mixture gives the full one-time equality and the stated C_r, whereas unreset stationary circulation is controlled by K(D/κ)−(D/κ)Kᵀ=2ωJ/κ. The supplied exact-rational checker was inspected, not run; its finite covariance checks cannot prove the entire inverse or equality of full laws.

## originality

PASS

The distinct content is the necessary-and-sufficient observable two-rate criterion, complete physical inverse fiber and admissibility test. The age mixture, Lyapunov relation and commuting-skew blindness mechanism are known inputs; the all-rate family is a resetting consequence of that mechanism, not an independent discovery of rotational blindness.

## value

PASS

The two measured covariances directly decide whether a natural controlled stationary experiment identifies both bath coefficients and the unconstrained planar drift. The complete feasibility test and open nonidentifiable fiber are more informative than generic dimension counting. The physically different all-rate example makes clear what can still be hidden even by finer one-time observations, without requiring that known mechanism to carry the novelty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
