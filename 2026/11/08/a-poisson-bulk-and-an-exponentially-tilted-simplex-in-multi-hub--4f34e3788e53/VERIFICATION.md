---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For fixed r>=3, fixed pendant counts h_i>=0 and M_n/n->rho>0, each occupied vertex sends at TOTAL rate one to uniformly chosen neighbor. Detailed balance gives unique fixed-mass canonical weights product of degrees^{occupation}; hub degrees n+h_i, n peripheral vertices degree r and H pendants degree 1. The exact generating coefficient factors (1-(n+h_i)z)^(-1), (1-rz)^(-n), (1-z)^(-H). Sum over fixed outside s and pendant ell, compare with hub composition T_n(M): binomial(n+s-1,s)(r/n)^s -> r^s/s!, uniform exponential factorial upper bound dominates tails; pendant weights suppress positive ell. Conditional hub weak-composition Riemann sums and log(1+h_i/n) expansion yield the exponentially tilted simplex and independence from Poisson(r). Independently checked 468 exact detailed-balance transitions for K_{3,4} with one pendant and three particles, plus tilted-marginal mean at rho=1 equals (3-e)/(e-2)=0.392211..., rather than 1/3. These finite checks do not prove convergence.

## originality

PASS

Best-of-knowledge original evaluated claim after statement/implication comparison with cited literature; see four checks and residual risks. No negative search is taken as priority proof.

## value

PASS

A multi-hub network with asymptotically tied degrees and a finite degree perturbation is a natural symmetry-breaking condensation model. The theorem identifies a full r-1 dimensional tilted sharing law, an independent tight Poisson bulk and a macroscopic effect from just one pendant edge; these are substantive asymptotic observables beyond the classical stationary product measure or one-defect condensation story. It does not claim mixing-time or dynamic condensation results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
