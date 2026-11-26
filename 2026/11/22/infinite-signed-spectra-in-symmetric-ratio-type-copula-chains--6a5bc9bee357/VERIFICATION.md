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

The mixed derivative uses only f and f′ at separate coordinates and is continuous under the denominator condition. Copula admissibility makes it nonnegative with uniform marginals, and symmetry gives a compact self-adjoint Markov contraction preserving the centered space. For positive θ, θ|f(0)|²<1 and the geometric expansion has centered derivative features (u f(u)^j)′. The norm bound on these features gives a finite sum of the traces of their weighted positive rank-one operators. Infinite rank follows from the Vandermonde independence of the first m integrated features at arbitrary distinct interior nodes. Independently of the proof's valid bump approximation, H_m is exactly the form matrix of P_θ at the centered indicators 1_[0,u_i]−u_i, by stationarity and the copula formula. This also checks the transfer for negative θ: Cauchy's determinant and diagonal scaling give determinant sign (−1)^(m(m+1)/2) for every leading block, so the LDLᵗ pivots alternate starting negative and the matrix has the stated strictly signed indices. The corresponding indicator spans yield unbounded dimensions of both signs for P_θ. The covariance identity γ_n=⟨h,P_θ^n h⟩ then gives all finite-difference inequalities in the positive case from the spectral measure on [0,1], and strictly alternating covariances for a negative eigenfunction. At θ=0 the centered operator vanishes. The 2024 Table 1 row (7) confirms the cited generator and range; θ=1 fails denominator positivity at the origin and is correctly excluded. CHECKER.py was inspected, not executed; its finite diagnostics do not prove the unbounded inertia result.

## originality

PASS

The supported distinct claim is the full centered transition-operator signature for the admissible ratio family, including infinitely many modes of both signs throughout its negative regime. The family, quadrant dependence, and parameter ranges are prior. The finite signature is a specialization of classical Cauchy/sign-regular matrix theory, not a new matrix-inertia principle, and complete monotonicity follows from the established positive spectrum by the spectral theorem.

## value

PASS

The classification shows exactly why the sign of a quadrant-dependence parameter does not determine the signs of all time-series covariances. Positive parameters yield covariance moment sequences for every centered observable, while even strictly negative quadrant dependence in this family coexists with infinitely many positive as well as alternating modes throughout the admissible nonsingular negative range. The result is a structural property of an established family, not merely a new use of terminology for Cauchy matrices or a two-point numerical witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
