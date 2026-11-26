---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For a fixed SPD matrix, diagonalize once; on mode λ each error is multiplied by 1−B_i h_i λ. Independence across attempts (not across eigenmodes) gives the product of expected squared multipliers, and a pure mode at any admissible λ realizes the robust spectral objective. Write z=λ/m, m=(μ+L)/2, c=(L−μ)/(L+μ), B=1−p+pc². Repeating a normalized step a minimizes the maximum absolute endpoint residual uniquely at a=1. At a_i=1+x_i, independently expanded the weighted endpoint certificate with weights (1+c)/2 and (1−c)/2. After subtracting B² it is p(1−c²) times [1−p(1+c²)](x₁²+x₂²)+2pc²(x₁+x₂+x₁x₂)²+p(1+c²)x₁²x₂². Thus p≤1/(1+c²) suffices globally, and even at equality the last two terms force x₁=x₂=0. For p above that bound, splitting symmetrically by d changes the objective by 2pz²[1−p−p(1−z)²]d²+p²z⁴d⁴, negative uniformly near either endpoint for small d, with uniform strict baseline slack on the compact remaining interval. Take d<1. The minimizing pair exists by continuity and coercivity, including p=1: at least one endpoint has |1−a₂z|≥c independently of a₂, while at both endpoints |1−a₁z| tends uniformly to infinity when a₁ does; exchange the steps for the other case. In the rational example, direct integer coefficient multiplication gives the quartic numerator [62500,−225000,311400,−194400,46656] in ascending powers of z, divided by 62500. Its second-derivative numerator discriminant is −34264166400 with positive leading coefficient. Thus the endpoint values 3233/31250 and 2873/31250 give the exact maximum, below 169/1600. No closed-form optimizer above the transition is proved. The supplied symbolic checker and output were inspected, not executed.

## originality

PASS

The independently omitted whole-step, worst-spectrum expected-square transition is not a matching theorem in the compared sources. Perfect delivery is the classical deterministic polynomial problem, not the new claim. The exact low-delivery uniqueness and cutover to strict benefit from unequal steps are the substantive increment. This assessment is limited to the inspected evidence.

## value

PASS

This gives an exact design boundary for a natural two-attempt budget: independently losing a step can make repetition uniquely optimal even when unequal steps would accelerate at perfect delivery. The lower-regime global certificate and full-interval strict improvement above the threshold distinguish those mechanisms, not just local instability. No conclusion is drawn about adaptive or longer schedules, or an unequal optimizer formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
