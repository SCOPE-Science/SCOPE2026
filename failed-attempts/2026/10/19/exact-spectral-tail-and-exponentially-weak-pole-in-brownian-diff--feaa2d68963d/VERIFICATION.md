---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

In stationarity the age since the last reset has survival ⟨1,exp(−tT_μ)1⟩ with T_μ=λ+μ(I−P) by Feynman–Kac; existence and uniqueness of the position marginal follow from almost sure divergence of the past integrated hazard. The age survival is a positive spectral mixture and mixing the Brownian heat kernel against each exponential age gives a Laplace density of inverse length √(s/D). The resolvent identity gives H(z)=φ_a(μ+z)/(1−μφ_a(μ+z)); μφ_a(u) decreases strictly from infinity to below 1 on (0,μ], giving the unique mode below the continuum. Jensen gives θ<a and the nonconstant eigenfunction (λ+u)^−1 gives an overlap strictly between zero and one. Its mass is −1/(μ²φ_a′(u))=au/(μθ); implicit differentiation gives u′=w and hence θ′=1−w. On compact subintervals of the open cut the resolvent boundary values are continuous with nonzero denominator, so inversion yields the recorded absolutely continuous measure there, with no singular part. The logarithmic branch-point divergence of φ_a makes H tend to −1/μ at the edge, excluding an edge atom. The support gap bounds the continuum by a strictly faster spatial exponential at fixed μ. The logarithmic and inverse-argument expansions of E1 give the two refresh asymptotics; in particular u=μ−a+a²/μ−2a³/μ²+O(a⁴/μ³) gives the weight correction at large μ. The variance is 2D H(0), yielding the inverse-log scale distinct from θ∼μ as μ/a→0. At μ=0 the rate mixture has a |x|^−3 density tail, consistent with the stated order-of-limits qualification. The frozen numerical checker was inspected, not executed; these are analytic checks, not a finite-distance crossover theorem.

## originality

FAIL

A distinct indexed result, 788807473647, gives equivalent coverage of the headline claim: the same isolated pole and exact residue, the same positive continuum with an all-distance remainder bound, the same exponentially small slow-refresh mass, and the exact and asymptotic variance comparison. The response identity follows immediately from differentiating its identical secular equation and using its stated mass. The fast-refresh expansion is a direct expansion of that same scalar equation and mass, not a substantive surviving contribution to the original finding. This is a judgment about demonstrable coverage and lack of a distinct supported result, not an inference of historical priority, copying, or chronology from catalogue paths. The earlier Arutkin–Reuveni transform alone is substantial prior overlap but is not the decisive reason for failure.

## value

PASS

The mathematical result addresses a substantive same-model discrepancy: fitting the stationary variance can give a parametrically wrong far-tail rate because the mode governing the ultimate tail carries exponentially little mass. The positive spectral decomposition and coefficient reveal why. This is useful science independently of the duplicated coverage; the response identity and fast-refresh expansion alone do not justify accepting a separate finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
