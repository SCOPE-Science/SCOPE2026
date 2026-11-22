---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Constant reproduction and nodal jump decomposition reduce the exact real BV operator norm to the maximum response to one step. Equispaced binomial blending weights w_i=(−1)^iβ_i have total zero and prefix L_j bounded by 2^(d−1), with equality for d≤j≤n−d+1. The established 2012 nonzero-denominator inequality and alternating partial-fraction limit D∞=2^dπ/sinπx yield global inverse-denominator control. Abel summation on one-sided alternating tails gives numerator L_j/(distance)+O_d(distance^-2) and differentiated O_d(distance^-3), with uniformly integrable errors across left/right sides and bounded single crossing-cell contribution. Thus Var response = |L_j|/2^d(∫_1^j |cosπu|/u du + ∫_1^(n−j+1)|cosπu|/u du)+O_d(1); mean(|cos|)=2/π proves the sharp uniform jump profile and global (2/π)log n+O_d(1). Reproduction of degree d and fixed d are essential. Independent n=24,48,96 quadrature for d=1,2,3 agrees with slope, not a universal proof.

## originality

PASS

The exact fixed-d positive-degree Floater–Hormann BV seminorm, sharp universal 2/pi coefficient, and uniform prefix-weight jump profile are not stated in the original construction, the Bos et al. Lebesgue-constant results, smooth-derivative interpolation theory or the related Berrut d=0 BV theorem. The last has the same leading constant but is a different operator, not an implication for all positive d. Full author manuscripts of the two most relevant published primary FH papers were inspected. Remaining risk is specialized historical variation norm work not indexed under BV terminology.

## value

PASS

Measures the precise total-variation cost of raising polynomial reproduction degree in a standard pole-free rational interpolation family. The universal log coefficient and location-sensitive jump profile are relevant to nonsmooth-data stability and are not determined by pointwise Lebesgue bounds or the Berrut d=0 case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
