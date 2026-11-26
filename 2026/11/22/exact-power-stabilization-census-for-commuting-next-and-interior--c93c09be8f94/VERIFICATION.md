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

At point i the two sides are inclusion predicates for the sets [f(i),n−1] and f([i,n−1]). Equality for every valuation is equivalent to their equality and forces monotonicity, fixed top and no upward step larger than one. Those conditions conversely give the suffix equality. The binary encoding f(i)=i+number of zeros at positions ≥i gives r zeros and image [r,n−1], including the r=0 identity and n=1 boundary. For r>0 the restriction to this image is again of the same form on n−r vertices. Its s zeros leave r−s zeros in the first r slots, giving binom(r,s) extensions. Surjectivity onto the first image cancels the first f in both adjacent powers, so the index is one plus that of the restriction. Following the least image point bounds the index by n−r: images are nested final intervals and equality of successive intervals forces identity on the current interval. Taking the final zero at position r+t−2 with all but one zero in the first r slots realizes t≥2; all r zeros in the first r slots give t=1. To attain n−r≥2 the minimum orbit must move by one at each remaining step, so the final suffix has exactly its last increment zero; there are r such extensions. There is one constant-top map if n−r=1. Singleton valuations distinguish unequal powers, proving the uniform interpretation. A fresh independent Python checker (`independent_check.py`) evaluated all maps and Boolean valuations through n=5 and directly composed all 4,095 encoded maps across n=1,…,12. It confirmed the recurrence and boundaries, including the n=8 histogram (1,7,46,42,20,8,3,1). These are bounded checks; the all-size result rests on surjective restriction.

## originality

PASS

The interval-image subclass and ordinary rank census are prior art, and the Catalan rank-depth census overlaps on the statistic and contains the maps as a subclass after reversing order. The supported distinct claim is the joint exact defect-index enumeration subject to the fixed-end, unit-step condition, not the map family, binomial rank counts, or the general rank upper bound. The broader series do not select this constrained family.

## value

PASS

Modal stabilization depth is the first uniform equality of successive next operators on arbitrary valuations, and measures information loss under iterating a single map. The joint census explains exactly how that depth varies at fixed first-step image loss, a statistic not recovered from counts by rank, fixed points or eventual rank. It provides all finite coefficients and the sharp multiplicity of the maximal delay within a natural topological subclass; the small histogram is just an illustration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
