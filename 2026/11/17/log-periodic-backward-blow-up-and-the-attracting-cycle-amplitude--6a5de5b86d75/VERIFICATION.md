---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and verification

The proof's critical identities are the exact polar equation \(w'=2p(\lambda+fw)/g\), the periodic integrating-factor solution \(w_*\), the global decomposition \(w=w_*+C\rho\), and the physical-time clock \(dt/d\theta=1/(gw)\). The remainder estimate is uniform on sufficiently negative angles because \(w_*\) and \(g^{-1}\) are bounded, while \(\rho\) grows exponentially in the backward angular direction. The strictly positive periodic derivative \(\Phi'=1/(gK)\) establishes invertibility of the asymptotic clock. These statements prove the general infinite-family theorem.

Run `python3 check.py` for symbolic verification of the cubic Cartesian-to-polar reduction and high-precision quadrature of the phase-resolved amplitude law and half-turn escape-time ratio. The execution reported `STAR_NODE_PHASE_BLOWUP_PROFILE_OK`. The numerical quadrature probes one parameter triple and finitely many negative angular positions; it is supplemental evidence, not an infinite proof.

The result assumes strict radial contraction, globally nonzero angular drift, a homogeneous polynomial nonlinearity, positive linear coefficient, and nonzero initial state. It does not cover angular stagnation, nonhomogeneous vector fields or perturbation stability. The literature comparison does not establish absolute publication priority. Independent validation has not been performed.
