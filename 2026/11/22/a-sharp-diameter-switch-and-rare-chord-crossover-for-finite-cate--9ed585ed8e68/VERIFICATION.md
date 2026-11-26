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

For a pair not touching a domain endpoint, move its larger-|x| member toward the endpoint on that side. The horizontal distance strictly increases and the absolute height separation cannot decrease. After reflection, maximizing reduces to Q_L(x) with one endpoint fixed at −L; Q_L is strictly increasing for −L<x≤0. On the positive side Q_L′=−2H_L, and H_L′=cosh(x)(cosh L−2cosh x) changes from positive to negative at most once. H_L is negative at 0 and L, so only the smaller crossing can give an interior maximum; neither a double root nor the local minimum can tie the endpoint. For x=rL, 0≤r<1, the normalized vertical difference has termwise positive L derivative, and a trial pair's crossover span is continuous in r and escapes uniformly on each bounded span range as r→1. This follows from the O(1−r) cosine-hyperbolic difference versus the square root of 4−(1+r)². The infimum is attained away from r=0 because the excess increases to first order in r there. Thus a unique nondegenerate interior contact ties the endpoint once; the positivity of the normalized excess's L derivative at this contact gives A_*>2 by stationarity. The endpoint-pair deficit is u+v to first order in inward parameter gaps. Each interior-contact pattern has deficit A u+B v² plus lower scaled order, giving limiting area 4/(3A√B) after division by ε^(3/2) and asymptotically constant sampling density. Counting two ordered endpoint neighborhoods and four ordered mixed neighborhoods reproduces both constants and the conditional law. In the moving window the budget for the mixed contact is ε[1+k min(λ,0)]+O(ε²), and uniform compact localization around the three unordered contact pairs shows that the ε^(−3/2) limit vanishes even at the cutoff. No uniformity away from the specified local window is used.

## originality

PASS

The strongest distinct indexed comparison gives the same local exponents for a parabola but neither its geometry nor its sampling law implies the finite-catenary phase boundary or moving arclength-volume law. The catenary minimum-disk transition is a different invariant. The judgment rests on the exact catenary classification, transversality and critical window, not on the catenary representation or the elementary linear/quadratic integral.

## value

PASS

For a canonical arclength-sampled curve this gives the full finite-span diameter phase diagram and quantifies the effect of competing, nonmerging chord geometries on rare-event probabilities. It distinguishes what survives at the contact itself from what contributes through the width-ε window. This matters beyond a decimal root or a change of variables from the parabola.

The dated certificate retains the supplied scientific assessment, sources and limitations.
