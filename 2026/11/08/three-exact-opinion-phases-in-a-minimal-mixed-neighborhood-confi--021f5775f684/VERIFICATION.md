---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

In the precise direction-specific NDW rule on the fixed path with endpoint opinions (0,1), center H0=1/2, ρ=1/2, ε∈(0,1/4], and uniform iid edge selection, center-to-leaf score is σH or σ(1−H), while a leaf score is σ times its center gap +(1−σ)/2. In σ<2ε both leaves remain fixed, while σ≥2ε leaves and center are frozen at initial state because of the strict confidence inequality. At σ≤ε both center updates occur for all finite times: binary-affine recursion gives dyadic uniform midpoint law, liminf=0 limsup=1 a.s. and limiting variance 1/12. For ε<σ<2ε, in overlap (1−ε/σ,ε/σ), repeated constant edge blocks force finite exit almost surely; the surviving one-way halvings give endpoint polarization with probabilities 1/2 each and variance limit 1/4. Sharp inclusion of boundaries σ=ε and σ=2ε and exact t-step variance for ε=1/5,σ=3/10 follow. Independent rational depth-eight tree checks agree for σ=0,1/5,3/10,2/5,1.

## originality

PASS

The original Krishnagopal–Porter NDW manuscript defines the mixed-direction rule and gives numerical behaviors; it does not classify the sharp three σ-regimes for this exact fixed three-agent profile. Earlier November 2 three-node theorem completely analyzes the both-directions-active oscillation wedge but not the intermediate one-way absorbing polarization or the high-σ no-update phase. Same-date pure-neighborhood star theorem explicitly assumes σ=0, so cannot entail the σ∈(ε,2ε) or σ≥2ε mixed-weight transitions. New content is the complete phase diagram and step variance, not the classical Bernoulli-affine recursion.

## value

PASS

The result gives an exact minimal-network phase diagram separating sustained nonconvergence, random one-sided convergence and frozen initial consensus, with sharp equality conventions and discontinuous nonmonotone limiting variance. It is a structural boundary analysis for the original NDW mechanism rather than a generic Bernoulli-recursion exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
