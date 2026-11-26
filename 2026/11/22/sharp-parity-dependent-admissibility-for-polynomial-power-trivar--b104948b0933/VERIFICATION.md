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

Grounding and uniform margins are immediate, and integration of the continuous mixed density over a box gives its volume increment. Thus a boundary violation also excludes the parameter, by an interior box with negative density. The density is 1−λD_m B_θ. The z factor has extrema −r_θ and 1, including B_0=2z−1. At fixed s=|x−y|, xy ranges over [0,1−s]. For m≥2 the positive term in the density's x,y factor on x≥y is at most m+1, and the subtracted term is at most m((m−2)/(m−1))^(m−2)≤m for m≥3, or 2 for m=2. At even m the negative extremum is obtained by setting xy=1−s and maximizing H_m; its derivative has the stated strictly decreasing quadratic factor for m≥4, and m=2 is maximized at s=0. At odd m the reversal of x and y supplies the opposite extremum, including m=1 by direct differentiation. Independence of factor arguments yields the stated closed intervals. The comparison H_m(1−2/m)/(m+1)>e^(−2) follows from the two logarithmic bounds in the proof; strict decrease of r_θ from 1 to e^(−2) then gives a unique even-exponent switch. The exact density bounds at m=2, θ=1 give [−1/2,1/3], and λ=−2/5 has minimum density 1/5. The independent bounded replay `python3 /workspace/reproduce_reviews.py` confirms endpoint and witness values and θ_2≈0.15352844952779. The analytical extrema, not finite optimization, establish the theorem.

## originality

PASS

Supported contribution: the exact interval of the first Chesneau family with its parity split and unique even-m switch, not the family, derivative, or density criterion. The strongest known same-family comparison is a sufficient-only parameter restriction. No competing statement available in this review supplies the two sharp extrema and switch. Priority is provisional, in particular because the primary comparison could not be freshly read in full.

## value

PASS

The interval tells users of an existing parametric dependence model exactly which proposed laws are valid. It gives a quantitative strict extension on a concrete example and a nontrivial shape transition throughout the even-exponent family, not just a density computation. It does not imply estimation or tail-performance guarantees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
