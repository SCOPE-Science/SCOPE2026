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

PASS. Let q=1-b, u=1-X and d=X+(a/q)Y-1; exact cancellation fixes d and gives u_(j+1)=u_j[1-q(u_j+d)]. For d=t/(qn), reciprocal h_j=1/(n u_j) satisfies exact forward difference (t h_j+q)/(n(1-t/n-q u_j)); positive denominator >=1-a. Uniform Gronwall on bounded t and initial u in compact (0,U), plus sum_(j<n)u_j=O(log n), justifies Euler limit H'=tH+q, H(0)=0, H(1)=q(e^t-1)/t; thus qn u_n -> t/(e^t-1) and anY_n -> f(t)+t. Change (X0,Y0)->(u0,d) has determinant q/a and t=qn d, giving n dX0dY0=(1/a)du0dt. Compact test support forces bounded t by exact difference of rescaled coordinates; endpoint u strips contribute arbitrarily little, proving vague limiting measure and conditional strip probability 2KU/(an). Independent recurrence at n=500,2000,8000 for t=.6 approaches (.7298215,1.3298215).

## originality

PASS

PASS best-of-knowledge. The original Boxonov operator, invariant lines and equilibrium limit theorem are prior, and logistic inverse-time scaling is classical; full relevant preprint §3 does not state the pushforward of uniform initial square states at generations n, its exact measure on a two-coordinate curve or strip-intensity U/a. Related same-model 2026 reciprocal logarithmic correction theorem cites the first-order ensemble limit as known but addresses a different second-order fixed-fiber problem. Unindexed general parabolic random-ensemble theorems remain a risk.

## value

PASS

PASS. The natural nonhyperbolic corner of a deterministic two-sex map has qualitatively different attracting equilibrium edges, so the exact n^-1 initial-data rare strip and dependent two-coordinate universal scaling limit are motivated geometric-dynamical information. The coarea prefactor U/a and conditional curve cannot be read from qualitative endpoint convergence and are useful beyond merely restating a scalar logistic approximation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
