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

The affine branches map onto unions of complete levels. Conditional uniformity on the current level is preserved under every finite admissible itinerary. Core levels 1–3 have combined unnormalized mass 1−λ³ and exit probability λ⁴; level 4 has mass λ³(1−λ) and exit probability λ³. Normalizing gives exactly A. Upon exit the height is 1+Geom(1−λ); outside the core the independent increments are Geom(1−λ)−1, with the geometric variable supported on the nonnegative integers. One-level passage has defective PGF r=z(1−λ)/(1−λr), taking the root vanishing at zero. Mixing the geometric entrance height and charging one departure iterate yields H=z(1−A)+Ar²=(1−A/λ)z+(A/λ)r. At z=1 the two regimes are given by r(1)=min(1,(1−λ)/λ); differentiation gives the mean below criticality, and the square-root singularity gives infinite mean at equality. At criticality the survival generating series of the one-level descent is (1−z)^(-1/2), with the core factor A/λ=2/15 for n≥1. As an independent crossover check, group the +1 steps of a Bernoulli walk with up probability p=λ into runs before each −1. The one-level passage exceeds n downward steps exactly when that walk has not hit −1 by time 2n−1. Reflection with the weight (1−p)/p gives its survival as P(S=1)+(1−(1−p)/p)P(S≥3), with S the position at time 2n−1. At p=1/2+u/(2√n), the local binomial limit gives √n P(S=1)→e^(−u²)/√π, while P(S≥3)→Φ(√2u) and the scaled multiplier tends to 2u, including negative u and u=0. This yields the frozen profile after multiplying by A/λ. The checked claims concern only the stated initial law and auxiliary iterates. Reviewed the branch-intersection verifier as finite evidence; did not execute it.

## originality

FAIL

A distinct indexed result on the same map, four-level base, start and clock gives the same complete return PGF, defect, mean and temporal crossover, as part of a larger space-time law. The critical survival identity is obtained from that PGF without an additional model assumption or theorem. This is demonstrated equivalent coverage, not a claim that the separate, later-indexed record was earlier or that Ji–Ma stated the return law.

## value

PASS

The return observable is natural for the transition from a finite exceptional core to the homogeneous tail. A sharp initial-law normalization and one profile across the recurrent and defective sides give useful quantitative information beyond the qualitative phase transition or a finite computation. This assesses the mathematical contribution of such a law; the complete overlap means it does not warrant a separate accepted finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
