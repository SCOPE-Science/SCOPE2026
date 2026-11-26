---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Rotate to W±=(X±Y)/sqrt(2). The two ordered cross-mode covariances are (D−A)/2 and (D+A)/2, both with common reference value d_s/2. Their future-noise terms are orthogonal to the reference variables by conditional martingale mean zero, so they decay by the respective scalar transition gains exp(−K−U) and exp(−K+U). This proves the inverse, the need for nonzero d_s in these two channels only, and almost-everywhere derivative recovery. The instantaneous triangle is convex, so every admissible control average is realizable by that constant control; its exact exponential image is the stated region including semidefinite boundaries. Orthogonal sum/difference on input and output diagonalizes the derivative up to signs, leaving singular values |d_s| times the two gains. In the two-temperature specialization the diagonal difference obeys d′=−2kd+2(T_x−T_y); its stationary initialization and positive integrating factor give sign preservation.

## originality

FAIL

The principal Brownian tomography and its stated refinements are directly implied by the published time-inhomogeneous linear-SDE lag covariance formula applied to the previously specified gyrator normal modes and control triangle. In those coordinates the selected observables are simply the two off-diagonal lagged covariances normalized by their common equal-time entry. The literature inspected did not print the full package in this notation and the textbook assumes Brownian noise. The martingale formulation replaces independent Brownian future noise by the conditional mean-zero orthogonality used in the same regression identity, without a distinct identification or control result beyond that identity.

## value

FAIL

The two cross-mode statistics are convenient descriptors but here the reconstruction, attainable set and Jacobian reduce to the scalar linear-SDE regression, the exponential image of a convex triangle, and differentiation in orthogonal coordinates. No nonmechanical inverse, sharp statistical limitation, or control obstruction is established in the stated scope. This is a routine specialization of the available results, not a distinct exact invariant requiring new analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
