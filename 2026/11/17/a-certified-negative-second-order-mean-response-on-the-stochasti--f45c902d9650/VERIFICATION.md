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

A strict exact root bracket at p0 near 0.500884210307218 and derivative four-return multiplier in (-0.031,-0.030) establish an attracting prime four-cycle of f(x)=7x(1-x)/2. Small uniform parameter noise admits four compatible trapping intervals and a uniformly contracting four-step random composition, so a unique localized invariant mixture exists and has smooth small-epsilon response. Expanding a stationary orbit gives U_(j+1)=a_j U_j+c_j xi_j, W_(j+1)=a_j W_j-lambda U_j^2+(1-2p_j)U_j xi_j. Fresh noise independence eliminates cross means; v_(j+1)=a_j^2 v_j+c_j^2 and b_(j+1)=a_j b_j-lambda v_j yield B=sum(b_j)/12. Independent high-precision recurrence gave B=-0.5470942806171606648079353 and multiplier -0.0304999759736671277, confirming the original exact-rational sign enclosure (which is the proof certificate). Uniform contraction, not Monte Carlo, supplies o(epsilon^2).

## originality

PASS

Cruz–Wei–Hardin–Radunskaya 2022/2024 prove period-one/two comparisons and explicitly *conjecture* a negative stationary-mean shift for period four, with simulations, not a certified 7/2 quadratic response. This result certifies one rational interior parameter and strict coefficient sign; proving a conjectural case is not implied by numerical plots. Ayers–Radunskaya 2024 focus on the chaotic range above 3.87, while Sato et al. study additive noise near a period-three cycle. An unindexed exact small-noise response calculation at 3.5 remains a genuine priority risk.

## value

PASS

The negative mean-shift direction in a period-four stochastic logistic population map was an expressly motivated numerical conjecture. An exact certified strict sign at the natural rational parameter 7/2 and a precise second-order response constant is a useful bounded advance even without resolving the entire interval.

The dated certificate retains the supplied scientific assessment, sources and limitations.
