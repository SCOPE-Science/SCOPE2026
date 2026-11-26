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

At the frozen critical rate β=k=γ+μ, the population sum is preserved on the simplex; the equations point inward at each vanishing population component and at A=0,1. With I=I_a+I_u, exact summation gives I'=kS_a I_a−kI. Since 0≤S_a≤1−I and 0≤I_a≤I, −kI≤I'≤−kI²; this preserves I>0 for every finite time even with I_a(0)=0 and gives the stated upper bound. Stable forced equations with asymptotically zero inputs successively yield A,R,S_u→0, and then S_a→1. Direct differentiation of q=I_u/I gives q'=(1−q)(δ₁A−kS_aq)−δ₂(1−A)q, so eventually q'≤δ₁A−δ₂q/2 and q→0. Hence I'/I→0. Dividing each stable filter by I^p adds pI'/I to its damping without changing the limiting positive decay coefficient. For p=1 this yields A/I→ρ/ω, R/I→γ/μ and S_u/I→(μ+κ₁)ρ/[(μ+κ₂)ω]; for p=2 the forcing divided by I² is δ₁(A/I)(1−q), yielding I_u/I²→δ₁ρ/[ω(δ₂+k)]. Substituting (1−S_a)/I=1+S_u/I+R/I gives (1/I)'→Q, including exactly both behavioral terms and the no-awareness baseline k²/μ. Time averaging, the ratio limits and integration of the resulting 1/t asymptotic verify all listed constants and the logarithmic integral. The source CHECK.py was inspected, not executed: its all-unit example gives Q=20/3 and inaccessible coefficient 3/400 by substitution; trajectory sampling is not needed for the universal proof.

## originality

PASS

The exact unforced SIRA model and critical parameter are inherited. The independent comparisons support a distinct model-specific theorem: a global endpoint argument for all seeded feasible trajectories and the normalized first- and second-order compartment tails. Critical inverse-time decay as a general phenomenon is not new.

## value

PASS

The theorem supplies quantitative information at a boundary not covered by the original strict-subthreshold result. The all-initial-state coefficient decomposes the two distinct modeled feedback contributions, and the second-order compartment tail and divergent logarithmic integral distinguish different notions of deterministic clearance. The finding is appropriately scoped to this exact autonomous system, not to empirical or stochastic extinction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
